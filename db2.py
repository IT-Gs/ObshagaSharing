_users = {
    'paul': {
        'name': 'Pavel Ok',
        'job_title': 'Phd Candidate',
        'workplace': 'UiB'
    },
    'igor': {
        'name': 'igor Ok',
        'job_title': 'Phd Candidate',
        'workplace': 'UiB'
    }
}

def get_user(username):
        return _users.get(username)