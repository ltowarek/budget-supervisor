# ReportResultAccounts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &#x60;id&#x60; of the [account](#accounts) | 
**name** | **str** | the unique name of the account | 
**nature** | **str** | The type of the account | 
**connection_id** | **str** | &#x60;id&#x60; of the [connection](#connections) to which the account belongs | 
**start_date** | **date** | the date of the first transaction | 
**end_date** | **date** | the date of the last transaction | 
**whole_months_count** | **int** | number of full months covered by the report | 
**days_count** | **int** | number of days covered by the report | 
**monthly_average_transactions_count** | [**ReportResultMonthlyAverageTransactionsCount**](ReportResultMonthlyAverageTransactionsCount.md) |  | 
**balance** | [**BalanceReport**](BalanceReport.md) |  | 
**income** | [**IncomeReport**](IncomeReport.md) |  | 
**expense** | [**ExpenseReport**](ExpenseReport.md) |  | 
**savings** | [**SavingsReport**](SavingsReport.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

