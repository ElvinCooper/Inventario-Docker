# PaginateProveedor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proveedores** | [**List[Proveedor]**](Proveedor.md) |  | [optional] 
**total** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**has_next** | **bool** |  | [optional] 
**has_prev** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.paginate_proveedor import PaginateProveedor

# TODO update the JSON string below
json = "{}"
# create an instance of PaginateProveedor from a JSON string
paginate_proveedor_instance = PaginateProveedor.from_json(json)
# print the JSON string representation of the object
print(PaginateProveedor.to_json())

# convert the object into a dict
paginate_proveedor_dict = paginate_proveedor_instance.to_dict()
# create an instance of PaginateProveedor from a dict
paginate_proveedor_from_dict = PaginateProveedor.from_dict(paginate_proveedor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


