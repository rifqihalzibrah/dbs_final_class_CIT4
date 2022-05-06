def signup(data: dict):
    from eclass_final.models.user import signup
    error = ''
    if data:
        if data.get('name') and data.get('username') and data.get('password') and not data.get('id'):
            _, error = signup(data)
    return _, error


def login(data: dict):
    from eclass_final.models.user import login
    error = ''
    if data:
        if data.get('username') and data.get('password'):
            _, error = login(data)
    return _, error


def get_all_users():
    from eclass_final.models.user import get_all_users
    users, error = get_all_users()
    return users, error


def get_all_works():
    from eclass_final.models.user import get_all_works
    works, error = get_all_works()
    return works, error