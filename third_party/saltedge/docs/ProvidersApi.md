# swagger_client.ProvidersApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providers_get**](ProvidersApi.md#providers_get) | **GET** /providers | List of providers
[**providers_provider_code_get**](ProvidersApi.md#providers_provider_code_get) | **GET** /providers/{provider_code} | Show a provider

# **providers_get**
> ProvidersResponse providers_get(from_id=from_id, from_date=from_date, country_code=country_code, mode=mode, include_fake_providers=include_fake_providers, include_provider_fields=include_provider_fields, provider_key_owner=provider_key_owner)

List of providers

Returns all the providers we operate with. If a provider becomes `disabled`, it is not included in the list. 

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))
from_id = 'from_id_example' # str |  (optional)
from_date = '2013-10-20' # date |  (optional)
country_code = 'country_code_example' # str |  (optional)
mode = 'mode_example' # str |  (optional)
include_fake_providers = true # bool |  (optional)
include_provider_fields = true # bool |  (optional)
provider_key_owner = 'provider_key_owner_example' # str |  (optional)

try:
    # List of providers
    api_response = api_instance.providers_get(from_id=from_id, from_date=from_date, country_code=country_code, mode=mode, include_fake_providers=include_fake_providers, include_provider_fields=include_provider_fields, provider_key_owner=provider_key_owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_id** | **str**|  | [optional] 
 **from_date** | **date**|  | [optional] 
 **country_code** | **str**|  | [optional] 
 **mode** | **str**|  | [optional] 
 **include_fake_providers** | **bool**|  | [optional] 
 **include_provider_fields** | **bool**|  | [optional] 
 **provider_key_owner** | **str**|  | [optional] 

### Return type

[**ProvidersResponse**](ProvidersResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_provider_code_get**
> ProviderResponse providers_provider_code_get(provider_code)

Show a provider

Allows you to inspect a single provider in order to give your users a proper interface to input their credentials. The response will have an array of `required_fields` and `interactive_fields`, which are explained in more detail in [the create section](#connections-create) of this reference. 

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
api_instance = swagger_client.ProvidersApi(swagger_client.ApiClient(configuration))
provider_code = 'provider_code_example' # str | 

try:
    # Show a provider
    api_response = api_instance.providers_provider_code_get(provider_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->providers_provider_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_code** | **str**|  | 

### Return type

[**ProviderResponse**](ProviderResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

