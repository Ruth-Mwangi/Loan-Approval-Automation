def get_categorical_columns(data):
    """
    Get the names of categorical columns in a DataFrame.

    Parameters:
    - data: A pandas DataFrame.

    Returns:
    - A list of column names that are of object type.
    """
    categorical_columns = data.select_dtypes(include=['object','string']).columns.tolist()
    return categorical_columns

def get_numerical_columns(data):
    """
    Get the names of numerical columns in a DataFrame.

    Parameters:
    - data: A pandas DataFrame.

    Returns:
    - A list of column names that are of numerical data types.
    """
    numerical_columns = data.select_dtypes(include=['int64', 'float64', 'int32', 'float32']).columns.tolist()
    return numerical_columns

def get_boolean_columns(data):
    """
    Get the names of boolean columns in a DataFrame.

    Parameters:
    - data: A pandas DataFrame.

    Returns:
    - A list of column names that are of  boolean data type.
    """
    boolean_columns = data.select_dtypes(include=['bool']).columns.tolist()
    return boolean_columns

