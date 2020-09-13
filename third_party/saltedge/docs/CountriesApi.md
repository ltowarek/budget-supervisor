# swagger_client.CountriesApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countries_get**](CountriesApi.md#countries_get) | **GET** /countries | List of countries

# **countries_get**
> CountriesResponse countries_get(include_fake_providers=include_fake_providers)

List of countries

Returns a list of countries supported by Account Information API.

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
api_instance = swagger_client.CountriesApi(swagger_client.ApiClient(configuration))
include_fake_providers = true # bool |  (optional)

try:
    # List of countries
    api_response = api_instance.countries_get(include_fake_providers=include_fake_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->countries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_fake_providers** | **bool**|  | [optional] 

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

