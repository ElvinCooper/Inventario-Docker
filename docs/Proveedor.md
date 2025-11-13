# Proveedor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_proveedor** | **str** |  | [optional] [readonly] 
**nombre_proveedor** | **str** |  | 
**contact** | **str** |  | 
**telefono** | **str** |  | 
**email** | **str** |  | 
**direccion** | **str** |  | 
**fecha_registro** | **datetime** |  | [optional] [readonly] 
**status** | **bool** |  | 

## Example

```python
from openapi_client.models.proveedor import Proveedor

# TODO update the JSON string below
json = "{}"
# create an instance of Proveedor from a JSON string
proveedor_instance = Proveedor.from_json(json)
# print the JSON string representation of the object
print(Proveedor.to_json())

# convert the object into a dict
proveedor_dict = proveedor_instance.to_dict()
# create an instance of Proveedor from a dict
proveedor_from_dict = Proveedor.from_dict(proveedor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


