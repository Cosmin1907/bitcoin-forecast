import plotly.express as px
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.data_management import load_btc_data

sns.set_style("whitegrid")

def page_price_study_body():
    # Load Bitcoin data
    df = load_btc_data()

    # Display header
    st.write("### Bitcoin Price Movement Correlation Study")
    st.info(
        "* This study analyzes the correlation between Bitcoin's daily price metrics and trading volume, "
        "focusing on the relationship between closing prices and trading volumes in USD and BTC."
    )

    # Inspect data
    if st.checkbox("Inspect Bitcoin Data"):
        st.write(
            f"* The dataset contains {df.shape[0]} rows and {df.shape[1]} columns. "
            "Below are the first 10 rows for reference."
        )
        st.write(df.head(10))

    st.write("---")

    # Summary of Correlation Study
    st.write(
        "* This analysis of Bitcoin price movements reveals distinct patterns across different market conditions. "
        "We observe how Bitcoin's price interacts with trading volumes and key price metrics in varying scenarios."
    )

    # Findings from the correlation analysis
    st.info(
        "* **Key Findings:**\n"
        "- In a **bull market** (e.g., 2017 run), the closing price tends to closely align with the high price, "
        "suggesting strong upward momentum.\n"
        "- In contrast, during a **market crash** (e.g., March 2020 COVID-19 crash), the closing price is more "
        "correlated with the low price, indicating a downward trend.\n"
        "- The **overlay plot** shows that periods with **positive volume** (USD) often align with price increases, "
        "while **negative volume** tends to align with price decreases."
    )


    # Bull Market Plot (2017 Bull Run)
    if st.checkbox("Show 2017 Bull Market Plot"):
        plot_bull_market(df)

    # Bear Market Plot (2020 COVID-19 Crash)
    if st.checkbox("Show 2020 COVID-19 Market Crash Plot"):
        plot_bear_market(df)

    # Overlay Volume Plot
    if st.checkbox("Show Bitcoin Closing Price and Volume Overlay"):
        plot_volume_overlay(df)

def plot_bull_market(df):
    # Filter data for bull market
    start_date = '2017-12-01'
    end_date = '2018-02-01'
    df_bull_run = df[(df.index >= start_date) & (df.index <= end_date)]

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_bull_run.index, df_bull_run['high'], label='High', color='green')
    ax.plot(df_bull_run.index, df_bull_run['low'], label='Low', color='red')
    ax.plot(df_bull_run.index, df_bull_run['close'], label='Close', color='blue')
    ax.fill_between(df_bull_run.index, df_bull_run['low'], df_bull_run['high'], color='grey', alpha=0.2)
    ax.set_title('Bitcoin Price During 2017 Bull Run')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def plot_bear_market(df):
    # Filter data for bear market
    start_date = '2020-02-01'
    end_date = '2020-05-01'
    df_crash = df[(df.index >= start_date) & (df.index <= end_date)]

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_crash.index, df_crash['high'], label='High', color='green')
    ax.plot(df_crash.index, df_crash['low'], label='Low', color='red')
    ax.plot(df_crash.index, df_crash['close'], label='Close', color='blue')
    ax.fill_between(df_crash.index, df_crash['low'], df_crash['high'], color='grey', alpha=0.2)
    ax.set_title('March 2020 Crash (COVID-19 Market Crash)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def plot_volume_overlay(df):
    # Filter data for overlay plot
    start_date = '2017-12-01'
    end_date = '2018-02-01'
    df_filtered = df[(df.index >= start_date) & (df.index <= end_date)]

    # Plot
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(df_filtered.index, df_filtered['close'], label='Close Price', color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price (USD)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_title('Bitcoin Closing Price and Volume Overlay')

    ax2 = ax1.twinx()
    positive_volume = df_filtered['Volume USD'][df_filtered['close'] > df_filtered['open']]
    negative_volume = df_filtered['Volume USD'][df_filtered['close'] <= df_filtered['open']]

    ax2.bar(df_filtered.index[df_filtered['close'] > df_filtered['open']],
            positive_volume, alpha=0.6, color='green', label='Positive Volume (USD)')
    ax2.bar(df_filtered.index[df_filtered['close'] <= df_filtered['open']],
            negative_volume, alpha=0.6, color='red', label='Negative Volume (USD)')
    ax2.set_ylabel('Volume (USD)', color='gray')
    ax2.tick_params(axis='y', labelcolor='gray')

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    st.pyplot(fig)
