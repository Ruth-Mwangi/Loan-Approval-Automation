import plotly.express as px


def create_bar_chart(data, category):
    """
    Create an interactive bar chart for the given category from the DataFrame using Plotly.

    Parameters:
    - data: A pandas DataFrame.
    - category: The column name in the DataFrame for which to create the bar chart.
    """
    # Compute value counts and reset index to prepare data for Plotly
    value_counts = data[category].value_counts().reset_index()
    value_counts.columns = [category, 'Count']

    # Create the bar chart using Plotly
    fig = px.bar(value_counts, x=category, y='Count', title=f'Bar Chart of {category}', labels={category: category, 'Count': 'Count'})
    
    # Update layout for better appearance
    fig.update_layout(xaxis_title=category, yaxis_title='Count', xaxis_tickangle=-45)
    
    # Show the chart
    fig.show()
