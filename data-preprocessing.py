# Import Libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load Data
data = pd.read_csv('sales_data.csv')

# Data Preprocessing
# Handle missing values
data.ffill(inplace=True)

# Print column names to ensure correct column reference
print(data.columns)

# Encoding categorical variables
label_encoder = LabelEncoder()

# Assuming 'User ID' and 'Product ID' are the columns that need encoding
data['User ID'] = label_encoder.fit_transform(data['User ID'])
data['Product ID'] = label_encoder.fit_transform(data['Product ID'])

# Save the preprocessed data for future use
data.to_csv('preprocessed_sales_data.csv', index=False)