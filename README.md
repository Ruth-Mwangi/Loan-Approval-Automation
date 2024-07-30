# Moneza-Loan-Approval-Automation
This is a machine learning project aimed at automating the approval or rejection of loan applications.
## Project Overview

The Loan Approval Automation project aims to develop a machine learning model to automate the loan application process. This model helps in reducing labor costs while minimizing losses due to incorrect decisions.

### Prerequisites

Ensure you have the following installed:
- Python 3.x

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone git@github.com:Ruth-Mwangi/Moneza-Loan-Approval-Automation.git
   ```
2. Create and activate virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Install Dependancies
    ```bash
    pip install -r requirements.txt
    ```
## Project Structure
### data
- **raw**: Contains raw data files that are used as the initial input for the project. These files are typically unprocessed and in their original form.
- **processed**: Contains data files that have been cleaned and processed. These files are the result of data preprocessing steps applied to the raw data.


### notebooks
- **01_data_preprocessing.ipynb**: Jupyter Notebook for data cleaning and preprocessing. 
- **02_eda.ipynb**: Jupyter Notebook for exploratory data analysis (EDA).
- **03_model_training.ipynb**: Jupyter Notebook for training and evaluating machine learning models.
- **04_threshold_optimization.ipynb**: Jupyter Notebook for determining the optimal probability thresholds for model predictions to balance between different performance metrics.
- **05_business_impact_analysis.ipynb**: Jupyter Notebook for analyzing the business impact of the model. This includes evaluating how the model’s predictions affect business metrics and decisions.

### src
Contains common functions.

### models
Contains the saved models

### reports
- **figures**: Directory for storing visualizations and figures used in reports. It includes plots, charts, and other graphical representations of the data.

# Notebook Execution

## Notebooks

### 01_data_preprocessing.ipynb
- **Purpose**: Data cleaning and preprocessing.
- **How to Run**:
  1. Open Jupyter Notebook in your project directory:
     ```bash
     jupyter notebook
     ```
  2. Navigate to `01_data_preprocessing.ipynb` in the Jupyter interface.
  3. Execute each cell

### 02_eda.ipynb
- **Purpose**: Exploratory Data Analysis (EDA).
- **How to Run**:
  1. Ensure Jupyter Notebook is running.
  2. Open `02_eda.ipynb` from the Jupyter interface.
  3. Execute each cell

### 03_model_training.ipynb
- **Purpose**: Training and evaluating machine learning models.
- **How to Run**:
  1. Open Jupyter Notebook.
  2. Open `03_model_training.ipynb`.
  3. Execute each cell

### 04_threshold_optimization.ipynb
- **Purpose**: Determining optimal probability thresholds for model predictions.
- **How to Run**:
  1. Open Jupyter Notebook.
  2. Open `04_threshold_optimization.ipynb`.
  3. Execute each cell

### 05_business_impact_analysis.ipynb
- **Purpose**: Analyzing the business impact of model predictions and decision thresholds.
- **How to Run**:
  1. Open Jupyter Notebook.
  2. Open `05_business_impact_analysis.ipynb`.
  3. Execute cells to evaluate the potential business outcomes, financial implications, and recommendations based on model results.

## General Tips for Running Jupyter Notebooks
- **Ensure Dependencies**: Install required libraries listed in `requirements.txt`.
- **Data Files**: Verify that data files are placed in the correct directories (`data/raw/` and `data/processed/`).
- **Environment**: Run notebooks in a consistent environment with all dependencies and data accessible.