import random
import pandas as pd
from faker import Faker

fake = Faker()

def generate_transaction():
    return {
        "transaction_id": fake.uuid4(),
        "user_id": random.randint(1, 1000),
        "amount": round(random.uniform(1.0, 1000.0), 2),
        "location": fake.city(),
        "timestamp": fake.date_time_this_year().isoformat(),
        "is_fraud": random.choices([0, 1], weights=[99, 1], k=1)[0]
    }

# Generate synthetic dataset
transactions = [generate_transaction() for _ in range(10000)]
df = pd.DataFrame(transactions)
df.to_csv("synthetic_transactions.csv", index=False)
print("Synthetic dataset created!")
