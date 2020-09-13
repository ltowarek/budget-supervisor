# ReportConnections

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &#x60;id&#x60; of the [connection](#connections) | 
**customer_id** | **int** | The &#x60;id&#x60; of the [customer](#customers) | 
**provider_code** | **str** | the code of the [Provider](#providers) the connection belongs to | 
**provider_name** | **str** | the name of the [Provider](#providers) the connection belongs to | 
**accounts** | [**list[ReportAccounts]**](ReportAccounts.md) | information related to accounts, which belong to this connection | 
**holder_info** | **str** | essential information about the account holder fetched from the connected provider | 
**client_name** | **str** | Name of the Salt Edge Client, who requested the Financial Insights report | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

