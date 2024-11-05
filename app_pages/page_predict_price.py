import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_model import regressor_performance  


def page_predict_price_body():
    """
    Display and evaluate the ML pipeline for predicting Bitcoin's closing price.

    Loads data, regression pipeline, and feature importance plot. 
    Shows pipeline details and evaluates model performance with training and testing data.
    """
    version = 'v2'
    reg_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_close/{version}/best_regressor_pipeline.pkl")
    reg_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_close/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_close/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_close/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_close/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_close/{version}/y_test.csv")

    st.write("### ML Pipeline: Predict Bitcoin Closing Price")

    st.info(
        f"* The regression model aims to predict the next closing price based on historical data.\n"
        f"* Target R² score was set at 0.70. Current performance shows an R² score of 0.89 on the train set and 0.79 on the test set."
    )

    st.write("---")

    st.write("* ML pipeline to predict the next Bitcoin closing price.")
    st.write(str(reg_pipeline))

    st.write("---")

    st.write("* The features the model was trained on and their importance:")
    st.image(reg_feat_importance)

    st.write("---")

    # Evaluate performance
    st.write("### Pipeline Performance")
    regressor_performance(X_train=X_train, y_train=y_train,
                          X_test=X_test, y_test=y_test,
                          pipeline=reg_pipeline)
