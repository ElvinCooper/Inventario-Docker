# PaginateMovimiento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movimientos** | [**List[Movimiento]**](Movimiento.md) |  | [optional] 
**total** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**has_next** | **bool** |  | [optional] 
**has_prev** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.paginate_movimiento import PaginateMovimiento

# TODO update the JSON string below
json = "{}"
# create an instance of PaginateMovimiento from a JSON string
paginate_movimiento_instance = PaginateMovimiento.from_json(json)
# print the JSON string representation of the object
print(PaginateMovimiento.to_json())

# convert the object into a dict
paginate_movimiento_dict = paginate_movimiento_instance.to_dict()
# create an instance of PaginateMovimiento from a dict
paginate_movimiento_from_dict = PaginateMovimiento.from_dict(paginate_movimiento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


