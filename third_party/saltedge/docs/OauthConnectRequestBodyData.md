# OauthConnectRequestBodyData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | the &#x60;id&#x60; of the customer received from [customer create](#customers-create). This field is optional for [&#x27;app&#x27; authentication](/general/#services_and_apps_authentication)  | 
**country_code** | **str** | the code of the country | 
**provider_code** | **str** | the code of the provider | 
**consent** | [**ConsentRequestBody**](ConsentRequestBody.md) |  | 
**attempt** | [**AttemptRequestBody**](AttemptRequestBody.md) |  | [optional] 
**daily_refresh** | **bool** | whether the connection should be automatically refreshed by Salt Edge. | [optional] 
**return_connection_id** | **bool** | whether to append &#x60;connection_id&#x60; to &#x60;return_to&#x60; URL. | [optional] 
**categorization** | **str** | the type of categorization applied. | [optional] [default to 'personal']
**include_fake_providers** | **bool** | if sent as &#x60;true&#x60;, the customers of [live](/general/#live) clients will be able to connect [fake providers](#providers-fake).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

