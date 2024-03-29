# coding: utf-8

"""
    Nordigen Account Information Services API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0 (v2)
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Aspsp(object):
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
        'name': 'str',
        'bic': 'str',
        'transaction_total_days': 'str',
        'countries': 'list[str]',
        'logo': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'bic': 'bic',
        'transaction_total_days': 'transaction_total_days',
        'countries': 'countries',
        'logo': 'logo'
    }

    def __init__(self, id=None, name=None, bic=None, transaction_total_days='90', countries=None, logo=None):  # noqa: E501
        """Aspsp - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._bic = None
        self._transaction_total_days = None
        self._countries = None
        self._logo = None
        self.discriminator = None
        self.id = id
        self.name = name
        if bic is not None:
            self.bic = bic
        if transaction_total_days is not None:
            self.transaction_total_days = transaction_total_days
        self.countries = countries
        self.logo = logo

    @property
    def id(self):
        """Gets the id of this Aspsp.  # noqa: E501


        :return: The id of this Aspsp.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Aspsp.


        :param id: The id of this Aspsp.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Aspsp.  # noqa: E501


        :return: The name of this Aspsp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Aspsp.


        :param name: The name of this Aspsp.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def bic(self):
        """Gets the bic of this Aspsp.  # noqa: E501


        :return: The bic of this Aspsp.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this Aspsp.


        :param bic: The bic of this Aspsp.  # noqa: E501
        :type: str
        """

        self._bic = bic

    @property
    def transaction_total_days(self):
        """Gets the transaction_total_days of this Aspsp.  # noqa: E501


        :return: The transaction_total_days of this Aspsp.  # noqa: E501
        :rtype: str
        """
        return self._transaction_total_days

    @transaction_total_days.setter
    def transaction_total_days(self, transaction_total_days):
        """Sets the transaction_total_days of this Aspsp.


        :param transaction_total_days: The transaction_total_days of this Aspsp.  # noqa: E501
        :type: str
        """

        self._transaction_total_days = transaction_total_days

    @property
    def countries(self):
        """Gets the countries of this Aspsp.  # noqa: E501


        :return: The countries of this Aspsp.  # noqa: E501
        :rtype: list[str]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this Aspsp.


        :param countries: The countries of this Aspsp.  # noqa: E501
        :type: list[str]
        """
        if countries is None:
            raise ValueError("Invalid value for `countries`, must not be `None`")  # noqa: E501

        self._countries = countries

    @property
    def logo(self):
        """Gets the logo of this Aspsp.  # noqa: E501


        :return: The logo of this Aspsp.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Aspsp.


        :param logo: The logo of this Aspsp.  # noqa: E501
        :type: str
        """
        if logo is None:
            raise ValueError("Invalid value for `logo`, must not be `None`")  # noqa: E501

        self._logo = logo

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
        if issubclass(Aspsp, dict):
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
        if not isinstance(other, Aspsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
