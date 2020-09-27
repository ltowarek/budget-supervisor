from urllib.parse import urlparse
from django.http import HttpResponseRedirect


def get_url_path(response: HttpResponseRedirect) -> str:
    return urlparse(response.url).path.rstrip("/") + "/"
