import asyncio

from trimble.id import ClientCredentialTokenProvider, ValidatedClaimsetProvider, OpenIdKeySetProvider, OpenIdEndpointProvider

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