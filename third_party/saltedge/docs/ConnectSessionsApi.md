# swagger_client.ConnectSessionsApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_sessions_create_post**](ConnectSessionsApi.md#connect_sessions_create_post) | **POST** /connect_sessions/create | Create Connect session
[**connect_sessions_reconnect_post**](ConnectSessionsApi.md#connect_sessions_reconnect_post) | **POST** /connect_sessions/reconnect | Create Connect session to reconnect
[**connect_sessions_refresh_post**](ConnectSessionsApi.md#connect_sessions_refresh_post) | **POST** /connect_sessions/refresh | Create Connect session to refresh

# **connect_sessions_create_post**
> ConnectSessionResponse connect_sessions_create_post(body=body)

Create Connect session

Allows you to create a connect session, which will be used to access Salt Edge Connect for connection creation.

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
api_instance = swagger_client.ConnectSessionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectSessionRequestBody() # ConnectSessionRequestBody |  (optional)

try:
    # Create Connect session
    api_response = api_instance.connect_sessions_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectSessionsApi->connect_sessions_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectSessionRequestBody**](ConnectSessionRequestBody.md)|  | [optional] 

### Return type

[**ConnectSessionResponse**](ConnectSessionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_sessions_reconnect_post**
> ConnectSessionResponse connect_sessions_reconnect_post(body=body)

Create Connect session to reconnect

Allows you to create a connect session, which will be used to access Salt Edge Connect to reconnect a connection.

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
api_instance = swagger_client.ConnectSessionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReconnectSessionRequestBody() # ReconnectSessionRequestBody |  (optional)

try:
    # Create Connect session to reconnect
    api_response = api_instance.connect_sessions_reconnect_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectSessionsApi->connect_sessions_reconnect_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReconnectSessionRequestBody**](ReconnectSessionRequestBody.md)|  | [optional] 

### Return type

[**ConnectSessionResponse**](ConnectSessionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_sessions_refresh_post**
> ConnectSessionResponse connect_sessions_refresh_post(body=body)

Create Connect session to refresh

Allows you to create a connect session, which will be used to access Salt Edge Connect to refresh a connection.

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
api_instance = swagger_client.ConnectSessionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.RefreshSessionRequestBody() # RefreshSessionRequestBody |  (optional)

try:
    # Create Connect session to refresh
    api_response = api_instance.connect_sessions_refresh_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectSessionsApi->connect_sessions_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefreshSessionRequestBody**](RefreshSessionRequestBody.md)|  | [optional] 

### Return type

[**ConnectSessionResponse**](ConnectSessionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

