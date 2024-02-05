import sys
from typing import Any, Annotated

from pydantic import Extra, Field, MongoDsn, PositiveInt, SecretStr, validator
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource

from pydantic.networks import UrlConstraints

from util.typing import LoggerLevel

MongoSRVDsn = Annotated[MultiHostUrl, UrlConstraints(allowed_schemes=['mongodb+srv'])]

class SettingsBase(BaseSettings):
    class Config:
        @classmethod
        def customize_sources(
            cls,
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
        ) -> tuple[PydanticBaseSettingsSource, ...]:
            return env_settings, init_settings, file_secret_settings

        extra = Extra.ignore
        frozen = True


class Tokens(SettingsBase):
    nira_bot: SecretStr = Field(min_length=1, env="BOT_TOKEN")


class Logging(SettingsBase):
    filepath: str = f"{sys.path[0]}/nira.log"
    format: str = "%(asctime)s$%(filename)s$%(lineno)d$%(funcName)s$%(levelname)s:%(message)s"
    level: int | LoggerLevel = "INFO"

    @validator("level", pre=True)
    def upper_level(cls, level: Any) -> Any:
        return level.upper() if isinstance(level, str) else level


class BotSettings(SettingsBase):
    # トークンとか (必須)
    tokens: Tokens

    # API キー
    translate: str | None = Field(default=None, min_length=1)
    voicevox: tuple[str, ...] = ()
    talk_api: str | None = Field(default=None, min_length=1)
    gcloud_api: str | None = Field(default=None, min_length=1)

    # データベース周り
    database_url: MongoSRVDsn
    database_name: str = Field(default="nira-bot", min_length=1)

    # Bot の起動に必要だがデフォルト値を提供できるもの
    prefix: str = "n!"
    shard_id: int = Field(default=0, ge=0)
    shard_count: PositiveInt = 1
    logging: Logging = Logging()

    # 上同だが任意のもの
    py_admin: tuple[int, ...] = ()
    guild_ids: tuple[int, ...] = ()

    # デバッグ用: Cog
    unload_cogs: tuple[str, ...] = ()
    load_cogs: tuple[str, ...] = ()

    # hoyo.py: HoYoverse 通行証のログインに使用するトークンと ID
    ltuid: int | None = None  # 見ようと思えば他人から見れる...はず
    ltoken: SecretStr | None = Field(default=None, min_length=1)  # 絶対アカン (private)
