# swagger_client.ConnectionsApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connections_connection_id_delete**](ConnectionsApi.md#connections_connection_id_delete) | **DELETE** /connections/{connection_id} | Remove a connection
[**connections_connection_id_get**](ConnectionsApi.md#connections_connection_id_get) | **GET** /connections/{connection_id} | Show a connection
[**connections_connection_id_interactive_put**](ConnectionsApi.md#connections_connection_id_interactive_put) | **PUT** /connections/{connection_id}/interactive | Interactive step
[**connections_connection_id_put**](ConnectionsApi.md#connections_connection_id_put) | **PUT** /connections/{connection_id} | Update connection
[**connections_connection_id_reconnect_put**](ConnectionsApi.md#connections_connection_id_reconnect_put) | **PUT** /connections/{connection_id}/reconnect | Reconnect a connection
[**connections_connection_id_refresh_put**](ConnectionsApi.md#connections_connection_id_refresh_put) | **PUT** /connections/{connection_id}/refresh | Refresh a connection
[**connections_get**](ConnectionsApi.md#connections_get) | **GET** /connections | List of connections
[**connections_post**](ConnectionsApi.md#connections_post) | **POST** /connections | Create a connection

# **connections_connection_id_delete**
> RemovedConnectionResponse connections_connection_id_delete(connection_id)

Remove a connection

Removes a connection from our system and revokes the consent. All the associated accounts and transactions to that connection will be destroyed as well. Salt Edge will send a [destroy](#destroy) callback to your web application. Make sure to specify the `Destroy URL` in your client account by accessing <a href='https://www.saltedge.com/clients/callbacks/edit' target=\"_blank\">callbacks page</a>. 

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
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 

try:
    # Remove a connection
    api_response = api_instance.connections_connection_id_delete(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->connections_connection_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**RemovedConnectionResponse**](RemovedConnectionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_connection_id_get**
> ConnectionResponse connections_connection_id_get(connection_id)

Show a connection

Returns a single connection object.

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
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 

try:
    # Show a connection
    api_response = api_instance.connections_connection_id_get(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->connections_connection_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_connection_id_interactive_put**
> ConnectionResponse connections_connection_id_interactive_put(connection_id, body=body)

Interactive step

If the currently fetching connection requires any interactive credentials for fetching, Salt Edge will send the [Interactive callback](#interactive). Make sure to specify the `Interactive URL` in your client account by accessing <a href='https://www.saltedge.com/clients/callbacks/edit' target=\"_blank\">callbacks page</a>.  Upon receiving the interactive callback, your app should ask the user for the interactive credentials and send them to the `/interactive` route for the connection. After that, the fetching process will continue as usual. 

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
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 
body = swagger_client.InteractiveConnectionRequestBody() # InteractiveConnectionRequestBody |  (optional)

try:
    # Interactive step
    api_response = api_instance.connections_connection_id_interactive_put(connection_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->connections_connection_id_interactive_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **body** | [**InteractiveConnectionRequestBody**](InteractiveConnectionRequestBody.md)|  | [optional] 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_connection_id_put**
> ConnectionResponse connections_connection_id_put(connection_id, body=body)

Update connection

Update `status`, `store_credentials` or `daily_refresh` of a connection. 

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
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 
body = swagger_client.UpdateConnectionRequestBody() # UpdateConnectionRequestBody |  (optional)

try:
    # Update connection
    api_response = api_instance.connections_connection_id_put(connection_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->connections_connection_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **body** | [**UpdateConnectionRequestBody**](UpdateConnectionRequestBody.md)|  | [optional] 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_connection_id_reconnect_put**
> ConnectionResponse connections_connection_id_reconnect_put(connection_id, body=body)

Reconnect a connection

In order to [reconnect](#connections-reconnect) a connection, your app needs to send the credentials object, connection's `id`, [consent object](#consents-object) and/or [attempt object](#attempts-object). This means that the consent confirmation should be handled on the client's side, and the 'access terms' the customer agreed on should be passed. 

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
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 
body = swagger_client.ReconnectConnectionRequestBody() # ReconnectConnectionRequestBody |  (optional)

try:
    # Reconnect a connection
    api_response = api_instance.connections_connection_id_reconnect_put(connection_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->connections_connection_id_reconnect_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **body** | [**ReconnectConnectionRequestBody**](ReconnectConnectionRequestBody.md)|  | [optional] 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_connection_id_refresh_put**
> ConnectionResponse connections_connection_id_refresh_put(connection_id, body=body)

Refresh a connection

Allows you to trigger a refetch of the data associated with a specific connection. Note that you can refresh a connection only if it has an active [consent](#consents). If the response is successful, it will contain the `next_refresh_possible_at` value, and you can expect the [usual callbacks](#callbacks) of the fetching workflow. 

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
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | 
body = swagger_client.RefreshConnectionRequestBody() # RefreshConnectionRequestBody |  (optional)

try:
    # Refresh a connection
    api_response = api_instance.connections_connection_id_refresh_put(connection_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->connections_connection_id_refresh_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 
 **body** | [**RefreshConnectionRequestBody**](RefreshConnectionRequestBody.md)|  | [optional] 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_get**
> ConnectionsResponse connections_get(customer_id, from_id=from_id)

List of connections

Returns all the connections accessible to your application for a certain customer. The connections are sorted in ascending order of their `id`, so the newest connections will come last. We recommend you fetch the whole list of connections to check whether any of the properties have changed. 

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
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
from_id = 'from_id_example' # str |  (optional)

try:
    # List of connections
    api_response = api_instance.connections_get(customer_id, from_id=from_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->connections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **from_id** | **str**|  | [optional] 

### Return type

[**ConnectionsResponse**](ConnectionsResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_post**
> ConnectionResponse connections_post(body=body)

Create a connection

When not using [Salt Edge Connect](#salt_edge_connect), your app will have to pass the user's values of provider's [fields](#providers-fields) within the payload.  The credentials object should be modeled after the provider's fields. 

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
api_instance = swagger_client.ConnectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateConnectionRequestBody() # CreateConnectionRequestBody |  (optional)

try:
    # Create a connection
    api_response = api_instance.connections_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->connections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateConnectionRequestBody**](CreateConnectionRequestBody.md)|  | [optional] 

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

