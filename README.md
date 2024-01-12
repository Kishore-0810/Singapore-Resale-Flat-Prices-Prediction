# Singapore-Resale-Flat-Prices-Prediction

The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. This predictive model will be based on historical data of resale flat transactions, and it aims to assist both potential buyers and sellers in estimating the resale value of a flat.


## Data Collection and Preprocessing: 
Collect a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) for the years 1990 to Till Date. Preprocess the data like handing missing values, checking duplicates etc.. to clean and structure it for machine learning model.

## Feature Engineering:
Extract relevant features from the dataset, including town, flat type, storey range, floor area, flat model, and lease commence date. Create any additional features that may enhance prediction accuracy.

## Encoding Categorical Variables:
Encode the categorical variables to numerical ones using label encoding or one-hot-encoding.

## Model Selection and Training: 
Choose an appropriate machine learning model for regression (e.g., linear regression, decision trees, or random forests). Train the model on the historical data, using a portion of the dataset for training.

## Model Evaluation:
Evaluate the model's predictive performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE) and R2 Score.

## Choosing Model:
After model evaluation, choosing random forest model for predicting the singapore resale flat price.

## Streamlit Web Application: 
Develop a user-friendly web application using Streamlit that allows users to input details of a flat (town, flat type, storey range, etc.). Utilize the trained machine learning model to predict the resale price based on user inputs.

# Best Model:
Random Forest Model
* Input feature - "year", "month", "flat_type_encode", "flat_model_encode", "floor_area_sqm", "town_encode", "lease_commence_date", "min_storey", "max_storey"
* Output feature - "resale_price"



