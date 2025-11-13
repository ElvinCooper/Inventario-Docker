# openapi_client.CategoriasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_categoria_create_post**](CategoriasApi.md#api_v1_categoria_create_post) | **POST** /api/v1/categoria/create | Ingresar una nueva categoria en el sistema
[**api_v1_categoria_delete_id_categoria_delete**](CategoriasApi.md#api_v1_categoria_delete_id_categoria_delete) | **DELETE** /api/v1/categoria/delete/{id_categoria} | Eliminar una categoria por su ID
[**api_v1_categoria_id_categoria_get**](CategoriasApi.md#api_v1_categoria_id_categoria_get) | **GET** /api/v1/categoria/{id_categoria} | Consultar las categoria por su ID
[**api_v1_categoria_update_id_categoria_put**](CategoriasApi.md#api_v1_categoria_update_id_categoria_put) | **PUT** /api/v1/categoria/update/{id_categoria} | Actualizar una categoria por su ID
[**api_v1_categorias_get**](CategoriasApi.md#api_v1_categorias_get) | **GET** /api/v1/categorias | Consultar todas las categorias


# **api_v1_categoria_create_post**
> Categoria api_v1_categoria_create_post(categoria)

Ingresar una nueva categoria en el sistema

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.categoria import Categoria
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CategoriasApi(api_client)
    categoria = openapi_client.Categoria() # Categoria | 

    try:
        # Ingresar una nueva categoria en el sistema
        api_response = api_instance.api_v1_categoria_create_post(categoria)
        print("The response of CategoriasApi->api_v1_categoria_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriasApi->api_v1_categoria_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categoria** | [**Categoria**](Categoria.md)|  | 

### Return type

[**Categoria**](Categoria.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**500** | Error interno del servidor |  -  |
**201** | Created |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_categoria_delete_id_categoria_delete**
> api_v1_categoria_delete_id_categoria_delete(id_categoria)

Eliminar una categoria por su ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CategoriasApi(api_client)
    id_categoria = 'id_categoria_example' # str | 

    try:
        # Eliminar una categoria por su ID
        api_instance.api_v1_categoria_delete_id_categoria_delete(id_categoria)
    except Exception as e:
        print("Exception when calling CategoriasApi->api_v1_categoria_delete_id_categoria_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_categoria** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_categoria_id_categoria_get**
> Categoria api_v1_categoria_id_categoria_get(id_categoria)

Consultar las categoria por su ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.categoria import Categoria
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CategoriasApi(api_client)
    id_categoria = 'id_categoria_example' # str | 

    try:
        # Consultar las categoria por su ID
        api_response = api_instance.api_v1_categoria_id_categoria_get(id_categoria)
        print("The response of CategoriasApi->api_v1_categoria_id_categoria_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriasApi->api_v1_categoria_id_categoria_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_categoria** | **str**|  | 

### Return type

[**Categoria**](Categoria.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_categoria_update_id_categoria_put**
> Categoria api_v1_categoria_update_id_categoria_put(id_categoria, categoria_update)

Actualizar una categoria por su ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.categoria import Categoria
from openapi_client.models.categoria_update import CategoriaUpdate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CategoriasApi(api_client)
    id_categoria = 'id_categoria_example' # str | 
    categoria_update = openapi_client.CategoriaUpdate() # CategoriaUpdate | 

    try:
        # Actualizar una categoria por su ID
        api_response = api_instance.api_v1_categoria_update_id_categoria_put(id_categoria, categoria_update)
        print("The response of CategoriasApi->api_v1_categoria_update_id_categoria_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriasApi->api_v1_categoria_update_id_categoria_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_categoria** | **str**|  | 
 **categoria_update** | [**CategoriaUpdate**](CategoriaUpdate.md)|  | 

### Return type

[**Categoria**](Categoria.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**404** | Categoria no encontrada |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_categorias_get**
> PaginateCategoria api_v1_categorias_get()

Consultar todas las categorias

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.paginate_categoria import PaginateCategoria
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CategoriasApi(api_client)

    try:
        # Consultar todas las categorias
        api_response = api_instance.api_v1_categorias_get()
        print("The response of CategoriasApi->api_v1_categorias_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriasApi->api_v1_categorias_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaginateCategoria**](PaginateCategoria.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

