# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the &#x60;id&#x60; of the account | 
**name** | **str** | the unique name of the account  &lt;strong&gt;Note:&lt;/strong&gt; The name directly identifies the account. In case the account’s name has changed (in the bank’s WEB/API interface, through code changes, etc.) a new account will be created.  | 
**nature** | **str** | the type of the account.  &lt;strong&gt;Note:&lt;/strong&gt; for &#x60;credit_card&#x60; nature, the balance represents the sum of all negative transactions, the positive ones do not count.  | 
**balance** | **float** | the account&#x27;s current balance | 
**currency_code** | **str** | \&quot;one of the possible values for [currency codes](#currencies). Maximum 3 letters.\&quot;  &lt;strong&gt;Note:&lt;/strong&gt; The currency directly identifies the account. In case the account’s currency code has changed (in the bank’s WEB/API interface, through code changes, etc.) a new account will be created.  | 
**extra** | [**AccountExtra**](AccountExtra.md) |  | 
**connection_id** | **str** | the &#x60;id&#x60; of the connection the account belongs to | 
**created_at** | **datetime** | time and date when the account was imported | 
**updated_at** | **datetime** | the last time when the account&#x27;s balance was changed or new transactions were imported | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

