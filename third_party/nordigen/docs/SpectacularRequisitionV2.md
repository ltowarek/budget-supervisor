# SpectacularRequisitionV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created** | **datetime** | The date &amp; time at which the requisition was created. | 
**redirect** | **str** | redirect URL to your application after end-user authorization with ASPSP | 
**status** | [**AllOfSpectacularRequisitionV2Status**](AllOfSpectacularRequisitionV2Status.md) | status of this requisition | 
**institution_id** | **str** | an Institution ID for this Requisition | 
**agreement** | **str** | EUA associated with this requisition | [optional] 
**reference** | **str** | additional ID to identify the end user | [optional] 
**accounts** | [**list[Object]**](Object.md) | array of account IDs retrieved within a scope of this requisition | 
**user_language** | **str** | A two-letter country code (ISO 639-1) | [optional] 
**link** | **str** | link to initiate authorization with Institution | [default to 'https://ob.nordigen.com/psd2/start/3fa85f64-5717-4562-b3fc-2c963f66afa6/{$INSTITUTION_ID}']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

