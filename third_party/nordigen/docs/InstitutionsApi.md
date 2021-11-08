# nordigen.InstitutionsApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_all_supported_institutions_in_a_given_country**](InstitutionsApi.md#retrieve_all_supported_institutions_in_a_given_country) | **GET** /api/v2/institutions/ | 
[**retrieve_institution**](InstitutionsApi.md#retrieve_institution) | **GET** /api/v2/institutions/{id}/ | 

# **retrieve_all_supported_institutions_in_a_given_country**
> list[Aspsp] retrieve_all_supported_institutions_in_a_given_country(country)



List all available institutions

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.InstitutionsApi(nordigen.ApiClient(configuration))
country = 'country_example' # str | ISO 3166 two-character country code

try:
    api_response = api_instance.retrieve_all_supported_institutions_in_a_given_country(country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->retrieve_all_supported_institutions_in_a_given_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| ISO 3166 two-character country code | 

### Return type

[**list[Aspsp]**](Aspsp.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_institution**
> Aspsp retrieve_institution(id)



Get details about a specific Institution

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.InstitutionsApi(nordigen.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.retrieve_institution(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->retrieve_institution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Aspsp**](Aspsp.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

