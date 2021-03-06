# coding: utf-8

"""
    Salt Edge Account Information API

    API Reference for services  # noqa: E501

    OpenAPI spec version: 5.0.0
    Contact: support@saltedge.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConnectSessionResponseData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'expires_at': 'datetime',
        'connect_url': 'str'
    }

    attribute_map = {
        'expires_at': 'expires_at',
        'connect_url': 'connect_url'
    }

    def __init__(self, expires_at=None, connect_url=None):  # noqa: E501
        """ConnectSessionResponseData - a model defined in Swagger"""  # noqa: E501
        self._expires_at = None
        self._connect_url = None
        self.discriminator = None
        if expires_at is not None:
            self.expires_at = expires_at
        if connect_url is not None:
            self.connect_url = connect_url

    @property
    def expires_at(self):
        """Gets the expires_at of this ConnectSessionResponseData.  # noqa: E501


        :return: The expires_at of this ConnectSessionResponseData.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this ConnectSessionResponseData.


        :param expires_at: The expires_at of this ConnectSessionResponseData.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def connect_url(self):
        """Gets the connect_url of this ConnectSessionResponseData.  # noqa: E501


        :return: The connect_url of this ConnectSessionResponseData.  # noqa: E501
        :rtype: str
        """
        return self._connect_url

    @connect_url.setter
    def connect_url(self, connect_url):
        """Sets the connect_url of this ConnectSessionResponseData.


        :param connect_url: The connect_url of this ConnectSessionResponseData.  # noqa: E501
        :type: str
        """

        self._connect_url = connect_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConnectSessionResponseData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConnectSessionResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
