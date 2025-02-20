import pandas as pd
from sklearn.linear_model import LogisticRegression
from pickle import dump

# Load data
data = pd.read_csv("diabetes.csv")
print(data)

# Define features and target
features = data[["FS", "FU"]]  # FS: Fasting Sugar, FU: Frequent Urination
target = data["Diabetes"]

# Convert categorical variables to dummy variables
nfeatures = pd.get_dummies(features)

# Initialize Logistic Regression model and fit the data
model = LogisticRegression()
model.fit(nfeatures.values, target)

# Save the model to a file
with open("diab.pkl", "wb") as f:
    dump(model, f)
