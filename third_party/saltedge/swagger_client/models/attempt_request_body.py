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

class AttemptRequestBody(object):
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
        'fetch_scopes': 'list[str]',
        'from_date': 'date',
        'to_date': 'date',
        'fetched_accounts_notify': 'bool',
        'custom_fields': 'object',
        'locale': 'str',
        'include_natures': 'list[str]',
        'customer_last_logged_at': 'datetime',
        'exclude_accounts': 'list[str]',
        'store_credentials': 'bool',
        'user_present': 'bool',
        'return_to': 'str'
    }

    attribute_map = {
        'fetch_scopes': 'fetch_scopes',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'fetched_accounts_notify': 'fetched_accounts_notify',
        'custom_fields': 'custom_fields',
        'locale': 'locale',
        'include_natures': 'include_natures',
        'customer_last_logged_at': 'customer_last_logged_at',
        'exclude_accounts': 'exclude_accounts',
        'store_credentials': 'store_credentials',
        'user_present': 'user_present',
        'return_to': 'return_to'
    }

    def __init__(self, fetch_scopes=None, from_date=None, to_date=None, fetched_accounts_notify=None, custom_fields=None, locale=None, include_natures=None, customer_last_logged_at=None, exclude_accounts=None, store_credentials=None, user_present=None, return_to=None):  # noqa: E501
        """AttemptRequestBody - a model defined in Swagger"""  # noqa: E501
        self._fetch_scopes = None
        self._from_date = None
        self._to_date = None
        self._fetched_accounts_notify = None
        self._custom_fields = None
        self._locale = None
        self._include_natures = None
        self._customer_last_logged_at = None
        self._exclude_accounts = None
        self._store_credentials = None
        self._user_present = None
        self._return_to = None
        self.discriminator = None
        if fetch_scopes is not None:
            self.fetch_scopes = fetch_scopes
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if fetched_accounts_notify is not None:
            self.fetched_accounts_notify = fetched_accounts_notify
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if locale is not None:
            self.locale = locale
        if include_natures is not None:
            self.include_natures = include_natures
        if customer_last_logged_at is not None:
            self.customer_last_logged_at = customer_last_logged_at
        if exclude_accounts is not None:
            self.exclude_accounts = exclude_accounts
        self.store_credentials = store_credentials
        if user_present is not None:
            self.user_present = user_present
        if return_to is not None:
            self.return_to = return_to

    @property
    def fetch_scopes(self):
        """Gets the fetch_scopes of this AttemptRequestBody.  # noqa: E501

        fetching mode. Defaults to [consent](#consents-object) scopes. The allowed values for this parameter must comply to the [consent](#consents-object) `scopes` restriction.   # noqa: E501

        :return: The fetch_scopes of this AttemptRequestBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._fetch_scopes

    @fetch_scopes.setter
    def fetch_scopes(self, fetch_scopes):
        """Sets the fetch_scopes of this AttemptRequestBody.

        fetching mode. Defaults to [consent](#consents-object) scopes. The allowed values for this parameter must comply to the [consent](#consents-object) `scopes` restriction.   # noqa: E501

        :param fetch_scopes: The fetch_scopes of this AttemptRequestBody.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["accounts", "holder_info", "transactions"]  # noqa: E501
        if not set(fetch_scopes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `fetch_scopes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(fetch_scopes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._fetch_scopes = fetch_scopes

    @property
    def from_date(self):
        """Gets the from_date of this AttemptRequestBody.  # noqa: E501

        date from which you want to fetch data for your connection. Defaults to [consent](#consents-object) `from_date`. The allowed values for this parameter must be within exactly 365 days ago and it should comply to the fetching period restrictions in the [consent](#consents-object).  # noqa: E501

        :return: The from_date of this AttemptRequestBody.  # noqa: E501
        :rtype: date
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this AttemptRequestBody.

        date from which you want to fetch data for your connection. Defaults to [consent](#consents-object) `from_date`. The allowed values for this parameter must be within exactly 365 days ago and it should comply to the fetching period restrictions in the [consent](#consents-object).  # noqa: E501

        :param from_date: The from_date of this AttemptRequestBody.  # noqa: E501
        :type: date
        """

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this AttemptRequestBody.  # noqa: E501

        date until which you want to fetch data for your connection. Defaults to `null` (today). The allowed values for this parameter must be equal or more than `from_date` and less or equal than tomorrow. Also it should comply to the fetching period restrictions in the [consent](#consents-object).  # noqa: E501

        :return: The to_date of this AttemptRequestBody.  # noqa: E501
        :rtype: date
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this AttemptRequestBody.

        date until which you want to fetch data for your connection. Defaults to `null` (today). The allowed values for this parameter must be equal or more than `from_date` and less or equal than tomorrow. Also it should comply to the fetching period restrictions in the [consent](#consents-object).  # noqa: E501

        :param to_date: The to_date of this AttemptRequestBody.  # noqa: E501
        :type: date
        """

        self._to_date = to_date

    @property
    def fetched_accounts_notify(self):
        """Gets the fetched_accounts_notify of this AttemptRequestBody.  # noqa: E501

        whether Salt Edge should send a success callback after fetching accounts.  # noqa: E501

        :return: The fetched_accounts_notify of this AttemptRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._fetched_accounts_notify

    @fetched_accounts_notify.setter
    def fetched_accounts_notify(self, fetched_accounts_notify):
        """Sets the fetched_accounts_notify of this AttemptRequestBody.

        whether Salt Edge should send a success callback after fetching accounts.  # noqa: E501

        :param fetched_accounts_notify: The fetched_accounts_notify of this AttemptRequestBody.  # noqa: E501
        :type: bool
        """

        self._fetched_accounts_notify = fetched_accounts_notify

    @property
    def custom_fields(self):
        """Gets the custom_fields of this AttemptRequestBody.  # noqa: E501

        a JSON object, which will be sent back on any of your callbacks.  # noqa: E501

        :return: The custom_fields of this AttemptRequestBody.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this AttemptRequestBody.

        a JSON object, which will be sent back on any of your callbacks.  # noqa: E501

        :param custom_fields: The custom_fields of this AttemptRequestBody.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def locale(self):
        """Gets the locale of this AttemptRequestBody.  # noqa: E501

        the language of the Connect widget or/and provider error message in the <a href='http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes' target=\"_blank\">ISO 639-1</a> format. Possible values are: `bg`, `cz`, `de`, `en`, `es-MX`, `es`, `fr`, `he`, `hu`, `it`, `nl`, `pl`, `pt-BR`, `pt`, `ro`, `ru`, `sk`, `tr`, `uk`, `zh-HK`(Traditional), `zh`(Simplified). Defaults to `en`  # noqa: E501

        :return: The locale of this AttemptRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this AttemptRequestBody.

        the language of the Connect widget or/and provider error message in the <a href='http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes' target=\"_blank\">ISO 639-1</a> format. Possible values are: `bg`, `cz`, `de`, `en`, `es-MX`, `es`, `fr`, `he`, `hu`, `it`, `nl`, `pl`, `pt-BR`, `pt`, `ro`, `ru`, `sk`, `tr`, `uk`, `zh-HK`(Traditional), `zh`(Simplified). Defaults to `en`  # noqa: E501

        :param locale: The locale of this AttemptRequestBody.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def include_natures(self):
        """Gets the include_natures of this AttemptRequestBody.  # noqa: E501

        the natures of the accounts that need to be fetched. Check [accounts attributes](#accounts-attributes) for possible values. If `null`, all accounts will be fetched.  # noqa: E501

        :return: The include_natures of this AttemptRequestBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._include_natures

    @include_natures.setter
    def include_natures(self, include_natures):
        """Sets the include_natures of this AttemptRequestBody.

        the natures of the accounts that need to be fetched. Check [accounts attributes](#accounts-attributes) for possible values. If `null`, all accounts will be fetched.  # noqa: E501

        :param include_natures: The include_natures of this AttemptRequestBody.  # noqa: E501
        :type: list[str]
        """

        self._include_natures = include_natures

    @property
    def customer_last_logged_at(self):
        """Gets the customer_last_logged_at of this AttemptRequestBody.  # noqa: E501

        the datetime when user was last active in your application  # noqa: E501

        :return: The customer_last_logged_at of this AttemptRequestBody.  # noqa: E501
        :rtype: datetime
        """
        return self._customer_last_logged_at

    @customer_last_logged_at.setter
    def customer_last_logged_at(self, customer_last_logged_at):
        """Sets the customer_last_logged_at of this AttemptRequestBody.

        the datetime when user was last active in your application  # noqa: E501

        :param customer_last_logged_at: The customer_last_logged_at of this AttemptRequestBody.  # noqa: E501
        :type: datetime
        """

        self._customer_last_logged_at = customer_last_logged_at

    @property
    def exclude_accounts(self):
        """Gets the exclude_accounts of this AttemptRequestBody.  # noqa: E501

        array of [account `ids`](#accounts-list) which will not be fetched. Applied to `reconnect` and `refresh` atempts.  # noqa: E501

        :return: The exclude_accounts of this AttemptRequestBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_accounts

    @exclude_accounts.setter
    def exclude_accounts(self, exclude_accounts):
        """Sets the exclude_accounts of this AttemptRequestBody.

        array of [account `ids`](#accounts-list) which will not be fetched. Applied to `reconnect` and `refresh` atempts.  # noqa: E501

        :param exclude_accounts: The exclude_accounts of this AttemptRequestBody.  # noqa: E501
        :type: list[str]
        """

        self._exclude_accounts = exclude_accounts

    @property
    def store_credentials(self):
        """Gets the store_credentials of this AttemptRequestBody.  # noqa: E501

        whether the credentials should be stored on Salt Edge side  # noqa: E501

        :return: The store_credentials of this AttemptRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._store_credentials

    @store_credentials.setter
    def store_credentials(self, store_credentials):
        """Sets the store_credentials of this AttemptRequestBody.

        whether the credentials should be stored on Salt Edge side  # noqa: E501

        :param store_credentials: The store_credentials of this AttemptRequestBody.  # noqa: E501
        :type: bool
        """
        if store_credentials is None:
            raise ValueError("Invalid value for `store_credentials`, must not be `None`")  # noqa: E501

        self._store_credentials = store_credentials

    @property
    def user_present(self):
        """Gets the user_present of this AttemptRequestBody.  # noqa: E501

        whether the request was initiated by the end-user of your application. It is taken into account only for PSD2-compliant providers and used for `reconnect` and `refresh`.  # noqa: E501

        :return: The user_present of this AttemptRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._user_present

    @user_present.setter
    def user_present(self, user_present):
        """Sets the user_present of this AttemptRequestBody.

        whether the request was initiated by the end-user of your application. It is taken into account only for PSD2-compliant providers and used for `reconnect` and `refresh`.  # noqa: E501

        :param user_present: The user_present of this AttemptRequestBody.  # noqa: E501
        :type: bool
        """

        self._user_present = user_present

    @property
    def return_to(self):
        """Gets the return_to of this AttemptRequestBody.  # noqa: E501

        the URL the user will be redirected to, defaults to client's home URL. If the provider has `api` mode and interactive `true` then this field is `mandatory`.  # noqa: E501

        :return: The return_to of this AttemptRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._return_to

    @return_to.setter
    def return_to(self, return_to):
        """Sets the return_to of this AttemptRequestBody.

        the URL the user will be redirected to, defaults to client's home URL. If the provider has `api` mode and interactive `true` then this field is `mandatory`.  # noqa: E501

        :param return_to: The return_to of this AttemptRequestBody.  # noqa: E501
        :type: str
        """

        self._return_to = return_to

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
        if issubclass(AttemptRequestBody, dict):
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
        if not isinstance(other, AttemptRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
