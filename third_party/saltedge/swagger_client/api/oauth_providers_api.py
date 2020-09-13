# coding: utf-8

"""
    Salt Edge Account Information API

    API Reference for services  # noqa: E501

    OpenAPI spec version: 5.0.0
    Contact: support@saltedge.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class OauthProvidersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def oauth_providers_authorize_put(self, **kwargs):  # noqa: E501
        """Authorize a connection  # noqa: E501

        Used to authorize a connection for an OAuth provider when using client owned [provider keys](/general/#client_provider_keys). In this flow, once the end-user will be authorized on the provider's side, they will be redirected to the `return_to` URL indicated in the [previous request](#oauth_providers-create), with a bunch of parameters appended to it by the provider that are needed for authorizing the connection.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_providers_authorize_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OauthAuthorizeRequestBody body:
        :return: OauthAuthorizedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oauth_providers_authorize_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oauth_providers_authorize_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def oauth_providers_authorize_put_with_http_info(self, **kwargs):  # noqa: E501
        """Authorize a connection  # noqa: E501

        Used to authorize a connection for an OAuth provider when using client owned [provider keys](/general/#client_provider_keys). In this flow, once the end-user will be authorized on the provider's side, they will be redirected to the `return_to` URL indicated in the [previous request](#oauth_providers-create), with a bunch of parameters appended to it by the provider that are needed for authorizing the connection.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_providers_authorize_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OauthAuthorizeRequestBody body:
        :return: OauthAuthorizedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_providers_authorize_put" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['app_id', 'secret']  # noqa: E501

        return self.api_client.call_api(
            '/oauth_providers/authorize', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OauthAuthorizedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oauth_providers_create_post(self, **kwargs):  # noqa: E501
        """Create connection for OAuth provider  # noqa: E501

        Used to create a connection for an OAuth provider. After receiving the response, the customer will be redirected to `return_to` URL.  Mobile clients receive a `connection_secret` parameter in the `return_to` URL if the connection was successfully connected and an `error_message` parameter if the connection failed to connect for some reason.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_providers_create_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OauthConnectRequestBody body:
        :return: OauthConnectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oauth_providers_create_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oauth_providers_create_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def oauth_providers_create_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create connection for OAuth provider  # noqa: E501

        Used to create a connection for an OAuth provider. After receiving the response, the customer will be redirected to `return_to` URL.  Mobile clients receive a `connection_secret` parameter in the `return_to` URL if the connection was successfully connected and an `error_message` parameter if the connection failed to connect for some reason.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_providers_create_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OauthConnectRequestBody body:
        :return: OauthConnectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_providers_create_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['app_id', 'secret']  # noqa: E501

        return self.api_client.call_api(
            '/oauth_providers/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OauthConnectResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def oauth_providers_reconnect_post(self, **kwargs):  # noqa: E501
        """Reconnect OAuth connection  # noqa: E501

        Used to reconnect a connection for an OAuth provider. After receiving the response, the customer will be redirected to the `return_to` URL.  Mobile clients receive a `connection_secret` parameter in the `return_to` URL if the connection was successfully connected and an `error_message` parameter if the connection failed to connect for some reason.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_providers_reconnect_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OauthReconnectRequestBody body:
        :return: OauthConnectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.oauth_providers_reconnect_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.oauth_providers_reconnect_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def oauth_providers_reconnect_post_with_http_info(self, **kwargs):  # noqa: E501
        """Reconnect OAuth connection  # noqa: E501

        Used to reconnect a connection for an OAuth provider. After receiving the response, the customer will be redirected to the `return_to` URL.  Mobile clients receive a `connection_secret` parameter in the `return_to` URL if the connection was successfully connected and an `error_message` parameter if the connection failed to connect for some reason.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_providers_reconnect_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OauthReconnectRequestBody body:
        :return: OauthConnectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_providers_reconnect_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['app_id', 'secret']  # noqa: E501

        return self.api_client.call_api(
            '/oauth_providers/reconnect', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OauthConnectResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
