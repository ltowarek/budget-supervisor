# nordigen.AccountsApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_account_balances**](AccountsApi.md#retrieve_account_balances) | **GET** /api/v2/accounts/{id}/balances/ | 
[**retrieve_account_details**](AccountsApi.md#retrieve_account_details) | **GET** /api/v2/accounts/{id}/details/ | 
[**retrieve_account_metadata**](AccountsApi.md#retrieve_account_metadata) | **GET** /api/v2/accounts/{id}/ | 
[**retrieve_account_transactions**](AccountsApi.md#retrieve_account_transactions) | **GET** /api/v2/accounts/{id}/transactions/ | 

# **retrieve_account_balances**
> retrieve_account_balances(id)



Access account balances.  Balances will be returned in Berlin Group PSD2 format.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.AccountsApi(nordigen.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_instance.retrieve_account_balances(id)
except ApiException as e:
    print("Exception when calling AccountsApi->retrieve_account_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_account_details**
> retrieve_account_details(id)



Access account details.  Account details will be returned in Berlin Group PSD2 format.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.AccountsApi(nordigen.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_instance.retrieve_account_details(id)
except ApiException as e:
    print("Exception when calling AccountsApi->retrieve_account_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_account_metadata**
> AccountV2 retrieve_account_metadata(id)



Access account metadata.  Information about the account record, such as the processing status and IBAN.  Account status is recalculated based on the error count in the latest req.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.AccountsApi(nordigen.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.retrieve_account_metadata(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->retrieve_account_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**AccountV2**](AccountV2.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_account_transactions**
> retrieve_account_transactions(id)



Access account transactions.  Transactions will be returned in Berlin Group PSD2 format.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.AccountsApi(nordigen.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_instance.retrieve_account_transactions(id)
except ApiException as e:
    print("Exception when calling AccountsApi->retrieve_account_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

