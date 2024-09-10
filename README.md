
# Waze User Churn Analysis Project

## Project Overview
This project aims to analyze user churn for **Waze**, a GPS navigation software. The goal is to perform a full data analytics pipeline, including **Exploratory Data Analysis (EDA)**, **statistical measurements**, **data visualizations**, and **predictive modeling** using **Python**. The project examines user behavior, identifies key drivers of churn, and builds machine learning models to predict and reduce future churn.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Analysis and Methods](#analysis-and-methods)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)
- [Contributors](#contributors)

## Dataset
The dataset includes user information such as:
- User demographics
- Activity metrics (e.g., app usage, session length)
- Engagement with Waze features
- Churn indicator (whether a user stopped using the app)

Data was pre-processed to handle missing values, outliers, and formatting issues.

## Project Structure
- `data/` - Directory containing raw and processed data files.
- `notebooks/` - Jupyter notebooks used for EDA, modeling, and visualization.
- `src/` - Python scripts for preprocessing, feature engineering, and model building.
- `models/` - Trained machine learning models.
- `outputs/` - Visualizations, reports, and model results.
- `README.md` - This documentation file.

## Analysis and Methods
1. **Exploratory Data Analysis (EDA)**:  
   - Overview of data distributions.
   - Churn rate calculations.
   - Statistical measurements, including summary statistics and correlation analysis.
2. **Data Visualization**:  
   - Visualizing churn trends across different user segments using **Tablau**, **matplotlib** and **seaborn**.
3. **Feature Engineering**:  
   - Creating new features based on user activity and engagement metrics.
4. **Machine Learning**:  
   - Building models to predict churn using algorithms such as **Logistic Regression**, **Random Forest**, and **XGBoost**.
   - Evaluation with precision, recall, and F1-score.

## Results


## Technologies Used
- Python
  - Libraries: **pandas**, **numpy**, **matplotlib**, **seaborn**, **scikit-learn**, **xgboost**
- Jupyter Notebooks
- Git for version control

## How to Run
1. Clone the repository:  
   ```
   git clone https://github.com/your-repo/waze-churn-analysis.git
   ```
2. Install the required dependencies:  
   ```
   pip install -r requirements.txt
   ```
3. Run the notebooks or scripts in the `src/` directory to reproduce the results.

## Contributors
- Sebastián Urbina (Data Scientist)


