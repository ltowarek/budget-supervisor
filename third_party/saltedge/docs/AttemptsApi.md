# swagger_client.AttemptsApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attempts_attempt_id_get**](AttemptsApi.md#attempts_attempt_id_get) | **GET** /attempts/{attempt_id} | Attempt object
[**attempts_get**](AttemptsApi.md#attempts_get) | **GET** /attempts | List of attempts

# **attempts_attempt_id_get**
> AttemptResponse attempts_attempt_id_get(attempt_id, connection_id)

Attempt object

Returns a single attempt object.

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
api_instance = swagger_client.AttemptsApi(swagger_client.ApiClient(configuration))
attempt_id = 'attempt_id_example' # str | 
connection_id = 'connection_id_example' # str | 

try:
    # Attempt object
    api_response = api_instance.attempts_attempt_id_get(attempt_id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttemptsApi->attempts_attempt_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attempt_id** | **str**|  | 
 **connection_id** | **str**|  | 

### Return type

[**AttemptResponse**](AttemptResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attempts_get**
> AttemptsResponse attempts_get(connection_id)

List of attempts

Returns a paginated list of all attempts for a certain connection.

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
api_instance = swagger_client.AttemptsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 

try:
    # List of attempts
    api_response = api_instance.attempts_get(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttemptsApi->attempts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**AttemptsResponse**](AttemptsResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

