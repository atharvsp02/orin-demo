# Self-hosting

Run the engine on your own VM.

## Requirements
- Python 3.10+
- Postgres 14+

## Environment

| var | purpose |
|-----|---------|
| `LLM_PROVIDER` | openai, deepseek, ... |
| `DATABASE_URL` | Postgres connection |

## Persistence
Graph and vector data persist in Postgres and the configured vector store.
