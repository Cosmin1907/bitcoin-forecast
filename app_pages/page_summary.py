import streamlit as st 

def page_summary_body():
    """
    Displays a quick project summary with key terms, dataset details,
    and main business objectives, including data analysis and model goals.
    """
    st.write("### Quick Project Summary")

    
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* **Bitcoin Closing Price**: The final price of Bitcoin at the close of each trading day.\n"
        f"* **Buy/Sell Signal**: A recommendation for trade action based on market trend predictions.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset includes daily Bitcoin trading data, including metrics such as opening price, "
        f"closing price, daily high/low, and trading volume in both BTC and USD.\n"
    )

    
    st.write(
        f"* For more details, please refer to the "
        f"[Project README file](https://github.com/Cosmin1907/bitcoin-forecast)."
    )

    
    st.success(
        f"The project has 2 main business objectives:\n"
        f"* 1 - **Data Visualization and Correlation Study**: The client aims to identify variables "
        f"strongly correlated with significant Bitcoin price changes. This will involve visualization and "
        f"correlation analysis with key metrics.\n"
        
        f"* 2 - **Predictive Models for Trading Decisions**: "
        f"Building two models—one for **predicting the next day's closing price** (regression) and another for "
        f"**determining buy/sell signals** based on market trends (classification)—to support informed trading decisions."
    )
