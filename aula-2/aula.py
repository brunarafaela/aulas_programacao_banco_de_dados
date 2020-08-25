

users = [
    {
        "id": 0,
        "name":  "Hero",

    },
    {
        "id": 1,
        "name":  "Dunn",

    },
    {
        "id": 2,
        "name":  "Sue",

    },
    {
        "id": 3,
        "name":  "Chi",

    },
    {
        "id": 4,
        "name":  "Thor",

    },
    {
        "id": 5,
        "name":  "Clive",

    },
    {
        "id": 6,
        "name":  "Hicks",

    },
    {
        "id": 7,
        "name":  "Devin",
    },
    {
        "id": 8,
        "name":  "Kate",

    },
    {
        "id": 9,
        "name":  "Klein"

    },
]

# lista = [1,2,3,4,5]
# lista[2] = 7
# lista = [1, 2]

# tupla = (1,2,3,4,5)
# print(tupla[2])
# tupla [2] = 3
# tupla (9, 9, 1)
# tupla = 2

frindships =[
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3,4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]
for user in users:
    user["friends"] = []

for i, j in frindships:
   users[i] ["friends"].append(users[j])
   users[j] ["friends"].append(users[i])

# print(users)  

# int numero (int a, int b){
#     return a + b;
# } 

def soma (a,b):
    return a + b
    
def number_of_fiends (user):
    return len (user['friends'])

print(number_of_fiends(users[0]))
