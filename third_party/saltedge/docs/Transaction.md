# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the transaction | 
**mode** | **str** |  | 
**status** | **str** |  | 
**made_on** | **date** | the date when the transaction was made | 
**amount** | **float** | transaction&#x27;s amount | 
**currency_code** | **str** | transaction&#x27;s currency code | 
**description** | **str** | transaction&#x27;s description | 
**category** | **str** | transaction&#x27;s category | 
**duplicated** | **bool** | whether the transaction is duplicated or not | 
**extra** | [**TransactionExtra**](TransactionExtra.md) |  | 
**account_id** | **str** | the &#x60;id&#x60; of the account the transaction belongs to | 
**created_at** | **datetime** | time and date when the transaction was imported | 
**updated_at** | **datetime** | the last time when the transaction&#x27;s attributes (duplicated flag set, category learned applied) were changed by the client | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

