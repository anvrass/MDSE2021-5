# MDSE2021-5
This is the Group 5 MDSE2021 github repository.

Overview of the Application
The application build for the first data engineering assignment is based on the dataset “Salt Lake City Housing Database”. The dataset consists of the house listings with the following attributes; acces, acres, amenities, days on the market, heating type, latitude, longitude, listed price, amount of floors, patio, parking spots, bathrooms, bedrooms, the area of the house in square feet, type of roof, taxes, sold price and year build. The aim of the application is to provide a prediction regarding the price of a house based on the specifications using a Ridge regression model.

The application consists of five operating containers: data storing container, pre-processing container, training container, predictions container and visualization container. In the first container, the data is fetched from the cloud and stored as readable data. This readable data is used by the second container for feature selection. The third container focuses on creating a model and training it based on the housing data. This trained model is used in the fourth container to predict housing prices, which are visualized in the fifth container. 
