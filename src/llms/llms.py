from langchain_openai import AzureChatOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from config import config

if config.azure_openai_api_key is None or config.azure_openai_api_key == "":
    if config.tenant_id is None or config.tenant_id == "":
        credentials = DefaultAzureCredential()
    else:
        credentials = DefaultAzureCredential(tenant_id=config.tenant_id)

    token_provider = get_bearer_token_provider(
        credentials, "https://cognitiveservices.azure.com/.default"
    )

    llm_4o = AzureChatOpenAI(
        azure_endpoint=config.azure_openai_endpoint,
        azure_deployment=config.azure_openai_deployment,
        api_version=config.azure_openai_version,
        azure_ad_token_provider=token_provider,
    )
else:
    llm_4o = AzureChatOpenAI(
        azure_endpoint=config.azure_openai_endpoint,
        azure_deployment=config.azure_openai_deployment,
        openai_api_key=config.azure_openai_api_key,
        api_version=config.azure_openai_version,
    )

__all__ = [llm_4o]
