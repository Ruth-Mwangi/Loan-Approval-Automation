from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.metrics import classification_report, confusion_matrix,accuracy_score


def get_categorical_columns(data):
    """
    Get the names of categorical columns in a DataFrame.

    Parameters:
    - data: A pandas DataFrame.

    Returns:
    - A list of column names that are of object type.
    """
    categorical_columns = data.select_dtypes(include=['object','string',"category"]).columns.tolist()
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

def print_model_score(true, pred, train=True):
    if train:
        clf_report = pd.DataFrame(classification_report(true, pred, output_dict=True))
        print("Train Result:\n================================================")
        print(f"Accuracy Score: {accuracy_score(true, pred) * 100:.2f}%")
        print("_______________________________________________")
        print(f"CLASSIFICATION REPORT:\n{clf_report}")
        print("_______________________________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(true, pred)}\n")
        
    elif train == False:
        clf_report = pd.DataFrame(classification_report(true, pred, output_dict=True))
        print("Test Result:\n================================================")
        print(f"Accuracy Score: {accuracy_score(true, pred) * 100:.2f}%")
        print("_______________________________________________")
        print(f"CLASSIFICATION REPORT:\n{clf_report}")
        print("_______________________________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(true, pred)}\n")

        # Plot the confusion matrix
    cm = confusion_matrix(true, pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', xticklabels=['Approved', 'Rejected'], yticklabels=['Approved', 'Rejected'])
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix - ' )
    plt.show()

def convert_to_data_type(data,column,data_type):
    """
    Convert a column in a DataFrame to a specified data type.

    Parameters:
    - data: A pandas DataFrame.
    - column: The column name to convert.
    - data_type: The data type to convert the column to.

    Returns:
    - The DataFrame with the column converted to the specified data type.
    """

    return data[column].astype(data_type)

def combine_features(feature_list,data):
    """
    Combine multiple features into a single feature.

    Parameters:
    - feature_list: A list of feature names to combine.
    - data: A pandas DataFrame.

    Returns:
    - The DataFrame with combined features.
    """
    
    new_feature_name="&".join(feature_list)
    data[new_feature_name]=(data[feature_list[0]]**3)*data[feature_list[1]].astype(int)
    return data

