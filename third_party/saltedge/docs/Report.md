# Report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ReportResult**](ReportResult.md) |  | 
**customer_id** | **int** | The &#x60;id&#x60; of the [customer](#customers) | 
**connection_ids** | **list[str]** | &#x60;ids&#x60; of [Connections](#connections) included in report | 
**connections** | [**list[ReportConnections]**](ReportConnections.md) | information related to connections included in report | 
**currency_code** | **str** | main [currency code](#currencies) used for report&#x27;s generation and value conversion | 
**exchange_rates** | **object** | a list of exchange rates at the time of report creation | 
**report_id** | **int** | the &#x60;id&#x60; of the generated report | 
**report_types** | **list[str]** | types of generated reports. | 
**status** | **str** | current report&#x27;s status. | 
**from_date** | **date** | the date from which the data in the report are included | 
**to_date** | **date** | the date to which the data in the report are included | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

