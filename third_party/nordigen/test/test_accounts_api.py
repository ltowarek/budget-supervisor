# coding: utf-8

"""
    Nordigen Account Information Services API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0 (v2)
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import nordigen
from nordigen.api.accounts_api import AccountsApi  # noqa: E501
from nordigen.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_account_balances(self):
        """Test case for retrieve_account_balances

        """
        pass

    def test_retrieve_account_details(self):
        """Test case for retrieve_account_details

        """
        pass

    def test_retrieve_account_metadata(self):
        """Test case for retrieve_account_metadata

        """
        pass

    def test_retrieve_account_transactions(self):
        """Test case for retrieve_account_transactions

        """
        pass


if __name__ == '__main__':
    unittest.main()
