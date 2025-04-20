# 1. Import necessary libraries
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import Binarizer
import joblib

# 2. Load diabetes dataset from sklearn
data = load_diabetes(as_frame=True)
X = data.data           # Features (inputs)
y = data.target         # Target (output)

# 3. Convert target from numbers to binary labels (0 or 1)
# We'll say: if target > 140 → diabetic (1), else → not diabetic (0)
binarizer = Binarizer(threshold=140)
y_binary = binarizer.fit_transform(y.values.reshape(-1, 1)).ravel()

# 4. Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

# 5. Train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 6. Save the trained model as model.pkl
joblib.dump(model, 'model.pkl')
