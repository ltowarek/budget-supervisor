# Provider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the &#x60;id&#x60; of the provider | 
**code** | **str** | provider&#x27;s code | 
**name** | **str** | provider&#x27;s name | 
**mode** | **str** | possible values are:     - &#x60;oauth&#x60; -- access through the bank&#x27;s dedicated API (&#x60;regulated: true&#x60;). The user is redirected to the bank&#x27;s page for authorization. For more details, check [OAuth providers](#oauth_providers).    - &#x60;web&#x60; -- access through the bank&#x27;s WEB interface using screen scraping technology. Therefore, a user undergoes the same authorization flow as in their bank&#x27;s web interface with an identical set of credentials.    - &#x60;api&#x60; -- access through a dedicated (&#x60;regulated: true&#x60;) or non-dedicated (&#x60;regulated: false&#x60;) bank&#x27;s API. Some required credentials fields might be present which the user should complete (IBAN, username, etc.). In case of a dedicated API, an [interactive redirect](#connections-interactive) might be present, but there are required credentials fields which the user should complete (IBAN, username, etc.). Using these credentials, we authorize the user on the bank&#x27;s side.    - &#x60;file&#x60; -- access through uploading a file of certain format (XLS, CSV, etc.), which is processed to extract information of their accounts and transactions.   | 
**status** | **str** |  | 
**automatic_fetch** | **bool** | whether the provider&#x27;s connections can be automatically fetched | 
**customer_notified_on_sign_in** | **bool** | whether the provider will notify the customer on log in attempt | 
**interactive** | **bool** | whether the provider requires interactive input | 
**identification_mode** | **str** | whether the request to the provider is made with your [authorization headers](/general/#client_provider_keys) or with Salt Edge&#x27;s. | 
**instruction** | **str** | guidance on how to connect the bank | 
**home_url** | **str** | the URL of the main page of the provider | 
**login_url** | **str** | point of entrance to provider&#x27;s login web interface | 
**logo_url** | **str** | the URL for the provider logo, may have a placeholder for providers with missing logos | 
**country_code** | **str** | code of the provider&#x27;s country | 
**refresh_timeout** | **int** | amount of time (in minutes) after which the provider&#x27;s connections are allowed to be refreshed | 
**holder_info** | **list[str]** | contains information on the account holder details that can be fetched from this provider | 
**max_consent_days** | **int** | maximum allowed consent duration. If it is &#x60;null&#x60;, then there are no limits | 
**created_at** | **datetime** | time and date when the provider was integrated | 
**updated_at** | **datetime** | the last time when any of provider&#x27;s attributes were changed | 
**timezone** | **str** | time zone data of capital/major city in a region corresponding to the provider | 
**max_interactive_delay** | **int** | delay in seconds before &#x60;InteractiveAdapterTimeout&#x60; error will be raised | 
**optional_interactivity** | **bool** | provider which supports flipping of the &#x60;interactive&#x60; and &#x60;automatic_fetch&#x60; flags after connect | 
**regulated** | **bool** | whether the provider is integrated via a regulated channel under PSD2 | 
**max_fetch_interval** | **int** | Maximum period of days that a provider can return from its interface | 
**supported_fetch_scopes** | **list[str]** | array of strings with supported &#x60;fetch_scopes&#x60; | 
**supported_account_extra_fields** | **list[str]** | array of possible [account extra](#accounts-extra) fields to be fetched | 
**supported_transaction_extra_fields** | **list[str]** | array of possible [transaction extra](#transactions-extra) fields to be fetched | 
**supported_account_natures** | **list[str]** | array of possible [account natures](#accounts-attributes) to be fetched | 
**supported_account_types** | **list[str]** |  | 
**identification_codes** | **list[str]** | List of codes identifying supported branches of a specific provider. It may include BLZ(Germany), ABI+CAB(Italy), Branch Codes(France) etc. | 
**bic_codes** | **list[str]** | List of BIC codes identifying supported branches of a specific provider. | 
**supported_iframe_embedding** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

