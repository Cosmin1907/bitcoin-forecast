import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_model import evaluate_model  # Changed to the new function

def page_predict_trend_body():
    version = 'v1'
    
    # Load needed files
    pipeline_data_cleaning_feat_eng = load_pkl_file(
        f'outputs/ml_pipeline/predict_buy_sell/{version}/clf_pipeline_data_cleaning_feat_eng.pkl'
    )
    pipeline_clf = load_pkl_file(
        f'outputs/ml_pipeline/predict_buy_sell/{version}/clf_pipeline_model.pkl'
    )
    buy_sell_feat_importance = plt.imread(
        f'outputs/ml_pipeline/predict_buy_sell/{version}/features_importance.png'
    )
    X_train = pd.read_csv(f'outputs/ml_pipeline/predict_buy_sell/{version}/X_train.csv')
    X_test = pd.read_csv(f'outputs/ml_pipeline/predict_buy_sell/{version}/X_test.csv')
    y_train = pd.read_csv(f'outputs/ml_pipeline/predict_buy_sell/{version}/y_train.csv').values
    y_test = pd.read_csv(f'outputs/ml_pipeline/predict_buy_sell/{version}/y_test.csv').values

    st.write("### ML Pipeline: Predict Buy/Sell Signals")
    
    # Display pipeline training summary conclusions
    st.info(
        f"* The classification model aims to predict potential 'buy' or 'sell' signals.\n"
        f"* Target recall was set at 80% for both 'Buy' and 'Sell' signals.\n"
        
    )


    # Show pipelines
    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")
    
    st.write(" * The first pipeline handles data cleaning and feature engineering, passing trade data through without modification since it requires no additional transformations.")
    st.write(str(pipeline_data_cleaning_feat_eng))
    
    st.write("* The second is for feature scaling and modeling.")
    st.write(str(pipeline_clf))

    # Show feature importance plot
    st.write("---")
    st.write("* The features the model was trained on and their importance:")
    st.image(buy_sell_feat_importance)

    # We don't need to apply the data cleaning and feature engineering pipeline, 
    # since X_train and X_test were already transformed in the data preparation process.

    # Evaluate performance on train and test set
    st.write("---")
    st.write("### Pipeline Performance")
    evaluate_model(X_train=X_train, y_train=y_train,
                   X_test=X_test, y_test=y_test,
                   pipeline=pipeline_clf,
                   label_map=["Sell", "Buy"])  
