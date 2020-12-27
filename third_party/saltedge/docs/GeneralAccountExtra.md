# GeneralAccountExtra

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | changeable name of the account | [optional] 
**account_number** | **str** | internal bank account number | [optional] 
**assets** | **list[str]** | array of crypto codes and their amounts assigned to investment account | [optional] 
**available_amount** | **float** | available amount in the account&#x27;s currency | [optional] 
**balance_type** | **str** | __Examples:__ &#x60;interimAvailable&#x60;, &#x60;closingBooked&#x60;, &#x60;interimBooked&#x60;, &#x60;authorised&#x60;, &#x60;expected&#x60;, &#x60;BOOKED&#x60;, &#x60;CLAV&#x60;, &#x60;CLBD&#x60;, &#x60;XPCD&#x60;, &#x60;OTHR&#x60;, etc.  __Note:__ The value is specific to the financial institution and can vary depending on the API standard, the bank&#x27;s implementation, the account&#x27;s type, country/region peculiarities, etc. This field holds an informative meaning. Usually, it is used to verify the balance consistency between customers of the same bank or between banks within the same country.  | [optional] 
**blocked_amount** | **float** | the amount currently blocked in account&#x27;s currency | [optional] 
**card_type** | **str** | type of the &#x60;card&#x60; account. | [optional] 
**cards** | **list[str]** | list of masked card numbers linked to the account | [optional] 
**client_name** | **str** | account client owner | [optional] 
**closing_balance** | **float** | account balance at the end of an accounting period | [optional] 
**credit_limit** | **float** | maximum amount of money that is allowed to be spent in account&#x27;s currency | [optional] 
**current_date** | **date** | date of provider statement generation (applicable to banks) | [optional] 
**current_time** | **datetime** | time of provider statement generation (applicable to banks) | [optional] 
**expiry_date** | **date** | card expiry date | [optional] 
**iban** | **str** | account&#x27;s IBAN | [optional] 
**interest_rate** | **float** | interest rate of the account as percentage value | [optional] 
**next_payment_amount** | **float** | next payment amount for loans or credits | [optional] 
**next_payment_date** | **date** | next payment date for loans or credits | [optional] 
**open_date** | **date** | the date when any type of account/card was opened | [optional] 
**opening_balance** | **float** | account balance that is brought forward from the end of one accounting period to the beginning of a new accounting period | [optional] 
**partial** | **bool** | account transactions were not imported or imported partially because of some internal error on the provider&#x27;s side | [optional] 
**sort_code** | **str** | routing number(US)/BSB code(Australia)/sort code(UK) | [optional] 
**statement_cut_date** | **date** | date when current statement becomes previous one | [optional] 
**status** | **str** | shows whether the account is &#x60;active&#x60; or &#x60;inactive&#x60; | [optional] 
**swift** | **str** | account SWIFT code | [optional] 
**total_payment_amount** | **float** | total payment amount for loans or credits | [optional] 
**transactions_count** | [**GeneralAccountExtraTransactionsCount**](GeneralAccountExtraTransactionsCount.md) |  | [optional] 
**payment_type** | **str** | account payment method | [optional] 
**cashback_amount** | **float** | accumulated CashBack / Cash Benefit | [optional] 
**monthly_total_payment** | **float** | the amount a borrower was paid for a month | [optional] 
**minimum_payment** | **float** | the lowest amount you can pay on your credit card to avoid penalties | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

