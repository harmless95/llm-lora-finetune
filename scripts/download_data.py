from llm_lora_finetune import config  # noqa: F401
from datasets import load_dataset

from llm_lora_finetune.data import split_dataset, format_split

print(f"HF cache: {config.settings.hf.home or '(дефолт)'}")

ds = load_dataset("b-mc2/sql-create-context")
ds["train"].to_parquet(str(config.ROOT_DIR / "data" / "raw" / "sql_create_context.parquet"))

splits = split_dataset(ds, seed=42, val_size=0.02, test_size=0.02)
for name, split in splits.items():
    formatted = format_split(split)
    formatted.to_parquet(str(config.ROOT_DIR / "data" / "processed" / f"{name}.parquet"))
    print(name, len(formatted))