# ProveedorUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nombre_proveedor** | **str** |  | [optional] 
**contact** | **str** |  | [optional] 
**telefono** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**direccion** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.proveedor_update import ProveedorUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProveedorUpdate from a JSON string
proveedor_update_instance = ProveedorUpdate.from_json(json)
# print the JSON string representation of the object
print(ProveedorUpdate.to_json())

# convert the object into a dict
proveedor_update_dict = proveedor_update_instance.to_dict()
# create an instance of ProveedorUpdate from a dict
proveedor_update_from_dict = ProveedorUpdate.from_dict(proveedor_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


