_users = {
    'paul': {
        'name': 'Pavel Ok',
        'job_title': 'Phd Candidate',
        'workplace': 'UiB'
    },
    'igor': {
        'name': 'igor Ot',
        'job_title': 'Student',
        'workplace': 'HSE'
    }
}

def get_user(username):
        return _users.get(username)
