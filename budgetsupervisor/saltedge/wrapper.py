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

    def show_customer(self, id):
        url = "https://www.saltedge.com/api/v5/customers/{}".format(id)
        response = self.salt_edge.get(url)
        response.raise_for_status()
        return response.json()

    def list_customers(self):
        url = "https://www.saltedge.com/api/v5/customers"
        response = self.salt_edge.get(url)
        response.raise_for_status()
        return response.json()

    def create_connect_session(self, customer_id, redirect_url):
        url = "https://www.saltedge.com/api/v5/connect_sessions/create"
        payload = json.dumps(
            {
                "data": {
                    "customer_id": str(customer_id),
                    "consent": {"scopes": ["account_details", "transactions_details"]},
                    "attempt": {"return_to": redirect_url},
                }
            }
        )
        response = self.salt_edge.post(url, payload)
        response.raise_for_status()
        return response.json()

    def create_connection(self, customer_id, country_code, provider_code):
        url = "https://www.saltedge.com/api/v5/connections"
        payload = json.dumps(
            {
                "data": {
                    "customer_id": str(customer_id),
                    "country_code": country_code,
                    "provider_code": provider_code,
                    "consent": {"scopes": ["account_details", "transactions_details"]},
                }
            }
        )
        response = self.salt_edge.post(url, payload)
        response.raise_for_status()
        return response.json()

    def remove_connection(self, id):
        url = "https://www.saltedge.com/api/v5/connections/{}".format(id)
        payload = json.dumps({})
        response = self.salt_edge.delete(url, payload)
        response.raise_for_status()
        return response.json()

    def show_connection(self, id):
        url = "https://www.saltedge.com/api/v5/connections/{}".format(id)
        response = self.salt_edge.get(url)
        response.raise_for_status()
        return response.json()

    def list_connections(self, customer_id):
        url = "https://www.saltedge.com/api/v5/connections?customer_id={}".format(
            customer_id
        )
        response = self.salt_edge.get(url)
        response.raise_for_status()
        return response.json()
