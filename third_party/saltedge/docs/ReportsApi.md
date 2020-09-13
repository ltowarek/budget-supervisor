# swagger_client.ReportsApi

All URIs are relative to *https://www.saltedge.com/api/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_get**](ReportsApi.md#reports_get) | **GET** /reports | List of reports
[**reports_post**](ReportsApi.md#reports_post) | **POST** /reports | Create Financial Insights report
[**reports_report_id_delete**](ReportsApi.md#reports_report_id_delete) | **DELETE** /reports/{report_id} | Removes a report.
[**reports_report_id_get**](ReportsApi.md#reports_report_id_get) | **GET** /reports/{report_id} | Show a report.

# **reports_get**
> ReportsResponse reports_get(customer_id=customer_id, from_id=from_id)

List of reports

Returns all the general available reports for a customer.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str |  (optional)
from_id = 'from_id_example' # str |  (optional)

try:
    # List of reports
    api_response = api_instance.reports_get(customer_id=customer_id, from_id=from_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | [optional] 
 **from_id** | **str**|  | [optional] 

### Return type

[**ReportsResponse**](ReportsResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_post**
> CreatedReportResponse reports_post(customer_id, report_types, currency_code, from_date, to_date)

Create Financial Insights report

Allows you to create a report for a [customer](#customers) for a specific date range. 

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
report_types = ['report_types_example'] # list[str] | 
currency_code = 'currency_code_example' # str | 
from_date = '2013-10-20' # date | 
to_date = '2013-10-20' # date | 

try:
    # Create Financial Insights report
    api_response = api_instance.reports_post(customer_id, report_types, currency_code, from_date, to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **report_types** | [**list[str]**](str.md)|  | 
 **currency_code** | **str**|  | 
 **from_date** | **date**|  | 
 **to_date** | **date**|  | 

### Return type

[**CreatedReportResponse**](CreatedReportResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_report_id_delete**
> RemovedReportResponse reports_report_id_delete(report_id)

Removes a report.

Removes a report.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
report_id = 'report_id_example' # str | 

try:
    # Removes a report.
    api_response = api_instance.reports_report_id_delete(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_report_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

### Return type

[**RemovedReportResponse**](RemovedReportResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_report_id_get**
> ReportResponse reports_report_id_get(report_id)

Show a report.

Shows the generated report with all the details.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
report_id = 'report_id_example' # str | 

try:
    # Show a report.
    api_response = api_instance.reports_report_id_get(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->reports_report_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[app_id](../README.md#app_id), [secret](../README.md#secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

