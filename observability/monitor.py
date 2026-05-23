import os
import json
from datetime import datetime

# Ensure observability directory exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OBS_DIR = os.path.join(BASE_DIR, 'observability')
os.makedirs(OBS_DIR, exist_ok=True)

PROMPT_LOG = os.path.join(OBS_DIR, 'prompt_logs.jsonl')
COST_LOG = os.path.join(OBS_DIR, 'cost_ledger.jsonl')

def _append_jsonl(file_path: str, data: dict):
    """Append a JSON line to the given file with a timestamp."""
    entry = {"timestamp": datetime.utcnow().isoformat() + 'Z', **data}
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry) + '\n')

def record_prompt(prompt: str, model: str, metadata: dict | None = None):
    """Record the prompt sent to an LLM.

    Args:
        prompt: The raw prompt string.
        model: Model identifier used.
        metadata: Optional additional information (e.g., temperature, system messages).
    """
    data = {"model": model, "prompt": prompt}
    if metadata:
        data["metadata"] = metadata
    _append_jsonl(PROMPT_LOG, data)

def record_cost(model: str, tokens: int, cost_usd: float, metadata: dict | None = None):
    """Record token usage and monetary cost for a model call.

    Args:
        model: Model identifier.
        tokens: Number of tokens consumed.
        cost_usd: Approximate cost in USD.
        metadata: Optional extra info.
    """
    data = {"model": model, "tokens": tokens, "cost_usd": cost_usd}
    if metadata:
        data["metadata"] = metadata
    _append_jsonl(COST_LOG, data)
