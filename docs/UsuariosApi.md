# openapi_client.UsuariosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_auth_login_post**](UsuariosApi.md#api_v1_auth_login_post) | **POST** /api/v1/auth/login | Login de usuarios
[**api_v1_auth_logout_post**](UsuariosApi.md#api_v1_auth_logout_post) | **POST** /api/v1/auth/logout | Logout usuarios
[**api_v1_auth_refresh_post**](UsuariosApi.md#api_v1_auth_refresh_post) | **POST** /api/v1/auth/refresh | Renovar los tokens
[**api_v1_usuario_id_usuario_get**](UsuariosApi.md#api_v1_usuario_id_usuario_get) | **GET** /api/v1/usuario/{id_usuario} | Consultar un usuario por su Id
[**api_v1_usuarios_get**](UsuariosApi.md#api_v1_usuarios_get) | **GET** /api/v1/usuarios | Consultar todos los usuarios del sistema


# **api_v1_auth_login_post**
> LoginResponse api_v1_auth_login_post(login)

Login de usuarios

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.login import Login
from openapi_client.models.login_response import LoginResponse
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
    api_instance = openapi_client.UsuariosApi(api_client)
    login = openapi_client.Login() # Login | 

    try:
        # Login de usuarios
        api_response = api_instance.api_v1_auth_login_post(login)
        print("The response of UsuariosApi->api_v1_auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsuariosApi->api_v1_auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | [**Login**](Login.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**500** | Error al generar token |  -  |
**401** | No esta autorizado |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_auth_logout_post**
> LogoutResponse api_v1_auth_logout_post()

Logout usuarios

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.logout_response import LogoutResponse
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
    api_instance = openapi_client.UsuariosApi(api_client)

    try:
        # Logout usuarios
        api_response = api_instance.api_v1_auth_logout_post()
        print("The response of UsuariosApi->api_v1_auth_logout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsuariosApi->api_v1_auth_logout_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LogoutResponse**](LogoutResponse.md)

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

# **api_v1_auth_refresh_post**
> TokenRefreshResponse api_v1_auth_refresh_post()

Renovar los tokens

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.token_refresh_response import TokenRefreshResponse
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
    api_instance = openapi_client.UsuariosApi(api_client)

    try:
        # Renovar los tokens
        api_response = api_instance.api_v1_auth_refresh_post()
        print("The response of UsuariosApi->api_v1_auth_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsuariosApi->api_v1_auth_refresh_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokenRefreshResponse**](TokenRefreshResponse.md)

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

# **api_v1_usuario_id_usuario_get**
> UserSimple api_v1_usuario_id_usuario_get(id_usuario)

Consultar un usuario por su Id

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.user_simple import UserSimple
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
    api_instance = openapi_client.UsuariosApi(api_client)
    id_usuario = 'id_usuario_example' # str | 

    try:
        # Consultar un usuario por su Id
        api_response = api_instance.api_v1_usuario_id_usuario_get(id_usuario)
        print("The response of UsuariosApi->api_v1_usuario_id_usuario_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsuariosApi->api_v1_usuario_id_usuario_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_usuario** | **str**|  | 

### Return type

[**UserSimple**](UserSimple.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Error interno del servidor |  -  |
**404** | Usuario no encontrado |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_usuarios_get**
> List[UserSimple] api_v1_usuarios_get()

Consultar todos los usuarios del sistema

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.user_simple import UserSimple
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
    api_instance = openapi_client.UsuariosApi(api_client)

    try:
        # Consultar todos los usuarios del sistema
        api_response = api_instance.api_v1_usuarios_get()
        print("The response of UsuariosApi->api_v1_usuarios_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsuariosApi->api_v1_usuarios_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserSimple]**](UserSimple.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Error interno del servidor |  -  |
**401** | No autorizado |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

