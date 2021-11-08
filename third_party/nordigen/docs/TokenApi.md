# nordigen.TokenApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**j_wt_obtain**](TokenApi.md#j_wt_obtain) | **POST** /api/v2/token/new/ | 
[**j_wt_refresh**](TokenApi.md#j_wt_refresh) | **POST** /api/v2/token/refresh/ | 

# **j_wt_obtain**
> SpectacularJWTObtain j_wt_obtain(body, secret_id2, secret_key2, secret_id, secret_key)



Obtain JWT pair

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.TokenApi(nordigen.ApiClient(configuration))
body = nordigen.JWTObtainPair() # JWTObtainPair | 
secret_id2 = 'secret_id_example' # str | 
secret_key2 = 'secret_key_example' # str | 
secret_id = 'secret_id_example' # str | 
secret_key = 'secret_key_example' # str | 

try:
    api_response = api_instance.j_wt_obtain(body, secret_id2, secret_key2, secret_id, secret_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->j_wt_obtain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JWTObtainPair**](JWTObtainPair.md)|  | 
 **secret_id2** | **str**|  | 
 **secret_key2** | **str**|  | 
 **secret_id** | **str**|  | 
 **secret_key** | **str**|  | 

### Return type

[**SpectacularJWTObtain**](SpectacularJWTObtain.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **j_wt_refresh**
> SpectacularJWTRefresh j_wt_refresh(body, refresh2, access2, refresh, access)



Refresh access token

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.TokenApi(nordigen.ApiClient(configuration))
body = nordigen.JWTRefresh() # JWTRefresh | 
refresh2 = 'refresh_example' # str | 
access2 = 'access_example' # str | 
refresh = 'refresh_example' # str | 
access = 'access_example' # str | 

try:
    api_response = api_instance.j_wt_refresh(body, refresh2, access2, refresh, access)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->j_wt_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JWTRefresh**](JWTRefresh.md)|  | 
 **refresh2** | **str**|  | 
 **access2** | **str**|  | 
 **refresh** | **str**|  | 
 **access** | **str**|  | 

### Return type

[**SpectacularJWTRefresh**](SpectacularJWTRefresh.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

