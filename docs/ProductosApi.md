# openapi_client.ProductosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_productos_categoria_id_categoria_get**](ProductosApi.md#api_v1_productos_categoria_id_categoria_get) | **GET** /api/v1/productos/categoria/{id_categoria} | Consultar los productos por su categoria
[**api_v1_productos_create_post**](ProductosApi.md#api_v1_productos_create_post) | **POST** /api/v1/productos/create | Ingresar un nuevo producto en el sistema
[**api_v1_productos_delete_id_producto_delete**](ProductosApi.md#api_v1_productos_delete_id_producto_delete) | **DELETE** /api/v1/productos/delete/{id_producto} | Eliminar un producto por su ID
[**api_v1_productos_get**](ProductosApi.md#api_v1_productos_get) | **GET** /api/v1/productos | Consultar todos los productos en el sistema
[**api_v1_productos_id_producto_get**](ProductosApi.md#api_v1_productos_id_producto_get) | **GET** /api/v1/productos/{id_producto} | Consultar los productos por su ID
[**api_v1_productos_update_id_producto_put**](ProductosApi.md#api_v1_productos_update_id_producto_put) | **PUT** /api/v1/productos/update/{id_producto} | Actualizar un producto por su ID


# **api_v1_productos_categoria_id_categoria_get**
> PaginateProducto api_v1_productos_categoria_id_categoria_get(id_categoria)

Consultar los productos por su categoria

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.paginate_producto import PaginateProducto
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
    api_instance = openapi_client.ProductosApi(api_client)
    id_categoria = 'id_categoria_example' # str | 

    try:
        # Consultar los productos por su categoria
        api_response = api_instance.api_v1_productos_categoria_id_categoria_get(id_categoria)
        print("The response of ProductosApi->api_v1_productos_categoria_id_categoria_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductosApi->api_v1_productos_categoria_id_categoria_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_categoria** | **str**|  | 

### Return type

[**PaginateProducto**](PaginateProducto.md)

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

# **api_v1_productos_create_post**
> Producto api_v1_productos_create_post(producto)

Ingresar un nuevo producto en el sistema

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.producto import Producto
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
    api_instance = openapi_client.ProductosApi(api_client)
    producto = openapi_client.Producto() # Producto | 

    try:
        # Ingresar un nuevo producto en el sistema
        api_response = api_instance.api_v1_productos_create_post(producto)
        print("The response of ProductosApi->api_v1_productos_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductosApi->api_v1_productos_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **producto** | [**Producto**](Producto.md)|  | 

### Return type

[**Producto**](Producto.md)

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
**404** | Categoría no encontrada |  -  |
**400** | Solicitud inválida |  -  |
**201** | Created |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_productos_delete_id_producto_delete**
> Producto api_v1_productos_delete_id_producto_delete(id_producto)

Eliminar un producto por su ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.producto import Producto
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
    api_instance = openapi_client.ProductosApi(api_client)
    id_producto = 'id_producto_example' # str | 

    try:
        # Eliminar un producto por su ID
        api_response = api_instance.api_v1_productos_delete_id_producto_delete(id_producto)
        print("The response of ProductosApi->api_v1_productos_delete_id_producto_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductosApi->api_v1_productos_delete_id_producto_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_producto** | **str**|  | 

### Return type

[**Producto**](Producto.md)

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

# **api_v1_productos_get**
> PaginateProducto api_v1_productos_get()

Consultar todos los productos en el sistema

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.paginate_producto import PaginateProducto
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
    api_instance = openapi_client.ProductosApi(api_client)

    try:
        # Consultar todos los productos en el sistema
        api_response = api_instance.api_v1_productos_get()
        print("The response of ProductosApi->api_v1_productos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductosApi->api_v1_productos_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaginateProducto**](PaginateProducto.md)

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

# **api_v1_productos_id_producto_get**
> Producto api_v1_productos_id_producto_get(id_producto)

Consultar los productos por su ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.producto import Producto
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
    api_instance = openapi_client.ProductosApi(api_client)
    id_producto = 'id_producto_example' # str | 

    try:
        # Consultar los productos por su ID
        api_response = api_instance.api_v1_productos_id_producto_get(id_producto)
        print("The response of ProductosApi->api_v1_productos_id_producto_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductosApi->api_v1_productos_id_producto_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_producto** | **str**|  | 

### Return type

[**Producto**](Producto.md)

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

# **api_v1_productos_update_id_producto_put**
> Producto api_v1_productos_update_id_producto_put(id_producto, producto_update)

Actualizar un producto por su ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.producto import Producto
from openapi_client.models.producto_update import ProductoUpdate
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
    api_instance = openapi_client.ProductosApi(api_client)
    id_producto = 'id_producto_example' # str | 
    producto_update = openapi_client.ProductoUpdate() # ProductoUpdate | 

    try:
        # Actualizar un producto por su ID
        api_response = api_instance.api_v1_productos_update_id_producto_put(id_producto, producto_update)
        print("The response of ProductosApi->api_v1_productos_update_id_producto_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductosApi->api_v1_productos_update_id_producto_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_producto** | **str**|  | 
 **producto_update** | [**ProductoUpdate**](ProductoUpdate.md)|  | 

### Return type

[**Producto**](Producto.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**404** | Producto no encontrado |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

