# UpdateConnectionRequestBodyData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**daily_refresh** | **bool** | whether the connection will be refreshed daily | [optional] 
**store_credentials** | **bool** | allows to not store credentials on Salt Edge side.  &lt;strong&gt;Note:&lt;/strong&gt; The usage of this flag is not available for &#x60;file&#x60; providers. In order to update the connection, reconnect is required. It will not be possible to use refresh option if &#x60;store_credentials&#x60; is set to &#x60;false&#x60;  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

