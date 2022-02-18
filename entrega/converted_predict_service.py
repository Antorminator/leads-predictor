import pandas as pd
# Flask service that receives a dict, transform it into a 2D array and predicts the target variable with a model

def predict_single(customer, model):
    # Transform the dict into a 2D array
    customer_df = pd.DataFrame(customer, index=[0])
    # Predict the target variable
    prediction = model.predict(customer_df)
    # Return the prediction
    return round(prediction[0])*100