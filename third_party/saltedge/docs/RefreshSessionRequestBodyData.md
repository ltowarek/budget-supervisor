# RefreshSessionRequestBodyData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | the &#x60;id&#x60; of the connection you wish to reconnect | 
**attempt** | [**AttemptRequestBody**](AttemptRequestBody.md) |  | [optional] 
**daily_refresh** | **bool** | whether the connection should be automatically refreshed by Salt Edge. | [optional] [default to False]
**return_connection_id** | **bool** | shows whether to append &#x60;connection_id&#x60; to &#x60;return_to&#x60; URL. | [optional] [default to False]
**provider_modes** | **list[str]** | restrict the list of the providers to only the ones that have the mode included in the array.  | [optional] 
**javascript_callback_type** | **str** | allows you to specify what kind of callback type you are expecting. If &#x60;null&#x60;, it means that you will not receive any callbacks. | [optional] 
**categorization** | **str** | the type of categorization applied. | [optional] [default to 'personal']
**lost_connection_notify** | **bool** | being sent as &#x60;true&#x60;, enables you to receive a javascript callback whenever the internet connection is lost during the fetching process. The type of the callback depends on the &#x60;javascript_callback_type&#x60; you specified. It has the following payload: &#x60;{data: {error_class: &#x27;ConnectionLost&#x27;, error_message: &#x27;Internet connection was lost&#x27;}}&#x60;. | [optional] 
**include_fake_providers** | **bool** | if sent as &#x60;true&#x60;, the customers of [live](/general/#live) clients will be able to connect [fake providers](#providers-fake). | [optional] 
**return_error_class** | **bool** | whether to append &#x60;error_class&#x60; to &#x60;return_to&#x60; URL. | [optional] 
**theme** | **str** | theme of Salt Edge Connect template. If not passed or available for the current template, will use &#x60;default&#x60;. | [optional] [default to 'default']
**connect_template** | **str** | defaults to &#x60;Salt Edge Connect&#x60; template unless a different template is passed and available for the current client | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

