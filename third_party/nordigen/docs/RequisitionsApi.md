# nordigen.RequisitionsApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_requisition_by_id_v2**](RequisitionsApi.md#delete_requisition_by_id_v2) | **DELETE** /api/v2/requisitions/{id}/ | 
[**requisition_by_id**](RequisitionsApi.md#requisition_by_id) | **GET** /api/v2/requisitions/{id}/ | 
[**requisition_created**](RequisitionsApi.md#requisition_created) | **POST** /api/v2/requisitions/ | 
[**retrieve_all_requisitions**](RequisitionsApi.md#retrieve_all_requisitions) | **GET** /api/v2/requisitions/ | 

# **delete_requisition_by_id_v2**
> delete_requisition_by_id_v2(id)



Delete Requisition and all End User Agreements.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.RequisitionsApi(nordigen.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this requisition.

try:
    api_instance.delete_requisition_by_id_v2(id)
except ApiException as e:
    print("Exception when calling RequisitionsApi->delete_requisition_by_id_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this requisition. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requisition_by_id**
> RequisitionV2 requisition_by_id(id)



API endpoints related to requisitions.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.RequisitionsApi(nordigen.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this requisition.

try:
    api_response = api_instance.requisition_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequisitionsApi->requisition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this requisition. | 

### Return type

[**RequisitionV2**](RequisitionV2.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **requisition_created**
> SpectacularRequisitionV2 requisition_created(body, id2, created2, redirect2, status2, institution_id2, agreement2, reference2, accounts2, user_language2, link2, id, created, redirect, status, institution_id, agreement, reference, accounts, user_language, link)



API endpoints related to requisitions.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.RequisitionsApi(nordigen.ApiClient(configuration))
body = nordigen.RequisitionV2() # RequisitionV2 | 
id2 = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
created2 = '2013-10-20T19:20:30+01:00' # datetime | 
redirect2 = 'redirect_example' # str | 
status2 = nordigen.Object() # Object | 
institution_id2 = 'institution_id_example' # str | 
agreement2 = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
reference2 = 'reference_example' # str | 
accounts2 = ['accounts_example'] # list[str] | 
user_language2 = 'user_language_example' # str | 
link2 = 'link_example' # str | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
created = '2013-10-20T19:20:30+01:00' # datetime | 
redirect = 'redirect_example' # str | 
status = nordigen.Object() # Object | 
institution_id = 'institution_id_example' # str | 
agreement = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
reference = 'reference_example' # str | 
accounts = ['accounts_example'] # list[str] | 
user_language = 'user_language_example' # str | 
link = 'link_example' # str | 

try:
    api_response = api_instance.requisition_created(body, id2, created2, redirect2, status2, institution_id2, agreement2, reference2, accounts2, user_language2, link2, id, created, redirect, status, institution_id, agreement, reference, accounts, user_language, link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequisitionsApi->requisition_created: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequisitionV2**](RequisitionV2.md)|  | 
 **id2** | [**str**](.md)|  | 
 **created2** | **datetime**|  | 
 **redirect2** | **str**|  | 
 **status2** | [**Object**](.md)|  | 
 **institution_id2** | **str**|  | 
 **agreement2** | [**str**](.md)|  | 
 **reference2** | **str**|  | 
 **accounts2** | [**list[str]**](str.md)|  | 
 **user_language2** | **str**|  | 
 **link2** | **str**|  | 
 **id** | [**str**](.md)|  | 
 **created** | **datetime**|  | 
 **redirect** | **str**|  | 
 **status** | [**Object**](.md)|  | 
 **institution_id** | **str**|  | 
 **agreement** | [**str**](.md)|  | 
 **reference** | **str**|  | 
 **accounts** | [**list[str]**](str.md)|  | 
 **user_language** | **str**|  | 
 **link** | **str**|  | 

### Return type

[**SpectacularRequisitionV2**](SpectacularRequisitionV2.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_requisitions**
> PaginatedRequisitionV2List retrieve_all_requisitions(limit=limit, offset=offset)



API endpoints related to requisitions.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.RequisitionsApi(nordigen.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.retrieve_all_requisitions(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequisitionsApi->retrieve_all_requisitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedRequisitionV2List**](PaginatedRequisitionV2List.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

