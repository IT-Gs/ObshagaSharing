_users = {
    'paul': {
        'Firstname': 'Pavel',
        'Lastname': 'Okop',
        'Username': 'PashaOk',
        'ObshagaAddress': 'Zaporozhskaya,21/A',
        'Room': '5',
        'Password': '1234567890'
    },
    'igor': {
        'Firstname': 'Igor',
        'Lastname': 'Dashkov',
        'Username': 'IgirDa',
        'ObshagaAddress': 'Vitebskaya,14',
        'Room': '23',
        'Password': '11111111'
    }
}


_user_list = []

for login, user_data in _users.items():
    _new_element = {'login': login}
    _new_element.update(user_data)
    _user_list.append(_new_element)


# Get users filtered by name
def get_users_by_name(q):
    results = []
    # SEARCH

    for user in _user_list:
       if user['Lastname'].lower() .find(q.lower()) >=0:
            results.append(user)

    return results


def get_user(username):
    return _users.get(username)





