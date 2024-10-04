## Dataset Content
* Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size and to have a shorter model training time. If you are doing an image recognition project, we suggest you consider using an image shape that is 100px × 100px or 50px × 50px, to ensure the model meets the performance requirement but is smaller than 100Mb for a smoother push to GitHub. A reasonably sized image set is ~5000 images, but you can choose ~10000 lines for numeric or textual data. 


# Machine Learning Project for Trading Company

## Business Requirements
The client is a trading company looking to gain a competitive advantage by predicting asset prices and trends.

1. **Objective**: Predict the next closing price and asset trends (upward/downward movement).
2. **Conventional Data Analysis**: Analyze historical price data to identify patterns.
3. **Deliverable**: 
   - A dashboard that visualizes predicted trends and closing prices.
4. **Success Criteria**:
   - A fully functioning dashboard with accurate predictions.
   - Detailed study on trend predictions.
   - Accurate next closing price predictions.
5. **Project Breakdown**:
   - **Epics**: Data collection, feature engineering, model training, and dashboard development.
   - **User Stories**: Real-time predictions, trend visualization, and user-friendly interface.
6. **Ethical Considerations**: Data has a Creative Commons license (CC); no privacy concerns.
7. **Data-Driven Insight**: Use regression to predict closing price and classification for buy/sell signals.

## Hypothesis and How to Validate
1. **Hypothesis 1**: Historical price movements and volume can predict future closing prices.
   - **Validation**: Correlation study between historical price/volume and future prices.
   
2. **Hypothesis 2**: External factors such as news or market sentiment influence asset trends.
   - **Validation**: Time series analysis and correlation studies between external market indicators and trend movements.

## The Rationale to Map the Business Requirements to the Data Visualizations and ML Tasks
1. **Predict Next Closing Price**:
   - **Data Visualization**: Plot historical vs predicted closing prices using time series graphs.
   - **ML Task**: Regression model to predict the next closing price.
   
2. **Predict Asset Trend**:
   - **Data Visualization**: Historical trends with buy/sell signals.
   - **ML Task**: Classification model to predict if the trend will move up or down.

## ML Business Case for Each Model

### Predict Next Closing Price
- **Model Type**: Regression
- **Goal**: Predict the next closing price based on historical data.
- **Success Metrics**: 
  - R² score of at least 0.8.
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



## Acknowledgements (optional)
* Thank the people that provided support through this project.

