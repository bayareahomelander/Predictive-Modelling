# Predictive Modeling Project
This project intends to create a supervised machine learning model using Python in order to predict whether a customer will churn (determine the current contract) or not.

Libraries used: Pandas, NumPy, MatplotLib, SciKit-Learn & Seaborn.

Tool used: Jupyter Notebook.

The project breaks down to 4 individual parts:

1. Preparation & Quick Check: imports necessary libraries, confirms datatypes, non-NaN values and categorical/numercial variables.
2. Exploratory Data Analysis: general feature exploration, data visualization using MatPlotLib and Seaborn (BoxPlot, CountPlot & BarPlot). This part of the project is to check for null values, visualize distribution and correlation between features. In addition, it also removes highly unique features, extracts categorical (non-numerical) values and assigns them with dummy variables. 
3. Churn Analysis: After part 2, it has been determined that Contract Type (tenure) is the most important feature when it comes to customer decision. Thus more in-depth analyses are applied. Since there's a negative correlation between churn rate and tenure, customers are divided into groups with a helper function, which categorizes customers based on contract length (e.g. 0 - 12 months, 12 - 24 months, 24 - 48 months and over 48 months). Correlation is then visualized using scatterplot.
4. Predictive Modeling: 4 tree-based methods are deployed here: Decision Tree, Random Forest, AdaBoost & Gradient Boosting. Each tree model is then evaluated using performance metrics: classification_report and confusionMatrix.

Best performance comes from AdaBoostClassfier

Potential future improvement for this project:
1. Perform GridSearching for optimal hyperparameters
2. Focus more on adjusting n_estimators such as doubling up

GitHub does not allow image upload in files, complete PDF file named "ML Project" with both image, code and comments with detailed analysis can be found under this project tree.
