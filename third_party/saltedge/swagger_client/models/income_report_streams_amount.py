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

class IncomeReportStreamsAmount(object):
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
        'total': 'float',
        'average': 'float',
        'median': 'float',
        'stdev': 'float'
    }

    attribute_map = {
        'total': 'total',
        'average': 'average',
        'median': 'median',
        'stdev': 'stdev'
    }

    def __init__(self, total=None, average=None, median=None, stdev=None):  # noqa: E501
        """IncomeReportStreamsAmount - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._average = None
        self._median = None
        self._stdev = None
        self.discriminator = None
        self.total = total
        self.average = average
        self.median = median
        self.stdev = stdev

    @property
    def total(self):
        """Gets the total of this IncomeReportStreamsAmount.  # noqa: E501

        Total stream income/expense  # noqa: E501

        :return: The total of this IncomeReportStreamsAmount.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this IncomeReportStreamsAmount.

        Total stream income/expense  # noqa: E501

        :param total: The total of this IncomeReportStreamsAmount.  # noqa: E501
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def average(self):
        """Gets the average of this IncomeReportStreamsAmount.  # noqa: E501

        Average stream income/expense  # noqa: E501

        :return: The average of this IncomeReportStreamsAmount.  # noqa: E501
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this IncomeReportStreamsAmount.

        Average stream income/expense  # noqa: E501

        :param average: The average of this IncomeReportStreamsAmount.  # noqa: E501
        :type: float
        """
        if average is None:
            raise ValueError("Invalid value for `average`, must not be `None`")  # noqa: E501

        self._average = average

    @property
    def median(self):
        """Gets the median of this IncomeReportStreamsAmount.  # noqa: E501

        Median stream income/expense  # noqa: E501

        :return: The median of this IncomeReportStreamsAmount.  # noqa: E501
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """Sets the median of this IncomeReportStreamsAmount.

        Median stream income/expense  # noqa: E501

        :param median: The median of this IncomeReportStreamsAmount.  # noqa: E501
        :type: float
        """
        if median is None:
            raise ValueError("Invalid value for `median`, must not be `None`")  # noqa: E501

        self._median = median

    @property
    def stdev(self):
        """Gets the stdev of this IncomeReportStreamsAmount.  # noqa: E501

        Standard deviation of the stream income/expense  # noqa: E501

        :return: The stdev of this IncomeReportStreamsAmount.  # noqa: E501
        :rtype: float
        """
        return self._stdev

    @stdev.setter
    def stdev(self, stdev):
        """Sets the stdev of this IncomeReportStreamsAmount.

        Standard deviation of the stream income/expense  # noqa: E501

        :param stdev: The stdev of this IncomeReportStreamsAmount.  # noqa: E501
        :type: float
        """
        if stdev is None:
            raise ValueError("Invalid value for `stdev`, must not be `None`")  # noqa: E501

        self._stdev = stdev

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
        if issubclass(IncomeReportStreamsAmount, dict):
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
        if not isinstance(other, IncomeReportStreamsAmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other