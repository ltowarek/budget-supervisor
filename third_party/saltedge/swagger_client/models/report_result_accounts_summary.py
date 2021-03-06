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

class ReportResultAccountsSummary(object):
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
        'start_date': 'date',
        'end_date': 'date',
        'whole_months_count': 'int',
        'days_count': 'int',
        'transactions_count': 'int',
        'monthly_average_transactions_count': 'ReportResultMonthlyAverageTransactionsCount',
        'balance': 'BalanceReport',
        'income': 'IncomeReport',
        'expense': 'ExpenseReport',
        'savings': 'SavingsReport'
    }

    attribute_map = {
        'start_date': 'start_date',
        'end_date': 'end_date',
        'whole_months_count': 'whole_months_count',
        'days_count': 'days_count',
        'transactions_count': 'transactions_count',
        'monthly_average_transactions_count': 'monthly_average_transactions_count',
        'balance': 'balance',
        'income': 'income',
        'expense': 'expense',
        'savings': 'savings'
    }

    def __init__(self, start_date=None, end_date=None, whole_months_count=None, days_count=None, transactions_count=None, monthly_average_transactions_count=None, balance=None, income=None, expense=None, savings=None):  # noqa: E501
        """ReportResultAccountsSummary - a model defined in Swagger"""  # noqa: E501
        self._start_date = None
        self._end_date = None
        self._whole_months_count = None
        self._days_count = None
        self._transactions_count = None
        self._monthly_average_transactions_count = None
        self._balance = None
        self._income = None
        self._expense = None
        self._savings = None
        self.discriminator = None
        self.start_date = start_date
        self.end_date = end_date
        self.whole_months_count = whole_months_count
        self.days_count = days_count
        self.transactions_count = transactions_count
        self.monthly_average_transactions_count = monthly_average_transactions_count
        self.balance = balance
        self.income = income
        self.expense = expense
        self.savings = savings

    @property
    def start_date(self):
        """Gets the start_date of this ReportResultAccountsSummary.  # noqa: E501

        the date of the first transaction  # noqa: E501

        :return: The start_date of this ReportResultAccountsSummary.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ReportResultAccountsSummary.

        the date of the first transaction  # noqa: E501

        :param start_date: The start_date of this ReportResultAccountsSummary.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ReportResultAccountsSummary.  # noqa: E501

        the date of the last transaction  # noqa: E501

        :return: The end_date of this ReportResultAccountsSummary.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ReportResultAccountsSummary.

        the date of the last transaction  # noqa: E501

        :param end_date: The end_date of this ReportResultAccountsSummary.  # noqa: E501
        :type: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def whole_months_count(self):
        """Gets the whole_months_count of this ReportResultAccountsSummary.  # noqa: E501

        number of full months covered by the report  # noqa: E501

        :return: The whole_months_count of this ReportResultAccountsSummary.  # noqa: E501
        :rtype: int
        """
        return self._whole_months_count

    @whole_months_count.setter
    def whole_months_count(self, whole_months_count):
        """Sets the whole_months_count of this ReportResultAccountsSummary.

        number of full months covered by the report  # noqa: E501

        :param whole_months_count: The whole_months_count of this ReportResultAccountsSummary.  # noqa: E501
        :type: int
        """
        if whole_months_count is None:
            raise ValueError("Invalid value for `whole_months_count`, must not be `None`")  # noqa: E501

        self._whole_months_count = whole_months_count

    @property
    def days_count(self):
        """Gets the days_count of this ReportResultAccountsSummary.  # noqa: E501

        number of days covered by the report  # noqa: E501

        :return: The days_count of this ReportResultAccountsSummary.  # noqa: E501
        :rtype: int
        """
        return self._days_count

    @days_count.setter
    def days_count(self, days_count):
        """Sets the days_count of this ReportResultAccountsSummary.

        number of days covered by the report  # noqa: E501

        :param days_count: The days_count of this ReportResultAccountsSummary.  # noqa: E501
        :type: int
        """
        if days_count is None:
            raise ValueError("Invalid value for `days_count`, must not be `None`")  # noqa: E501

        self._days_count = days_count

    @property
    def transactions_count(self):
        """Gets the transactions_count of this ReportResultAccountsSummary.  # noqa: E501

        total number of transactions  # noqa: E501

        :return: The transactions_count of this ReportResultAccountsSummary.  # noqa: E501
        :rtype: int
        """
        return self._transactions_count

    @transactions_count.setter
    def transactions_count(self, transactions_count):
        """Sets the transactions_count of this ReportResultAccountsSummary.

        total number of transactions  # noqa: E501

        :param transactions_count: The transactions_count of this ReportResultAccountsSummary.  # noqa: E501
        :type: int
        """
        if transactions_count is None:
            raise ValueError("Invalid value for `transactions_count`, must not be `None`")  # noqa: E501

        self._transactions_count = transactions_count

    @property
    def monthly_average_transactions_count(self):
        """Gets the monthly_average_transactions_count of this ReportResultAccountsSummary.  # noqa: E501


        :return: The monthly_average_transactions_count of this ReportResultAccountsSummary.  # noqa: E501
        :rtype: ReportResultMonthlyAverageTransactionsCount
        """
        return self._monthly_average_transactions_count

    @monthly_average_transactions_count.setter
    def monthly_average_transactions_count(self, monthly_average_transactions_count):
        """Sets the monthly_average_transactions_count of this ReportResultAccountsSummary.


        :param monthly_average_transactions_count: The monthly_average_transactions_count of this ReportResultAccountsSummary.  # noqa: E501
        :type: ReportResultMonthlyAverageTransactionsCount
        """
        if monthly_average_transactions_count is None:
            raise ValueError("Invalid value for `monthly_average_transactions_count`, must not be `None`")  # noqa: E501

        self._monthly_average_transactions_count = monthly_average_transactions_count

    @property
    def balance(self):
        """Gets the balance of this ReportResultAccountsSummary.  # noqa: E501


        :return: The balance of this ReportResultAccountsSummary.  # noqa: E501
        :rtype: BalanceReport
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ReportResultAccountsSummary.


        :param balance: The balance of this ReportResultAccountsSummary.  # noqa: E501
        :type: BalanceReport
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def income(self):
        """Gets the income of this ReportResultAccountsSummary.  # noqa: E501


        :return: The income of this ReportResultAccountsSummary.  # noqa: E501
        :rtype: IncomeReport
        """
        return self._income

    @income.setter
    def income(self, income):
        """Sets the income of this ReportResultAccountsSummary.


        :param income: The income of this ReportResultAccountsSummary.  # noqa: E501
        :type: IncomeReport
        """
        if income is None:
            raise ValueError("Invalid value for `income`, must not be `None`")  # noqa: E501

        self._income = income

    @property
    def expense(self):
        """Gets the expense of this ReportResultAccountsSummary.  # noqa: E501


        :return: The expense of this ReportResultAccountsSummary.  # noqa: E501
        :rtype: ExpenseReport
        """
        return self._expense

    @expense.setter
    def expense(self, expense):
        """Sets the expense of this ReportResultAccountsSummary.


        :param expense: The expense of this ReportResultAccountsSummary.  # noqa: E501
        :type: ExpenseReport
        """
        if expense is None:
            raise ValueError("Invalid value for `expense`, must not be `None`")  # noqa: E501

        self._expense = expense

    @property
    def savings(self):
        """Gets the savings of this ReportResultAccountsSummary.  # noqa: E501


        :return: The savings of this ReportResultAccountsSummary.  # noqa: E501
        :rtype: SavingsReport
        """
        return self._savings

    @savings.setter
    def savings(self, savings):
        """Sets the savings of this ReportResultAccountsSummary.


        :param savings: The savings of this ReportResultAccountsSummary.  # noqa: E501
        :type: SavingsReport
        """
        if savings is None:
            raise ValueError("Invalid value for `savings`, must not be `None`")  # noqa: E501

        self._savings = savings

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
        if issubclass(ReportResultAccountsSummary, dict):
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
        if not isinstance(other, ReportResultAccountsSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
