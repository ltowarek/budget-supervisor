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

class ReportTransactions(object):
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
        'start_date': 'str',
        'end_date': 'str',
        'first_id': 'str',
        'last_id': 'str',
        'count': 'int'
    }

    attribute_map = {
        'start_date': 'start_date',
        'end_date': 'end_date',
        'first_id': 'first_id',
        'last_id': 'last_id',
        'count': 'count'
    }

    def __init__(self, start_date=None, end_date=None, first_id=None, last_id=None, count=None):  # noqa: E501
        """ReportTransactions - a model defined in Swagger"""  # noqa: E501
        self._start_date = None
        self._end_date = None
        self._first_id = None
        self._last_id = None
        self._count = None
        self.discriminator = None
        self.start_date = start_date
        self.end_date = end_date
        self.first_id = first_id
        self.last_id = last_id
        self.count = count

    @property
    def start_date(self):
        """Gets the start_date of this ReportTransactions.  # noqa: E501

        the date of the first transaction  # noqa: E501

        :return: The start_date of this ReportTransactions.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ReportTransactions.

        the date of the first transaction  # noqa: E501

        :param start_date: The start_date of this ReportTransactions.  # noqa: E501
        :type: str
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ReportTransactions.  # noqa: E501

        the date of the last transaction  # noqa: E501

        :return: The end_date of this ReportTransactions.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ReportTransactions.

        the date of the last transaction  # noqa: E501

        :param end_date: The end_date of this ReportTransactions.  # noqa: E501
        :type: str
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def first_id(self):
        """Gets the first_id of this ReportTransactions.  # noqa: E501

        the `id` of the first [transaction](#transactions)  # noqa: E501

        :return: The first_id of this ReportTransactions.  # noqa: E501
        :rtype: str
        """
        return self._first_id

    @first_id.setter
    def first_id(self, first_id):
        """Sets the first_id of this ReportTransactions.

        the `id` of the first [transaction](#transactions)  # noqa: E501

        :param first_id: The first_id of this ReportTransactions.  # noqa: E501
        :type: str
        """
        if first_id is None:
            raise ValueError("Invalid value for `first_id`, must not be `None`")  # noqa: E501

        self._first_id = first_id

    @property
    def last_id(self):
        """Gets the last_id of this ReportTransactions.  # noqa: E501

        the `id` of the last [transaction](#transactions)  # noqa: E501

        :return: The last_id of this ReportTransactions.  # noqa: E501
        :rtype: str
        """
        return self._last_id

    @last_id.setter
    def last_id(self, last_id):
        """Sets the last_id of this ReportTransactions.

        the `id` of the last [transaction](#transactions)  # noqa: E501

        :param last_id: The last_id of this ReportTransactions.  # noqa: E501
        :type: str
        """
        if last_id is None:
            raise ValueError("Invalid value for `last_id`, must not be `None`")  # noqa: E501

        self._last_id = last_id

    @property
    def count(self):
        """Gets the count of this ReportTransactions.  # noqa: E501

        total number of transactions  # noqa: E501

        :return: The count of this ReportTransactions.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ReportTransactions.

        total number of transactions  # noqa: E501

        :param count: The count of this ReportTransactions.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

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
        if issubclass(ReportTransactions, dict):
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
        if not isinstance(other, ReportTransactions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
