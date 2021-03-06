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

class UpdateConnectionRequestBodyData(object):
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
        'status': 'str',
        'daily_refresh': 'bool',
        'store_credentials': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'daily_refresh': 'daily_refresh',
        'store_credentials': 'store_credentials'
    }

    def __init__(self, status=None, daily_refresh=None, store_credentials=True):  # noqa: E501
        """UpdateConnectionRequestBodyData - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._daily_refresh = None
        self._store_credentials = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if daily_refresh is not None:
            self.daily_refresh = daily_refresh
        if store_credentials is not None:
            self.store_credentials = store_credentials

    @property
    def status(self):
        """Gets the status of this UpdateConnectionRequestBodyData.  # noqa: E501


        :return: The status of this UpdateConnectionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateConnectionRequestBodyData.


        :param status: The status of this UpdateConnectionRequestBodyData.  # noqa: E501
        :type: str
        """
        allowed_values = ["inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def daily_refresh(self):
        """Gets the daily_refresh of this UpdateConnectionRequestBodyData.  # noqa: E501

        whether the connection will be refreshed daily  # noqa: E501

        :return: The daily_refresh of this UpdateConnectionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._daily_refresh

    @daily_refresh.setter
    def daily_refresh(self, daily_refresh):
        """Sets the daily_refresh of this UpdateConnectionRequestBodyData.

        whether the connection will be refreshed daily  # noqa: E501

        :param daily_refresh: The daily_refresh of this UpdateConnectionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._daily_refresh = daily_refresh

    @property
    def store_credentials(self):
        """Gets the store_credentials of this UpdateConnectionRequestBodyData.  # noqa: E501

        allows to not store credentials on Salt Edge side.  <strong>Note:</strong> The usage of this flag is not available for `file` providers. In order to update the connection, reconnect is required. It will not be possible to use refresh option if `store_credentials` is set to `false`   # noqa: E501

        :return: The store_credentials of this UpdateConnectionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._store_credentials

    @store_credentials.setter
    def store_credentials(self, store_credentials):
        """Sets the store_credentials of this UpdateConnectionRequestBodyData.

        allows to not store credentials on Salt Edge side.  <strong>Note:</strong> The usage of this flag is not available for `file` providers. In order to update the connection, reconnect is required. It will not be possible to use refresh option if `store_credentials` is set to `false`   # noqa: E501

        :param store_credentials: The store_credentials of this UpdateConnectionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._store_credentials = store_credentials

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
        if issubclass(UpdateConnectionRequestBodyData, dict):
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
        if not isinstance(other, UpdateConnectionRequestBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
