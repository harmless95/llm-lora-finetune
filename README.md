# llm-lora-finetune

LoRA/QLoRA fine-tuning and evaluation of an open LLM on a domain task (text-to-SQL).

## Setup

```
uv sync --group dev --extra ml
cp .env.example .env   # при необходимости поправь HF__HOME под свой путь
```

## Data

Датасет: [`b-mc2/sql-create-context`](https://huggingface.co/datasets/b-mc2/sql-create-context) (question → SQL по схеме таблицы).

```
uv run python scripts/download_data.py
```

Скачивает сырые данные в `data/raw/`, режет на train/validation/test (seed=42, 2%/2%/96%) и сохраняет отформатированные под чат-промпт примеры в `data/processed/` (всё — вне git, см. `.gitignore`).
