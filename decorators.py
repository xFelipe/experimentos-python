from typing import List
import functools

ADMIN_PASSWORD = 'admin_password_here_1234zz*'
user = {'username': 'felipe', 'access_level': 'admin'}

def allowed_access(access_levels: List[str]):
    def decorator(func):
        @functools.wraps(func)
        def wrapped_function(*args, **kwargs):
            if user['access_level'] in access_levels:
                return func(*args, **kwargs)
            else:
                raise PermissionError(
                    f'User {user} have no one of following '
                    f'supported access levels: {access_levels}.'
                )
        return wrapped_function
    return decorator


if __name__ == '__main__':
    @allowed_access(['admin'])
    def get_admin_password():
        return ADMIN_PASSWORD

    assert get_admin_password() == print(ADMIN_PASSWORD) or ADMIN_PASSWORD
    user['access_level'] = 'gest'
    try:
        print(get_admin_password())
    except PermissionError as error:
        print(error)
    else:
        assert False, 'PermissionError not raised'
