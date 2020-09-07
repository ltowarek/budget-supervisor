from ..wrapper import SaltEdgeWrapper
import json


class MockSaltEdgeWrapper(SaltEdgeWrapper):
    def __init__(self, app_id, secret, private_path):
        super().__init__(app_id, secret, private_path)
        self.customers = []

    def create_customer(
        self,
        idetifier,
        mock_id="222222222222222222",
        mock_secret="AtQX6Q8vRyMrPjUVtW7J_O1n06qYQ25bvUJ8CIC80-8",
    ):
        customer = {
            "id": mock_id,
            "identifier": idetifier,
            "secret": mock_secret,
        }
        self.customers.append(customer)
        return {"data": customer}

    def remove_customer(self, id):
        self.customers = [c for c in self.customers if c["data"]["id"] != id]
        return {"data": {"deleted": True, "id": id,}}

    def list_customers(self):
        # TODO: Handle paging
        return {"data": self.customers, "meta": {"next_id": None, "next_page": None}}

    def create_connect_session(
        self,
        customer_id,
        redirect_url,
        mock_expiration="2020-09-04T14:54:35Z",
        mock_url="https://www.saltedge.com/connect?token=GENERATED_TOKEN",
    ):
        return {"data": {"expires_at": mock_expiration, "connect_url": mock_url,}}
