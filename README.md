# trimble-id

Trimble Identity SDK for Python

## <a name="getting-started">Getting Started</a>

### Installation

You can install with `pip`:

```sh
pip install trimble-id
```

### Configure Trimble Identity

Create a new application in the [Trimble Developer Console](https://developer.console.trimble.com) portal and configure the following settings:

To register your application in Trimble Developer Console:

1. On the left pane select "Applications".

2. On the Applications home page, in the top right corner select + NEW APPLICATION. The Create Application page displays.

3. Select Continue to enter the applications details.

    | Field       | Description |
    | ----------- | ----------- |
    | Name        | Name of your application                    |
    | Description | Provide a description for the application.  |

4. Configure OAuth application grant types  `Client Credentials` in order to use this SDK.

5. Select "Create Application" to save changes.

Take note of the Client ID and URLs under the "Basic Information" section. You'll need these values to configure the SDK.

**Scopes**

Trimble Identity uses scopes to determine the aud claim in the returned access token. Scope is mandatory for the application to work. You can use the scope as the application name registered in the Trimble Developer Console. For example, if you have registered an application with the name "test", then it must be registered in the format {some_uuid}-"test". For eg., 12345678-1234-1234-1234-123456789012-test.

For more information, see [Authentication documentation](https://developer.trimble.com/docs/authentication).

## <a name="usage-reference">Usage Reference</a>

### Well-Known URL endpoint
The well-known URL endpoint is used to retrieve the authorization, token and user info endpoints for a given environment. The following endpoints are available for the staging and production environments:

<table>
    <tbody>
        <tr>
            <th>Endpoint</th>
            <td>https://id.trimble.com/.well-known/openid-configuration</td>
        </tr>
    </tbody>
</table>

## OpenID Endpoint Provider

This endpoint provider is used to retrieve the endpoints from a well-known URL endpoint.

### Usage
```python
from trimble.id.open_id_endpoint_provider import OpenIdEndpointProvider

endpoint_provider = OpenIdEndpointProvider("https://id.trimble.com/.well-known/openid-configuration")
auth_endpoint = await endpoint_provider.retrieve_authorization_endpoint()
token_endpoint = await endpoint_provider.retrieve_token_endpoint()
```

## Fixed Endpoint Provider

This endpoint provider is used to provide a fixed set of endpoints.

### Usage
```python
from trimble.id.fixed_endpoint_provider import FixedEndpointProvider

endpoint_provider = FixedEndpointProvider("https://authorization.url", "https://token.url", "https://userinfo.url")
endpoint = await endpoint_provider.retrieve_authorization_endpoint()
```

## Client Credential Token Provider

This token provider is used to retrieve an access token using the client credentials grant type.

### Usage
```python
from trimble.id.client_credential_token_provider import ClientCredentialTokenProvider

token_provider = ClientCredentialTokenProvider(endpoint_provider, "client_id", "client_secret").with_scopes(["scope"])

access_token = await token_provider.retrieve_token()
```

> **_NOTE:_** Refer samples for better understanding.

## Sample Code

See here for [Sample Code](https://github.com/trimble-oss/trimble-id-sdk-docs-for-python/blob/main/samples) for reference.

## Release notes

See here for [releases](https://github.com/trimble-oss/trimble-id-sdk-docs-for-python/blob/main/release-notes/CHANGELOG.md)

## Raise an issue

To provide feedback or report a bug, please [raise an issue on our issue tracker](https://github.com/trimble-oss/trimble-id-sdk-docs-for-python/issues).

## <a name="support">Support</a>

Send email to [support@trimble.com](mailto:support@trimble.com)