# Categoria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_categoria** | **str** |  | [optional] [readonly] 
**nombre_categoria** | **str** |  | 
**descripcion_cat** | **str** |  | 
**fecha_creacion** | **datetime** |  | [optional] [readonly] 
**status** | **bool** |  | 

## Example

```python
from openapi_client.models.categoria import Categoria

# TODO update the JSON string below
json = "{}"
# create an instance of Categoria from a JSON string
categoria_instance = Categoria.from_json(json)
# print the JSON string representation of the object
print(Categoria.to_json())

# convert the object into a dict
categoria_dict = categoria_instance.to_dict()
# create an instance of Categoria from a dict
categoria_from_dict = Categoria.from_dict(categoria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


