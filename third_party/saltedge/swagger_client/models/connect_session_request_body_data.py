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

class ConnectSessionRequestBodyData(object):
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
        'consent': 'ConsentRequestBody',
        'attempt': 'AttemptRequestBody',
        'allowed_countries': 'list[str]',
        'provider_code': 'str',
        'daily_refresh': 'bool',
        'disable_provider_search': 'bool',
        'return_connection_id': 'bool',
        'provider_modes': 'list[str]',
        'categorization': 'str',
        'javascript_callback_type': 'str',
        'include_fake_providers': 'bool',
        'lost_connection_notify': 'bool',
        'show_consent_confirmation': 'bool',
        'credentials_strategy': 'str',
        'return_error_class': 'bool',
        'theme': 'str',
        'connect_template': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'consent': 'consent',
        'attempt': 'attempt',
        'allowed_countries': 'allowed_countries',
        'provider_code': 'provider_code',
        'daily_refresh': 'daily_refresh',
        'disable_provider_search': 'disable_provider_search',
        'return_connection_id': 'return_connection_id',
        'provider_modes': 'provider_modes',
        'categorization': 'categorization',
        'javascript_callback_type': 'javascript_callback_type',
        'include_fake_providers': 'include_fake_providers',
        'lost_connection_notify': 'lost_connection_notify',
        'show_consent_confirmation': 'show_consent_confirmation',
        'credentials_strategy': 'credentials_strategy',
        'return_error_class': 'return_error_class',
        'theme': 'theme',
        'connect_template': 'connect_template'
    }

    def __init__(self, customer_id=None, consent=None, attempt=None, allowed_countries=None, provider_code=None, daily_refresh=None, disable_provider_search=None, return_connection_id=None, provider_modes=None, categorization='personal', javascript_callback_type=None, include_fake_providers=None, lost_connection_notify=None, show_consent_confirmation=True, credentials_strategy='store', return_error_class=None, theme='default', connect_template=None):  # noqa: E501
        """ConnectSessionRequestBodyData - a model defined in Swagger"""  # noqa: E501
        self._customer_id = None
        self._consent = None
        self._attempt = None
        self._allowed_countries = None
        self._provider_code = None
        self._daily_refresh = None
        self._disable_provider_search = None
        self._return_connection_id = None
        self._provider_modes = None
        self._categorization = None
        self._javascript_callback_type = None
        self._include_fake_providers = None
        self._lost_connection_notify = None
        self._show_consent_confirmation = None
        self._credentials_strategy = None
        self._return_error_class = None
        self._theme = None
        self._connect_template = None
        self.discriminator = None
        self.customer_id = customer_id
        self.consent = consent
        if attempt is not None:
            self.attempt = attempt
        if allowed_countries is not None:
            self.allowed_countries = allowed_countries
        if provider_code is not None:
            self.provider_code = provider_code
        if daily_refresh is not None:
            self.daily_refresh = daily_refresh
        if disable_provider_search is not None:
            self.disable_provider_search = disable_provider_search
        if return_connection_id is not None:
            self.return_connection_id = return_connection_id
        if provider_modes is not None:
            self.provider_modes = provider_modes
        if categorization is not None:
            self.categorization = categorization
        if javascript_callback_type is not None:
            self.javascript_callback_type = javascript_callback_type
        if include_fake_providers is not None:
            self.include_fake_providers = include_fake_providers
        if lost_connection_notify is not None:
            self.lost_connection_notify = lost_connection_notify
        if show_consent_confirmation is not None:
            self.show_consent_confirmation = show_consent_confirmation
        if credentials_strategy is not None:
            self.credentials_strategy = credentials_strategy
        if return_error_class is not None:
            self.return_error_class = return_error_class
        if theme is not None:
            self.theme = theme
        if connect_template is not None:
            self.connect_template = connect_template

    @property
    def customer_id(self):
        """Gets the customer_id of this ConnectSessionRequestBodyData.  # noqa: E501

        the `id` of the customer received from [customer create](#customers-create). This field is optional for ['app' authentication](/general/#services_and_apps_authentication)  # noqa: E501

        :return: The customer_id of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ConnectSessionRequestBodyData.

        the `id` of the customer received from [customer create](#customers-create). This field is optional for ['app' authentication](/general/#services_and_apps_authentication)  # noqa: E501

        :param customer_id: The customer_id of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: str
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def consent(self):
        """Gets the consent of this ConnectSessionRequestBodyData.  # noqa: E501


        :return: The consent of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: ConsentRequestBody
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this ConnectSessionRequestBodyData.


        :param consent: The consent of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: ConsentRequestBody
        """
        if consent is None:
            raise ValueError("Invalid value for `consent`, must not be `None`")  # noqa: E501

        self._consent = consent

    @property
    def attempt(self):
        """Gets the attempt of this ConnectSessionRequestBodyData.  # noqa: E501


        :return: The attempt of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: AttemptRequestBody
        """
        return self._attempt

    @attempt.setter
    def attempt(self, attempt):
        """Sets the attempt of this ConnectSessionRequestBodyData.


        :param attempt: The attempt of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: AttemptRequestBody
        """

        self._attempt = attempt

    @property
    def allowed_countries(self):
        """Gets the allowed_countries of this ConnectSessionRequestBodyData.  # noqa: E501

        the list of countries that will be accessible in Salt Edge Connect, e.g.: `['US', 'DE']`.  # noqa: E501

        :return: The allowed_countries of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_countries

    @allowed_countries.setter
    def allowed_countries(self, allowed_countries):
        """Sets the allowed_countries of this ConnectSessionRequestBodyData.

        the list of countries that will be accessible in Salt Edge Connect, e.g.: `['US', 'DE']`.  # noqa: E501

        :param allowed_countries: The allowed_countries of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: list[str]
        """

        self._allowed_countries = allowed_countries

    @property
    def provider_code(self):
        """Gets the provider_code of this ConnectSessionRequestBodyData.  # noqa: E501

        the code of the desired provider, defaults to `null`  # noqa: E501

        :return: The provider_code of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._provider_code

    @provider_code.setter
    def provider_code(self, provider_code):
        """Sets the provider_code of this ConnectSessionRequestBodyData.

        the code of the desired provider, defaults to `null`  # noqa: E501

        :param provider_code: The provider_code of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: str
        """

        self._provider_code = provider_code

    @property
    def daily_refresh(self):
        """Gets the daily_refresh of this ConnectSessionRequestBodyData.  # noqa: E501

        whether the connection should be automatically refreshed by Salt Edge.  # noqa: E501

        :return: The daily_refresh of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._daily_refresh

    @daily_refresh.setter
    def daily_refresh(self, daily_refresh):
        """Sets the daily_refresh of this ConnectSessionRequestBodyData.

        whether the connection should be automatically refreshed by Salt Edge.  # noqa: E501

        :param daily_refresh: The daily_refresh of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._daily_refresh = daily_refresh

    @property
    def disable_provider_search(self):
        """Gets the disable_provider_search of this ConnectSessionRequestBodyData.  # noqa: E501

        whether the provider search will be disabled, works only if `provider_code` parameter is sent.  # noqa: E501

        :return: The disable_provider_search of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._disable_provider_search

    @disable_provider_search.setter
    def disable_provider_search(self, disable_provider_search):
        """Sets the disable_provider_search of this ConnectSessionRequestBodyData.

        whether the provider search will be disabled, works only if `provider_code` parameter is sent.  # noqa: E501

        :param disable_provider_search: The disable_provider_search of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._disable_provider_search = disable_provider_search

    @property
    def return_connection_id(self):
        """Gets the return_connection_id of this ConnectSessionRequestBodyData.  # noqa: E501

        whether to append `connection_id` to `return_to` URL.  # noqa: E501

        :return: The return_connection_id of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._return_connection_id

    @return_connection_id.setter
    def return_connection_id(self, return_connection_id):
        """Sets the return_connection_id of this ConnectSessionRequestBodyData.

        whether to append `connection_id` to `return_to` URL.  # noqa: E501

        :param return_connection_id: The return_connection_id of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._return_connection_id = return_connection_id

    @property
    def provider_modes(self):
        """Gets the provider_modes of this ConnectSessionRequestBodyData.  # noqa: E501

        restricts the list of the providers to only the ones that have the mode included in the array.  # noqa: E501

        :return: The provider_modes of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: list[str]
        """
        return self._provider_modes

    @provider_modes.setter
    def provider_modes(self, provider_modes):
        """Sets the provider_modes of this ConnectSessionRequestBodyData.

        restricts the list of the providers to only the ones that have the mode included in the array.  # noqa: E501

        :param provider_modes: The provider_modes of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["oauth", "web", "api", "file"]  # noqa: E501
        if not set(provider_modes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `provider_modes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(provider_modes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._provider_modes = provider_modes

    @property
    def categorization(self):
        """Gets the categorization of this ConnectSessionRequestBodyData.  # noqa: E501

        the type of categorization applied.  # noqa: E501

        :return: The categorization of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._categorization

    @categorization.setter
    def categorization(self, categorization):
        """Sets the categorization of this ConnectSessionRequestBodyData.

        the type of categorization applied.  # noqa: E501

        :param categorization: The categorization of this ConnectSessionRequestBodyData.  # noqa: E501
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
    def javascript_callback_type(self):
        """Gets the javascript_callback_type of this ConnectSessionRequestBodyData.  # noqa: E501

        allows you to specify what kind of callback type you are expecting.  # noqa: E501

        :return: The javascript_callback_type of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._javascript_callback_type

    @javascript_callback_type.setter
    def javascript_callback_type(self, javascript_callback_type):
        """Sets the javascript_callback_type of this ConnectSessionRequestBodyData.

        allows you to specify what kind of callback type you are expecting.  # noqa: E501

        :param javascript_callback_type: The javascript_callback_type of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: str
        """
        allowed_values = ["iframe", "external_saltbridge", "external_notify", "post_message"]  # noqa: E501
        if javascript_callback_type not in allowed_values:
            raise ValueError(
                "Invalid value for `javascript_callback_type` ({0}), must be one of {1}"  # noqa: E501
                .format(javascript_callback_type, allowed_values)
            )

        self._javascript_callback_type = javascript_callback_type

    @property
    def include_fake_providers(self):
        """Gets the include_fake_providers of this ConnectSessionRequestBodyData.  # noqa: E501

        if sent as `true`, the customers of [live](/general/#live) clients will be able to connect [fake providers](#providers-fake).  # noqa: E501

        :return: The include_fake_providers of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._include_fake_providers

    @include_fake_providers.setter
    def include_fake_providers(self, include_fake_providers):
        """Sets the include_fake_providers of this ConnectSessionRequestBodyData.

        if sent as `true`, the customers of [live](/general/#live) clients will be able to connect [fake providers](#providers-fake).  # noqa: E501

        :param include_fake_providers: The include_fake_providers of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._include_fake_providers = include_fake_providers

    @property
    def lost_connection_notify(self):
        """Gets the lost_connection_notify of this ConnectSessionRequestBodyData.  # noqa: E501

        being sent as `true`, enables you to receive a javascript callback whenever the internet connection is lost during the fetching process. The type of the callback depends on the `javascript_callback_type` you specified. It has the following payload: `{data: {error_class: 'ConnectionLost', error_message: 'Internet connection was lost'}}`.  # noqa: E501

        :return: The lost_connection_notify of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._lost_connection_notify

    @lost_connection_notify.setter
    def lost_connection_notify(self, lost_connection_notify):
        """Sets the lost_connection_notify of this ConnectSessionRequestBodyData.

        being sent as `true`, enables you to receive a javascript callback whenever the internet connection is lost during the fetching process. The type of the callback depends on the `javascript_callback_type` you specified. It has the following payload: `{data: {error_class: 'ConnectionLost', error_message: 'Internet connection was lost'}}`.  # noqa: E501

        :param lost_connection_notify: The lost_connection_notify of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._lost_connection_notify = lost_connection_notify

    @property
    def show_consent_confirmation(self):
        """Gets the show_consent_confirmation of this ConnectSessionRequestBodyData.  # noqa: E501

        if consent confirmation is handled on the client's side, this parameter should be sent as `false` so, upon submitting the form, the user will not be asked to give his consent to Salt Edge Inc.  # noqa: E501

        :return: The show_consent_confirmation of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._show_consent_confirmation

    @show_consent_confirmation.setter
    def show_consent_confirmation(self, show_consent_confirmation):
        """Sets the show_consent_confirmation of this ConnectSessionRequestBodyData.

        if consent confirmation is handled on the client's side, this parameter should be sent as `false` so, upon submitting the form, the user will not be asked to give his consent to Salt Edge Inc.  # noqa: E501

        :param show_consent_confirmation: The show_consent_confirmation of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._show_consent_confirmation = show_consent_confirmation

    @property
    def credentials_strategy(self):
        """Gets the credentials_strategy of this ConnectSessionRequestBodyData.  # noqa: E501

        the strategy of storing customer's credentials.  <strong>Note:</strong> If the value is `ask`, on the Connect page customer will be able to choose whether to save or not his credentials on Salt Edge side   # noqa: E501

        :return: The credentials_strategy of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._credentials_strategy

    @credentials_strategy.setter
    def credentials_strategy(self, credentials_strategy):
        """Sets the credentials_strategy of this ConnectSessionRequestBodyData.

        the strategy of storing customer's credentials.  <strong>Note:</strong> If the value is `ask`, on the Connect page customer will be able to choose whether to save or not his credentials on Salt Edge side   # noqa: E501

        :param credentials_strategy: The credentials_strategy of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: str
        """
        allowed_values = ["store", "do_not_store", "ask"]  # noqa: E501
        if credentials_strategy not in allowed_values:
            raise ValueError(
                "Invalid value for `credentials_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(credentials_strategy, allowed_values)
            )

        self._credentials_strategy = credentials_strategy

    @property
    def return_error_class(self):
        """Gets the return_error_class of this ConnectSessionRequestBodyData.  # noqa: E501

        whether to append `error_class` to `return_to` URL.  # noqa: E501

        :return: The return_error_class of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: bool
        """
        return self._return_error_class

    @return_error_class.setter
    def return_error_class(self, return_error_class):
        """Sets the return_error_class of this ConnectSessionRequestBodyData.

        whether to append `error_class` to `return_to` URL.  # noqa: E501

        :param return_error_class: The return_error_class of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: bool
        """

        self._return_error_class = return_error_class

    @property
    def theme(self):
        """Gets the theme of this ConnectSessionRequestBodyData.  # noqa: E501

        theme of Salt Edge Connect template. If not passed or available for the current template, will use `default`.  # noqa: E501

        :return: The theme of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this ConnectSessionRequestBodyData.

        theme of Salt Edge Connect template. If not passed or available for the current template, will use `default`.  # noqa: E501

        :param theme: The theme of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: str
        """
        allowed_values = ["default", "dark"]  # noqa: E501
        if theme not in allowed_values:
            raise ValueError(
                "Invalid value for `theme` ({0}), must be one of {1}"  # noqa: E501
                .format(theme, allowed_values)
            )

        self._theme = theme

    @property
    def connect_template(self):
        """Gets the connect_template of this ConnectSessionRequestBodyData.  # noqa: E501

        defaults to `Salt Edge Connect` template unless a different template is passed and available for the current client  # noqa: E501

        :return: The connect_template of this ConnectSessionRequestBodyData.  # noqa: E501
        :rtype: str
        """
        return self._connect_template

    @connect_template.setter
    def connect_template(self, connect_template):
        """Sets the connect_template of this ConnectSessionRequestBodyData.

        defaults to `Salt Edge Connect` template unless a different template is passed and available for the current client  # noqa: E501

        :param connect_template: The connect_template of this ConnectSessionRequestBodyData.  # noqa: E501
        :type: str
        """

        self._connect_template = connect_template

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
        if issubclass(ConnectSessionRequestBodyData, dict):
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
        if not isinstance(other, ConnectSessionRequestBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
