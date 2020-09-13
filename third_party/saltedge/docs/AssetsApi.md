# swagger_client.AssetsApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_get**](AssetsApi.md#assets_get) | **GET** /assets | List of assets

# **assets_get**
> AssetsResponse assets_get()

List of assets

You can get the list of all the assets that we support.

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
api_instance = swagger_client.AssetsApi(swagger_client.ApiClient(configuration))

try:
    # List of assets
    api_response = api_instance.assets_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AssetsResponse**](AssetsResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

