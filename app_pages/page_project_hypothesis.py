import streamlit as st

def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* Hypothesis 1: Bitcoin price changes correlate with trading volume (in BTC and USD). "
        f"A correlation study supports this relationship, indicating a link between price movements and volume.\n\n"
        
        f"* Hypothesis 2: Daily closing prices are influenced by the daily high and low prices. "
        f"Correlation analysis shows that high and low prices have a notable impact on the closing price, "
        f"supporting this hypothesis for further investigation."
    )
