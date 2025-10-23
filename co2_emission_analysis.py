# CO2 Emissions Forecasting Project
# Author: Francis Promise
# Description: This script analyzes CO2 emissions data and predicts future emissions using Linear Regression.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load dataset (replace with your actual path if needed)
file_path = 'CO2 emissions per capita - cleaned - excel.xlsx'
df = pd.read_excel(file_path)

# Clean and prepare data
df.columns = df.columns.astype(str)
df_clean = df.loc[:, ~df.columns.str.contains('^Unnamed', na=False)]

# Focus on Nigeria as an example
nigeria_data = df_clean[df_clean['Country Name'] == 'Nigeria'].iloc[:, 2:]
nigeria_data = nigeria_data.transpose().reset_index()
nigeria_data.columns = ['Year', 'CO2_per_capita']
nigeria_data['Year'] = nigeria_data['Year'].astype(float)
nigeria_data.dropna(inplace=True)

# Plot historical CO2 emissions for Nigeria
plt.figure(figsize=(10, 6))
plt.plot(nigeria_data['Year'], nigeria_data['CO2_per_capita'], marker='o')
plt.title('Nigeria CO₂ Emissions per Capita (1990–2021)')
plt.xlabel('Year')
plt.ylabel('CO₂ (metric tons per capita)')
plt.grid(True)
plt.show()

# Predict future CO2 emissions (2025–2030)
X = nigeria_data[['Year']]
y = nigeria_data['CO2_per_capita']
model = LinearRegression()
model.fit(X, y)

future_years = np.array([2025, 2026, 2027, 2028, 2029, 2030]).reshape(-1, 1)
predictions = model.predict(future_years)

# Create prediction dataframe
pred_df = pd.DataFrame({'Year': future_years.flatten(), 'Predicted_CO2_per_capita': predictions})
print(pred_df)

# Plot predictions
plt.figure(figsize=(10, 6))
plt.plot(nigeria_data['Year'], nigeria_data['CO2_per_capita'], label='Historical', marker='o')
plt.plot(pred_df['Year'], pred_df['Predicted_CO2_per_capita'], label='Predicted', marker='x', linestyle='--')
plt.title('Nigeria CO₂ Emissions Forecast (to 2030)')
plt.xlabel('Year')
plt.ylabel('CO₂ (metric tons per capita)')
plt.legend()
plt.grid(True)
plt.show()

# Save predicted data to CSV
pred_df.to_csv('predicted_co2_emissions.csv', index=False)
print("Predicted data saved as 'predicted_co2_emissions.csv'.")
