# ConsentRequestBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **list[str]** | data to be allowed for fetching.  The allowed values for this parameter must fall within the client&#x27;s &#x60;allowed_fetch_scopes&#x60; and/or provider&#x27;s &#x60;supported_fetch_scopes&#x60; restrictions. To change the client&#x27;s allowed scopes, please &lt;a href&#x3D;&#x27;https://www.saltedge.com/pages/contact&#x27; target&#x3D;\&quot;_blank\&quot;&gt;contact our Sales team&lt;/a&gt;.  | 
**from_date** | **date** | date to be allowed for fetching the data from. Defaults to &#x60;90 days ago&#x60;. This parameter is used when &#x60;scopes&#x60; parameter contains &#x60;transactions_details&#x60;. The allowed values for this parameter must be within exactly 365 days ago. | [optional] 
**to_date** | **date** | date to be allowed for fetching the data until. The allowed values for this parameter must be equal or more than &#x60;from_date&#x60;. | [optional] 
**period_days** | **int** | determines the period the consent will be valid for. Defaults to &#x60;null&#x60; (limitless) or provider&#x27;s &#x60;max_consent_days&#x60;. The allowed value for this parameter must not be higher than the provider&#x27;s &#x60;max_consent_days&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

