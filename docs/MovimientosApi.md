# openapi_client.MovimientosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_movimiento_id_movimiento_get**](MovimientosApi.md#api_v1_movimiento_id_movimiento_get) | **GET** /api/v1/movimiento/{id_movimiento} | Consultar los movimientos por su ID
[**api_v1_movimientos_get**](MovimientosApi.md#api_v1_movimientos_get) | **GET** /api/v1/movimientos | Consultar todos los movimientos en el sistema
[**api_v1_movimientos_id_usuario_get**](MovimientosApi.md#api_v1_movimientos_id_usuario_get) | **GET** /api/v1/movimientos/{id_usuario} | Consultar todos los movimientos de un usuario
[**api_v1_tipos_movimientos_tipo_movimiento_get**](MovimientosApi.md#api_v1_tipos_movimientos_tipo_movimiento_get) | **GET** /api/v1/tipos-movimientos/{tipo_movimiento} | Consultar los movimientos por su tipo


# **api_v1_movimiento_id_movimiento_get**
> Movimiento api_v1_movimiento_id_movimiento_get(id_movimiento)

Consultar los movimientos por su ID

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.movimiento import Movimiento
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
    api_instance = openapi_client.MovimientosApi(api_client)
    id_movimiento = 'id_movimiento_example' # str | 

    try:
        # Consultar los movimientos por su ID
        api_response = api_instance.api_v1_movimiento_id_movimiento_get(id_movimiento)
        print("The response of MovimientosApi->api_v1_movimiento_id_movimiento_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MovimientosApi->api_v1_movimiento_id_movimiento_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_movimiento** | **str**|  | 

### Return type

[**Movimiento**](Movimiento.md)

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

# **api_v1_movimientos_get**
> PaginateMovimiento api_v1_movimientos_get()

Consultar todos los movimientos en el sistema

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.paginate_movimiento import PaginateMovimiento
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
    api_instance = openapi_client.MovimientosApi(api_client)

    try:
        # Consultar todos los movimientos en el sistema
        api_response = api_instance.api_v1_movimientos_get()
        print("The response of MovimientosApi->api_v1_movimientos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MovimientosApi->api_v1_movimientos_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaginateMovimiento**](PaginateMovimiento.md)

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

# **api_v1_movimientos_id_usuario_get**
> PaginateMovimiento api_v1_movimientos_id_usuario_get(id_usuario)

Consultar todos los movimientos de un usuario

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.paginate_movimiento import PaginateMovimiento
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
    api_instance = openapi_client.MovimientosApi(api_client)
    id_usuario = 'id_usuario_example' # str | 

    try:
        # Consultar todos los movimientos de un usuario
        api_response = api_instance.api_v1_movimientos_id_usuario_get(id_usuario)
        print("The response of MovimientosApi->api_v1_movimientos_id_usuario_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MovimientosApi->api_v1_movimientos_id_usuario_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_usuario** | **str**|  | 

### Return type

[**PaginateMovimiento**](PaginateMovimiento.md)

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

# **api_v1_tipos_movimientos_tipo_movimiento_get**
> PaginateMovimiento api_v1_tipos_movimientos_tipo_movimiento_get(tipo_movimiento)

Consultar los movimientos por su tipo

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.paginate_movimiento import PaginateMovimiento
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
    api_instance = openapi_client.MovimientosApi(api_client)
    tipo_movimiento = 'tipo_movimiento_example' # str | 

    try:
        # Consultar los movimientos por su tipo
        api_response = api_instance.api_v1_tipos_movimientos_tipo_movimiento_get(tipo_movimiento)
        print("The response of MovimientosApi->api_v1_tipos_movimientos_tipo_movimiento_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MovimientosApi->api_v1_tipos_movimientos_tipo_movimiento_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tipo_movimiento** | **str**|  | 

### Return type

[**PaginateMovimiento**](PaginateMovimiento.md)

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

