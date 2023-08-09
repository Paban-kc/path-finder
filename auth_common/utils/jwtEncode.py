from rest_framework_simplejwt.tokens import AccessToken


def jwt_encode(user):
    token = AccessToken.for_user(user)
    return token
