import pandas as pd
import plotly.graph_objects as go
import json

# Load JSON files
def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Load processed JSON data for different log types
auth_data = load_json('data/processed_logs/authentication_parsed.json')
kernel_data = load_json('data/processed_logs/kernel_parsed.json')
system_data = load_json('data/processed_logs/system_parsed.json')
anomalous_events_data = load_json('data/anomalies/anomalous_events.json')
anomalous_messages_data = load_json('data/anomalies/anomalous_messages.json')

# Convert data to DataFrame
auth_df = pd.DataFrame(auth_data)
kernel_df = pd.DataFrame(kernel_data)
system_df = pd.DataFrame(system_data)

# Anomalous Events Visualization
events_df = pd.DataFrame(anomalous_events_data)

# Check if 'event_type' exists in the DataFrame
if 'event_type' in events_df.columns and 'count' in events_df.columns:
    event_counts = events_df.groupby('event_type').sum()['count'].reset_index()

# Anomalous Messages Visualization
messages_df = pd.DataFrame(anomalous_messages_data)

# Check if 'message' exists in the DataFrame
if 'message' in messages_df.columns and 'count' in messages_df.columns:
    message_counts = messages_df.groupby('message').sum()['count'].reset_index()

# Visualization Functions
def create_bar_chart(df, x_column, y_column, title, xaxis_label, yaxis_label, max_labels=10):
    # Limit the number of labels displayed
    if len(df) > max_labels:
        df = df.nlargest(max_labels, y_column)

    # Truncate long messages for better display
    df[x_column] = df[x_column].apply(lambda x: x[:50] + '...' if isinstance(x, str) else x)

    fig = go.Figure([go.Bar(
        x=df[x_column],  # X-axis uses the provided x_column
        y=df[y_column],  # Y-axis uses the provided y_column (like 'count')
        text=df[y_column],  # Display the frequency as text on the bars
        textposition='auto'
    )])

    fig.update_layout(
        title=title,
        xaxis_title=xaxis_label,
        yaxis_title=yaxis_label,
        template="plotly_dark",
        xaxis_tickangle=-45,  # Rotate the x-axis labels
        xaxis={'tickmode': 'array'},  # Ensure custom ticks
    )
    return fig

# Visualize Anomalous Events
if 'event_type' in event_counts.columns and 'count' in event_counts.columns:
    events_fig = create_bar_chart(event_counts, 'event_type', 'count', "Anomalous Events", "Event Type", "Frequency of Anomalies")
    events_fig.show()

# Visualize Anomalous Messages
if 'message' in message_counts.columns and 'count' in message_counts.columns:
    messages_fig = create_bar_chart(message_counts, 'message', 'count', "Anomalous Messages", "Message", "Frequency of Anomalies")
    messages_fig.show()

# Visualize Authentication Log Messages
if 'message' in auth_df.columns:
    auth_message_counts = auth_df['message'].value_counts().reset_index()
    auth_message_counts.columns = ['message', 'count']
    auth_fig = create_bar_chart(auth_message_counts, 'message', 'count', "Authentication Log Messages", "Message", "Frequency")
    auth_fig.show()

# Visualize Kernel Log Messages
if 'message' in kernel_df.columns:
    kernel_message_counts = kernel_df['message'].value_counts().reset_index()
    kernel_message_counts.columns = ['message', 'count']
    kernel_fig = create_bar_chart(kernel_message_counts, 'message', 'count', "Kernel Log Messages", "Message", "Frequency")
    kernel_fig.show()

# Visualize System Log Messages
if 'message' in system_df.columns:
    system_message_counts = system_df['message'].value_counts().reset_index()
    system_message_counts.columns = ['message', 'count']
    system_fig = create_bar_chart(system_message_counts, 'message', 'count', "System Log Messages", "Message", "Frequency")
    system_fig.show()
