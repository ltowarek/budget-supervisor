# swagger_client.TransactionsApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_delete**](TransactionsApi.md#transactions_delete) | **DELETE** /transactions | Remove transactions
[**transactions_duplicate_put**](TransactionsApi.md#transactions_duplicate_put) | **PUT** /transactions/duplicate | Mark as duplicate
[**transactions_duplicates_get**](TransactionsApi.md#transactions_duplicates_get) | **GET** /transactions/duplicates | List of duplicated transactions
[**transactions_get**](TransactionsApi.md#transactions_get) | **GET** /transactions | List of transactions
[**transactions_pending_get**](TransactionsApi.md#transactions_pending_get) | **GET** /transactions/pending | List of pending transactions
[**transactions_unduplicate_put**](TransactionsApi.md#transactions_unduplicate_put) | **PUT** /transactions/unduplicate | Remove duplicate flag

# **transactions_delete**
> RemovedTransactionsResponse transactions_delete(account_id, customer_id, keep_days)

Remove transactions

Remove transactions older than a specified period.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 
customer_id = 'customer_id_example' # str | 
keep_days = 56 # int | 

try:
    # Remove transactions
    api_response = api_instance.transactions_delete(account_id, customer_id, keep_days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **customer_id** | **str**|  | 
 **keep_days** | **int**|  | 

### Return type

[**RemovedTransactionsResponse**](RemovedTransactionsResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_duplicate_put**
> DuplicatedTransactionResponse transactions_duplicate_put(body=body)

Mark as duplicate

Mark a list of transactions as `duplicated`.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DuplicateTransactionsRequestBody() # DuplicateTransactionsRequestBody |  (optional)

try:
    # Mark as duplicate
    api_response = api_instance.transactions_duplicate_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_duplicate_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DuplicateTransactionsRequestBody**](DuplicateTransactionsRequestBody.md)|  | [optional] 

### Return type

[**DuplicatedTransactionResponse**](DuplicatedTransactionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_duplicates_get**
> TransactionsResponse transactions_duplicates_get(connection_id, account_id=account_id, from_id=from_id)

List of duplicated transactions

You can see the list of the duplicated transactions of an account.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 
account_id = 'account_id_example' # str |  (optional)
from_id = 'from_id_example' # str |  (optional)

try:
    # List of duplicated transactions
    api_response = api_instance.transactions_duplicates_get(connection_id, account_id=account_id, from_id=from_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_duplicates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **account_id** | **str**|  | [optional] 
 **from_id** | **str**|  | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_get**
> TransactionsResponse transactions_get(connection_id, account_id=account_id, from_id=from_id)

List of transactions

You can see the list of non-duplicated transactions of an account.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 
account_id = 'account_id_example' # str |  (optional)
from_id = 'from_id_example' # str |  (optional)

try:
    # List of transactions
    api_response = api_instance.transactions_get(connection_id, account_id=account_id, from_id=from_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **account_id** | **str**|  | [optional] 
 **from_id** | **str**|  | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_pending_get**
> TransactionsResponse transactions_pending_get(connection_id, account_id=account_id, from_id=from_id)

List of pending transactions

You can use this route to obtain the currently pending transactions for an account.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 
account_id = 'account_id_example' # str |  (optional)
from_id = 'from_id_example' # str |  (optional)

try:
    # List of pending transactions
    api_response = api_instance.transactions_pending_get(connection_id, account_id=account_id, from_id=from_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_pending_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **account_id** | **str**|  | [optional] 
 **from_id** | **str**|  | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_unduplicate_put**
> UnduplicatedTransactionResponse transactions_unduplicate_put(body=body)

Remove duplicate flag

Remove the duplicated flag from a list of transactions.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UnduplicateTransactionsRequestBody() # UnduplicateTransactionsRequestBody |  (optional)

try:
    # Remove duplicate flag
    api_response = api_instance.transactions_unduplicate_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_unduplicate_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnduplicateTransactionsRequestBody**](UnduplicateTransactionsRequestBody.md)|  | [optional] 

### Return type

[**UnduplicatedTransactionResponse**](UnduplicatedTransactionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

