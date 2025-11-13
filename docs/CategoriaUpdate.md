# CategoriaUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nombre_categoria** | **str** |  | [optional] 
**descripcion_cat** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.categoria_update import CategoriaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriaUpdate from a JSON string
categoria_update_instance = CategoriaUpdate.from_json(json)
# print the JSON string representation of the object
print(CategoriaUpdate.to_json())

# convert the object into a dict
categoria_update_dict = categoria_update_instance.to_dict()
# create an instance of CategoriaUpdate from a dict
categoria_update_from_dict = CategoriaUpdate.from_dict(categoria_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


