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

class CreateConnectionRequestBodyData(object):
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
        'customer_id': 'str',
        'country_code': 'str',
        'provider_code': 'str',
        'consent': 'ConsentRequestBody',
        'attempt': 'AttemptRequestBody',
        'credentials': 'object',
        'encrypted_credentials': 'object',
        'daily_refresh': 'bool',
        'include_fake_providers': 'bool',
        'categorization': 'str',
        'file_url': 'bool'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'country_code': 'country_code',
        'provider_code': 'provider_code',
        'consent': 'consent',
        'attempt': 'attempt',
        'credentials': 'credentials',
        'encrypted_credentials': 'encrypted_credentials',
        'daily_refresh': 'daily_refresh',
        'include_fake_providers': 'include_fake_providers',
        'categorization': 'categorization',
        'file_url': 'file_url'
    }

    def __init__(self, customer_id=None, country_code=None, provider_code=None, consent=None, attempt=None, credentials=None, encrypted_credentials=None, daily_refresh=None, include_fake_providers=None, categorization='personal', file_url=None):  # noqa: E501
        """CreateConnectionRequestBodyData - a model defined in Swagger"""  # noqa: E501
        self._customer_id = None
        self._country_code = None
        self._provider_code = None
        self._consent = None
        self._attempt = None
        self._credentials = None
        self._encrypted_credentials = None
        self._daily_refresh = None
        self._include_fake_providers = None
        self._categorization = None
        self._file_url = None
        self.discriminator = None
        self.customer_id = customer_id
        self.country_code = country_code
        self.provider_code = provider_code
        self.consent = consent
        if attempt is not None:
            self.attempt = attempt
        if credentials is not None:
            self.credentials = credentials
        if encrypted_credentials is not None:
            self.encrypted_credentials = encrypted_credentials
        if daily_refresh is not None:
            self.daily_refresh = daily_refresh
        if include_fake_providers is not None:
            self.include_fake_providers = include_fake_providers
        if categorization is not None:
            self.categorization = categorization
        if file_url is not None:
            self.file_url = file_url

    @property
    def customer_id(self):
        """Gets the customer_id of this CreateConnectionRequestBodyData.  # noqa: E501

        the `id` of the customer  # noqa: E501

        :return: The customer_id of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CreateConnectionRequestBodyData.

        the `id` of the customer  # noqa: E501

        :param customer_id: The customer_id of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: str
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def country_code(self):
        """Gets the country_code of this CreateConnectionRequestBodyData.  # noqa: E501

        the country code of the desired provider  # noqa: E501

        :return: The country_code of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this CreateConnectionRequestBodyData.

        the country code of the desired provider  # noqa: E501

        :param country_code: The country_code of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def provider_code(self):
        """Gets the provider_code of this CreateConnectionRequestBodyData.  # noqa: E501

        the code of the desired provider  # noqa: E501

        :return: The provider_code of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._provider_code

    @provider_code.setter
    def provider_code(self, provider_code):
        """Sets the provider_code of this CreateConnectionRequestBodyData.

        the code of the desired provider  # noqa: E501

        :param provider_code: The provider_code of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: str
        """
        if provider_code is None:
            raise ValueError("Invalid value for `provider_code`, must not be `None`")  # noqa: E501

        self._provider_code = provider_code

    @property
    def consent(self):
        """Gets the consent of this CreateConnectionRequestBodyData.  # noqa: E501


        :return: The consent of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: ConsentRequestBody
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this CreateConnectionRequestBodyData.


        :param consent: The consent of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: ConsentRequestBody
        """
        if consent is None:
            raise ValueError("Invalid value for `consent`, must not be `None`")  # noqa: E501

        self._consent = consent

    @property
    def attempt(self):
        """Gets the attempt of this CreateConnectionRequestBodyData.  # noqa: E501


        :return: The attempt of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: AttemptRequestBody
        """
        return self._attempt

    @attempt.setter
    def attempt(self, attempt):
        """Sets the attempt of this CreateConnectionRequestBodyData.


        :param attempt: The attempt of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: AttemptRequestBody
        """

        self._attempt = attempt

    @property
    def credentials(self):
        """Gets the credentials of this CreateConnectionRequestBodyData.  # noqa: E501

        the credentials required to access the data  # noqa: E501

        :return: The credentials of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this CreateConnectionRequestBodyData.

        the credentials required to access the data  # noqa: E501

        :param credentials: The credentials of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: object
        """

        self._credentials = credentials

    @property
    def encrypted_credentials(self):
        """Gets the encrypted_credentials of this CreateConnectionRequestBodyData.  # noqa: E501

        the [encrypted credentials](#encrypted_credentials) required to access the data  # noqa: E501

        :return: The encrypted_credentials of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: object
        """
        return self._encrypted_credentials

    @encrypted_credentials.setter
    def encrypted_credentials(self, encrypted_credentials):
        """Sets the encrypted_credentials of this CreateConnectionRequestBodyData.

        the [encrypted credentials](#encrypted_credentials) required to access the data  # noqa: E501

        :param encrypted_credentials: The encrypted_credentials of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: object
        """

        self._encrypted_credentials = encrypted_credentials

    @property
    def daily_refresh(self):
        """Gets the daily_refresh of this CreateConnectionRequestBodyData.  # noqa: E501

        whether the connection should be automatically refreshed by Salt Edge.  # noqa: E501

        :return: The daily_refresh of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._daily_refresh

    @daily_refresh.setter
    def daily_refresh(self, daily_refresh):
        """Sets the daily_refresh of this CreateConnectionRequestBodyData.

        whether the connection should be automatically refreshed by Salt Edge.  # noqa: E501

        :param daily_refresh: The daily_refresh of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._daily_refresh = daily_refresh

    @property
    def include_fake_providers(self):
        """Gets the include_fake_providers of this CreateConnectionRequestBodyData.  # noqa: E501

        being [live](/general/#live), the customer will not be able to create [fake](#providers-fake) providers. This flag allows it, if sent as `true` the customer will have the possibility to create any fake provider available.  # noqa: E501

        :return: The include_fake_providers of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._include_fake_providers

    @include_fake_providers.setter
    def include_fake_providers(self, include_fake_providers):
        """Sets the include_fake_providers of this CreateConnectionRequestBodyData.

        being [live](/general/#live), the customer will not be able to create [fake](#providers-fake) providers. This flag allows it, if sent as `true` the customer will have the possibility to create any fake provider available.  # noqa: E501

        :param include_fake_providers: The include_fake_providers of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._include_fake_providers = include_fake_providers

    @property
    def categorization(self):
        """Gets the categorization of this CreateConnectionRequestBodyData.  # noqa: E501

        the type of categorization applied.  # noqa: E501

        :return: The categorization of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._categorization

    @categorization.setter
    def categorization(self, categorization):
        """Sets the categorization of this CreateConnectionRequestBodyData.

        the type of categorization applied.  # noqa: E501

        :param categorization: The categorization of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "personal", "business"]  # noqa: E501
        if categorization not in allowed_values:
            raise ValueError(
                "Invalid value for `categorization` ({0}), must be one of {1}"  # noqa: E501
                .format(categorization, allowed_values)
            )

        self._categorization = categorization

    @property
    def file_url(self):
        """Gets the file_url of this CreateConnectionRequestBodyData.  # noqa: E501

        URL of a file. Is used when creating a connection for a provider with `file` mode  # noqa: E501

        :return: The file_url of this CreateConnectionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """Sets the file_url of this CreateConnectionRequestBodyData.

        URL of a file. Is used when creating a connection for a provider with `file` mode  # noqa: E501

        :param file_url: The file_url of this CreateConnectionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._file_url = file_url

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
        if issubclass(CreateConnectionRequestBodyData, dict):
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
        if not isinstance(other, CreateConnectionRequestBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other