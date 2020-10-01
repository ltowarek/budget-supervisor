# CreateConnectionRequestBodyData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | the &#x60;id&#x60; of the customer | 
**country_code** | **str** | the country code of the desired provider | 
**provider_code** | **str** | the code of the desired provider | 
**consent** | [**ConsentRequestBody**](ConsentRequestBody.md) |  | 
**attempt** | [**AttemptRequestBody**](AttemptRequestBody.md) |  | [optional] 
**credentials** | **object** | the credentials required to access the data | [optional] 
**encrypted_credentials** | **object** | the [encrypted credentials](#encrypted_credentials) required to access the data | [optional] 
**daily_refresh** | **bool** | whether the connection should be automatically refreshed by Salt Edge. | [optional] 
**include_fake_providers** | **bool** | being [live](/general/#live), the customer will not be able to create [fake](#providers-fake) providers. This flag allows it, if sent as &#x60;true&#x60; the customer will have the possibility to create any fake provider available. | [optional] 
**categorization** | **str** | the type of categorization applied. | [optional] [default to 'personal']
**file_url** | **bool** | URL of a file. Is used when creating a connection for a provider with &#x60;file&#x60; mode | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
