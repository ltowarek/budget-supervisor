# swagger_client.MerchantsApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchants_post**](MerchantsApi.md#merchants_post) | **POST** /merchants | List of merchants

# **merchants_post**
> MerchantResponse merchants_post(body=body)

List of merchants

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
api_instance = swagger_client.MerchantsApi(swagger_client.ApiClient(configuration))
body = swagger_client.MerchantRequestBody() # MerchantRequestBody |  (optional)

try:
    # List of merchants
    api_response = api_instance.merchants_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MerchantsApi->merchants_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MerchantRequestBody**](MerchantRequestBody.md)|  | [optional] 

### Return type

[**MerchantResponse**](MerchantResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

