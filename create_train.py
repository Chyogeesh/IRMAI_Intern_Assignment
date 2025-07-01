# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta
# import random

# # Parameters
# num_rows = 1000
# start_time = datetime.now() - timedelta(days=10)
# user_ids = ['user_1', 'user_2', 'user_3']

# # Generate data
# data = []
# for _ in range(num_rows):
#     timestamp = start_time + timedelta(minutes=random.randint(0, 14400))  # ~10 days worth
#     user_id = random.choice(user_ids)
#     response_time = np.random.normal(loc=200, scale=50)  # mean=200ms, std=50ms
#     anomaly = 1 if response_time > 300 or random.random() < 0.02 else 0  # Inject anomalies
#     data.append([user_id, timestamp, round(response_time, 2), anomaly])

# # Create DataFrame
# df = pd.DataFrame(data, columns=["user_id", "timestamp", "response_time", "anomaly"])

# # Save to CSV
# df.to_csv("train.csv", index=False)
# print("✅ train.csv generated successfully.")


# import pandas as pd

# data = [
#     {
#         "input": "User 123 had a spike in latency at 12:45PM",
#         "target": "This may indicate network congestion or a DDoS attack."
#     },
#     {
#         "input": "High CPU usage detected on server xyz",
#         "target": "Possible causes include inefficient code or a resource-intensive task."
#     },
#     {
#         "input": "Login attempts failed repeatedly for user456",
#         "target": "This could be a brute-force attack or the user forgot the password."
#     }
# ]

# df = pd.DataFrame(data)
# df.to_csv("data/train.csv", index=False)
# print("✅ train.csv created successfully!")


import pandas as pd
import random
from datetime import datetime, timedelta

# More realistic synthetic prompts
users = [f"user_{i}" for i in range(1, 6)]
issues = [
    ("response_time of 520ms", "This exceeds the normal threshold and may indicate a backend delay."),
    ("10 failed login attempts in 2 minutes", "This could be a brute-force login attack."),
    ("sudden balance drop of $5000", "Unusual withdrawal detected. Could be fraud or internal transfer."),
    ("transaction from a new device in Berlin", "Geolocation mismatch. Could be suspicious login."),
    ("CPU usage at 98% on node alpha", "System overload. Might be due to a misconfigured task.")
]

examples = []
for _ in range(1000):
    user = random.choice(users)
    issue, reason = random.choice(issues)
    timestamp = (datetime.now() - timedelta(hours=random.randint(0, 100))).strftime("%Y-%m-%d %H:%M")
    input_text = f"User {user} had {issue} at {timestamp}."
    examples.append({"input": input_text, "target": reason})

df = pd.DataFrame(examples)
df.to_csv("data/train.csv", index=False)
print("✅ Updated train.csv created with realistic anomaly explanations!")
