import os
from .saltedge import SaltEdge


def get_saltedge_app():
    return SaltEdge(os.environ["APP_ID"], os.environ["SECRET"], "saltedge/private.pem")
