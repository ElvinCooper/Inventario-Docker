# PaginateCategoria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categorias** | [**List[Categoria]**](Categoria.md) |  | [optional] 
**total** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**has_next** | **bool** |  | [optional] 
**has_prev** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.paginate_categoria import PaginateCategoria

# TODO update the JSON string below
json = "{}"
# create an instance of PaginateCategoria from a JSON string
paginate_categoria_instance = PaginateCategoria.from_json(json)
# print the JSON string representation of the object
print(PaginateCategoria.to_json())

# convert the object into a dict
paginate_categoria_dict = paginate_categoria_instance.to_dict()
# create an instance of PaginateCategoria from a dict
paginate_categoria_from_dict = PaginateCategoria.from_dict(paginate_categoria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


