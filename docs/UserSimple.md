# UserSimple


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_usuario** | **str** |  | [optional] [readonly] 
**nombre** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**rol** | **str** |  | [optional] 
**fecha_registro** | **datetime** |  | [optional] 
**ultimo_acceso** | **datetime** |  | [optional] 
**movimientos** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_simple import UserSimple

# TODO update the JSON string below
json = "{}"
# create an instance of UserSimple from a JSON string
user_simple_instance = UserSimple.from_json(json)
# print the JSON string representation of the object
print(UserSimple.to_json())

# convert the object into a dict
user_simple_dict = user_simple_instance.to_dict()
# create an instance of UserSimple from a dict
user_simple_from_dict = UserSimple.from_dict(user_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


