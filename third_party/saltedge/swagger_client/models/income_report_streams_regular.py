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

class IncomeReportStreamsRegular(object):
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
        'end_date': 'date',
        'amount': 'IncomeReportStreamsAmount',
        'frequency': 'str',
        'days_count': 'int',
        'category_code': 'str',
        'description': 'str',
        'merchant': 'IncomeReportStreamsMerchant'
    }

    attribute_map = {
        'transactions_count': 'transactions_count',
        'transaction_ids': 'transaction_ids',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'amount': 'amount',
        'frequency': 'frequency',
        'days_count': 'days_count',
        'category_code': 'category_code',
        'description': 'description',
        'merchant': 'merchant'
    }

    def __init__(self, transactions_count=None, transaction_ids=None, start_date=None, end_date=None, amount=None, frequency=None, days_count=None, category_code=None, description=None, merchant=None):  # noqa: E501
        """IncomeReportStreamsRegular - a model defined in Swagger"""  # noqa: E501
        self._transactions_count = None
        self._transaction_ids = None
        self._start_date = None
        self._end_date = None
        self._amount = None
        self._frequency = None
        self._days_count = None
        self._category_code = None
        self._description = None
        self._merchant = None
        self.discriminator = None
        self.transactions_count = transactions_count
        self.transaction_ids = transaction_ids
        self.start_date = start_date
        self.end_date = end_date
        self.amount = amount
        self.frequency = frequency
        self.days_count = days_count
        self.category_code = category_code
        self.description = description
        self.merchant = merchant

    @property
    def transactions_count(self):
        """Gets the transactions_count of this IncomeReportStreamsRegular.  # noqa: E501

        number of transactions, which belong to the stream  # noqa: E501

        :return: The transactions_count of this IncomeReportStreamsRegular.  # noqa: E501
        :rtype: int
        """
        return self._transactions_count

    @transactions_count.setter
    def transactions_count(self, transactions_count):
        """Sets the transactions_count of this IncomeReportStreamsRegular.

        number of transactions, which belong to the stream  # noqa: E501

        :param transactions_count: The transactions_count of this IncomeReportStreamsRegular.  # noqa: E501
        :type: int
        """
        if transactions_count is None:
            raise ValueError("Invalid value for `transactions_count`, must not be `None`")  # noqa: E501

        self._transactions_count = transactions_count

    @property
    def transaction_ids(self):
        """Gets the transaction_ids of this IncomeReportStreamsRegular.  # noqa: E501

        `ids` of [transactions](#transactions), which belong to the stream  # noqa: E501

        :return: The transaction_ids of this IncomeReportStreamsRegular.  # noqa: E501
        :rtype: list[str]
        """
        return self._transaction_ids

    @transaction_ids.setter
    def transaction_ids(self, transaction_ids):
        """Sets the transaction_ids of this IncomeReportStreamsRegular.

        `ids` of [transactions](#transactions), which belong to the stream  # noqa: E501

        :param transaction_ids: The transaction_ids of this IncomeReportStreamsRegular.  # noqa: E501
        :type: list[str]
        """
        if transaction_ids is None:
            raise ValueError("Invalid value for `transaction_ids`, must not be `None`")  # noqa: E501

        self._transaction_ids = transaction_ids

    @property
    def start_date(self):
        """Gets the start_date of this IncomeReportStreamsRegular.  # noqa: E501

        the date of the first [transaction](#transactions) from the stream  # noqa: E501

        :return: The start_date of this IncomeReportStreamsRegular.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this IncomeReportStreamsRegular.

        the date of the first [transaction](#transactions) from the stream  # noqa: E501

        :param start_date: The start_date of this IncomeReportStreamsRegular.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this IncomeReportStreamsRegular.  # noqa: E501

        the date of the last [transaction](#transactions) from the stream  # noqa: E501

        :return: The end_date of this IncomeReportStreamsRegular.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this IncomeReportStreamsRegular.

        the date of the last [transaction](#transactions) from the stream  # noqa: E501

        :param end_date: The end_date of this IncomeReportStreamsRegular.  # noqa: E501
        :type: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def amount(self):
        """Gets the amount of this IncomeReportStreamsRegular.  # noqa: E501


        :return: The amount of this IncomeReportStreamsRegular.  # noqa: E501
        :rtype: IncomeReportStreamsAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this IncomeReportStreamsRegular.


        :param amount: The amount of this IncomeReportStreamsRegular.  # noqa: E501
        :type: IncomeReportStreamsAmount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def frequency(self):
        """Gets the frequency of this IncomeReportStreamsRegular.  # noqa: E501

        average period of time between two [transactions](#transactions) in the stream.  # noqa: E501

        :return: The frequency of this IncomeReportStreamsRegular.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this IncomeReportStreamsRegular.

        average period of time between two [transactions](#transactions) in the stream.  # noqa: E501

        :param frequency: The frequency of this IncomeReportStreamsRegular.  # noqa: E501
        :type: str
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501
        allowed_values = ["daily", "3_times_a_week", "twice_a_week", "weekly", "3_times_a_month", "every_2_weeks", "monthly", "every_2_months", "quarterly", "3_times_a_year", "2_times_a_year", "annual", "few_years"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def days_count(self):
        """Gets the days_count of this IncomeReportStreamsRegular.  # noqa: E501

        average number of days between two [transactions](#transactions) in the stream  # noqa: E501

        :return: The days_count of this IncomeReportStreamsRegular.  # noqa: E501
        :rtype: int
        """
        return self._days_count

    @days_count.setter
    def days_count(self, days_count):
        """Sets the days_count of this IncomeReportStreamsRegular.

        average number of days between two [transactions](#transactions) in the stream  # noqa: E501

        :param days_count: The days_count of this IncomeReportStreamsRegular.  # noqa: E501
        :type: int
        """
        if days_count is None:
            raise ValueError("Invalid value for `days_count`, must not be `None`")  # noqa: E501

        self._days_count = days_count

    @property
    def category_code(self):
        """Gets the category_code of this IncomeReportStreamsRegular.  # noqa: E501

        category of transactions which belong to the stream  # noqa: E501

        :return: The category_code of this IncomeReportStreamsRegular.  # noqa: E501
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """Sets the category_code of this IncomeReportStreamsRegular.

        category of transactions which belong to the stream  # noqa: E501

        :param category_code: The category_code of this IncomeReportStreamsRegular.  # noqa: E501
        :type: str
        """
        if category_code is None:
            raise ValueError("Invalid value for `category_code`, must not be `None`")  # noqa: E501

        self._category_code = category_code

    @property
    def description(self):
        """Gets the description of this IncomeReportStreamsRegular.  # noqa: E501

        [transaction's](#transactions) description common for the stream  # noqa: E501

        :return: The description of this IncomeReportStreamsRegular.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IncomeReportStreamsRegular.

        [transaction's](#transactions) description common for the stream  # noqa: E501

        :param description: The description of this IncomeReportStreamsRegular.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def merchant(self):
        """Gets the merchant of this IncomeReportStreamsRegular.  # noqa: E501


        :return: The merchant of this IncomeReportStreamsRegular.  # noqa: E501
        :rtype: IncomeReportStreamsMerchant
        """
        return self._merchant

    @merchant.setter
    def merchant(self, merchant):
        """Sets the merchant of this IncomeReportStreamsRegular.


        :param merchant: The merchant of this IncomeReportStreamsRegular.  # noqa: E501
        :type: IncomeReportStreamsMerchant
        """
        if merchant is None:
            raise ValueError("Invalid value for `merchant`, must not be `None`")  # noqa: E501

        self._merchant = merchant

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
        if issubclass(IncomeReportStreamsRegular, dict):
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
        if not isinstance(other, IncomeReportStreamsRegular):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
