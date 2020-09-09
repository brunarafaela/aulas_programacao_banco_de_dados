import sys
import traceback
from itertools import groupby

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8)
]

for user in users:
    user["age"] = []
    user["sex"] = []


for i, j in friendships:
    users[i]["age"].append(users[j])
    users[j]["age"].append(users[i])

    users[i]["sex"].append(users[j])
    users[j]["sex"].append(users[i])

def number_of_ages(user):
    return len(user['age'])

def number_of_users_sex(user):
    return len(user['sex'])

Conecctions = sum(number_of_ages(user) for user in users) and sum(number_of_users_sex(user) for user in users)

num_users = len(users)
div_connections = Conecctions / num_users