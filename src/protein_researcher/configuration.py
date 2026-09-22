import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field

class Configuration(BaseModel):

    LLM_PROVIDER:str=Field(
        default="cstcloud",
    )
    LOCAL_LLM:str=Field(
        default="qwen3.5",
    )
    OPENAI_API_KEY:str=Field(
        default="",
    )
    OPENAI_BASE_URL:str=Field(
        default="https://uni-api.cstcloud.cn/v1",
    )

    @classmethod
    def load_from_env(cls):
        """手动加载 .env 文件，并实例化 BaseModel"""
        # 1. 加载当前目录或上级目录的 .env 文件到 os.environ
        load_dotenv()

        # 2. 从 os.environ 获取值，如果不存在则使用 None（这样会触发 Pydantic 的 Field default）
        # 如果你想强制使用系统的环境变量，可以把 get 的第二个参数留空
        return cls(
            LLM_PROVIDER=os.environ.get("LLM_PROVIDER", "cstcloud"),
            LOCAL_LLM=os.environ.get("LOCAL_LLM", "qwen3.5"),
            OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY", ""),
            OPENAI_BASE_URL=os.environ.get("OPENAI_BASE_URL", "https://cstcloud.cn"),
        )
