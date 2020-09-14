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

class Transaction(object):
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
        'mode': 'str',
        'status': 'str',
        'made_on': 'date',
        'amount': 'float',
        'currency_code': 'str',
        'description': 'str',
        'category': 'str',
        'duplicated': 'bool',
        'extra': 'TransactionExtra',
        'account_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'mode': 'mode',
        'status': 'status',
        'made_on': 'made_on',
        'amount': 'amount',
        'currency_code': 'currency_code',
        'description': 'description',
        'category': 'category',
        'duplicated': 'duplicated',
        'extra': 'extra',
        'account_id': 'account_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, mode=None, status=None, made_on=None, amount=None, currency_code=None, description=None, category=None, duplicated=None, extra=None, account_id=None, created_at=None, updated_at=None):  # noqa: E501
        """Transaction - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._mode = None
        self._status = None
        self._made_on = None
        self._amount = None
        self._currency_code = None
        self._description = None
        self._category = None
        self._duplicated = None
        self._extra = None
        self._account_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.id = id
        self.mode = mode
        self.status = status
        self.made_on = made_on
        self.amount = amount
        self.currency_code = currency_code
        self.description = description
        self.category = category
        self.duplicated = duplicated
        self.extra = extra
        self.account_id = account_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Transaction.  # noqa: E501

        id of the transaction  # noqa: E501

        :return: The id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transaction.

        id of the transaction  # noqa: E501

        :param id: The id of this Transaction.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def mode(self):
        """Gets the mode of this Transaction.  # noqa: E501


        :return: The mode of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Transaction.


        :param mode: The mode of this Transaction.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["normal", "fee", "transfer"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def status(self):
        """Gets the status of this Transaction.  # noqa: E501


        :return: The status of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Transaction.


        :param status: The status of this Transaction.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["posted", "pending"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def made_on(self):
        """Gets the made_on of this Transaction.  # noqa: E501

        the date when the transaction was made  # noqa: E501

        :return: The made_on of this Transaction.  # noqa: E501
        :rtype: date
        """
        return self._made_on

    @made_on.setter
    def made_on(self, made_on):
        """Sets the made_on of this Transaction.

        the date when the transaction was made  # noqa: E501

        :param made_on: The made_on of this Transaction.  # noqa: E501
        :type: date
        """
        if made_on is None:
            raise ValueError("Invalid value for `made_on`, must not be `None`")  # noqa: E501

        self._made_on = made_on

    @property
    def amount(self):
        """Gets the amount of this Transaction.  # noqa: E501

        transaction's amount  # noqa: E501

        :return: The amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transaction.

        transaction's amount  # noqa: E501

        :param amount: The amount of this Transaction.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency_code(self):
        """Gets the currency_code of this Transaction.  # noqa: E501

        transaction's currency code  # noqa: E501

        :return: The currency_code of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Transaction.

        transaction's currency code  # noqa: E501

        :param currency_code: The currency_code of this Transaction.  # noqa: E501
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def description(self):
        """Gets the description of this Transaction.  # noqa: E501

        transaction's description  # noqa: E501

        :return: The description of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Transaction.

        transaction's description  # noqa: E501

        :param description: The description of this Transaction.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def category(self):
        """Gets the category of this Transaction.  # noqa: E501

        transaction's category  # noqa: E501

        :return: The category of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Transaction.

        transaction's category  # noqa: E501

        :param category: The category of this Transaction.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def duplicated(self):
        """Gets the duplicated of this Transaction.  # noqa: E501

        whether the transaction is duplicated or not  # noqa: E501

        :return: The duplicated of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._duplicated

    @duplicated.setter
    def duplicated(self, duplicated):
        """Sets the duplicated of this Transaction.

        whether the transaction is duplicated or not  # noqa: E501

        :param duplicated: The duplicated of this Transaction.  # noqa: E501
        :type: bool
        """
        if duplicated is None:
            raise ValueError("Invalid value for `duplicated`, must not be `None`")  # noqa: E501

        self._duplicated = duplicated

    @property
    def extra(self):
        """Gets the extra of this Transaction.  # noqa: E501


        :return: The extra of this Transaction.  # noqa: E501
        :rtype: TransactionExtra
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this Transaction.


        :param extra: The extra of this Transaction.  # noqa: E501
        :type: TransactionExtra
        """
        if extra is None:
            raise ValueError("Invalid value for `extra`, must not be `None`")  # noqa: E501

        self._extra = extra

    @property
    def account_id(self):
        """Gets the account_id of this Transaction.  # noqa: E501

        the `id` of the account the transaction belongs to  # noqa: E501

        :return: The account_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Transaction.

        the `id` of the account the transaction belongs to  # noqa: E501

        :param account_id: The account_id of this Transaction.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def created_at(self):
        """Gets the created_at of this Transaction.  # noqa: E501

        time and date when the transaction was imported  # noqa: E501

        :return: The created_at of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Transaction.

        time and date when the transaction was imported  # noqa: E501

        :param created_at: The created_at of this Transaction.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Transaction.  # noqa: E501

        the last time when the transaction's attributes (duplicated flag set, category learned applied) were changed by the client  # noqa: E501

        :return: The updated_at of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Transaction.

        the last time when the transaction's attributes (duplicated flag set, category learned applied) were changed by the client  # noqa: E501

        :param updated_at: The updated_at of this Transaction.  # noqa: E501
        :type: datetime
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
        if issubclass(Transaction, dict):
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
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
