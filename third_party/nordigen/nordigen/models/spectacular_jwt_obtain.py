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

class SpectacularJWTObtain(object):
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
        'password': 'str',
        'access': 'str',
        'access_expires': 'int',
        'refresh': 'str',
        'refresh_expires': 'int'
    }

    attribute_map = {
        'password': 'password',
        'access': 'access',
        'access_expires': 'access_expires',
        'refresh': 'refresh',
        'refresh_expires': 'refresh_expires'
    }

    def __init__(self, password=None, access=None, access_expires=86400, refresh=None, refresh_expires=2592000):  # noqa: E501
        """SpectacularJWTObtain - a model defined in Swagger"""  # noqa: E501
        self._password = None
        self._access = None
        self._access_expires = None
        self._refresh = None
        self._refresh_expires = None
        self.discriminator = None
        if password is not None:
            self.password = password
        self.access = access
        self.access_expires = access_expires
        self.refresh = refresh
        self.refresh_expires = refresh_expires

    @property
    def password(self):
        """Gets the password of this SpectacularJWTObtain.  # noqa: E501


        :return: The password of this SpectacularJWTObtain.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SpectacularJWTObtain.


        :param password: The password of this SpectacularJWTObtain.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def access(self):
        """Gets the access of this SpectacularJWTObtain.  # noqa: E501

        Your access token  # noqa: E501

        :return: The access of this SpectacularJWTObtain.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this SpectacularJWTObtain.

        Your access token  # noqa: E501

        :param access: The access of this SpectacularJWTObtain.  # noqa: E501
        :type: str
        """
        if access is None:
            raise ValueError("Invalid value for `access`, must not be `None`")  # noqa: E501

        self._access = access

    @property
    def access_expires(self):
        """Gets the access_expires of this SpectacularJWTObtain.  # noqa: E501

        Access token expires in seconds  # noqa: E501

        :return: The access_expires of this SpectacularJWTObtain.  # noqa: E501
        :rtype: int
        """
        return self._access_expires

    @access_expires.setter
    def access_expires(self, access_expires):
        """Sets the access_expires of this SpectacularJWTObtain.

        Access token expires in seconds  # noqa: E501

        :param access_expires: The access_expires of this SpectacularJWTObtain.  # noqa: E501
        :type: int
        """
        if access_expires is None:
            raise ValueError("Invalid value for `access_expires`, must not be `None`")  # noqa: E501

        self._access_expires = access_expires

    @property
    def refresh(self):
        """Gets the refresh of this SpectacularJWTObtain.  # noqa: E501

        Your refresh token  # noqa: E501

        :return: The refresh of this SpectacularJWTObtain.  # noqa: E501
        :rtype: str
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this SpectacularJWTObtain.

        Your refresh token  # noqa: E501

        :param refresh: The refresh of this SpectacularJWTObtain.  # noqa: E501
        :type: str
        """
        if refresh is None:
            raise ValueError("Invalid value for `refresh`, must not be `None`")  # noqa: E501

        self._refresh = refresh

    @property
    def refresh_expires(self):
        """Gets the refresh_expires of this SpectacularJWTObtain.  # noqa: E501

        Refresh token expires in seconds  # noqa: E501

        :return: The refresh_expires of this SpectacularJWTObtain.  # noqa: E501
        :rtype: int
        """
        return self._refresh_expires

    @refresh_expires.setter
    def refresh_expires(self, refresh_expires):
        """Sets the refresh_expires of this SpectacularJWTObtain.

        Refresh token expires in seconds  # noqa: E501

        :param refresh_expires: The refresh_expires of this SpectacularJWTObtain.  # noqa: E501
        :type: int
        """
        if refresh_expires is None:
            raise ValueError("Invalid value for `refresh_expires`, must not be `None`")  # noqa: E501

        self._refresh_expires = refresh_expires

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
        if issubclass(SpectacularJWTObtain, dict):
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
        if not isinstance(other, SpectacularJWTObtain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
