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

class Attempt(object):
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
        'api_mode': 'str',
        'api_version': 'str',
        'automatic_fetch': 'bool',
        'daily_refresh': 'bool',
        'categorization': 'str',
        'created_at': 'datetime',
        'custom_fields': 'object',
        'device_type': 'str',
        'remote_ip': 'str',
        'exclude_accounts': 'list[str]',
        'user_present': 'bool',
        'customer_last_logged_at': 'datetime',
        'fail_at': 'datetime',
        'fail_error_class': 'str',
        'fail_message': 'str',
        'fetch_scopes': 'list[str]',
        'finished': 'bool',
        'finished_recent': 'bool',
        'from_date': 'date',
        'id': 'str',
        'interactive': 'bool',
        'locale': 'str',
        'partial': 'bool',
        'store_credentials': 'bool',
        'success_at': 'datetime',
        'to_date': 'datetime',
        'updated_at': 'datetime',
        'show_consent_confirmation': 'bool',
        'include_natures': 'list[str]',
        'stages': 'list[Stage]'
    }

    attribute_map = {
        'api_mode': 'api_mode',
        'api_version': 'api_version',
        'automatic_fetch': 'automatic_fetch',
        'daily_refresh': 'daily_refresh',
        'categorization': 'categorization',
        'created_at': 'created_at',
        'custom_fields': 'custom_fields',
        'device_type': 'device_type',
        'remote_ip': 'remote_ip',
        'exclude_accounts': 'exclude_accounts',
        'user_present': 'user_present',
        'customer_last_logged_at': 'customer_last_logged_at',
        'fail_at': 'fail_at',
        'fail_error_class': 'fail_error_class',
        'fail_message': 'fail_message',
        'fetch_scopes': 'fetch_scopes',
        'finished': 'finished',
        'finished_recent': 'finished_recent',
        'from_date': 'from_date',
        'id': 'id',
        'interactive': 'interactive',
        'locale': 'locale',
        'partial': 'partial',
        'store_credentials': 'store_credentials',
        'success_at': 'success_at',
        'to_date': 'to_date',
        'updated_at': 'updated_at',
        'show_consent_confirmation': 'show_consent_confirmation',
        'include_natures': 'include_natures',
        'stages': 'stages'
    }

    def __init__(self, api_mode=None, api_version=None, automatic_fetch=None, daily_refresh=None, categorization='personal', created_at=None, custom_fields=None, device_type=None, remote_ip=None, exclude_accounts=None, user_present=None, customer_last_logged_at=None, fail_at=None, fail_error_class=None, fail_message=None, fetch_scopes=None, finished=None, finished_recent=None, from_date=None, id=None, interactive=None, locale=None, partial=None, store_credentials=None, success_at=None, to_date=None, updated_at=None, show_consent_confirmation=None, include_natures=None, stages=None):  # noqa: E501
        """Attempt - a model defined in Swagger"""  # noqa: E501
        self._api_mode = None
        self._api_version = None
        self._automatic_fetch = None
        self._daily_refresh = None
        self._categorization = None
        self._created_at = None
        self._custom_fields = None
        self._device_type = None
        self._remote_ip = None
        self._exclude_accounts = None
        self._user_present = None
        self._customer_last_logged_at = None
        self._fail_at = None
        self._fail_error_class = None
        self._fail_message = None
        self._fetch_scopes = None
        self._finished = None
        self._finished_recent = None
        self._from_date = None
        self._id = None
        self._interactive = None
        self._locale = None
        self._partial = None
        self._store_credentials = None
        self._success_at = None
        self._to_date = None
        self._updated_at = None
        self._show_consent_confirmation = None
        self._include_natures = None
        self._stages = None
        self.discriminator = None
        self.api_mode = api_mode
        self.api_version = api_version
        self.automatic_fetch = automatic_fetch
        self.daily_refresh = daily_refresh
        self.categorization = categorization
        self.created_at = created_at
        self.custom_fields = custom_fields
        self.device_type = device_type
        self.remote_ip = remote_ip
        self.exclude_accounts = exclude_accounts
        self.user_present = user_present
        self.customer_last_logged_at = customer_last_logged_at
        self.fail_at = fail_at
        self.fail_error_class = fail_error_class
        self.fail_message = fail_message
        self.fetch_scopes = fetch_scopes
        self.finished = finished
        self.finished_recent = finished_recent
        self.from_date = from_date
        self.id = id
        self.interactive = interactive
        self.locale = locale
        self.partial = partial
        self.store_credentials = store_credentials
        self.success_at = success_at
        self.to_date = to_date
        self.updated_at = updated_at
        self.show_consent_confirmation = show_consent_confirmation
        self.include_natures = include_natures
        self.stages = stages

    @property
    def api_mode(self):
        """Gets the api_mode of this Attempt.  # noqa: E501

        the API mode of the customer that queried the API.  # noqa: E501

        :return: The api_mode of this Attempt.  # noqa: E501
        :rtype: str
        """
        return self._api_mode

    @api_mode.setter
    def api_mode(self, api_mode):
        """Sets the api_mode of this Attempt.

        the API mode of the customer that queried the API.  # noqa: E501

        :param api_mode: The api_mode of this Attempt.  # noqa: E501
        :type: str
        """
        if api_mode is None:
            raise ValueError("Invalid value for `api_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["app", "service"]  # noqa: E501
        if api_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `api_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(api_mode, allowed_values)
            )

        self._api_mode = api_mode

    @property
    def api_version(self):
        """Gets the api_version of this Attempt.  # noqa: E501

        the API version in which the attempt was created  # noqa: E501

        :return: The api_version of this Attempt.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this Attempt.

        the API version in which the attempt was created  # noqa: E501

        :param api_version: The api_version of this Attempt.  # noqa: E501
        :type: str
        """
        if api_version is None:
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def automatic_fetch(self):
        """Gets the automatic_fetch of this Attempt.  # noqa: E501

        whether the connection related to the attempt can be automatically fetched  # noqa: E501

        :return: The automatic_fetch of this Attempt.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_fetch

    @automatic_fetch.setter
    def automatic_fetch(self, automatic_fetch):
        """Sets the automatic_fetch of this Attempt.

        whether the connection related to the attempt can be automatically fetched  # noqa: E501

        :param automatic_fetch: The automatic_fetch of this Attempt.  # noqa: E501
        :type: bool
        """
        if automatic_fetch is None:
            raise ValueError("Invalid value for `automatic_fetch`, must not be `None`")  # noqa: E501

        self._automatic_fetch = automatic_fetch

    @property
    def daily_refresh(self):
        """Gets the daily_refresh of this Attempt.  # noqa: E501

        latest assigned value for `daily_refresh` in connection  # noqa: E501

        :return: The daily_refresh of this Attempt.  # noqa: E501
        :rtype: bool
        """
        return self._daily_refresh

    @daily_refresh.setter
    def daily_refresh(self, daily_refresh):
        """Sets the daily_refresh of this Attempt.

        latest assigned value for `daily_refresh` in connection  # noqa: E501

        :param daily_refresh: The daily_refresh of this Attempt.  # noqa: E501
        :type: bool
        """
        if daily_refresh is None:
            raise ValueError("Invalid value for `daily_refresh`, must not be `None`")  # noqa: E501

        self._daily_refresh = daily_refresh

    @property
    def categorization(self):
        """Gets the categorization of this Attempt.  # noqa: E501

        the type of categorization applied.  # noqa: E501

        :return: The categorization of this Attempt.  # noqa: E501
        :rtype: str
        """
        return self._categorization

    @categorization.setter
    def categorization(self, categorization):
        """Sets the categorization of this Attempt.

        the type of categorization applied.  # noqa: E501

        :param categorization: The categorization of this Attempt.  # noqa: E501
        :type: str
        """
        if categorization is None:
            raise ValueError("Invalid value for `categorization`, must not be `None`")  # noqa: E501
        allowed_values = ["none", "personal", "business"]  # noqa: E501
        if categorization not in allowed_values:
            raise ValueError(
                "Invalid value for `categorization` ({0}), must be one of {1}"  # noqa: E501
                .format(categorization, allowed_values)
            )

        self._categorization = categorization

    @property
    def created_at(self):
        """Gets the created_at of this Attempt.  # noqa: E501

        when the attempt was made  # noqa: E501

        :return: The created_at of this Attempt.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Attempt.

        when the attempt was made  # noqa: E501

        :param created_at: The created_at of this Attempt.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Attempt.  # noqa: E501

        the custom fields that had been sent when creating connection/connect\\_session/oauth\\_provider  # noqa: E501

        :return: The custom_fields of this Attempt.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Attempt.

        the custom fields that had been sent when creating connection/connect\\_session/oauth\\_provider  # noqa: E501

        :param custom_fields: The custom_fields of this Attempt.  # noqa: E501
        :type: object
        """
        if custom_fields is None:
            raise ValueError("Invalid value for `custom_fields`, must not be `None`")  # noqa: E501

        self._custom_fields = custom_fields

    @property
    def device_type(self):
        """Gets the device_type of this Attempt.  # noqa: E501

        the type of the device that created the attempt.  # noqa: E501

        :return: The device_type of this Attempt.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this Attempt.

        the type of the device that created the attempt.  # noqa: E501

        :param device_type: The device_type of this Attempt.  # noqa: E501
        :type: str
        """
        if device_type is None:
            raise ValueError("Invalid value for `device_type`, must not be `None`")  # noqa: E501
        allowed_values = ["desktop", "tablet", "mobile"]  # noqa: E501
        if device_type not in allowed_values:
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def remote_ip(self):
        """Gets the remote_ip of this Attempt.  # noqa: E501

        the IP of the device that created the attempt  # noqa: E501

        :return: The remote_ip of this Attempt.  # noqa: E501
        :rtype: str
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        """Sets the remote_ip of this Attempt.

        the IP of the device that created the attempt  # noqa: E501

        :param remote_ip: The remote_ip of this Attempt.  # noqa: E501
        :type: str
        """
        if remote_ip is None:
            raise ValueError("Invalid value for `remote_ip`, must not be `None`")  # noqa: E501

        self._remote_ip = remote_ip

    @property
    def exclude_accounts(self):
        """Gets the exclude_accounts of this Attempt.  # noqa: E501

        the `ids` of accounts that do not need to be refreshed  # noqa: E501

        :return: The exclude_accounts of this Attempt.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_accounts

    @exclude_accounts.setter
    def exclude_accounts(self, exclude_accounts):
        """Sets the exclude_accounts of this Attempt.

        the `ids` of accounts that do not need to be refreshed  # noqa: E501

        :param exclude_accounts: The exclude_accounts of this Attempt.  # noqa: E501
        :type: list[str]
        """
        if exclude_accounts is None:
            raise ValueError("Invalid value for `exclude_accounts`, must not be `None`")  # noqa: E501

        self._exclude_accounts = exclude_accounts

    @property
    def user_present(self):
        """Gets the user_present of this Attempt.  # noqa: E501

        whether the request was initiated by the end-user of your application  # noqa: E501

        :return: The user_present of this Attempt.  # noqa: E501
        :rtype: bool
        """
        return self._user_present

    @user_present.setter
    def user_present(self, user_present):
        """Sets the user_present of this Attempt.

        whether the request was initiated by the end-user of your application  # noqa: E501

        :param user_present: The user_present of this Attempt.  # noqa: E501
        :type: bool
        """
        if user_present is None:
            raise ValueError("Invalid value for `user_present`, must not be `None`")  # noqa: E501

        self._user_present = user_present

    @property
    def customer_last_logged_at(self):
        """Gets the customer_last_logged_at of this Attempt.  # noqa: E501

        the datetime when user was last active in your application  # noqa: E501

        :return: The customer_last_logged_at of this Attempt.  # noqa: E501
        :rtype: datetime
        """
        return self._customer_last_logged_at

    @customer_last_logged_at.setter
    def customer_last_logged_at(self, customer_last_logged_at):
        """Sets the customer_last_logged_at of this Attempt.

        the datetime when user was last active in your application  # noqa: E501

        :param customer_last_logged_at: The customer_last_logged_at of this Attempt.  # noqa: E501
        :type: datetime
        """
        if customer_last_logged_at is None:
            raise ValueError("Invalid value for `customer_last_logged_at`, must not be `None`")  # noqa: E501

        self._customer_last_logged_at = customer_last_logged_at

    @property
    def fail_at(self):
        """Gets the fail_at of this Attempt.  # noqa: E501

        when the attempt failed to finish  # noqa: E501

        :return: The fail_at of this Attempt.  # noqa: E501
        :rtype: datetime
        """
        return self._fail_at

    @fail_at.setter
    def fail_at(self, fail_at):
        """Sets the fail_at of this Attempt.

        when the attempt failed to finish  # noqa: E501

        :param fail_at: The fail_at of this Attempt.  # noqa: E501
        :type: datetime
        """
        if fail_at is None:
            raise ValueError("Invalid value for `fail_at`, must not be `None`")  # noqa: E501

        self._fail_at = fail_at

    @property
    def fail_error_class(self):
        """Gets the fail_error_class of this Attempt.  # noqa: E501

        class of error that triggered the fail for attempt  # noqa: E501

        :return: The fail_error_class of this Attempt.  # noqa: E501
        :rtype: str
        """
        return self._fail_error_class

    @fail_error_class.setter
    def fail_error_class(self, fail_error_class):
        """Sets the fail_error_class of this Attempt.

        class of error that triggered the fail for attempt  # noqa: E501

        :param fail_error_class: The fail_error_class of this Attempt.  # noqa: E501
        :type: str
        """
        if fail_error_class is None:
            raise ValueError("Invalid value for `fail_error_class`, must not be `None`")  # noqa: E501

        self._fail_error_class = fail_error_class

    @property
    def fail_message(self):
        """Gets the fail_message of this Attempt.  # noqa: E501

        message that describes the error class  # noqa: E501

        :return: The fail_message of this Attempt.  # noqa: E501
        :rtype: str
        """
        return self._fail_message

    @fail_message.setter
    def fail_message(self, fail_message):
        """Sets the fail_message of this Attempt.

        message that describes the error class  # noqa: E501

        :param fail_message: The fail_message of this Attempt.  # noqa: E501
        :type: str
        """
        if fail_message is None:
            raise ValueError("Invalid value for `fail_message`, must not be `None`")  # noqa: E501

        self._fail_message = fail_message

    @property
    def fetch_scopes(self):
        """Gets the fetch_scopes of this Attempt.  # noqa: E501

        fetching mode.  # noqa: E501

        :return: The fetch_scopes of this Attempt.  # noqa: E501
        :rtype: list[str]
        """
        return self._fetch_scopes

    @fetch_scopes.setter
    def fetch_scopes(self, fetch_scopes):
        """Sets the fetch_scopes of this Attempt.

        fetching mode.  # noqa: E501

        :param fetch_scopes: The fetch_scopes of this Attempt.  # noqa: E501
        :type: list[str]
        """
        if fetch_scopes is None:
            raise ValueError("Invalid value for `fetch_scopes`, must not be `None`")  # noqa: E501
        allowed_values = ["accounts", "holder_info", "transactions"]  # noqa: E501
        if not set(fetch_scopes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `fetch_scopes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(fetch_scopes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._fetch_scopes = fetch_scopes

    @property
    def finished(self):
        """Gets the finished of this Attempt.  # noqa: E501

        whether the connection had finished fetching  # noqa: E501

        :return: The finished of this Attempt.  # noqa: E501
        :rtype: bool
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this Attempt.

        whether the connection had finished fetching  # noqa: E501

        :param finished: The finished of this Attempt.  # noqa: E501
        :type: bool
        """
        if finished is None:
            raise ValueError("Invalid value for `finished`, must not be `None`")  # noqa: E501

        self._finished = finished

    @property
    def finished_recent(self):
        """Gets the finished_recent of this Attempt.  # noqa: E501

        whether the connection had finished data for recent range  # noqa: E501

        :return: The finished_recent of this Attempt.  # noqa: E501
        :rtype: bool
        """
        return self._finished_recent

    @finished_recent.setter
    def finished_recent(self, finished_recent):
        """Sets the finished_recent of this Attempt.

        whether the connection had finished data for recent range  # noqa: E501

        :param finished_recent: The finished_recent of this Attempt.  # noqa: E501
        :type: bool
        """
        if finished_recent is None:
            raise ValueError("Invalid value for `finished_recent`, must not be `None`")  # noqa: E501

        self._finished_recent = finished_recent

    @property
    def from_date(self):
        """Gets the from_date of this Attempt.  # noqa: E501

        date from which the data had been fetched  # noqa: E501

        :return: The from_date of this Attempt.  # noqa: E501
        :rtype: date
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this Attempt.

        date from which the data had been fetched  # noqa: E501

        :param from_date: The from_date of this Attempt.  # noqa: E501
        :type: date
        """
        if from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501

        self._from_date = from_date

    @property
    def id(self):
        """Gets the id of this Attempt.  # noqa: E501

        `id` of the attempt  # noqa: E501

        :return: The id of this Attempt.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Attempt.

        `id` of the attempt  # noqa: E501

        :param id: The id of this Attempt.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def interactive(self):
        """Gets the interactive of this Attempt.  # noqa: E501

        whether the connection related to the attempt is interactive  # noqa: E501

        :return: The interactive of this Attempt.  # noqa: E501
        :rtype: bool
        """
        return self._interactive

    @interactive.setter
    def interactive(self, interactive):
        """Sets the interactive of this Attempt.

        whether the connection related to the attempt is interactive  # noqa: E501

        :param interactive: The interactive of this Attempt.  # noqa: E501
        :type: bool
        """
        if interactive is None:
            raise ValueError("Invalid value for `interactive`, must not be `None`")  # noqa: E501

        self._interactive = interactive

    @property
    def locale(self):
        """Gets the locale of this Attempt.  # noqa: E501

        the language of the Connect widget or/and provider error message in the <a href='http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes' target=\"_blank\">ISO 639-1</a> format. Possible values are: `bg`, `cz`, `de`, `en`, `es-MX`, `es`, `fr`, `he`, `hu`, `it`, `nl`, `pl`, `pt-BR`, `pt`, `ro`, `ru`, `sk`, `tr`, `uk`, `zh-HK`(Traditional), `zh`(Simplified). Defaults to `en`  # noqa: E501

        :return: The locale of this Attempt.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Attempt.

        the language of the Connect widget or/and provider error message in the <a href='http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes' target=\"_blank\">ISO 639-1</a> format. Possible values are: `bg`, `cz`, `de`, `en`, `es-MX`, `es`, `fr`, `he`, `hu`, `it`, `nl`, `pl`, `pt-BR`, `pt`, `ro`, `ru`, `sk`, `tr`, `uk`, `zh-HK`(Traditional), `zh`(Simplified). Defaults to `en`  # noqa: E501

        :param locale: The locale of this Attempt.  # noqa: E501
        :type: str
        """
        if locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")  # noqa: E501

        self._locale = locale

    @property
    def partial(self):
        """Gets the partial of this Attempt.  # noqa: E501

        whether the connection was partially fetched  # noqa: E501

        :return: The partial of this Attempt.  # noqa: E501
        :rtype: bool
        """
        return self._partial

    @partial.setter
    def partial(self, partial):
        """Sets the partial of this Attempt.

        whether the connection was partially fetched  # noqa: E501

        :param partial: The partial of this Attempt.  # noqa: E501
        :type: bool
        """
        if partial is None:
            raise ValueError("Invalid value for `partial`, must not be `None`")  # noqa: E501

        self._partial = partial

    @property
    def store_credentials(self):
        """Gets the store_credentials of this Attempt.  # noqa: E501

        whether the credentials were stored on our side  # noqa: E501

        :return: The store_credentials of this Attempt.  # noqa: E501
        :rtype: bool
        """
        return self._store_credentials

    @store_credentials.setter
    def store_credentials(self, store_credentials):
        """Sets the store_credentials of this Attempt.

        whether the credentials were stored on our side  # noqa: E501

        :param store_credentials: The store_credentials of this Attempt.  # noqa: E501
        :type: bool
        """
        if store_credentials is None:
            raise ValueError("Invalid value for `store_credentials`, must not be `None`")  # noqa: E501

        self._store_credentials = store_credentials

    @property
    def success_at(self):
        """Gets the success_at of this Attempt.  # noqa: E501

        when the attempt succeeded and finished  # noqa: E501

        :return: The success_at of this Attempt.  # noqa: E501
        :rtype: datetime
        """
        return self._success_at

    @success_at.setter
    def success_at(self, success_at):
        """Sets the success_at of this Attempt.

        when the attempt succeeded and finished  # noqa: E501

        :param success_at: The success_at of this Attempt.  # noqa: E501
        :type: datetime
        """
        if success_at is None:
            raise ValueError("Invalid value for `success_at`, must not be `None`")  # noqa: E501

        self._success_at = success_at

    @property
    def to_date(self):
        """Gets the to_date of this Attempt.  # noqa: E501

        date until which the data has been fetched  # noqa: E501

        :return: The to_date of this Attempt.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this Attempt.

        date until which the data has been fetched  # noqa: E501

        :param to_date: The to_date of this Attempt.  # noqa: E501
        :type: datetime
        """
        if to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501

        self._to_date = to_date

    @property
    def updated_at(self):
        """Gets the updated_at of this Attempt.  # noqa: E501

        when last attempt update occurred  # noqa: E501

        :return: The updated_at of this Attempt.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Attempt.

        when last attempt update occurred  # noqa: E501

        :param updated_at: The updated_at of this Attempt.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def show_consent_confirmation(self):
        """Gets the show_consent_confirmation of this Attempt.  # noqa: E501

        whether any consent was given for this connection  # noqa: E501

        :return: The show_consent_confirmation of this Attempt.  # noqa: E501
        :rtype: bool
        """
        return self._show_consent_confirmation

    @show_consent_confirmation.setter
    def show_consent_confirmation(self, show_consent_confirmation):
        """Sets the show_consent_confirmation of this Attempt.

        whether any consent was given for this connection  # noqa: E501

        :param show_consent_confirmation: The show_consent_confirmation of this Attempt.  # noqa: E501
        :type: bool
        """
        if show_consent_confirmation is None:
            raise ValueError("Invalid value for `show_consent_confirmation`, must not be `None`")  # noqa: E501

        self._show_consent_confirmation = show_consent_confirmation

    @property
    def include_natures(self):
        """Gets the include_natures of this Attempt.  # noqa: E501

        the natures of the accounts that need to be fetched  # noqa: E501

        :return: The include_natures of this Attempt.  # noqa: E501
        :rtype: list[str]
        """
        return self._include_natures

    @include_natures.setter
    def include_natures(self, include_natures):
        """Sets the include_natures of this Attempt.

        the natures of the accounts that need to be fetched  # noqa: E501

        :param include_natures: The include_natures of this Attempt.  # noqa: E501
        :type: list[str]
        """
        if include_natures is None:
            raise ValueError("Invalid value for `include_natures`, must not be `None`")  # noqa: E501

        self._include_natures = include_natures

    @property
    def stages(self):
        """Gets the stages of this Attempt.  # noqa: E501

        information about [stages](#attempts-stages) through which the connection has passed  # noqa: E501

        :return: The stages of this Attempt.  # noqa: E501
        :rtype: list[Stage]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this Attempt.

        information about [stages](#attempts-stages) through which the connection has passed  # noqa: E501

        :param stages: The stages of this Attempt.  # noqa: E501
        :type: list[Stage]
        """
        if stages is None:
            raise ValueError("Invalid value for `stages`, must not be `None`")  # noqa: E501

        self._stages = stages

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
        if issubclass(Attempt, dict):
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
        if not isinstance(other, Attempt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
