import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_price_study import page_price_study_body
from app_pages.page_forecast import page_forecast_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_trend import page_predict_trend_body
from app_pages.page_predict_price import page_predict_price_body

app = MultiPage(app_name="Bitcoin Forecast")  # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Price Study", page_price_study_body)
app.add_page("Bitcoin Forecast", page_forecast_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Predict Trend", page_predict_trend_body)
app.add_page("ML: Prospect Price", page_predict_price_body)

app.run()  # Run the  app