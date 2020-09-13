# swagger_client.CustomersApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_delete**](CustomersApi.md#customers_customer_id_delete) | **DELETE** /customers/{customer_id} | Remove a customer
[**customers_customer_id_get**](CustomersApi.md#customers_customer_id_get) | **GET** /customers/{customer_id} | Show customer
[**customers_customer_id_lock_put**](CustomersApi.md#customers_customer_id_lock_put) | **PUT** /customers/{customer_id}/lock | Lock customer
[**customers_customer_id_unlock_put**](CustomersApi.md#customers_customer_id_unlock_put) | **PUT** /customers/{customer_id}/unlock | Unlock customer
[**customers_get**](CustomersApi.md#customers_get) | **GET** /customers | All customers.
[**customers_post**](CustomersApi.md#customers_post) | **POST** /customers | Creates a customer.

# **customers_customer_id_delete**
> RemovedCustomerResponse customers_customer_id_delete(customer_id)

Remove a customer

Deletes a customer, returning the customer object. Revokes all consents for this customer. This route is available only for web applications. 

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 56 # int | 

try:
    # Remove a customer
    api_response = api_instance.customers_customer_id_delete(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_customer_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

[**RemovedCustomerResponse**](RemovedCustomerResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_customer_id_get**
> CustomerResponse customers_customer_id_get(customer_id)

Show customer

Returns the customer object.

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 56 # int | 

try:
    # Show customer
    api_response = api_instance.customers_customer_id_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_customer_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_customer_id_lock_put**
> LockedCustomerResponse customers_customer_id_lock_put(customer_id)

Lock customer

 Locks a customer and its data, returning the customer object.  All customer related data including connections, accounts, transactions, attempts will not be available for reading, updating or deleting even by Salt Edge. This route is available only for web applications. 

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 56 # int | 

try:
    # Lock customer
    api_response = api_instance.customers_customer_id_lock_put(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_customer_id_lock_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

[**LockedCustomerResponse**](LockedCustomerResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_customer_id_unlock_put**
> UnlockedCustomerResponse customers_customer_id_unlock_put(customer_id)

Unlock customer

Unlocks a customer and its data, returning the customer object. This route is available only for web applications. 

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 56 # int | 

try:
    # Unlock customer
    api_response = api_instance.customers_customer_id_unlock_put(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_customer_id_unlock_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

[**UnlockedCustomerResponse**](UnlockedCustomerResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_get**
> CustomersResponse customers_get(identifier=identifier)

All customers.

List all of your app's customers. This route is available only for web applications, not mobile ones. 

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
identifier = 'identifier_example' # str |  (optional)

try:
    # All customers.
    api_response = api_instance.customers_get(identifier=identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | [optional] 

### Return type

[**CustomersResponse**](CustomersResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_post**
> CreatedCustomerResponse customers_post(body=body)

Creates a customer.

Creates a customer, returning the customer object.

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomerRequestBody() # CustomerRequestBody |  (optional)

try:
    # Creates a customer.
    api_response = api_instance.customers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerRequestBody**](CustomerRequestBody.md)|  | [optional] 

### Return type

[**CreatedCustomerResponse**](CreatedCustomerResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

