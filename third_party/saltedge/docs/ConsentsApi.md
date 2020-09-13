# swagger_client.ConsentsApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consents_consent_id_get**](ConsentsApi.md#consents_consent_id_get) | **GET** /consents/{consent_id} | Show consent
[**consents_consent_id_revoke_put**](ConsentsApi.md#consents_consent_id_revoke_put) | **PUT** /consents/{consent_id}/revoke | Revoke consent
[**consents_get**](ConsentsApi.md#consents_get) | **GET** /consents | List of consents

# **consents_consent_id_get**
> ConsentResponse consents_consent_id_get(consent_id, connection_id=connection_id, customer_id=customer_id)

Show consent

Returns the [consent object](#consents-attributes).

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
api_instance = swagger_client.ConsentsApi(swagger_client.ApiClient(configuration))
consent_id = 'consent_id_example' # str | 
connection_id = 'connection_id_example' # str |  (optional)
customer_id = 'customer_id_example' # str |  (optional)

try:
    # Show consent
    api_response = api_instance.consents_consent_id_get(consent_id, connection_id=connection_id, customer_id=customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->consents_consent_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  | 
 **connection_id** | **str**|  | [optional] 
 **customer_id** | **str**|  | [optional] 

### Return type

[**ConsentResponse**](ConsentResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consents_consent_id_revoke_put**
> ConsentResponse consents_consent_id_revoke_put(consent_id, connection_id=connection_id, customer_id=customer_id)

Revoke consent

Allows you to revoke a consent for a connection or a customer.

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
api_instance = swagger_client.ConsentsApi(swagger_client.ApiClient(configuration))
consent_id = 'consent_id_example' # str | 
connection_id = 'connection_id_example' # str |  (optional)
customer_id = 'customer_id_example' # str |  (optional)

try:
    # Revoke consent
    api_response = api_instance.consents_consent_id_revoke_put(consent_id, connection_id=connection_id, customer_id=customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->consents_consent_id_revoke_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**|  | 
 **connection_id** | **str**|  | [optional] 
 **customer_id** | **str**|  | [optional] 

### Return type

[**ConsentResponse**](ConsentResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consents_get**
> ConsentsResponse consents_get(from_id=from_id, connection_id=connection_id, customer_id=customer_id)

List of consents

Returns all the consents accessible to your application for a certain customer or a connection.

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
api_instance = swagger_client.ConsentsApi(swagger_client.ApiClient(configuration))
from_id = 'from_id_example' # str |  (optional)
connection_id = 'connection_id_example' # str |  (optional)
customer_id = 'customer_id_example' # str |  (optional)

try:
    # List of consents
    api_response = api_instance.consents_get(from_id=from_id, connection_id=connection_id, customer_id=customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentsApi->consents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_id** | **str**|  | [optional] 
 **connection_id** | **str**|  | [optional] 
 **customer_id** | **str**|  | [optional] 

### Return type

[**ConsentsResponse**](ConsentsResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

