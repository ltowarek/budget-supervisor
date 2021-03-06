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

class IncomeReportStreamsMerchant(object):
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
        'name': 'str',
        'email': 'str',
        'phone': 'str',
        'address': 'str',
        'website': 'str'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'phone': 'phone',
        'address': 'address',
        'website': 'website'
    }

    def __init__(self, name=None, email=None, phone=None, address=None, website=None):  # noqa: E501
        """IncomeReportStreamsMerchant - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._email = None
        self._phone = None
        self._address = None
        self._website = None
        self.discriminator = None
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.website = website

    @property
    def name(self):
        """Gets the name of this IncomeReportStreamsMerchant.  # noqa: E501

        merchant's name  # noqa: E501

        :return: The name of this IncomeReportStreamsMerchant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IncomeReportStreamsMerchant.

        merchant's name  # noqa: E501

        :param name: The name of this IncomeReportStreamsMerchant.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this IncomeReportStreamsMerchant.  # noqa: E501

        merchant's email address  # noqa: E501

        :return: The email of this IncomeReportStreamsMerchant.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this IncomeReportStreamsMerchant.

        merchant's email address  # noqa: E501

        :param email: The email of this IncomeReportStreamsMerchant.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this IncomeReportStreamsMerchant.  # noqa: E501

        merchant's phone  # noqa: E501

        :return: The phone of this IncomeReportStreamsMerchant.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this IncomeReportStreamsMerchant.

        merchant's phone  # noqa: E501

        :param phone: The phone of this IncomeReportStreamsMerchant.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def address(self):
        """Gets the address of this IncomeReportStreamsMerchant.  # noqa: E501

        merchant's address  # noqa: E501

        :return: The address of this IncomeReportStreamsMerchant.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IncomeReportStreamsMerchant.

        merchant's address  # noqa: E501

        :param address: The address of this IncomeReportStreamsMerchant.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def website(self):
        """Gets the website of this IncomeReportStreamsMerchant.  # noqa: E501

        merchant's website  # noqa: E501

        :return: The website of this IncomeReportStreamsMerchant.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this IncomeReportStreamsMerchant.

        merchant's website  # noqa: E501

        :param website: The website of this IncomeReportStreamsMerchant.  # noqa: E501
        :type: str
        """
        if website is None:
            raise ValueError("Invalid value for `website`, must not be `None`")  # noqa: E501

        self._website = website

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
        if issubclass(IncomeReportStreamsMerchant, dict):
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
        if not isinstance(other, IncomeReportStreamsMerchant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
