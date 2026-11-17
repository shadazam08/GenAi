import pandas as pd
import numpy as np

# Reproducibility ke liye random seed set karein
np.random.seed(42)

n_rows = 10000

data = {
    "ID": range(1, n_rows + 1),
    "Gender": np.random.choice(["Male", "Female"], size=n_rows),
    "Age": np.random.randint(18, 28, size=n_rows),
    "Academic_Pressure": np.random.randint(1, 6, size=n_rows),
    "Study_Satisfaction": np.random.randint(1, 6, size=n_rows),
    "Sleep_Duration": np.random.choice(["Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"], size=n_rows),
    "Dietary_Habits": np.random.choice(["Healthy", "Moderate", "Unhealthy"], size=n_rows),
    "Suicidal_Thoughts": np.random.choice(["Yes", "No"], size=n_rows, p=[0.2, 0.8]),
    "Study_Hours": np.random.randint(1, 10, size=n_rows),
    "Financial_Stress": np.random.randint(1, 6, size=n_rows),
    "Family_History": np.random.choice(["Yes", "No"], size=n_rows, p=[0.3, 0.7]),
    "Depression": np.random.choice([0, 1], size=n_rows, p=[0.6, 0.4])
}

df = pd.DataFrame(data)

# CSV file ke taur par save karein
df.to_csv("student_depression_dataset.csv", index=False)
print("Dataset successfully created and saved as 'student_depression_dataset.csv'!")