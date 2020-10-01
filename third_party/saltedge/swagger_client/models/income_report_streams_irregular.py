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

class IncomeReportStreamsIrregular(object):
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
        'transactions_count': 'int',
        'transaction_ids': 'list[str]',
        'start_date': 'date',
        'end_date': 'date'
    }

    attribute_map = {
        'transactions_count': 'transactions_count',
        'transaction_ids': 'transaction_ids',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, transactions_count=None, transaction_ids=None, start_date=None, end_date=None):  # noqa: E501
        """IncomeReportStreamsIrregular - a model defined in Swagger"""  # noqa: E501
        self._transactions_count = None
        self._transaction_ids = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None
        self.transactions_count = transactions_count
        self.transaction_ids = transaction_ids
        self.start_date = start_date
        self.end_date = end_date

    @property
    def transactions_count(self):
        """Gets the transactions_count of this IncomeReportStreamsIrregular.  # noqa: E501

        number of transactions, which belong to the stream  # noqa: E501

        :return: The transactions_count of this IncomeReportStreamsIrregular.  # noqa: E501
        :rtype: int
        """
        return self._transactions_count

    @transactions_count.setter
    def transactions_count(self, transactions_count):
        """Sets the transactions_count of this IncomeReportStreamsIrregular.

        number of transactions, which belong to the stream  # noqa: E501

        :param transactions_count: The transactions_count of this IncomeReportStreamsIrregular.  # noqa: E501
        :type: int
        """
        if transactions_count is None:
            raise ValueError("Invalid value for `transactions_count`, must not be `None`")  # noqa: E501

        self._transactions_count = transactions_count

    @property
    def transaction_ids(self):
        """Gets the transaction_ids of this IncomeReportStreamsIrregular.  # noqa: E501

        `ids` of [transactions](#transactions), which belong to the stream  # noqa: E501

        :return: The transaction_ids of this IncomeReportStreamsIrregular.  # noqa: E501
        :rtype: list[str]
        """
        return self._transaction_ids

    @transaction_ids.setter
    def transaction_ids(self, transaction_ids):
        """Sets the transaction_ids of this IncomeReportStreamsIrregular.

        `ids` of [transactions](#transactions), which belong to the stream  # noqa: E501

        :param transaction_ids: The transaction_ids of this IncomeReportStreamsIrregular.  # noqa: E501
        :type: list[str]
        """
        if transaction_ids is None:
            raise ValueError("Invalid value for `transaction_ids`, must not be `None`")  # noqa: E501

        self._transaction_ids = transaction_ids

    @property
    def start_date(self):
        """Gets the start_date of this IncomeReportStreamsIrregular.  # noqa: E501

        the date of the first [transaction](#transactions) from the stream  # noqa: E501

        :return: The start_date of this IncomeReportStreamsIrregular.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this IncomeReportStreamsIrregular.

        the date of the first [transaction](#transactions) from the stream  # noqa: E501

        :param start_date: The start_date of this IncomeReportStreamsIrregular.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this IncomeReportStreamsIrregular.  # noqa: E501

        the date of the last [transaction](#transactions) from the stream  # noqa: E501

        :return: The end_date of this IncomeReportStreamsIrregular.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this IncomeReportStreamsIrregular.

        the date of the last [transaction](#transactions) from the stream  # noqa: E501

        :param end_date: The end_date of this IncomeReportStreamsIrregular.  # noqa: E501
        :type: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

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
        if issubclass(IncomeReportStreamsIrregular, dict):
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
        if not isinstance(other, IncomeReportStreamsIrregular):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other