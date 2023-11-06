import asyncio

from trimble.id.client_credential_token_provider import ClientCredentialTokenProvider
from trimble.id.validated_claimset_provider import ValidatedClaimsetProvider
from trimble.id.open_id_keyset_provider import OpenIdKeySetProvider
from trimble.id.open_id_endpoint_provider import OpenIdEndpointProvider

endpoint_provider = OpenIdEndpointProvider("<OPENID_CONFIGURATION_URL>")

# Create a token provider with the OpenID endpoint provider and client credentials
token_provider = ClientCredentialTokenProvider(endpoint_provider,"<CLIENT_ID>", "<CLIENT_SECRET>").with_scopes(["<SCOPE>"])

# Retrieve access token
async def get_access_token():
    return await token_provider.retrieve_token()

# Retrieve claimset
async def get_claimset(access_token):
    keyset_provider = OpenIdKeySetProvider(endpoint_provider)
    claimsetProvider = ValidatedClaimsetProvider(keyset_provider)
    return await claimsetProvider.retrieve_claimset(access_token)

async def main():
    access_token = await get_access_token()

    # Use the access token to retrieve the claimset
    claimset = await get_claimset(access_token)

asyncio.run(main())   