from langchain_openai import ChatOpenAI
from src.protein_researcher.configuration import Configuration



def get_llm():

    config = Configuration.load_from_env()

    return ChatOpenAI(
            model=config.LOCAL_LLM,
            api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_BASE_URL,
            temperature=0,
        )