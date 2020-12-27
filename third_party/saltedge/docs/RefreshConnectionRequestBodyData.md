# RefreshConnectionRequestBodyData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | [**AttemptRequestBody**](AttemptRequestBody.md) |  | [optional] 
**daily_refresh** | **bool** | whether the connection should be automatically refreshed by Salt Edge. | [optional] 
**include_fake_providers** | **bool** | if sent as &#x60;true&#x60;, the customers of [live](/general/#live) clients will be able to connect [fake providers](#providers-fake). | [optional] 
**categorization** | **str** | the type of categorization applied. | [optional] [default to 'personal']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

