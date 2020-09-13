# swagger_client.HolderInfoApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**holder_info_get**](HolderInfoApi.md#holder_info_get) | **GET** /holder_info | Holder info

# **holder_info_get**
> HolderInfoResponse holder_info_get(connection_id=connection_id)

Holder info

You can query essential information about the account holder. Make sure to request this feature to be [enabled](#know_your_customer) for your client account. 

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
api_instance = swagger_client.HolderInfoApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str |  (optional)

try:
    # Holder info
    api_response = api_instance.holder_info_get(connection_id=connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HolderInfoApi->holder_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | [optional] 

### Return type

[**HolderInfoResponse**](HolderInfoResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

