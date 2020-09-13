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

class RefreshConnectionRequestBodyData(object):
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
        'attempt': 'AttemptRequestBody',
        'daily_refresh': 'bool',
        'include_fake_providers': 'bool',
        'categorization': 'str'
    }

    attribute_map = {
        'attempt': 'attempt',
        'daily_refresh': 'daily_refresh',
        'include_fake_providers': 'include_fake_providers',
        'categorization': 'categorization'
    }

    def __init__(self, attempt=None, daily_refresh=None, include_fake_providers=None, categorization='personal'):  # noqa: E501
        """RefreshConnectionRequestBodyData - a model defined in Swagger"""  # noqa: E501
        self._attempt = None
        self._daily_refresh = None
        self._include_fake_providers = None
        self._categorization = None
        self.discriminator = None
        if attempt is not None:
            self.attempt = attempt
        if daily_refresh is not None:
            self.daily_refresh = daily_refresh
        if include_fake_providers is not None:
            self.include_fake_providers = include_fake_providers
        if categorization is not None:
            self.categorization = categorization

    @property
    def attempt(self):
        """Gets the attempt of this RefreshConnectionRequestBodyData.  # noqa: E501


        :return: The attempt of this RefreshConnectionRequestBodyData.  # noqa: E501
        :rtype: AttemptRequestBody
        """
        return self._attempt

    @attempt.setter
    def attempt(self, attempt):
        """Sets the attempt of this RefreshConnectionRequestBodyData.


        :param attempt: The attempt of this RefreshConnectionRequestBodyData.  # noqa: E501
        :type: AttemptRequestBody
        """

        self._attempt = attempt

    @property
    def daily_refresh(self):
        """Gets the daily_refresh of this RefreshConnectionRequestBodyData.  # noqa: E501

        whether the connection should be automatically refreshed by Salt Edge.  # noqa: E501

        :return: The daily_refresh of this RefreshConnectionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._daily_refresh

    @daily_refresh.setter
    def daily_refresh(self, daily_refresh):
        """Sets the daily_refresh of this RefreshConnectionRequestBodyData.

        whether the connection should be automatically refreshed by Salt Edge.  # noqa: E501

        :param daily_refresh: The daily_refresh of this RefreshConnectionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._daily_refresh = daily_refresh

    @property
    def include_fake_providers(self):
        """Gets the include_fake_providers of this RefreshConnectionRequestBodyData.  # noqa: E501

        being [live](/general/#live), the customer will not be able to create [fake](#providers-fake) providers. This flag allows it, if sent as `true` the customer will have the possibility to create any fake provider available.  # noqa: E501

        :return: The include_fake_providers of this RefreshConnectionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._include_fake_providers

    @include_fake_providers.setter
    def include_fake_providers(self, include_fake_providers):
        """Sets the include_fake_providers of this RefreshConnectionRequestBodyData.

        being [live](/general/#live), the customer will not be able to create [fake](#providers-fake) providers. This flag allows it, if sent as `true` the customer will have the possibility to create any fake provider available.  # noqa: E501

        :param include_fake_providers: The include_fake_providers of this RefreshConnectionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._include_fake_providers = include_fake_providers

    @property
    def categorization(self):
        """Gets the categorization of this RefreshConnectionRequestBodyData.  # noqa: E501

        the type of categorization applied.  # noqa: E501

        :return: The categorization of this RefreshConnectionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._categorization

    @categorization.setter
    def categorization(self, categorization):
        """Sets the categorization of this RefreshConnectionRequestBodyData.

        the type of categorization applied.  # noqa: E501

        :param categorization: The categorization of this RefreshConnectionRequestBodyData.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "personal", "business"]  # noqa: E501
        if categorization not in allowed_values:
            raise ValueError(
                "Invalid value for `categorization` ({0}), must be one of {1}"  # noqa: E501
                .format(categorization, allowed_values)
            )

        self._categorization = categorization

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
        if issubclass(RefreshConnectionRequestBodyData, dict):
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
        if not isinstance(other, RefreshConnectionRequestBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
