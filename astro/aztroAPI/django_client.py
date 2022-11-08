from aztro.client import AztroClient


def get_client_from_settings(sign_name):
    return AztroClient(sign_name)
