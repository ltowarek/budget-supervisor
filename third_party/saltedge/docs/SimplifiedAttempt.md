# SimplifiedAttempt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_mode** | **str** | the API mode of the customer that queried the API. | [optional] 
**api_version** | **str** | the API version in which the attempt was created | [optional] 
**automatic_fetch** | **bool** | whether the connection related to the attempt can be automatically fetched | [optional] 
**daily_refresh** | **bool** | latest assigned value for &#x60;daily_refresh&#x60; in connection | [optional] 
**categorization** | **str** | the type of categorization applied. | [optional] [default to 'personal']
**created_at** | **datetime** | when the attempt was made | [optional] 
**custom_fields** | **object** | the custom fields that had been sent when creating connection/connect\\_session/oauth\\_provider | [optional] 
**device_type** | **str** | the type of the device that created the attempt. | [optional] 
**remote_ip** | **str** | the IP of the device that created the attempt | [optional] 
**exclude_accounts** | **list[str]** | the &#x60;ids&#x60; of accounts that do not need to be refreshed | [optional] 
**user_present** | **bool** | whether the request was initiated by the end-user of your application | [optional] 
**customer_last_logged_at** | **datetime** | the datetime when user was last active in your application | [optional] 
**fail_at** | **datetime** | when the attempt failed to finish | [optional] 
**fail_error_class** | **str** | class of error that triggered the fail for attempt | [optional] 
**fail_message** | **str** | message that describes the error class | [optional] 
**fetch_scopes** | **list[str]** | fetching mode. | [optional] 
**finished** | **bool** | whether the connection had finished fetching | [optional] 
**finished_recent** | **bool** | whether the connection had finished data for recent range | [optional] 
**from_date** | **date** | date from which the data had been fetched | [optional] 
**id** | **str** | &#x60;id&#x60; of the attempt | [optional] 
**interactive** | **bool** | whether the connection related to the attempt is interactive | [optional] 
**locale** | **str** | the language of the Connect widget or/and provider error message in the &lt;a href&#x3D;&#x27;http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes&#x27; target&#x3D;\&quot;_blank\&quot;&gt;ISO 639-1&lt;/a&gt; format. Possible values are: &#x60;bg&#x60;, &#x60;cz&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es-MX&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;he&#x60;, &#x60;hu&#x60;, &#x60;it&#x60;, &#x60;nl&#x60;, &#x60;pl&#x60;, &#x60;pt-BR&#x60;, &#x60;pt&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sk&#x60;, &#x60;tr&#x60;, &#x60;uk&#x60;, &#x60;zh-hk&#x60;(Traditional), &#x60;zh&#x60;(Simplified). Defaults to &#x60;en&#x60; | [optional] 
**partial** | **bool** | whether the connection was partially fetched | [optional] 
**store_credentials** | **bool** | whether the credentials were stored on our side | [optional] 
**success_at** | **datetime** | when the attempt succeeded and finished | [optional] 
**to_date** | **datetime** | date until which the data has been fetched | [optional] 
**updated_at** | **datetime** | when last attempt update occurred | [optional] 
**show_consent_confirmation** | **bool** | whether any consent was given for this connection | [optional] 
**include_natures** | **list[str]** | the natures of the accounts that need to be fetched | [optional] 
**last_stage** | [**Stage**](Stage.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

