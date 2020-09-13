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

class SavingsReportForecastedAverage(object):
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
        'next_month': 'float',
        'next_quarter': 'float',
        'next_year': 'float'
    }

    attribute_map = {
        'next_month': 'next_month',
        'next_quarter': 'next_quarter',
        'next_year': 'next_year'
    }

    def __init__(self, next_month=None, next_quarter=None, next_year=None):  # noqa: E501
        """SavingsReportForecastedAverage - a model defined in Swagger"""  # noqa: E501
        self._next_month = None
        self._next_quarter = None
        self._next_year = None
        self.discriminator = None
        self.next_month = next_month
        self.next_quarter = next_quarter
        self.next_year = next_year

    @property
    def next_month(self):
        """Gets the next_month of this SavingsReportForecastedAverage.  # noqa: E501

        forecasted average savings for the next calendar month  # noqa: E501

        :return: The next_month of this SavingsReportForecastedAverage.  # noqa: E501
        :rtype: float
        """
        return self._next_month

    @next_month.setter
    def next_month(self, next_month):
        """Sets the next_month of this SavingsReportForecastedAverage.

        forecasted average savings for the next calendar month  # noqa: E501

        :param next_month: The next_month of this SavingsReportForecastedAverage.  # noqa: E501
        :type: float
        """
        if next_month is None:
            raise ValueError("Invalid value for `next_month`, must not be `None`")  # noqa: E501

        self._next_month = next_month

    @property
    def next_quarter(self):
        """Gets the next_quarter of this SavingsReportForecastedAverage.  # noqa: E501

        forecasted average savings for the next 3 calendar months  # noqa: E501

        :return: The next_quarter of this SavingsReportForecastedAverage.  # noqa: E501
        :rtype: float
        """
        return self._next_quarter

    @next_quarter.setter
    def next_quarter(self, next_quarter):
        """Sets the next_quarter of this SavingsReportForecastedAverage.

        forecasted average savings for the next 3 calendar months  # noqa: E501

        :param next_quarter: The next_quarter of this SavingsReportForecastedAverage.  # noqa: E501
        :type: float
        """
        if next_quarter is None:
            raise ValueError("Invalid value for `next_quarter`, must not be `None`")  # noqa: E501

        self._next_quarter = next_quarter

    @property
    def next_year(self):
        """Gets the next_year of this SavingsReportForecastedAverage.  # noqa: E501

        forecasted average savings for the next 12 calendar months  # noqa: E501

        :return: The next_year of this SavingsReportForecastedAverage.  # noqa: E501
        :rtype: float
        """
        return self._next_year

    @next_year.setter
    def next_year(self, next_year):
        """Sets the next_year of this SavingsReportForecastedAverage.

        forecasted average savings for the next 12 calendar months  # noqa: E501

        :param next_year: The next_year of this SavingsReportForecastedAverage.  # noqa: E501
        :type: float
        """
        if next_year is None:
            raise ValueError("Invalid value for `next_year`, must not be `None`")  # noqa: E501

        self._next_year = next_year

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
        if issubclass(SavingsReportForecastedAverage, dict):
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
        if not isinstance(other, SavingsReportForecastedAverage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
