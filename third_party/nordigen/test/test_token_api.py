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
from nordigen.api.token_api import TokenApi  # noqa: E501
from nordigen.rest import ApiException


class TestTokenApi(unittest.TestCase):
    """TokenApi unit test stubs"""

    def setUp(self):
        self.api = TokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_j_wt_obtain(self):
        """Test case for j_wt_obtain

        """
        pass

    def test_j_wt_refresh(self):
        """Test case for j_wt_refresh

        """
        pass


if __name__ == '__main__':
    unittest.main()