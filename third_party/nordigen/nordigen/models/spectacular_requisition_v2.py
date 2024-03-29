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

class SpectacularRequisitionV2(object):
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
        'redirect': 'str',
        'status': 'AllOfSpectacularRequisitionV2Status',
        'institution_id': 'str',
        'agreement': 'str',
        'reference': 'str',
        'accounts': 'list[Object]',
        'user_language': 'str',
        'link': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'redirect': 'redirect',
        'status': 'status',
        'institution_id': 'institution_id',
        'agreement': 'agreement',
        'reference': 'reference',
        'accounts': 'accounts',
        'user_language': 'user_language',
        'link': 'link'
    }

    def __init__(self, id=None, created=None, redirect=None, status=None, institution_id=None, agreement=None, reference=None, accounts=None, user_language=None, link='https://ob.nordigen.com/psd2/start/3fa85f64-5717-4562-b3fc-2c963f66afa6/{$INSTITUTION_ID}'):  # noqa: E501
        """SpectacularRequisitionV2 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._redirect = None
        self._status = None
        self._institution_id = None
        self._agreement = None
        self._reference = None
        self._accounts = None
        self._user_language = None
        self._link = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.redirect = redirect
        self.status = status
        self.institution_id = institution_id
        if agreement is not None:
            self.agreement = agreement
        if reference is not None:
            self.reference = reference
        self.accounts = accounts
        if user_language is not None:
            self.user_language = user_language
        self.link = link

    @property
    def id(self):
        """Gets the id of this SpectacularRequisitionV2.  # noqa: E501


        :return: The id of this SpectacularRequisitionV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SpectacularRequisitionV2.


        :param id: The id of this SpectacularRequisitionV2.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this SpectacularRequisitionV2.  # noqa: E501

        The date & time at which the requisition was created.  # noqa: E501

        :return: The created of this SpectacularRequisitionV2.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SpectacularRequisitionV2.

        The date & time at which the requisition was created.  # noqa: E501

        :param created: The created of this SpectacularRequisitionV2.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def redirect(self):
        """Gets the redirect of this SpectacularRequisitionV2.  # noqa: E501

        redirect URL to your application after end-user authorization with ASPSP  # noqa: E501

        :return: The redirect of this SpectacularRequisitionV2.  # noqa: E501
        :rtype: str
        """
        return self._redirect

    @redirect.setter
    def redirect(self, redirect):
        """Sets the redirect of this SpectacularRequisitionV2.

        redirect URL to your application after end-user authorization with ASPSP  # noqa: E501

        :param redirect: The redirect of this SpectacularRequisitionV2.  # noqa: E501
        :type: str
        """
        if redirect is None:
            raise ValueError("Invalid value for `redirect`, must not be `None`")  # noqa: E501

        self._redirect = redirect

    @property
    def status(self):
        """Gets the status of this SpectacularRequisitionV2.  # noqa: E501

        status of this requisition  # noqa: E501

        :return: The status of this SpectacularRequisitionV2.  # noqa: E501
        :rtype: AllOfSpectacularRequisitionV2Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SpectacularRequisitionV2.

        status of this requisition  # noqa: E501

        :param status: The status of this SpectacularRequisitionV2.  # noqa: E501
        :type: AllOfSpectacularRequisitionV2Status
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def institution_id(self):
        """Gets the institution_id of this SpectacularRequisitionV2.  # noqa: E501

        an Institution ID for this Requisition  # noqa: E501

        :return: The institution_id of this SpectacularRequisitionV2.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this SpectacularRequisitionV2.

        an Institution ID for this Requisition  # noqa: E501

        :param institution_id: The institution_id of this SpectacularRequisitionV2.  # noqa: E501
        :type: str
        """
        if institution_id is None:
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def agreement(self):
        """Gets the agreement of this SpectacularRequisitionV2.  # noqa: E501

        EUA associated with this requisition  # noqa: E501

        :return: The agreement of this SpectacularRequisitionV2.  # noqa: E501
        :rtype: str
        """
        return self._agreement

    @agreement.setter
    def agreement(self, agreement):
        """Sets the agreement of this SpectacularRequisitionV2.

        EUA associated with this requisition  # noqa: E501

        :param agreement: The agreement of this SpectacularRequisitionV2.  # noqa: E501
        :type: str
        """

        self._agreement = agreement

    @property
    def reference(self):
        """Gets the reference of this SpectacularRequisitionV2.  # noqa: E501

        additional ID to identify the end user  # noqa: E501

        :return: The reference of this SpectacularRequisitionV2.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SpectacularRequisitionV2.

        additional ID to identify the end user  # noqa: E501

        :param reference: The reference of this SpectacularRequisitionV2.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def accounts(self):
        """Gets the accounts of this SpectacularRequisitionV2.  # noqa: E501

        array of account IDs retrieved within a scope of this requisition  # noqa: E501

        :return: The accounts of this SpectacularRequisitionV2.  # noqa: E501
        :rtype: list[Object]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this SpectacularRequisitionV2.

        array of account IDs retrieved within a scope of this requisition  # noqa: E501

        :param accounts: The accounts of this SpectacularRequisitionV2.  # noqa: E501
        :type: list[Object]
        """
        if accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

    @property
    def user_language(self):
        """Gets the user_language of this SpectacularRequisitionV2.  # noqa: E501

        A two-letter country code (ISO 639-1)  # noqa: E501

        :return: The user_language of this SpectacularRequisitionV2.  # noqa: E501
        :rtype: str
        """
        return self._user_language

    @user_language.setter
    def user_language(self, user_language):
        """Sets the user_language of this SpectacularRequisitionV2.

        A two-letter country code (ISO 639-1)  # noqa: E501

        :param user_language: The user_language of this SpectacularRequisitionV2.  # noqa: E501
        :type: str
        """

        self._user_language = user_language

    @property
    def link(self):
        """Gets the link of this SpectacularRequisitionV2.  # noqa: E501

        link to initiate authorization with Institution  # noqa: E501

        :return: The link of this SpectacularRequisitionV2.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SpectacularRequisitionV2.

        link to initiate authorization with Institution  # noqa: E501

        :param link: The link of this SpectacularRequisitionV2.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

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
        if issubclass(SpectacularRequisitionV2, dict):
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
        if not isinstance(other, SpectacularRequisitionV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
