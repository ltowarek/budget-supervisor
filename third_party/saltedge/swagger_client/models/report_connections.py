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

class ReportConnections(object):
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
        'id': 'str',
        'customer_id': 'int',
        'provider_code': 'str',
        'provider_name': 'str',
        'accounts': 'list[ReportAccounts]',
        'holder_info': 'str',
        'client_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'customer_id': 'customer_id',
        'provider_code': 'provider_code',
        'provider_name': 'provider_name',
        'accounts': 'accounts',
        'holder_info': 'holder_info',
        'client_name': 'client_name'
    }

    def __init__(self, id=None, customer_id=None, provider_code=None, provider_name=None, accounts=None, holder_info=None, client_name=None):  # noqa: E501
        """ReportConnections - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._customer_id = None
        self._provider_code = None
        self._provider_name = None
        self._accounts = None
        self._holder_info = None
        self._client_name = None
        self.discriminator = None
        self.id = id
        self.customer_id = customer_id
        self.provider_code = provider_code
        self.provider_name = provider_name
        self.accounts = accounts
        self.holder_info = holder_info
        self.client_name = client_name

    @property
    def id(self):
        """Gets the id of this ReportConnections.  # noqa: E501

        The `id` of the [connection](#connections)  # noqa: E501

        :return: The id of this ReportConnections.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportConnections.

        The `id` of the [connection](#connections)  # noqa: E501

        :param id: The id of this ReportConnections.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def customer_id(self):
        """Gets the customer_id of this ReportConnections.  # noqa: E501

        The `id` of the [customer](#customers)  # noqa: E501

        :return: The customer_id of this ReportConnections.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ReportConnections.

        The `id` of the [customer](#customers)  # noqa: E501

        :param customer_id: The customer_id of this ReportConnections.  # noqa: E501
        :type: int
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def provider_code(self):
        """Gets the provider_code of this ReportConnections.  # noqa: E501

        the code of the [Provider](#providers) the connection belongs to  # noqa: E501

        :return: The provider_code of this ReportConnections.  # noqa: E501
        :rtype: str
        """
        return self._provider_code

    @provider_code.setter
    def provider_code(self, provider_code):
        """Sets the provider_code of this ReportConnections.

        the code of the [Provider](#providers) the connection belongs to  # noqa: E501

        :param provider_code: The provider_code of this ReportConnections.  # noqa: E501
        :type: str
        """
        if provider_code is None:
            raise ValueError("Invalid value for `provider_code`, must not be `None`")  # noqa: E501

        self._provider_code = provider_code

    @property
    def provider_name(self):
        """Gets the provider_name of this ReportConnections.  # noqa: E501

        the name of the [Provider](#providers) the connection belongs to  # noqa: E501

        :return: The provider_name of this ReportConnections.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this ReportConnections.

        the name of the [Provider](#providers) the connection belongs to  # noqa: E501

        :param provider_name: The provider_name of this ReportConnections.  # noqa: E501
        :type: str
        """
        if provider_name is None:
            raise ValueError("Invalid value for `provider_name`, must not be `None`")  # noqa: E501

        self._provider_name = provider_name

    @property
    def accounts(self):
        """Gets the accounts of this ReportConnections.  # noqa: E501

        information related to accounts, which belong to this connection  # noqa: E501

        :return: The accounts of this ReportConnections.  # noqa: E501
        :rtype: list[ReportAccounts]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this ReportConnections.

        information related to accounts, which belong to this connection  # noqa: E501

        :param accounts: The accounts of this ReportConnections.  # noqa: E501
        :type: list[ReportAccounts]
        """
        if accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

    @property
    def holder_info(self):
        """Gets the holder_info of this ReportConnections.  # noqa: E501

        essential information about the account holder fetched from the connected provider  # noqa: E501

        :return: The holder_info of this ReportConnections.  # noqa: E501
        :rtype: str
        """
        return self._holder_info

    @holder_info.setter
    def holder_info(self, holder_info):
        """Sets the holder_info of this ReportConnections.

        essential information about the account holder fetched from the connected provider  # noqa: E501

        :param holder_info: The holder_info of this ReportConnections.  # noqa: E501
        :type: str
        """
        if holder_info is None:
            raise ValueError("Invalid value for `holder_info`, must not be `None`")  # noqa: E501

        self._holder_info = holder_info

    @property
    def client_name(self):
        """Gets the client_name of this ReportConnections.  # noqa: E501

        Name of the Salt Edge Client, who requested the Financial Insights report  # noqa: E501

        :return: The client_name of this ReportConnections.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this ReportConnections.

        Name of the Salt Edge Client, who requested the Financial Insights report  # noqa: E501

        :param client_name: The client_name of this ReportConnections.  # noqa: E501
        :type: str
        """
        if client_name is None:
            raise ValueError("Invalid value for `client_name`, must not be `None`")  # noqa: E501

        self._client_name = client_name

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
        if issubclass(ReportConnections, dict):
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
        if not isinstance(other, ReportConnections):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
