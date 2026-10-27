
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Small example dataset for demonstrating the workflow
data = pd.DataFrame({
    "passing_yards": [300, 250, 350, 180, 320, 200, 280, 150],
    "passing_tds":   [3, 2, 4, 1, 3, 1, 2, 0],
    "rushing_yards": [20, 40, 15, 80, 30, 60, 25, 90],
    "mvp":            [1, 0, 1, 0, 1, 0, 0, 0],
})

features = ["passing_yards", "passing_tds", "rushing_yards"]
X = data[features]
y = data["mvp"]

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

# Demonstrate a prediction for a hypothetical player
player = pd.DataFrame([{
    "passing_yards": 320,
    "passing_tds": 3,
    "rushing_yards": 25,
}])

probability = model.predict_proba(player)[0][
    list(model.classes_).index(1)
]

print(f"Demo MVP probability: {probability:.1%}")
print("This is a demonstration using fictional sample data.")
