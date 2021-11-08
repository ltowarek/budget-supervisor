# nordigen.AgreementsApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_eua**](AgreementsApi.md#accept_eua) | **PUT** /api/v2/agreements/enduser/{id}/accept/ | 
[**create_eua_v2**](AgreementsApi.md#create_eua_v2) | **POST** /api/v2/agreements/enduser/ | 
[**delete_eua_by_id_v2**](AgreementsApi.md#delete_eua_by_id_v2) | **DELETE** /api/v2/agreements/enduser/{id}/ | 
[**retrieve_all_eu_as_for_an_end_user_v2**](AgreementsApi.md#retrieve_all_eu_as_for_an_end_user_v2) | **GET** /api/v2/agreements/enduser/ | 
[**retrieve_eua_by_id_v2**](AgreementsApi.md#retrieve_eua_by_id_v2) | **GET** /api/v2/agreements/enduser/{id}/ | 
[**retrieve_eua_text**](AgreementsApi.md#retrieve_eua_text) | **GET** /api/v2/agreements/enduser/{id}/text/ | 

# **accept_eua**
> EndUserAgreement accept_eua(body, user_agent2, ip_address2, user_agent, ip_address, id)



Accept an end-user agreement via the API.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.AgreementsApi(nordigen.ApiClient(configuration))
body = nordigen.EnduserAcceptanceDetails() # EnduserAcceptanceDetails | 
user_agent2 = 'user_agent_example' # str | 
ip_address2 = 'ip_address_example' # str | 
user_agent = 'user_agent_example' # str | 
ip_address = 'ip_address_example' # str | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this end user agreement.

try:
    api_response = api_instance.accept_eua(body, user_agent2, ip_address2, user_agent, ip_address, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->accept_eua: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnduserAcceptanceDetails**](EnduserAcceptanceDetails.md)|  | 
 **user_agent2** | **str**|  | 
 **ip_address2** | **str**|  | 
 **user_agent** | **str**|  | 
 **ip_address** | **str**|  | 
 **id** | [**str**](.md)| A UUID string identifying this end user agreement. | 

### Return type

[**EndUserAgreement**](EndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_eua_v2**
> EndUserAgreement create_eua_v2(body, id2, created2, max_historical_days2, access_valid_for_days2, access_scope2, accepted2, institution_id2, id, created, max_historical_days, access_valid_for_days, access_scope, accepted, institution_id)



API endpoints related to end-user agreements.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.AgreementsApi(nordigen.ApiClient(configuration))
body = nordigen.EndUserAgreement() # EndUserAgreement | 
id2 = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
created2 = '2013-10-20T19:20:30+01:00' # datetime | 
max_historical_days2 = 56 # int | 
access_valid_for_days2 = 56 # int | 
access_scope2 = ['access_scope_example'] # list[str] | 
accepted2 = '2013-10-20T19:20:30+01:00' # datetime | 
institution_id2 = 'institution_id_example' # str | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
created = '2013-10-20T19:20:30+01:00' # datetime | 
max_historical_days = 56 # int | 
access_valid_for_days = 56 # int | 
access_scope = ['access_scope_example'] # list[str] | 
accepted = '2013-10-20T19:20:30+01:00' # datetime | 
institution_id = 'institution_id_example' # str | 

try:
    api_response = api_instance.create_eua_v2(body, id2, created2, max_historical_days2, access_valid_for_days2, access_scope2, accepted2, institution_id2, id, created, max_historical_days, access_valid_for_days, access_scope, accepted, institution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->create_eua_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndUserAgreement**](EndUserAgreement.md)|  | 
 **id2** | [**str**](.md)|  | 
 **created2** | **datetime**|  | 
 **max_historical_days2** | **int**|  | 
 **access_valid_for_days2** | **int**|  | 
 **access_scope2** | [**list[str]**](str.md)|  | 
 **accepted2** | **datetime**|  | 
 **institution_id2** | **str**|  | 
 **id** | [**str**](.md)|  | 
 **created** | **datetime**|  | 
 **max_historical_days** | **int**|  | 
 **access_valid_for_days** | **int**|  | 
 **access_scope** | [**list[str]**](str.md)|  | 
 **accepted** | **datetime**|  | 
 **institution_id** | **str**|  | 

### Return type

[**EndUserAgreement**](EndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_eua_by_id_v2**
> dict(str, Object) delete_eua_by_id_v2(id)



Delete End User Agreement.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.AgreementsApi(nordigen.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this end user agreement.

try:
    api_response = api_instance.delete_eua_by_id_v2(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->delete_eua_by_id_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this end user agreement. | 

### Return type

[**dict(str, Object)**](Object.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_eu_as_for_an_end_user_v2**
> PaginatedEndUserAgreementList retrieve_all_eu_as_for_an_end_user_v2(limit=limit, offset=offset)



API endpoints related to end-user agreements.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.AgreementsApi(nordigen.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.retrieve_all_eu_as_for_an_end_user_v2(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->retrieve_all_eu_as_for_an_end_user_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedEndUserAgreementList**](PaginatedEndUserAgreementList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_eua_by_id_v2**
> EndUserAgreement retrieve_eua_by_id_v2(id)



API endpoints related to end-user agreements.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.AgreementsApi(nordigen.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this end user agreement.

try:
    api_response = api_instance.retrieve_eua_by_id_v2(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgreementsApi->retrieve_eua_by_id_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this end user agreement. | 

### Return type

[**EndUserAgreement**](EndUserAgreement.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_eua_text**
> retrieve_eua_text(id)



Show the text of the end-user agreement.

### Example
```python
from __future__ import print_function
import time
import nordigen
from nordigen.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nordigen.AgreementsApi(nordigen.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this end user agreement.

try:
    api_instance.retrieve_eua_text(id)
except ApiException as e:
    print("Exception when calling AgreementsApi->retrieve_eua_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this end user agreement. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

