# CategoriesRequestBodyDataTransactions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the &#x60;id&#x60; of the transaction | 
**category_code** | **str** | the new category code of the transaction | 
**immediate** | **bool** | If sent as &#x60;false&#x60;, the learning threshold of the categorizer will be applied - the categorizer will store information about the user&#x27;s custom category for the transaction with this description. In case the categorizer identifies that the category has been updated 3 times for the transaction with this description, further transactions with this description will be automatically categorized for this user under this category.  If sent as &#x60;true&#x60;, the learning threshold of the categorizer will be ignored and further transactions with the same description will be classified under the category chosen by the user.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

