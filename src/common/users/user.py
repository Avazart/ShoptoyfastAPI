


def authenticate_user(get_user_by_name, username: str, password: str):
    user = get_user_by_name(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
