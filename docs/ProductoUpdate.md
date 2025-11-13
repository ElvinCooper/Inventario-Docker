# ProductoUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nombre_producto** | **str** |  | [optional] 
**descripcion** | **str** |  | [optional] 
**precio** | **str** |  | [optional] 
**stock_minimo** | **int** |  | [optional] 
**stock_actual** | **int** |  | [optional] 
**imagen_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.producto_update import ProductoUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProductoUpdate from a JSON string
producto_update_instance = ProductoUpdate.from_json(json)
# print the JSON string representation of the object
print(ProductoUpdate.to_json())

# convert the object into a dict
producto_update_dict = producto_update_instance.to_dict()
# create an instance of ProductoUpdate from a dict
producto_update_from_dict = ProductoUpdate.from_dict(producto_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


