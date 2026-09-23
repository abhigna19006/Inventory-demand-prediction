\# Inventory Demand Prediction and Stock Optimization Intelligence System



\## Project Overview



This project develops a Business Intelligence system for analyzing retail inventory, understanding sales patterns, predicting demand, and identifying potential inventory risks.



The project follows a complete analytics workflow:



\*\*Raw Data → Data Cleaning → EDA → Demand Prediction → Dashboard → Business Insights\*\*



\## Business Problem



Retail businesses need to maintain the right inventory levels.



Too much inventory can increase holding costs, while too little inventory can create potential stock shortages.



This project uses historical retail data to understand demand patterns and support better inventory planning.



\## Dataset



The project uses the Retail Store Inventory Forecasting Dataset.



Dataset size:



\- 73,100 records

\- 15 columns

\- No missing values

\- No duplicate rows after cleaning



Important fields include:



\- Date

\- Store ID

\- Product ID

\- Category

\- Region

\- Inventory Level

\- Units Sold

\- Units Ordered

\- Demand Forecast

\- Price

\- Discount

\- Weather Condition

\- Holiday/Promotion

\- Competitor Pricing

\- Seasonality



\## Data Cleaning



The data cleaning process includes:



\- Loading the raw CSV dataset

\- Checking missing values

\- Checking duplicate records

\- Converting the Date column to datetime format

\- Removing duplicate records

\- Removing invalid dates

\- Cleaning column names

\- Saving the cleaned dataset



The cleaned dataset is saved as:



`data/retail\_store\_inventory\_cleaned.csv`



\## Exploratory Data Analysis



The EDA analyzes:



\- Total units sold

\- Sales by category

\- Sales by region

\- Daily sales trends

\- Average inventory

\- Average units sold

\- Average units ordered

\- Demand forecast versus actual sales

\- Inventory gap

\- Potential inventory risk



\### Key Results



\- Total Units Sold: 9,975,582

\- Average Inventory Level: 274.47

\- Average Units Sold: 136.46

\- Average Demand Forecast: 141.49

\- Average Forecast Gap: 5.03 units



\## Demand Prediction



A Linear Regression model is used to predict Units Sold.



The model uses:



\- Inventory Level

\- Units Ordered

\- Price

\- Discount

\- Competitor Pricing



The dataset is divided into training and testing sets.



Model evaluation metrics include:



\- Mean Absolute Error (MAE)

\- Mean Squared Error (MSE)



The current model produced

