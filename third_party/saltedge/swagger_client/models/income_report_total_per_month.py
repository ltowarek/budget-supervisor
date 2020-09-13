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

class IncomeReportTotalPerMonth(object):
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
        'year': 'int',
        'month': 'int',
        'is_whole_month': 'bool',
        'amount': 'float'
    }

    attribute_map = {
        'year': 'year',
        'month': 'month',
        'is_whole_month': 'is_whole_month',
        'amount': 'amount'
    }

    def __init__(self, year=None, month=None, is_whole_month=None, amount=None):  # noqa: E501
        """IncomeReportTotalPerMonth - a model defined in Swagger"""  # noqa: E501
        self._year = None
        self._month = None
        self._is_whole_month = None
        self._amount = None
        self.discriminator = None
        self.year = year
        self.month = month
        self.is_whole_month = is_whole_month
        self.amount = amount

    @property
    def year(self):
        """Gets the year of this IncomeReportTotalPerMonth.  # noqa: E501

        year that the calculation was made for  # noqa: E501

        :return: The year of this IncomeReportTotalPerMonth.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this IncomeReportTotalPerMonth.

        year that the calculation was made for  # noqa: E501

        :param year: The year of this IncomeReportTotalPerMonth.  # noqa: E501
        :type: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def month(self):
        """Gets the month of this IncomeReportTotalPerMonth.  # noqa: E501

        month that the calculation was made for  # noqa: E501

        :return: The month of this IncomeReportTotalPerMonth.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this IncomeReportTotalPerMonth.

        month that the calculation was made for  # noqa: E501

        :param month: The month of this IncomeReportTotalPerMonth.  # noqa: E501
        :type: int
        """
        if month is None:
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def is_whole_month(self):
        """Gets the is_whole_month of this IncomeReportTotalPerMonth.  # noqa: E501

        will be `true` if the whole month is covered by the report  # noqa: E501

        :return: The is_whole_month of this IncomeReportTotalPerMonth.  # noqa: E501
        :rtype: bool
        """
        return self._is_whole_month

    @is_whole_month.setter
    def is_whole_month(self, is_whole_month):
        """Sets the is_whole_month of this IncomeReportTotalPerMonth.

        will be `true` if the whole month is covered by the report  # noqa: E501

        :param is_whole_month: The is_whole_month of this IncomeReportTotalPerMonth.  # noqa: E501
        :type: bool
        """
        if is_whole_month is None:
            raise ValueError("Invalid value for `is_whole_month`, must not be `None`")  # noqa: E501

        self._is_whole_month = is_whole_month

    @property
    def amount(self):
        """Gets the amount of this IncomeReportTotalPerMonth.  # noqa: E501

        amount of income/expense per specified month and year  # noqa: E501

        :return: The amount of this IncomeReportTotalPerMonth.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this IncomeReportTotalPerMonth.

        amount of income/expense per specified month and year  # noqa: E501

        :param amount: The amount of this IncomeReportTotalPerMonth.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if issubclass(IncomeReportTotalPerMonth, dict):
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
        if not isinstance(other, IncomeReportTotalPerMonth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
