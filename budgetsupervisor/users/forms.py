from django import forms
from saltedge.saltedge import SaltEdge
from .models import Profile
import os
import json


class ProfileConnectForm(forms.Form):
    def create_customer(self, profile):
        app = SaltEdge(
            os.environ["APP_ID"], os.environ["SECRET"], "saltedge/private.pem"
        )
        url = "https://www.saltedge.com/api/v5/customers"
        payload = json.dumps({"data": {"identifier": profile.user.id,}})
        response = app.post(url, payload)
        data = response.json()

        profile.external_id = data["data"]["id"]
        profile.save()
