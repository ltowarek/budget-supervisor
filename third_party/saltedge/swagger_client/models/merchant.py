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

class Merchant(object):
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
        'names': 'list[MerchantNames]',
        'address': 'MerchantAddress',
        'contact': 'list[MerchantContact]'
    }

    attribute_map = {
        'id': 'id',
        'names': 'names',
        'address': 'address',
        'contact': 'contact'
    }

    def __init__(self, id=None, names=None, address=None, contact=None):  # noqa: E501
        """Merchant - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._names = None
        self._address = None
        self._contact = None
        self.discriminator = None
        self.id = id
        self.names = names
        self.address = address
        self.contact = contact

    @property
    def id(self):
        """Gets the id of this Merchant.  # noqa: E501

        the `id` of the merchant  # noqa: E501

        :return: The id of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Merchant.

        the `id` of the merchant  # noqa: E501

        :param id: The id of this Merchant.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def names(self):
        """Gets the names of this Merchant.  # noqa: E501

        merchant names that are used to name a company, corporation, brand name, franchise name or any other entity who is participating in  the customer's transaction.   # noqa: E501

        :return: The names of this Merchant.  # noqa: E501
        :rtype: list[MerchantNames]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this Merchant.

        merchant names that are used to name a company, corporation, brand name, franchise name or any other entity who is participating in  the customer's transaction.   # noqa: E501

        :param names: The names of this Merchant.  # noqa: E501
        :type: list[MerchantNames]
        """
        if names is None:
            raise ValueError("Invalid value for `names`, must not be `None`")  # noqa: E501

        self._names = names

    @property
    def address(self):
        """Gets the address of this Merchant.  # noqa: E501


        :return: The address of this Merchant.  # noqa: E501
        :rtype: MerchantAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Merchant.


        :param address: The address of this Merchant.  # noqa: E501
        :type: MerchantAddress
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def contact(self):
        """Gets the contact of this Merchant.  # noqa: E501

        contact information via which the merchant can be accessed, eg. via website, phone or social media  # noqa: E501

        :return: The contact of this Merchant.  # noqa: E501
        :rtype: list[MerchantContact]
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Merchant.

        contact information via which the merchant can be accessed, eg. via website, phone or social media  # noqa: E501

        :param contact: The contact of this Merchant.  # noqa: E501
        :type: list[MerchantContact]
        """
        if contact is None:
            raise ValueError("Invalid value for `contact`, must not be `None`")  # noqa: E501

        self._contact = contact

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
        if issubclass(Merchant, dict):
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
        if not isinstance(other, Merchant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
