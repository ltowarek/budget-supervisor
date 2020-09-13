# swagger_client.CategoriesApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories_get**](CategoriesApi.md#categories_get) | **GET** /categories | List of categories
[**categories_learn_post**](CategoriesApi.md#categories_learn_post) | **POST** /categories/learn | Improve transaction categorization

# **categories_get**
> CategoriesResponse categories_get()

List of categories

You can get the list of [all the categories that we support](/data_enrichment/v5/#categories-list).

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))

try:
    # List of categories
    api_response = api_instance.categories_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->categories_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories_learn_post**
> LearnCategoryResponse categories_learn_post(body=body)

Improve transaction categorization

Your customers can change the category of some of their transactions, thus improving the categorization accuracy. 

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CategoriesRequestBody() # CategoriesRequestBody |  (optional)

try:
    # Improve transaction categorization
    api_response = api_instance.categories_learn_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->categories_learn_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategoriesRequestBody**](CategoriesRequestBody.md)|  | [optional] 

### Return type

[**LearnCategoryResponse**](LearnCategoryResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

