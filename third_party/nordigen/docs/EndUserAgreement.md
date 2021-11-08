# EndUserAgreement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this End User Agreement, used to refer to this end user agreement in other API calls. | 
**created** | **datetime** | The date &amp; time at which the end user agreement was created. | 
**max_historical_days** | **int** | Maximum number of days of transaction data to retrieve. | [optional] [default to 90]
**access_valid_for_days** | **int** | Number of days from acceptance that the access can be used. | [optional] [default to 90]
**access_scope** | **list[str]** | Array containing one or several values of [&#x27;balances&#x27;, &#x27;details&#x27;, &#x27;transactions&#x27;] | [optional] 
**accepted** | **datetime** | The date &amp; time at which the end user accepted the agreement. | 
**institution_id** | **str** | an Institution ID for this EUA | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

