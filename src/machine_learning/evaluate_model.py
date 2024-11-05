import streamlit as st
import pandas as pd
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    mean_squared_error,
    r2_score,
)


def confusion_matrix_and_report(X, y, pipeline, label_map):
    prediction = pipeline.predict(X)

    st.write('#### Confusion Matrix')
    st.code(pd.DataFrame(confusion_matrix(y_true=y, y_pred=prediction),
                         columns=[["Actual " + sub for sub in label_map]],
                         index=[["Prediction " + sub for sub in label_map]]
                         ))

    st.write('#### Classification Report')
    st.code(classification_report(y, prediction, target_names=label_map), "\n")


def clf_performance(X_train, y_train, X_test, y_test, pipeline, label_map):
    st.info("Train Set")
    confusion_matrix_and_report(X_train, y_train, pipeline, label_map)

    st.info("Test Set")
    confusion_matrix_and_report(X_test, y_test, pipeline, label_map)


def regressor_performance(X_train, y_train, X_test, y_test, pipeline):
    y_train_pred = pipeline.predict(X_train)
    y_test_pred = pipeline.predict(X_test)

    st.write("### Regression Model Performance")
    st.write(f"**Train Set**")
    st.write(f"Mean Squared Error: {mean_squared_error(y_train, y_train_pred):.2f}")
    st.write(f"R² Score: {r2_score(y_train, y_train_pred):.2f}")

    st.write("**Test Set**")
    st.write(f"Mean Squared Error: {mean_squared_error(y_test, y_test_pred):.2f}")
    st.write(f"R² Score: {r2_score(y_test, y_test_pred):.2f}")


def evaluate_model(X_train, y_train, X_test, y_test, pipeline, label_map=None):
    if label_map is not None:
        # If label_map is provided, we assume it's a classification problem
        clf_performance(X_train, y_train, X_test, y_test, pipeline, label_map)
    else:
        # No label_map means it's a regression problem
        regressor_performance(X_train, y_train, X_test, y_test, pipeline)
