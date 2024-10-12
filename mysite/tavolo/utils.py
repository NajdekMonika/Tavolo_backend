import numpy as np
from sklearn.cluster import KMeans
from .models import User, Table


def cluster_users():
    users = User.objects.filter(availability=True)
    if not users.exists():
        return

    interest_data = []
    user_ids = []
    for user in users:
        interest_data.append(list(user.interest_ratings.values()))
        user_ids.append(user.id)

    X = np.array(interest_data)

    nb_of_clusters = Table.objects.count()

    kmeans = KMeans(n_clusters=nb_of_clusters, random_state=0).fit(X)
    labels = kmeans.labels_

    for i, user_id in enumerate(user_ids):
        user = User.objects.get(id=user_id)
        table = Table.objects.get(number=labels[i] + 1)  # if table numbers start from 1
        table.users.add(user)


def update_clusters(instance):
    if instance.availability:
        cluster_users()
