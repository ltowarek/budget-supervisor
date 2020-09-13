# coding: utf-8

"""
    Salt Edge Account Information API

    API Reference for services  # noqa: E501

    OpenAPI spec version: 5.0.0
    Contact: support@saltedge.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.connections_api import ConnectionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestConnectionsApi(unittest.TestCase):
    """ConnectionsApi unit test stubs"""

    def setUp(self):
        self.api = ConnectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_connections_connection_id_delete(self):
        """Test case for connections_connection_id_delete

        Remove a connection  # noqa: E501
        """
        pass

    def test_connections_connection_id_get(self):
        """Test case for connections_connection_id_get

        Show a connection  # noqa: E501
        """
        pass

    def test_connections_connection_id_interactive_put(self):
        """Test case for connections_connection_id_interactive_put

        Interactive step  # noqa: E501
        """
        pass

    def test_connections_connection_id_put(self):
        """Test case for connections_connection_id_put

        Update connection  # noqa: E501
        """
        pass

    def test_connections_connection_id_reconnect_put(self):
        """Test case for connections_connection_id_reconnect_put

        Reconnect a connection  # noqa: E501
        """
        pass

    def test_connections_connection_id_refresh_put(self):
        """Test case for connections_connection_id_refresh_put

        Refresh a connection  # noqa: E501
        """
        pass

    def test_connections_get(self):
        """Test case for connections_get

        List of connections  # noqa: E501
        """
        pass

    def test_connections_post(self):
        """Test case for connections_post

        Create a connection  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
