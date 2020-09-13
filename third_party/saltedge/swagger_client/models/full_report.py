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
from swagger_client.models.basic_report import BasicReport  # noqa: F401,E501

class FullReport(BasicReport):
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
        'currency_code': 'str',
        'from_date': 'date',
        'to_date': 'date',
        'report_types': 'list[str]',
        'data': 'Report',
        'created_at': 'date',
        'updated_at': 'date'
    }
    if hasattr(BasicReport, "swagger_types"):
        swagger_types.update(BasicReport.swagger_types)

    attribute_map = {
        'currency_code': 'currency_code',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'report_types': 'report_types',
        'data': 'data',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }
    if hasattr(BasicReport, "attribute_map"):
        attribute_map.update(BasicReport.attribute_map)

    def __init__(self, currency_code=None, from_date=None, to_date=None, report_types=None, data=None, created_at=None, updated_at=None, *args, **kwargs):  # noqa: E501
        """FullReport - a model defined in Swagger"""  # noqa: E501
        self._currency_code = None
        self._from_date = None
        self._to_date = None
        self._report_types = None
        self._data = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.currency_code = currency_code
        self.from_date = from_date
        self.to_date = to_date
        self.report_types = report_types
        self.data = data
        self.created_at = created_at
        self.updated_at = updated_at
        BasicReport.__init__(self, *args, **kwargs)

    @property
    def currency_code(self):
        """Gets the currency_code of this FullReport.  # noqa: E501

        main [currency code](#currencies) used for report's the generation and value conversion  # noqa: E501

        :return: The currency_code of this FullReport.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this FullReport.

        main [currency code](#currencies) used for report's the generation and value conversion  # noqa: E501

        :param currency_code: The currency_code of this FullReport.  # noqa: E501
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def from_date(self):
        """Gets the from_date of this FullReport.  # noqa: E501

        the date from which the data in the report are included  # noqa: E501

        :return: The from_date of this FullReport.  # noqa: E501
        :rtype: date
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this FullReport.

        the date from which the data in the report are included  # noqa: E501

        :param from_date: The from_date of this FullReport.  # noqa: E501
        :type: date
        """
        if from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this FullReport.  # noqa: E501

        the date to which the data in the report are included  # noqa: E501

        :return: The to_date of this FullReport.  # noqa: E501
        :rtype: date
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this FullReport.

        the date to which the data in the report are included  # noqa: E501

        :param to_date: The to_date of this FullReport.  # noqa: E501
        :type: date
        """
        if to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501

        self._to_date = to_date

    @property
    def report_types(self):
        """Gets the report_types of this FullReport.  # noqa: E501

        types of reports  # noqa: E501

        :return: The report_types of this FullReport.  # noqa: E501
        :rtype: list[str]
        """
        return self._report_types

    @report_types.setter
    def report_types(self, report_types):
        """Sets the report_types of this FullReport.

        types of reports  # noqa: E501

        :param report_types: The report_types of this FullReport.  # noqa: E501
        :type: list[str]
        """
        if report_types is None:
            raise ValueError("Invalid value for `report_types`, must not be `None`")  # noqa: E501
        allowed_values = ["balance", "expense", "income", "savings"]  # noqa: E501
        if not set(report_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `report_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(report_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._report_types = report_types

    @property
    def data(self):
        """Gets the data of this FullReport.  # noqa: E501


        :return: The data of this FullReport.  # noqa: E501
        :rtype: Report
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FullReport.


        :param data: The data of this FullReport.  # noqa: E501
        :type: Report
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def created_at(self):
        """Gets the created_at of this FullReport.  # noqa: E501


        :return: The created_at of this FullReport.  # noqa: E501
        :rtype: date
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FullReport.


        :param created_at: The created_at of this FullReport.  # noqa: E501
        :type: date
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FullReport.  # noqa: E501

        the date when the report was last updated  # noqa: E501

        :return: The updated_at of this FullReport.  # noqa: E501
        :rtype: date
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FullReport.

        the date when the report was last updated  # noqa: E501

        :param updated_at: The updated_at of this FullReport.  # noqa: E501
        :type: date
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if issubclass(FullReport, dict):
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
        if not isinstance(other, FullReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
