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


class ConnectSessionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def connect_sessions_create_post(self, **kwargs):  # noqa: E501
        """Create Connect session  # noqa: E501

        Allows you to create a connect session, which will be used to access Salt Edge Connect for connection creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connect_sessions_create_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectSessionRequestBody body:
        :return: ConnectSessionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connect_sessions_create_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.connect_sessions_create_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def connect_sessions_create_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Connect session  # noqa: E501

        Allows you to create a connect session, which will be used to access Salt Edge Connect for connection creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connect_sessions_create_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectSessionRequestBody body:
        :return: ConnectSessionResponse
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
                    " to method connect_sessions_create_post" % key
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
            '/connect_sessions/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectSessionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connect_sessions_reconnect_post(self, **kwargs):  # noqa: E501
        """Create Connect session to reconnect  # noqa: E501

        Allows you to create a connect session, which will be used to access Salt Edge Connect to reconnect a connection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connect_sessions_reconnect_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ReconnectSessionRequestBody body:
        :return: ConnectSessionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connect_sessions_reconnect_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.connect_sessions_reconnect_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def connect_sessions_reconnect_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Connect session to reconnect  # noqa: E501

        Allows you to create a connect session, which will be used to access Salt Edge Connect to reconnect a connection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connect_sessions_reconnect_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ReconnectSessionRequestBody body:
        :return: ConnectSessionResponse
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
                    " to method connect_sessions_reconnect_post" % key
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
            '/connect_sessions/reconnect', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectSessionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connect_sessions_refresh_post(self, **kwargs):  # noqa: E501
        """Create Connect session to refresh  # noqa: E501

        Allows you to create a connect session, which will be used to access Salt Edge Connect to refresh a connection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connect_sessions_refresh_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefreshSessionRequestBody body:
        :return: ConnectSessionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connect_sessions_refresh_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.connect_sessions_refresh_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def connect_sessions_refresh_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Connect session to refresh  # noqa: E501

        Allows you to create a connect session, which will be used to access Salt Edge Connect to refresh a connection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connect_sessions_refresh_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefreshSessionRequestBody body:
        :return: ConnectSessionResponse
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
                    " to method connect_sessions_refresh_post" % key
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
            '/connect_sessions/refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectSessionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)