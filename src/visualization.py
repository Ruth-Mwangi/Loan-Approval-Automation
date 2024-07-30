import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
        if split_column == 'AR':
            # Map 0 to 'Approved' and 1 to 'Rejected'
            grouped_data["AR"] = grouped_data["AR"].map({0: 'Approved', 1: 'Rejected'})
        
        # Create the bar chart using Seaborn
        # plt.figure(figsize=(10, 6))
        ax=sns.barplot(data=grouped_data, x=category, y='Count', hue=split_column)
        plt.title(f'Bar Chart of {category} by {split_column}')
        plt.xlabel(category)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
       
        
        
    else:
        if category == 'AR':
        # Map 0 to 'Approved' and 1 to 'Rejected'
            data[category] = data[category].map({0: 'Approved', 1: 'Rejected'})
        # Compute value counts and reset index to prepare data for Seaborn
        value_counts = data[category].value_counts().reset_index()
        value_counts.columns = [category, 'Count']
        
        # Create the bar chart using Seaborn
        # plt.figure(figsize=(10, 6))
        ax=sns.barplot(data=value_counts, x=category, y='Count',palette="tab10",hue=category)
        plt.title(f'Bar Chart of {category}')
        plt.xlabel(category)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        # Annotate bars with values
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.0f}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'baseline', 
                        fontsize=10, color='black', xytext=(0, 5), 
                        textcoords='offset points')

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

def create_heat_map(data):
    """
    Create a heatmap for the given DataFrame using Seaborn.

    Parameters:
    - data: A pandas DataFrame representing a correlation matrix.

    Returns:
    - None
    """
    
    plt.figure(figsize=(30, 10))

    sns.heatmap(data, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

    plt.title('Correlation Matrix')

   

def create_pie_chart(data):
    """
    Create a pie chart for the given data using Matplotlib.

    Parameters:
    - data: A pandas DataFrame or Series representing the data to plot. If DataFrame, the column "AR" is used.

    Returns:
    - None
    """
    count = ""
    if isinstance(data, pd.DataFrame):
        count = data["AR"].value_counts()
    else:
        count = data.value_counts()


    count.plot(kind = 'pie', explode = [0, 0.1], 

                figsize = (6, 6), autopct = '%1.1f%%', shadow = True)

    plt.show()