# RefreshConnectionRequestBodyData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | [**AttemptRequestBody**](AttemptRequestBody.md) |  | [optional] 
**daily_refresh** | **bool** | whether the connection should be automatically refreshed by Salt Edge. | [optional] 
**include_fake_providers** | **bool** | being [live](/general/#live), the customer will not be able to create [fake](#providers-fake) providers. This flag allows it, if sent as &#x60;true&#x60; the customer will have the possibility to create any fake provider available. | [optional] 
**categorization** | **str** | the type of categorization applied. | [optional] [default to 'personal']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

