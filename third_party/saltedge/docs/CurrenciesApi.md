# swagger_client.CurrenciesApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currencies_get**](CurrenciesApi.md#currencies_get) | **GET** /currencies | List of currencies

# **currencies_get**
> CurrenciesResponse currencies_get()

List of currencies

You can get the list of all the currencies that we support.

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
api_instance = swagger_client.CurrenciesApi(swagger_client.ApiClient(configuration))

try:
    # List of currencies
    api_response = api_instance.currencies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->currencies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrenciesResponse**](CurrenciesResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

