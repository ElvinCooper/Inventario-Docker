# Movimiento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_movimiento** | **str** |  | [optional] [readonly] 
**id_productos** | **str** |  | 
**id_usuario** | **str** |  | 
**tipo_movimiento** | **str** |  | 
**cantidad** | **int** |  | 
**precio_unitario** | **float** |  | 
**motivo** | **str** |  | 
**referencia** | **str** |  | [optional] 
**fecha_movimiento** | **datetime** |  | [optional] [readonly] 
**observaciones** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.movimiento import Movimiento

# TODO update the JSON string below
json = "{}"
# create an instance of Movimiento from a JSON string
movimiento_instance = Movimiento.from_json(json)
# print the JSON string representation of the object
print(Movimiento.to_json())

# convert the object into a dict
movimiento_dict = movimiento_instance.to_dict()
# create an instance of Movimiento from a dict
movimiento_from_dict = Movimiento.from_dict(movimiento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


