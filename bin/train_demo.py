
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the NFL data from your notebook
data = pd.read_csv("nfl_mvp_features.csv")

# Choose the player statistics used by the model
features = [
    "PassingYards",
    "PassingTouchdowns",
    "RushingYards",
    "RushingTouchdowns",
    "ReceivingYards",
    "ReceivingTouchdowns"
]

# Check whether MVP labels are available
if "MVP" not in data.columns:
    print("NFL data loaded successfully!")
    print("MVP labels are missing. Add historical MVP winners to train the model.")
else:
    data = data.dropna(subset=features + ["MVP"])
    X = data[features]
    y = data["MVP"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    print("Model trained successfully!")
    print("Model accuracy:", model.score(X_test, y_test))
