import streamlit as st

def page_project_hypothesis_body():
    """
    Display project hypotheses and validation results in Streamlit.
    """
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* Hypothesis 1: Bitcoin price changes correlate with trading volume (in BTC and USD). "
        f"A correlation study supports this relationship, indicating a link between price movements and volume.\n\n"
        
        f"* Hypothesis 2: A correlation analysis indicates that the daily closing prices of Bitcoin are influenced by the daily high and low prices, impacting the trend direction and strength. This relationship suggests that further exploration of these variables is warranted."
    )
