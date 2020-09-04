from .saltedge import SaltEdge
import json


class SaltEdgeWrapper:
    def __init__(self, app_id, secret, private_path):
        self.salt_edge = SaltEdge(app_id, secret, private_path)

    def create_customer(self, identifier):
        url = "https://www.saltedge.com/api/v5/customers"
        payload = json.dumps({"data": {"identifier": identifier}})
        response = self.salt_edge.post(url, payload)
        response.raise_for_status()
        return response.json()

    def remove_customer(self, id):
        url = "https://www.saltedge.com/api/v5/customers/{}".format(id)
        payload = json.dumps({})
        response = self.salt_edge.delete(url, payload)
        response.raise_for_status()
        return response.json()

    def list_customers(self):
        url = "https://www.saltedge.com/api/v5/customers"
        response = self.salt_edge.get(url)
        response.raise_for_status()
        return response.json()
