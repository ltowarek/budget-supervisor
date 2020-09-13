# swagger_client.RatesApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rates_get**](RatesApi.md#rates_get) | **GET** /rates | List of rates

# **rates_get**
> RatesResponse rates_get(_date=_date)

List of rates

You can get the list of all the currency rates that we support. You will receive the currency rates starting March 21, 2014. If any older date is requested, you will still receive the rates starting March 21, 2014. 

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
api_instance = swagger_client.RatesApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20' # date |  (optional)

try:
    # List of rates
    api_response = api_instance.rates_get(_date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->rates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **date**|  | [optional] 

### Return type

[**RatesResponse**](RatesResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

