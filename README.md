## Table of contents

- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Project hypothesis and validation](#hypothesis-and-how-to-validate)
- [Rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
- [ML Business Case](#ml-business-case-for-each-model)
- [Dashboard Design](#dashboard-design)
- [Fixed Bugs](#fixed-bugs)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment to Heroku](#deployment-to-heroku)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Credits](#credits)

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/prasoonkottarathil/btcinusd). This dataset provides historical Bitcoin data to facilitate predictive analytics and research in cryptocurrency trends.
* The dataset contains daily historical data, represented by various metrics for Bitcoin (BTC) trading. It includes information such as opening, closing, high, and low prices, along with trading volumes for the currency. Additionally, it has been augmented with new features to enhance analysis.

### Original Dataset Variables

| Variable           | Meaning                                           | Units                            |
|:-------------------|:--------------------------------------------------|:---------------------------------|
| Unix Timestamp     | Unix timestamp or Epoch Time                      | Seconds since 1970-01-01 00:00:00 UTC |
| Date               | The date corresponding to the timestamp           | UTC Timezone                     |
| Symbol             | The cryptocurrency symbol associated with the data| BTC                             |
| Open               | Opening price for the time period                 | USD                              |
| High               | Highest price for the time period                 | USD                              |
| Low                | Lowest price for the time period                  | USD                              |
| Close              | Closing price for the time period                 | USD                              |
| Volume (Crypto)    | Volume transacted in the cryptocurrency           | BTC                              |
| Volume Base Ccy    | Volume transacted in the base currency            | USD                              |

### Augmented Features

| Variable           | Meaning                                           | Units                            |
|:-------------------|:--------------------------------------------------|:---------------------------------|
| Price Mean         | Average price computed from open, high, low, and close | USD                         |
| Upper Shadow       | Difference between the high and the maximum of open and close | USD                       |
| Lower Shadow       | Difference between the minimum of open and close and the low | USD                     |
| Spread             | Difference between the high and the low            | USD                              |
| Trade              | Difference between the closing and opening prices  | USD                              |
| 12EMA              | 12-period Exponential Moving Average of closing price | USD                          |
| 26EMA              | 26-period Exponential Moving Average of closing price | USD                          |
| MACD               | Moving Average Convergence Divergence (12EMA - 26EMA) | USD                          |
| Buy/Sell Signal    | Indicator of price movement (1 for buy, 0 for sell) | Binary (0 or 1)              |

### Citation
```bibtex
@misc{Kottarathil2020,
  author = {Prasoon Kottarathil},
  title = {Bitcoin Historical Dataset},
  year = {2020},
  publisher = {Kaggle},
  journal = {Kaggle Dataset},
  howpublished = {\url{https://www.kaggle.com/prasoonkottarathil/btcinusd}}
}
```
[Back to Table of contents](#table-of-contents)

# Machine Learning Project for Trading Company

## Business Requirements

The client is a trading company aiming to gain a competitive edge by identifying patterns in Bitcoin price movements to make informed trading decisions.

**Objective:**

1. Identify key variables that correlate with significant Bitcoin price changes.
2. Predict if Bitcoin's price will rise or fall in the near term and determine the likely trend strength. 

1. **Business Requirement 1:** Data Visualization and Correlation study:
   - Will inspect the data related to the closing price.
   - Will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to the closing price.
   - Will plot the main variables against the closing price to visualize insights.
   
2. **Business Requirement 2:** Classification, Regression:
   - We want to predict the closing price of the new day. Will build a regression model.
   - We want to predict if it is a good momnet o buy or to sell. We want to build a classification model for buy and sell signals.

[Back to Table of contents](#table-of-contents)

## Hypothesis and How to Validate

1. Hypothesis: Bitcoin price changes correlate with trading volume (in BTC and USD).

- Validation: A Correlation study can help in this investigation
   
2. Hypothesis: Daily closing prices are influenced by the daily high and low prices.

- Validation: A Correlation study can help in this investigation

[Back to Table of contents](#table-of-contents)

## The Rationale to Map the Business Requirements to the Data Visualizations and ML Tasks

### Epics:

- __Data collection and preparation__
- __Data visualization__
- __Model training, optimization, and evaluation__
- __Dashboard development and deployment__

### User stories:

#### Data Collection and Preparation

1. **User Story:** As a developer, I can gather and prepare a high-quality dataset to ensure reliable model training.
   - **Task:** Acquire the necessary datasets and organize them in a structured folder format for easy access.

#### Data Visualization

1. **User Story:** As a developer, I can create engaging visualizations to help stakeholders grasp key insights from the data.
   - **Task:** Select suitable visualization tools, generate visual representations, and export them for integration.

2. **User Story:** As a developer, I can embed visualizations within the dashboard to facilitate intuitive data exploration.
   - **Task:** Design a user-friendly interface that incorporates interactive visual elements.

#### Model Training, Optimization, and Evaluation

1. **User Story:** As a developer, I can identify the best hyperparameters for my model to enhance its performance.
   - **Task:** Implement hyperparameter tuning techniques such as Grid Search to determine optimal settings.

2. **User Story:** As a developer, I can train my machine learning model using the optimal hyperparameters to achieve accurate predictions.
   - **Task:** Define the model architecture and create functions that utilize the optimal parameters for training.

3. **User Story:** As a developer, I can assess my model's performance using various evaluation metrics to ensure it meets business requirements.
   - **Task:** Utilize machine learning libraries to conduct evaluations and visualize the results effectively.

4. **User Story:** As a user, I can view comprehensive evaluation results to understand the model's strengths and weaknesses.
   - **Task:** Create an interface that presents detailed performance reports for the user.

#### Dashboard Development and Deployment

1. **User Story:** As a developer, I can implement interactive features in Streamlit to enhance user engagement with the dashboard.
   - **Task:** Develop and integrate various Streamlit functionalities that make the dashboard intuitive and responsive.

2. **User Story:** As a developer, I can successfully deploy the Streamlit dashboard to ensure it is available for public use.
   - **Task:** Deploy the application on Heroku and confirm that users can access the dashboard online.


   [Back to Table of contents](#table-of-contents)

## ML Business Case for Each Model

### Predict Next Closing Price
- **Model Type**: Regression
- **Goal**: Predict the next closing price based on historical data.
- **Success Metrics**: 
  - R² score of at least 0.7.
- **Failure Conditions**: 
  - More than 30% of predictions being off by 20% after 6 months.

### Predict Buy/Sell Signals
- **Model Type**: Classification
- **Goal**: Predict whether the market trend is favorable for a "buy" or "sell" decision.
- **Success Metrics**: 
  - 80% recall for buy/sell signals.
- **Failure Conditions**: 
  - More than 30% incorrect buy/sell predictions after 3 months.

## Client Benefits
- Data-driven insights for better trading decisions.
- Real-time predictions for increased market responsiveness.
- Enhanced profitability by accurate forecasting of prices and trends.

[Back to Table of contents](#table-of-contents)

## Dashboard Design

### Page 1: Quick Project Summary
- Quick project summary
    - Project Terms & Jargon
    - Describe Project Dataset
    - State Business Requirements

### Page 2: Bitcoin Price Movement Correlation Study
- Adresses Business Requirement No. 1: Data Visualization and Correlation Study.
- Checkbox: Data inspection on Bitcoin metrics (display the number of rows and columns in the data, and display the first ten rows of the data).
- Checkbox: Individual plots for closing prices against high/low prices.
- Checkbox: Visualize the overlay plot for trading volume and price changes.

### Page 3: Bitcoin Price Prediction and Buy/Sell Signal
- Addresses Business Requirement No. 2: Price Forecasting, providing a brief overview of the prediction methods used while running predictions on live data.

### Page 4: Project Hypothesis and Validation
Before the analysis, we aimed to outline each project hypothesis, the conclusions drawn, and the validation methods employed. After conducting the data analysis, we can report the following:

- Hypothesis 1: Bitcoin price changes correlate with trading volume in USD.

This relationship is supported by our correlation study, indicating a significant link between price movements and trading volume in USD.

- Hypothesis 2: Daily closing prices of Bitcoin are influenced by the daily high and low prices, impacting the trend direction and strength.

This hypothesis is validated by correlation analysis, suggesting that further exploration of these variables is warranted.

### Page 5: Predict Buy/Sell Signals (Trend)
- Considerations and conclusions after the pipeline is trained
- Present ML pipeline steps
- Feature importance
- Pipeline performance
  
### Page 6: Predict Bitcoin Closing Price
- Considerations and conclusions after the pipeline is trained
- Present ML pipeline steps
- Feature importance
- Pipeline performance

[Back to Table of contents](#table-of-contents)

## Fixed Bugs

* The initial regression model struggled to make accurate predictions on live data. To address this, I developed Version 2 of the regression model, which involved a thorough review of the feature set. During this process, I eliminated the simple moving averages as they appeared redundant. Moreover, the 100-day and 50-day SMAs required a substantial amount of historical data to produce their first data points.

* After retraining Version 2 of the model, I observed improved results, although they were still not optimal. To further enhance performance, I accessed the dataset directly from the Binance API, which I refer to as 'live data.' This dataset includes approximately one year of additional historical data, providing more context. I retrained the model using this API data by fitting it with the transformed features, excluding the 'close' column for predictions. Then, I used the retrained model to predict the closing price for the most recent day, achieving satisfactory results. This approach significantly improved the model's predictive capability.

[Back to Table of contents](#table-of-contents)

## Unfixed Bugs

* There are no Unfixed Bugs.

[Back to Table of contents](#table-of-contents)

## Deployment to Heroku

* The App live link is: https://bitcoin-forecast-21da6c961a62.herokuapp.com/
*  Deployed on the Heroku-20 stack, this project utilizes a currently supported version of Python as outlined in the [Heroku documentation](https://devcenter.heroku.com/articles/python-support#supported-runtimes) 

* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

[Back to Table of contents](#table-of-contents)

## Main Data Analysis and Machine Learning Libraries

* Libraries used in this project:
- numpy==1.24.4
- pandas
- matplotlib==3.3.1
- seaborn
- streamlit
- joblib==1.4.2
- feature-engine==1.6.2
- scikit-learn==1.3.2

Examples: 
- Matplotlib is used extensively for creating and displaying various plots related to Bitcoin price movements.
- Pandas is used extensively for data manipulation and analysis.
- NumPy is used for a few key operations, primarily to perform mathematical calculations on the DataFrame.

[Back to Table of contents](#table-of-contents)

## Credits 

* This project draws inspiration from various sources, including the Code Institute Walkthrough Project 2 for general project structure and guidance. Additionally, the BTC to USD Dataset on Kaggle served as a key source for content inspiration and practical guidance on dataset handling and manipulation techniques.

### Content 

-  [BTC to USD Dataset on Kaggle](https://www.kaggle.com/prasoonkottarathil/btcinusd)

## Sources

The following resources were used as references and guides for this project:

1. [Churnometer repo by Code Institute](https://github.com/Code-Institute-Solutions/churnometer) - General guide for project structure.
2. [Data Plot Types for Visualization](https://www.analyticsvidhya.com/blog/2021/12/12-data-plot-types-for-visualization/) 
3. [Pandas Documentation: `date_range`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html) - Reference for generating date ranges in Pandas.
4. [Line Plots in Matplotlib](https://www.datacamp.com/tutorial/line-plots-in-matplotlib-with-python) - Tutorial on creating line plots using Matplotlib.
5. [BTC to USD Dataset on Kaggle](https://www.kaggle.com/prasoonkottarathil/btcinusd)

[Back to Table of contents](#table-of-contents)