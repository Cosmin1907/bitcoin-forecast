## Dataset Content
* Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size and to have a shorter model training time. If you are doing an image recognition project, we suggest you consider using an image shape that is 100px × 100px or 50px × 50px, to ensure the model meets the performance requirement but is smaller than 100Mb for a smoother push to GitHub. A reasonably sized image set is ~5000 images, but you can choose ~10000 lines for numeric or textual data. 


# Machine Learning Project for Trading Company

## Business Requirements

The client is a trading company aiming to gain a competitive edge by identifying patterns in Bitcoin price movements to make informed trading decisions.

**Objective:**

1. Identify key variables that correlate with significant Bitcoin price changes.
2. Predict if Bitcoin's price will rise or fall in the near term and determine the likely trend strength. 

## Hypothesis and How to Validate

1. Hypothesis: Bitcoin price changes correlate with trading volume (in BTC and USD).

- Validation: A Correlation study can help in this investigation
   
2. Hypothesis: Daily closing prices are influenced by the daily high and low prices.

- Validation: A Correlation study can help in this investigation

## The Rationale to Map the Business Requirements to the Data Visualizations and ML Tasks
1. **Business Requirement 1:** Data Visualization and Correlation study:
   - Will inspect the data related to the closing price.
   - Will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to the closing price.
   - Will plot the main variables against the closing price to visualize insights.
   
2. **Business Requirement 2:** Classification, Regression:
   - We want to predict the closing price of the new day. Will build a regression model.
   - We want to predict if it is a good momnet o buy or to sell. We want to build a classification model for buy and sell signals.

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


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site


## Sources: 
https://www.analyticsvidhya.com/blog/2021/12/12-data-plot-types-for-visualization/
https://pandas.pydata.org/docs/reference/api/pandas.date_range.html
https://www.datacamp.com/tutorial/line-plots-in-matplotlib-with-python
Code institute walktrugh project 2

