import plotly.express as px
import pandas as pd

def create_bar_chart(data, category, split_column=None):
    """
    Create an interactive bar chart for the given category from the DataFrame using Plotly.
    The chart will split the counts based on the values of the split_column if provided.

    Parameters:
    - data: A pandas DataFrame.
    - category: The column name in the DataFrame for which to create the bar chart.
    - split_column: Optional; the column name in the DataFrame to split the data by (e.g., 'AR').
    """
    
    if split_column:
        # Check if split_column exists in the data
        if split_column not in data.columns:
            raise ValueError(f"Column '{split_column}' does not exist in the DataFrame")
        
        # Compute value counts for the category, split by the split_column
        grouped_data = data.groupby([split_column, category]).size().reset_index(name='Count')
        
        # Create the bar chart using Plotly
        fig = px.histogram(grouped_data, x=category, y='Count', color=split_column, 
                     title=f'Bar Chart of {category} by {split_column}',
                     labels={category: category, 'Count': 'Count', split_column: split_column},text_auto=True,barmode="group")
        
        
    else:
        # Compute value counts and reset index to prepare data for Plotly
        value_counts = data[category].value_counts().reset_index()
        value_counts.columns = [category, 'Count']
        
        # Create the bar chart using Plotly
        fig = px.bar(value_counts, x=category, y='Count', 
                     title=f'Bar Chart of {category}', 
                     labels={category: category, 'Count': 'Count'})
    
    # Update layout for better appearance
    fig.update_layout(xaxis_title=category, yaxis_title='Count', xaxis_tickangle=-45)
    
    # Show the chart
    fig.show()

def create_line_chart(data, numeric_column, split_column=None):
    """
    Create an interactive line chart for the given numerical column from the DataFrame using Plotly.
    The chart will show counts of occurrences and can split by the values of the split_column if provided.

    Parameters:
    - data: A pandas DataFrame.
    - numeric_column: The column name in the DataFrame representing numerical data.
    - split_column: Optional; the column name in the DataFrame to split the data by (e.g., 'AR').
    """
    
    if split_column:
        # Check if split_column exists in the data
        if split_column not in data.columns:
            raise ValueError(f"Column '{split_column}' does not exist in the DataFrame")
        
        # Compute counts for the numeric_column, split by the split_column
        grouped_data = data.groupby([split_column, numeric_column]).size().reset_index(name='Count')
        
        # Create the line chart using Plotly
        fig = px.line(grouped_data, x=numeric_column, y='Count', color=split_column, 
                      title=f'Line Chart of {numeric_column} by {split_column}',
                      labels={numeric_column: numeric_column, 'Count': 'Count', split_column: split_column})
        
    else:
        # Compute counts for the numeric_column
        grouped_data = data[numeric_column].value_counts().reset_index()
        grouped_data.columns = [numeric_column, 'Count']
        
        # Create the line chart using Plotly
        fig = px.line(grouped_data, x=numeric_column, y='Count', 
                      title=f'Line Chart of {numeric_column}', 
                      labels={numeric_column: numeric_column, 'Count': 'Count'})
    
    # Update layout for better appearance
    fig.update_layout(xaxis_title=numeric_column, yaxis_title='Count')
    
    # Show the chart
    fig.show()
    