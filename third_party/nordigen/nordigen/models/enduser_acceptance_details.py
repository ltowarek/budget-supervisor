# coding: utf-8

"""
    Nordigen Account Information Services API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0 (v2)
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EnduserAcceptanceDetails(object):
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
        'user_agent': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'user_agent': 'user_agent',
        'ip_address': 'ip_address'
    }

    def __init__(self, user_agent=None, ip_address=None):  # noqa: E501
        """EnduserAcceptanceDetails - a model defined in Swagger"""  # noqa: E501
        self._user_agent = None
        self._ip_address = None
        self.discriminator = None
        self.user_agent = user_agent
        self.ip_address = ip_address

    @property
    def user_agent(self):
        """Gets the user_agent of this EnduserAcceptanceDetails.  # noqa: E501


        :return: The user_agent of this EnduserAcceptanceDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this EnduserAcceptanceDetails.


        :param user_agent: The user_agent of this EnduserAcceptanceDetails.  # noqa: E501
        :type: str
        """
        if user_agent is None:
            raise ValueError("Invalid value for `user_agent`, must not be `None`")  # noqa: E501

        self._user_agent = user_agent

    @property
    def ip_address(self):
        """Gets the ip_address of this EnduserAcceptanceDetails.  # noqa: E501


        :return: The ip_address of this EnduserAcceptanceDetails.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this EnduserAcceptanceDetails.


        :param ip_address: The ip_address of this EnduserAcceptanceDetails.  # noqa: E501
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

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
        if issubclass(EnduserAcceptanceDetails, dict):
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
        if not isinstance(other, EnduserAcceptanceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
