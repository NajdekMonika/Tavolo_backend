import numpy as np
from sklearn.cluster import KMeans

NB_TABLES = 5
user_names = [f'user{idx}' for idx in range(20)]
interests = [f'interest{idx}' for idx in range(5)]

Users = {user: {interest: np.random.randint(1, 5) for interest in interests} for user in user_names}
print(Users)

interests = []
for user, interest_ratings in Users.items():
    interests.append(list(interest_ratings.values()))

X = np.array(interests)
kmeans = KMeans(n_clusters=NB_TABLES, random_state=42).fit(X)
labels = kmeans.labels_

assigned_tables = {user: labels[index] + 1 for index, user in enumerate(user_names)}
print(assigned_tables)
nb_of_ppl_per_table = {f"table_{table}": list(assigned_tables.values()).count(table) for table in range(1, NB_TABLES + 1)}
print(nb_of_ppl_per_table)
