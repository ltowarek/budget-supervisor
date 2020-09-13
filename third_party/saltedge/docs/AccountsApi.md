# swagger_client.AccountsApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_get**](AccountsApi.md#accounts_get) | **GET** /accounts | List of accounts

# **accounts_get**
> AccountsResponse accounts_get(connection_id, customer_id=customer_id, from_id=from_id)

List of accounts

You can see the list of accounts of a connection.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 
customer_id = 'customer_id_example' # str |  (optional)
from_id = 'from_id_example' # str |  (optional)

try:
    # List of accounts
    api_response = api_instance.accounts_get(connection_id, customer_id=customer_id, from_id=from_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **customer_id** | **str**|  | [optional] 
 **from_id** | **str**|  | [optional] 

### Return type

[**AccountsResponse**](AccountsResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

