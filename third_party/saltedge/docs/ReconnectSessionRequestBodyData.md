# ReconnectSessionRequestBodyData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | the &#x60;id&#x60; of the connection you wish to reconnect | 
**consent** | [**ConsentRequestBody**](ConsentRequestBody.md) |  | 
**attempt** | [**AttemptRequestBody**](AttemptRequestBody.md) |  | [optional] 
**daily_refresh** | **bool** | whether the connection should be automatically refreshed by Salt Edge. | [optional] 
**return_connection_id** | **bool** | whether to append &#x60;connection_id&#x60; to &#x60;return_to&#x60; URL. | [optional] 
**provider_modes** | **list[str]** | restricts the list of the providers to only the ones that have the mode included in the array. | [optional] 
**javascript_callback_type** | **str** | allows you to specify what kind of callback type you are expecting. | [optional] 
**categorization** | **str** | the type of categorization applied. | [optional] [default to 'personal']
**include_fake_providers** | **bool** | if sent as &#x60;true&#x60;, the customers of [live](/general/#live) clients will be able to connect [fake providers](#providers-fake). | [optional] 
**lost_connection_notify** | **bool** | being sent as &#x60;true&#x60;, enables you to receive a javascript callback whenever the internet connection is lost during the fetching process. The type of the callback depends on the &#x60;javascript_callback_type&#x60; you specified. It has the following payload: &#x60;{data: {error_class: &#x27;ConnectionLost&#x27;, error_message: &#x27;Internet connection was lost&#x27; }}&#x60;. | [optional] 
**show_consent_confirmation** | **bool** | if consent confirmation is handled on the client&#x27;s side, this parameter should be sent as &#x60;false&#x60; so, upon submitting the form, the user will not be asked to give his consent to Salt Edge Inc. | [optional] [default to True]
**credentials_strategy** | **str** | the strategy of storing customer&#x27;s credentials.  &lt;strong&gt;Note:&lt;/strong&gt; If the value is &#x60;ask&#x60;, on the Connect page customer will be able to choose whether to save or not his credentials on Salt Edge side  | [optional] [default to 'store']
**return_error_class** | **bool** | whether to append &#x60;error_class&#x60; to &#x60;return_to&#x60; URL. | [optional] 
**theme** | **str** | theme of Salt Edge Connect template. If not passed or available for the current template, will use &#x60;default&#x60;. | [optional] [default to 'default']
**connect_template** | **str** | defaults to &#x60;Salt Edge Connect&#x60; template unless a different template is passed and available for the current client | [optional] 
**override_credentials_strategy** | **str** | If sent as &#x60;ask&#x60;, the user will be required to confirm the credentials override upon submitting the form, in the scenario where the new credentials are different from the ones in the previous attempt. If sent as &#x60;override&#x60;, the new credentials will automatically override the old ones. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

