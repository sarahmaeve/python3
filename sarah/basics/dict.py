

users = [
    {'first_name': 'Monica', 'last_name': 'Barents', 'uid': '4', 'last': '1592326630'},
    {'first_name': 'Angela', 'last_name': 'Johnson', 'uid': '128', 'last': '1571326642'},
    {'first_name': 'Bilal', 'last_name': 'Thabit', 'uid': '17', 'last': '1582326654'},
    {'first_name': 'Jyothi', 'last_name': 'Rao', 'uid': '240', 'last': '1560707847'},
    {'first_name': 'Lawrence', 'last_name': 'Cheng', 'uid': '311', 'last': '1592323341'},
    {'first_name': 'Alyx', 'last_name': 'Cormier', 'uid': '6', 'last': '1592326778'}
        ]

def sort_by_id(i):
    return int(i['uid'])


# for user in sorted(users, key=lambda i: int(i['uid'])):
for user in sorted(users, key=sort_by_id):
    print(user['uid'], user['last_name'], user['first_name'])

