# IncomeReportStreamsRegular

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions_count** | **int** | number of transactions, which belong to the stream | 
**transaction_ids** | **list[str]** | &#x60;ids&#x60; of [transactions](#transactions), which belong to the stream | 
**start_date** | **date** | the date of the first [transaction](#transactions) from the stream | 
**end_date** | **date** | the date of the last [transaction](#transactions) from the stream | 
**amount** | [**IncomeReportStreamsAmount**](IncomeReportStreamsAmount.md) |  | 
**frequency** | **str** | average period of time between two [transactions](#transactions) in the stream. | 
**days_count** | **int** | average number of days between two [transactions](#transactions) in the stream | 
**category_code** | **str** | category of transactions which belong to the stream | 
**description** | **str** | [transaction&#x27;s](#transactions) description common for the stream | 
**merchant** | [**IncomeReportStreamsMerchant**](IncomeReportStreamsMerchant.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

