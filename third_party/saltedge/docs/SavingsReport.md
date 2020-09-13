# SavingsReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_month** | [**list[SavingsReportPerMonth]**](SavingsReportPerMonth.md) | information related to net savings per each month | 
**average** | [**SavingsReportAverage**](SavingsReportAverage.md) |  | 
**forecasted_average** | [**SavingsReportForecastedAverage**](SavingsReportForecastedAverage.md) |  | 
**runway** | **float** | provides an estimate (number of months) on how long the customer&#x27;s current balance will be sufficient until they run out of money. The customer&#x27;s income and expenses are taken into account.  &lt;strong&gt;Note:&lt;/strong&gt; This indicator is calculated only for cases when the customer has positive current balance and the amount of their expenses exceeds the amount of their income  | 
**expense_to_savings_rate** | **float** | shows whether the customer increases or loses his capital. Taking into account the customer&#x27;s income and expenses, this indicator shows the number of months during which the customer&#x27;s savings are either increased or reduced by an amount equal to 1 month of expenses.  &lt;strong&gt;Note:&lt;/strong&gt; This indicator is calculated only for cases when the customer has both savings/dissavings and expenses  | 
**stress_runway** | **float** | provides an estimate (number of months) on how long the customer&#x27;s current balance will be sufficient to cover their regular expenses in case they unexpectedly stops receiving income.  &lt;strong&gt;Note:&lt;/strong&gt; This indicator is calculated for all cases, except the one, when the customer has no expenses  | 
**income_stability** | **float** | average weighted stability of income from all the sources  &lt;strong&gt;Note:&lt;/strong&gt; it is close to &#x60;1&#x60;, if customer has stable income  | 
**income_regularity** | **float** | average weighted regularity of income from all the sources  &lt;strong&gt;Note:&lt;/strong&gt; it is close to &#x60;1&#x60;, if customer has regular income  | 
**income_to_expense_rate** | **float** | ratio of average monthly income to average monthly expense\&quot; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

