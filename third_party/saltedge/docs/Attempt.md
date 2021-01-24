# Attempt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_mode** | **str** | the API mode of the customer that queried the API. | 
**api_version** | **str** | the API version in which the attempt was created | 
**automatic_fetch** | **bool** | whether the connection related to the attempt can be automatically fetched | 
**daily_refresh** | **bool** | latest assigned value for &#x60;daily_refresh&#x60; in connection | 
**categorization** | **str** | the type of categorization applied. | [default to 'personal']
**created_at** | **datetime** | when the attempt was made | 
**custom_fields** | **object** | the custom fields that had been sent when creating connection/connect\\_session/oauth\\_provider | 
**device_type** | **str** | the type of the device that created the attempt. | 
**remote_ip** | **str** | the IP of the device that created the attempt | 
**exclude_accounts** | **list[str]** | the &#x60;ids&#x60; of accounts that do not need to be refreshed | 
**user_present** | **bool** | whether the request was initiated by the end-user of your application | 
**customer_last_logged_at** | **datetime** | the datetime when user was last active in your application | 
**fail_at** | **datetime** | when the attempt failed to finish | 
**fail_error_class** | **str** | class of error that triggered the fail for attempt | 
**fail_message** | **str** | message that describes the error class | 
**fetch_scopes** | **list[str]** | fetching mode. | 
**finished** | **bool** | whether the connection had finished fetching | 
**finished_recent** | **bool** | whether the connection had finished data for recent range | 
**from_date** | **date** | date from which the data had been fetched | 
**id** | **str** | &#x60;id&#x60; of the attempt | 
**interactive** | **bool** | whether the connection related to the attempt is interactive | 
**locale** | **str** | the language of the Connect widget or/and provider error message in the &lt;a href&#x3D;&#x27;http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes&#x27; target&#x3D;\&quot;_blank\&quot;&gt;ISO 639-1&lt;/a&gt; format. Possible values are: &#x60;bg&#x60;, &#x60;cz&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es-MX&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;he&#x60;, &#x60;hu&#x60;, &#x60;it&#x60;, &#x60;nl&#x60;, &#x60;pl&#x60;, &#x60;pt-BR&#x60;, &#x60;pt&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sk&#x60;, &#x60;tr&#x60;, &#x60;uk&#x60;, &#x60;zh-HK&#x60;(Traditional), &#x60;zh&#x60;(Simplified). Defaults to &#x60;en&#x60; | 
**partial** | **bool** | whether the connection was partially fetched | 
**store_credentials** | **bool** | whether the credentials were stored on our side | 
**success_at** | **datetime** | when the attempt succeeded and finished | 
**to_date** | **datetime** | date until which the data has been fetched | 
**updated_at** | **datetime** | when last attempt update occurred | 
**show_consent_confirmation** | **bool** | whether any consent was given for this connection | 
**include_natures** | **list[str]** | the natures of the accounts that need to be fetched | 
**stages** | [**list[Stage]**](Stage.md) | information about [stages](#attempts-stages) through which the connection has passed | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

