# Connection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the &#x60;id&#x60; of the connection | 
**secret** | **str** | the secret key associated with a specific &#x60;connection&#x60;. It allows to read the information related to a connection using API keys of type &#x60;app&#x60;. | 
**provider_id** | **str** | the &#x60;id&#x60; of the provider the connection belongs to | 
**provider_code** | **str** | the code of the provider the connection belongs to | 
**provider_name** | **str** | the name of the provider the connection belongs to | 
**daily_refresh** | **bool** | whether the connection will be refreshed daily | 
**customer_id** | **str** | customer&#x27;s &#x60;id&#x60; | 
**created_at** | **datetime** | time and date when the connection was added | 
**updated_at** | **datetime** | the last time when the connection&#x27;s balance was changed, new accounts were imported or new transactions added/removed | 
**last_success_at** | **datetime** | time when the connection was successfully fetched | 
**status** | **str** |  | 
**country_code** | **str** | code of the country the provider belongs to | 
**next_refresh_possible_at** | **datetime** | when the next refresh will be available. May contain &#x60;null&#x60; value if connection has &#x60;automatic_fetch&#x60; set as &#x60;false&#x60;, or is already processing | [optional] 
**store_credentials** | **bool** | whether the credentials were stored on our side | 
**last_attempt** | [**SimplifiedAttempt**](SimplifiedAttempt.md) |  | 
**show_consent_confirmation** | **bool** | whether any consent was given for this connection on Salt Edge side | 
**last_consent_id** | **str** | the &#x60;id&#x60; of the last [consent](#consents) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

