# IncomeReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | the date of the first income/expense [transaction](#transactions) | 
**end_date** | **date** | the date of the last income/expense [transaction](#transactions) | 
**transactions_count** | **int** | number of income/expense [transactions](#transactions) | 
**last_year_amount** | **float** | total amount of income/expense for the last fully covered 12 months | 
**total** | **float** | total amount of income/expense per the calculated period | 
**total_per_month** | [**list[IncomeReportTotalPerMonth]**](IncomeReportTotalPerMonth.md) | total amount of income/expense per each month | 
**average** | [**IncomeReportAverage**](IncomeReportAverage.md) |  | 
**forecasted_average** | [**IncomeReportForecastedAverage**](IncomeReportForecastedAverage.md) |  | 
**streams** | [**IncomeReportStreams**](IncomeReportStreams.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

