import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Load the dataset
df = pd.read_csv('C:/Users/user/Desktop/Github/Insurance_solution/data/MachineLearningRating_v3.txt', delimiter='|', low_memory=False)

# Step 2: Initial DataFrame Info
print("Initial dataset shape:", df.shape)
print("Initial DataFrame sample:")
print(df.head())

# Step 3: Identify numerical and categorical columns
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

# Step 4: Handle missing values
# Remove columns that are entirely empty
df_clean = df.dropna(axis=1, how='all')

# Ensure columns are in the DataFrame before imputation
existing_num_cols = [col for col in num_cols if col in df_clean.columns]
existing_cat_cols = [col for col in cat_cols if col in df_clean.columns]

# Impute numerical columns with mean
if existing_num_cols:
    num_imputer = SimpleImputer(strategy='mean')
    df_clean[existing_num_cols] = num_imputer.fit_transform(df_clean[existing_num_cols])

# Impute categorical columns with the most frequent value
if existing_cat_cols:
    cat_imputer = SimpleImputer(strategy='most_frequent')
    df_clean[existing_cat_cols] = cat_imputer.fit_transform(df_clean[existing_cat_cols])

# Optionally encode categorical variables
label_encoders = {}
for col in existing_cat_cols:
    le = LabelEncoder()
    df_clean[col] = le.fit_transform(df_clean[col])
    label_encoders[col] = le

# Step 5: Define the target variables
# You're predicting both TotalPremium and TotalClaims
target_columns = ['TotalPremium', 'TotalClaims']

# Check if both target columns are present in the DataFrame
for target_column in target_columns:
    if target_column not in df_clean.columns:
        raise ValueError(f"Target variable '{target_column}' not found in the DataFrame.")

# Features (X) are all columns except TotalPremium and TotalClaims
X = df_clean.drop(target_columns, axis=1)

# Target (y) are both TotalPremium and TotalClaims
y = df_clean[target_columns]

# Step 6: Train-Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Model Building and Evaluation
# Linear Regression for multi-target regression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predict both TotalPremium and TotalClaims
y_pred_lr = lr.predict(X_test)

# Evaluate the model for both targets
lr_mse_totalpremium = mean_squared_error(y_test['TotalPremium'], y_pred_lr[:, 0])
lr_mse_totalclaims = mean_squared_error(y_test['TotalClaims'], y_pred_lr[:, 1])

print("Mean Squared Error for TotalPremium prediction:", lr_mse_totalpremium)
print("Mean Squared Error for TotalClaims prediction:", lr_mse_totalclaims)
