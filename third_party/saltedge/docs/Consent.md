# Consent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the &#x60;id&#x60; of the consent | 
**connection_id** | **str** | the &#x60;id&#x60; of the [connection](#connections) | 
**customer_id** | **str** | the &#x60;id&#x60; of the [customer](#customers) | 
**scopes** | **list[str]** | data that is allowed to be fetched. | 
**period_days** | **int** | the period the consent will be valid for | 
**expires_at** | **datetime** | the date when the consent will expire | 
**from_date** | **date** | the date from which the data has been allowed to be fetched | 
**to_date** | **date** | the date until which the data has been allowed to be fetched | 
**collected_by** | **str** | entity who collected the consent. | 
**revoked_at** | **datetime** | the date when consent was revoked | 
**revoke_reason** | **str** | revoke reason. | 
**created_at** | **datetime** | when the consent was created | 
**updated_at** | **datetime** | when the consent was updated | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

