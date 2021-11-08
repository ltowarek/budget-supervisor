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

class AccountV2(object):
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
        'created': 'datetime',
        'last_accessed': 'datetime',
        'iban': 'str',
        'institution_id': 'str',
        'status': 'AllOfAccountV2Status'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'last_accessed': 'last_accessed',
        'iban': 'iban',
        'institution_id': 'institution_id',
        'status': 'status'
    }

    def __init__(self, id=None, created=None, last_accessed=None, iban=None, institution_id=None, status=None):  # noqa: E501
        """AccountV2 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._last_accessed = None
        self._iban = None
        self._institution_id = None
        self._status = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.last_accessed = last_accessed
        self.iban = iban
        self.institution_id = institution_id
        self.status = status

    @property
    def id(self):
        """Gets the id of this AccountV2.  # noqa: E501

        The ID of this Account, used to refer to this account in other API calls.  # noqa: E501

        :return: The id of this AccountV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountV2.

        The ID of this Account, used to refer to this account in other API calls.  # noqa: E501

        :param id: The id of this AccountV2.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this AccountV2.  # noqa: E501

        The date & time at which the account object was created.  # noqa: E501

        :return: The created of this AccountV2.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AccountV2.

        The date & time at which the account object was created.  # noqa: E501

        :param created: The created of this AccountV2.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def last_accessed(self):
        """Gets the last_accessed of this AccountV2.  # noqa: E501

        The date & time at which the account object was last accessed.  # noqa: E501

        :return: The last_accessed of this AccountV2.  # noqa: E501
        :rtype: datetime
        """
        return self._last_accessed

    @last_accessed.setter
    def last_accessed(self, last_accessed):
        """Sets the last_accessed of this AccountV2.

        The date & time at which the account object was last accessed.  # noqa: E501

        :param last_accessed: The last_accessed of this AccountV2.  # noqa: E501
        :type: datetime
        """
        if last_accessed is None:
            raise ValueError("Invalid value for `last_accessed`, must not be `None`")  # noqa: E501

        self._last_accessed = last_accessed

    @property
    def iban(self):
        """Gets the iban of this AccountV2.  # noqa: E501

        The Account IBAN  # noqa: E501

        :return: The iban of this AccountV2.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this AccountV2.

        The Account IBAN  # noqa: E501

        :param iban: The iban of this AccountV2.  # noqa: E501
        :type: str
        """
        if iban is None:
            raise ValueError("Invalid value for `iban`, must not be `None`")  # noqa: E501

        self._iban = iban

    @property
    def institution_id(self):
        """Gets the institution_id of this AccountV2.  # noqa: E501

        The ASPSP associated with this account.  # noqa: E501

        :return: The institution_id of this AccountV2.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this AccountV2.

        The ASPSP associated with this account.  # noqa: E501

        :param institution_id: The institution_id of this AccountV2.  # noqa: E501
        :type: str
        """
        if institution_id is None:
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def status(self):
        """Gets the status of this AccountV2.  # noqa: E501

        The processing status of this account.  # noqa: E501

        :return: The status of this AccountV2.  # noqa: E501
        :rtype: AllOfAccountV2Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountV2.

        The processing status of this account.  # noqa: E501

        :param status: The status of this AccountV2.  # noqa: E501
        :type: AllOfAccountV2Status
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(AccountV2, dict):
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
        if not isinstance(other, AccountV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other