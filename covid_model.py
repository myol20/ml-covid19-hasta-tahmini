print("PROGRAM BAŞLADI")

import pandas as pd

df = pd.read_csv("Covid Dataset.csv")

print(df.head())

print("PROGRAM BİTTİ")
import pandas as pd

df = pd.read_csv("Covid Dataset.csv")
df["COVID-19"] = df["COVID-19"].map({"Yes": 1, "No": 0})
df = df.replace({"Yes": 1, "No": 0})

# hedef değişken (sonuç sütunu)
y = df["COVID-19"]   # burada sütun adı farklı olabilir
X = df.drop("COVID-19", axis=1)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.linear_model import LogisticRegression

model_lr = LogisticRegression(max_iter=1000)
model_lr.fit(X_train, y_train)

y_pred_lr = model_lr.predict(X_test)
from sklearn.ensemble import RandomForestClassifier

model_rf = RandomForestClassifier()
model_rf.fit(X_train, y_train)

y_pred_rf = model_rf.predict(X_test)
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("LR Accuracy:", accuracy_score(y_test, y_pred_lr))
print("RF Accuracy:", accuracy_score(y_test, y_pred_rf))

print("Confusion Matrix RF:\n", confusion_matrix(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))
print(df.columns)
print("PROGRAM BAŞLADI")

import pandas as pd

df = pd.read_csv("Covid Dataset.csv")

print(df.head())
print(df.columns)

print("PROGRAM BİTTİ")

