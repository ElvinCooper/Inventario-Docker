# PaginateProducto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**productos** | [**List[Producto]**](Producto.md) |  | [optional] 
**total** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**has_next** | **bool** |  | [optional] 
**has_prev** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.paginate_producto import PaginateProducto

# TODO update the JSON string below
json = "{}"
# create an instance of PaginateProducto from a JSON string
paginate_producto_instance = PaginateProducto.from_json(json)
# print the JSON string representation of the object
print(PaginateProducto.to_json())

# convert the object into a dict
paginate_producto_dict = paginate_producto_instance.to_dict()
# create an instance of PaginateProducto from a dict
paginate_producto_from_dict = PaginateProducto.from_dict(paginate_producto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


