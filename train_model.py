import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample
import pickle
import warnings

warnings.filterwarnings("ignore")

# ---------------------------
# Load dataset
# ---------------------------
df = pd.read_csv("data/anemia.csv")

majorclass = df[df['Result'] == 0]
minorclass = df[df['Result'] == 1]
major_downsample = resample(
    majorclass,
    replace=False,
    n_samples=len(minorclass),
    random_state=42
)
df = pd.concat([major_downsample, minorclass])

# Features & labels
X = df.drop("Result", axis=1)
Y = df["Result"]

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=20
)

# ---------------------------
# Train multiple models
# ---------------------------
models = {
    "LogisticRegression": LogisticRegression(),
    "RandomForest": RandomForestClassifier(),
    "DecisionTree": DecisionTreeClassifier(),
    "GaussianNB": GaussianNB(),
    "SVC": SVC(),
    "GradientBoosting": GradientBoostingClassifier()
}

best_model = None
best_acc = 0

for name, model in models.items():
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model: {name}")
    print("Accuracy:", acc)
    print(classification_report(y_test, y_pred))

    if acc > best_acc:
        best_acc = acc
        best_model = model

print(f"\n Best Model: {best_model.__class__.__name__} with Accuracy: {best_acc:.2f}")

# ---------------------------
# Save best model
# ---------------------------
pickle.dump(best_model, open("model.pkl", "wb"))
print(" Model saved as model.pkl")
