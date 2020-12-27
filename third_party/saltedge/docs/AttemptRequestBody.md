# AttemptRequestBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fetch_scopes** | **list[str]** | fetching mode. Defaults to [consent](#consents-object) scopes. The allowed values for this parameter must comply to the [consent](#consents-object) &#x60;scopes&#x60; restriction.  | [optional] 
**from_date** | **date** | date from which you want to fetch data for your connection. Defaults to [consent](#consents-object) &#x60;from_date&#x60;. The allowed values for this parameter must be within exactly 365 days ago and it should comply to the fetching period restrictions in the [consent](#consents-object). | [optional] 
**to_date** | **date** | date until which you want to fetch data for your connection. Defaults to &#x60;null&#x60; (today). The allowed values for this parameter must be equal or more than &#x60;from_date&#x60; and less or equal than tomorrow. Also it should comply to the fetching period restrictions in the [consent](#consents-object). | [optional] 
**fetched_accounts_notify** | **bool** | whether Salt Edge should send a success callback after fetching accounts. | [optional] 
**custom_fields** | **object** | a JSON object, which will be sent back on any of your callbacks. | [optional] 
**locale** | **str** | the language of the Connect widget or/and provider error message in the &lt;a href&#x3D;&#x27;http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes&#x27; target&#x3D;\&quot;_blank\&quot;&gt;ISO 639-1&lt;/a&gt; format. Possible values are: &#x60;bg&#x60;, &#x60;cz&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es-MX&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;he&#x60;, &#x60;hu&#x60;, &#x60;it&#x60;, &#x60;nl&#x60;, &#x60;pl&#x60;, &#x60;pt-BR&#x60;, &#x60;pt&#x60;, &#x60;ro&#x60;, &#x60;ru&#x60;, &#x60;sk&#x60;, &#x60;tr&#x60;, &#x60;uk&#x60;, &#x60;zh-hk&#x60;(Traditional), &#x60;zh&#x60;(Simplified). Defaults to &#x60;en&#x60; | [optional] 
**include_natures** | **list[str]** | the natures of the accounts that need to be fetched. Check [accounts attributes](#accounts-attributes) for possible values. If &#x60;null&#x60;, all accounts will be fetched. | [optional] 
**customer_last_logged_at** | **datetime** | the datetime when user was last active in your application | [optional] 
**exclude_accounts** | **list[str]** | array of [account &#x60;ids&#x60;](#accounts-list) which will not be fetched. Applied to &#x60;reconnect&#x60; and &#x60;refresh&#x60; atempts. | [optional] 
**store_credentials** | **bool** | whether the credentials should be stored on Salt Edge side | 
**user_present** | **bool** | whether the request was initiated by the end-user of your application. It is taken into account only for PSD2-compliant providers and used for &#x60;reconnect&#x60; and &#x60;refresh&#x60;. | [optional] 
**return_to** | **str** | the URL the user will be redirected to, defaults to client&#x27;s home URL. If the provider has &#x60;api&#x60; mode and interactive &#x60;true&#x60; then this field is &#x60;mandatory&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

