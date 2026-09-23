SYSTEM_PROMPT = (
    "You are a SQL expert. Given a database schema and a question in natural "
    "language, write a single SQL query that answers the question. "
    "Respond with SQL only, no explanation."
)


def build_user_prompt(schema: str, question: str) -> str:
    return f"### Schema:\n{schema.strip()}\n\n### Question:\n{question.strip()}"


def build_chat_example(schema: str, question: str, sql: str | None = None) -> list[dict]:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": build_user_prompt(schema, question)},
    ]
    if sql is not None:
        messages.append({"role": "assistant", "content": sql.strip()})
    return messages

def split_dataset(dataset, seed: int = 42, val_size: float = 0.02, test_size: float = 0.02):
    train_test = dataset["train"].train_test_split(test_size=test_size, seed=seed)
    train_val = train_test["train"].train_test_split(test_size=val_size, seed=seed)
    return {
        "train": train_val["train"],
        "validation": train_val["test"],
        "test": train_test["test"],
    }

def format_split(split):
    return split.map(
        lambda row: {
            "messages": build_chat_example(
                schema=row["context"], question=row["question"], sql=row["answer"]
            )
        },
        remove_columns=split.column_names,
    )