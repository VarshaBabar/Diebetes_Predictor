from pickle import load

# Load the saved model
with open("diab.pkl", "rb") as f:
    model = load(f)

# Get user input
fs = float(input("Enter fasting sugar: "))
fu = int(input("Freq. urination: 1 for no and 2 for yes: "))

# Prepare data based on input
if fu == 1:
    data = [[fs, 1, 0]]  # Mapping input to one-hot encoded values
else:
    data = [[fs, 0, 1]]

# Make prediction
ans = model.predict(data)
print("Diabetes prediction:", ans)
