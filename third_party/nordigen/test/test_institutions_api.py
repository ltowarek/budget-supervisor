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
from nordigen.api.institutions_api import InstitutionsApi  # noqa: E501
from nordigen.rest import ApiException


class TestInstitutionsApi(unittest.TestCase):
    """InstitutionsApi unit test stubs"""

    def setUp(self):
        self.api = InstitutionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_all_supported_institutions_in_a_given_country(self):
        """Test case for retrieve_all_supported_institutions_in_a_given_country

        """
        pass

    def test_retrieve_institution(self):
        """Test case for retrieve_institution

        """
        pass


if __name__ == '__main__':
    unittest.main()
