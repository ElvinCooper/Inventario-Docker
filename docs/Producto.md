# Producto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_producto** | **str** |  | [optional] [readonly] 
**nombre_producto** | **str** |  | 
**descripcion** | **str** |  | 
**codigo_barras** | **str** |  | 
**precio** | **float** |  | 
**stock_minimo** | **int** |  | 
**stock_actual** | **int** |  | 
**id_categoria** | **str** |  | 
**imagen_url** | **str** |  | [optional] 
**fecha_creacion** | **datetime** |  | [optional] [readonly] 
**fecha_actualizacion** | **datetime** |  | [optional] [readonly] 
**status** | **bool** |  | 

## Example

```python
from openapi_client.models.producto import Producto

# TODO update the JSON string below
json = "{}"
# create an instance of Producto from a JSON string
producto_instance = Producto.from_json(json)
# print the JSON string representation of the object
print(Producto.to_json())

# convert the object into a dict
producto_dict = producto_instance.to_dict()
# create an instance of Producto from a dict
producto_from_dict = Producto.from_dict(producto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


