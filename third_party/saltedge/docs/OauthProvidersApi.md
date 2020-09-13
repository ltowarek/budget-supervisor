# swagger_client.OauthProvidersApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_providers_authorize_put**](OauthProvidersApi.md#oauth_providers_authorize_put) | **PUT** /oauth_providers/authorize | Authorize a connection
[**oauth_providers_create_post**](OauthProvidersApi.md#oauth_providers_create_post) | **POST** /oauth_providers/create | Create connection for OAuth provider
[**oauth_providers_reconnect_post**](OauthProvidersApi.md#oauth_providers_reconnect_post) | **POST** /oauth_providers/reconnect | Reconnect OAuth connection

# **oauth_providers_authorize_put**
> OauthAuthorizedResponse oauth_providers_authorize_put(body=body)

Authorize a connection

Used to authorize a connection for an OAuth provider when using client owned [provider keys](/general/#client_provider_keys). In this flow, once the end-user will be authorized on the provider's side, they will be redirected to the `return_to` URL indicated in the [previous request](#oauth_providers-create), with a bunch of parameters appended to it by the provider that are needed for authorizing the connection. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: app_id
configuration = swagger_client.Configuration()
configuration.api_key['App-id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['App-id'] = 'Bearer'
# Configure API key authorization: secret
configuration = swagger_client.Configuration()
configuration.api_key['Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Secret'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OauthProvidersApi(swagger_client.ApiClient(configuration))
body = swagger_client.OauthAuthorizeRequestBody() # OauthAuthorizeRequestBody |  (optional)

try:
    # Authorize a connection
    api_response = api_instance.oauth_providers_authorize_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthProvidersApi->oauth_providers_authorize_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OauthAuthorizeRequestBody**](OauthAuthorizeRequestBody.md)|  | [optional] 

### Return type

[**OauthAuthorizedResponse**](OauthAuthorizedResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_providers_create_post**
> OauthConnectResponse oauth_providers_create_post(body=body)

Create connection for OAuth provider

Used to create a connection for an OAuth provider. After receiving the response, the customer will be redirected to `return_to` URL.  Mobile clients receive a `connection_secret` parameter in the `return_to` URL if the connection was successfully connected and an `error_message` parameter if the connection failed to connect for some reason. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: app_id
configuration = swagger_client.Configuration()
configuration.api_key['App-id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['App-id'] = 'Bearer'
# Configure API key authorization: secret
configuration = swagger_client.Configuration()
configuration.api_key['Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Secret'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OauthProvidersApi(swagger_client.ApiClient(configuration))
body = swagger_client.OauthConnectRequestBody() # OauthConnectRequestBody |  (optional)

try:
    # Create connection for OAuth provider
    api_response = api_instance.oauth_providers_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthProvidersApi->oauth_providers_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OauthConnectRequestBody**](OauthConnectRequestBody.md)|  | [optional] 

### Return type

[**OauthConnectResponse**](OauthConnectResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_providers_reconnect_post**
> OauthConnectResponse oauth_providers_reconnect_post(body=body)

Reconnect OAuth connection

Used to reconnect a connection for an OAuth provider. After receiving the response, the customer will be redirected to the `return_to` URL.  Mobile clients receive a `connection_secret` parameter in the `return_to` URL if the connection was successfully connected and an `error_message` parameter if the connection failed to connect for some reason. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: app_id
configuration = swagger_client.Configuration()
configuration.api_key['App-id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['App-id'] = 'Bearer'
# Configure API key authorization: secret
configuration = swagger_client.Configuration()
configuration.api_key['Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Secret'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OauthProvidersApi(swagger_client.ApiClient(configuration))
body = swagger_client.OauthReconnectRequestBody() # OauthReconnectRequestBody |  (optional)

try:
    # Reconnect OAuth connection
    api_response = api_instance.oauth_providers_reconnect_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthProvidersApi->oauth_providers_reconnect_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OauthReconnectRequestBody**](OauthReconnectRequestBody.md)|  | [optional] 

### Return type

[**OauthConnectResponse**](OauthConnectResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

