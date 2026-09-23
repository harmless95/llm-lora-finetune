from __future__ import annotations

import os
from pathlib import Path

from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parents[2]


class HfConfig(BaseModel):
    home: Path | None = None
    token: SecretStr | None = None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        extra="ignore",
    )

    hf: HfConfig = HfConfig()


settings = Settings()

if settings.hf.home is not None:
    os.environ.setdefault("HF_HOME", str(settings.hf.home))
if settings.hf.token is not None:
    os.environ.setdefault("HF_TOKEN", settings.hf.token.get_secret_value())