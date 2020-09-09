from ..wrapper import SaltEdgeWrapper
import json


class MockSaltEdgeWrapper(SaltEdgeWrapper):
    def __init__(self, app_id, secret, private_path):
        super().__init__(app_id, secret, private_path)
        self.customers = []
        self.connections = []
        self.accounts = []

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
        self.customers = [c for c in self.customers if c["id"] != id]
        return {"data": {"id": id, "deleted": True}}

    def show_customer(self, id):
        for c in self.customers:
            if c["id"] == id:
                return {"data": c}

    def list_customers(self):
        return {"data": self.customers, "meta": {"next_id": None, "next_page": None}}

    def create_connect_session(
        self, customer_id, redirect_url,
    ):
        return {
            "data": {
                "expires_at": "2020-09-04T14:54:35Z",
                "connect_url": "https://www.saltedge.com/connect?token=GENERATED_TOKEN",
            }
        }

    def create_connection(self, customer_id):
        connection = {
            "id": "111111111111111111",
            "secret": "AtQX6Q8vRyMrPjUVtW7J_O1n06qYQ25bvUJ8CIC80-8",
            "provider_id": "1234",
            "provider_code": "fakebank_simple_xf",
            "provider_name": "Fakebank Simple",
            "customer_id": str(customer_id),
            "next_refresh_possible_at": "2020-09-07T12:35:46Z",
            "created_at": "2020-09-06T11:35:46Z",
            "updated_at": "2020-09-07T10:55:46Z",
            "status": "active",
            "categorization": "personal",
            "daily_refresh": False,
            "store_credentials": True,
            "country_code": "XF",
            "last_success_at": "2020-09-07T10:55:46Z",
            "show_consent_confirmation": False,
            "last_consent_id": "555555555555555555",
            "last_attempt": {
                "api_mode": "service",
                "api_version": "5",
                "automatic_fetch": True,
                "user_present": True,
                "daily_refresh": False,
                "categorization": "personal",
                "created_at": "2020-09-07T10:55:46Z",
                "customer_last_logged_at": "2020-09-07T08:35:46Z",
                "custom_fields": {},
                "device_type": "desktop",
                "remote_ip": "93.184.216.34",
                "exclude_accounts": [],
                "fail_at": None,
                "fail_error_class": None,
                "fail_message": None,
                "fetch_scopes": ["accounts", "transactions"],
                "finished": True,
                "finished_recent": True,
                "from_date": "2020-06-07",
                "id": "777777777777777777",
                "interactive": False,
                "locale": "en",
                "partial": False,
                "store_credentials": True,
                "success_at": "2020-09-07T10:55:46Z",
                "to_date": "2020-09-07",
                "updated_at": "2020-09-07T10:55:46Z",
                "show_consent_confirmation": False,
                "consent_id": "555555555555555555",
                "include_natures": ["account", "card", "bonus"],
                "last_stage": {
                    "created_at": "2020-09-07T10:55:46Z",
                    "id": "888888888888888888",
                    "interactive_fields_names": None,
                    "interactive_html": None,
                    "name": "finish",
                    "updated_at": "2020-09-07T10:55:46Z",
                },
            },
        }
        self.connections.append(connection)
        return {"data": connection}

    def remove_connection(self, id):
        self.connections = [c for c in self.connections if c["id"] != id]
        return {"data": {"deleted": True, "id": id,}}

    def show_connection(self, id):
        for c in self.connections:
            if c["id"] == id:
                return {"data": c}

    def list_connections(self, customer_id):
        return {
            "data": self.connections,
            "meta": {"next_id": None, "next_page": None,},
        }

    def create_account(self, connection_id):
        account = {
            "id": "333333333333333333",
            "connection_id": str(connection_id),
            "name": "Fake account 1",
            "nature": "card",
            "balance": 2007.2,
            "currency_code": "EUR",
            "extra": {"client_name": "Fake name"},
            "created_at": "2020-09-07T08:35:46Z",
            "updated_at": "2020-09-07T08:35:46Z",
        }
        self.accounts.append(account)
        return account

    def list_accounts(self, connection_id):
        return {
            "data": self.accounts,
            "meta": {"next_id": None, "next_page": None,},
        }
