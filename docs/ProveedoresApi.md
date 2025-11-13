# openapi_client.ProveedoresApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_proveedor_create_post**](ProveedoresApi.md#api_v1_proveedor_create_post) | **POST** /api/v1/proveedor/create | Ingresar un nuevo proveedor en el sistema
[**api_v1_proveedor_delete_id_proveedor_delete**](ProveedoresApi.md#api_v1_proveedor_delete_id_proveedor_delete) | **DELETE** /api/v1/proveedor/delete/{id_proveedor} | Eliminar un proveedor por su ID
[**api_v1_proveedor_update_id_proveedor_put**](ProveedoresApi.md#api_v1_proveedor_update_id_proveedor_put) | **PUT** /api/v1/proveedor/update/{id_proveedor} | Actualizar un proveedor por su ID
[**api_v1_proveedores_get**](ProveedoresApi.md#api_v1_proveedores_get) | **GET** /api/v1/proveedores | Consultar todos los proveedores
[**api_v1_proveedores_id_proveedor_get**](ProveedoresApi.md#api_v1_proveedores_id_proveedor_get) | **GET** /api/v1/proveedores/{id_proveedor} | Consultar los proveedores por su id


# **api_v1_proveedor_create_post**
> Proveedor api_v1_proveedor_create_post(proveedor)

Ingresar un nuevo proveedor en el sistema

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.proveedor import Proveedor
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
    api_instance = openapi_client.ProveedoresApi(api_client)
    proveedor = openapi_client.Proveedor() # Proveedor | 

    try:
        # Ingresar un nuevo proveedor en el sistema
        api_response = api_instance.api_v1_proveedor_create_post(proveedor)
        print("The response of ProveedoresApi->api_v1_proveedor_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProveedoresApi->api_v1_proveedor_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proveedor** | [**Proveedor**](Proveedor.md)|  | 

### Return type

[**Proveedor**](Proveedor.md)

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

# **api_v1_proveedor_delete_id_proveedor_delete**
> api_v1_proveedor_delete_id_proveedor_delete(id_proveedor)

Eliminar un proveedor por su ID

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
    api_instance = openapi_client.ProveedoresApi(api_client)
    id_proveedor = 'id_proveedor_example' # str | 

    try:
        # Eliminar un proveedor por su ID
        api_instance.api_v1_proveedor_delete_id_proveedor_delete(id_proveedor)
    except Exception as e:
        print("Exception when calling ProveedoresApi->api_v1_proveedor_delete_id_proveedor_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_proveedor** | **str**|  | 

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

# **api_v1_proveedor_update_id_proveedor_put**
> Proveedor api_v1_proveedor_update_id_proveedor_put(id_proveedor, proveedor_update)

Actualizar un proveedor por su ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.proveedor import Proveedor
from openapi_client.models.proveedor_update import ProveedorUpdate
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
    api_instance = openapi_client.ProveedoresApi(api_client)
    id_proveedor = 'id_proveedor_example' # str | 
    proveedor_update = openapi_client.ProveedorUpdate() # ProveedorUpdate | 

    try:
        # Actualizar un proveedor por su ID
        api_response = api_instance.api_v1_proveedor_update_id_proveedor_put(id_proveedor, proveedor_update)
        print("The response of ProveedoresApi->api_v1_proveedor_update_id_proveedor_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProveedoresApi->api_v1_proveedor_update_id_proveedor_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_proveedor** | **str**|  | 
 **proveedor_update** | [**ProveedorUpdate**](ProveedorUpdate.md)|  | 

### Return type

[**Proveedor**](Proveedor.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**404** | Proveedor no encontrado |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_proveedores_get**
> PaginateProveedor api_v1_proveedores_get()

Consultar todos los proveedores

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.paginate_proveedor import PaginateProveedor
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
    api_instance = openapi_client.ProveedoresApi(api_client)

    try:
        # Consultar todos los proveedores
        api_response = api_instance.api_v1_proveedores_get()
        print("The response of ProveedoresApi->api_v1_proveedores_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProveedoresApi->api_v1_proveedores_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaginateProveedor**](PaginateProveedor.md)

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

# **api_v1_proveedores_id_proveedor_get**
> Proveedor api_v1_proveedores_id_proveedor_get(id_proveedor)

Consultar los proveedores por su id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.proveedor import Proveedor
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
    api_instance = openapi_client.ProveedoresApi(api_client)
    id_proveedor = 'id_proveedor_example' # str | 

    try:
        # Consultar los proveedores por su id
        api_response = api_instance.api_v1_proveedores_id_proveedor_get(id_proveedor)
        print("The response of ProveedoresApi->api_v1_proveedores_id_proveedor_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProveedoresApi->api_v1_proveedores_id_proveedor_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_proveedor** | **str**|  | 

### Return type

[**Proveedor**](Proveedor.md)

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

