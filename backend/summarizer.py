# summarizer.py

from transformers.pipelines import pipeline
from transformers import AutoTokenizer
import torch

MODEL_NAME = "facebook/bart-large-cnn"

# Load summarization pipeline and tokenizer with GPU if available
summarizer = pipeline(
    "summarization",
    model=MODEL_NAME,
    device=0 if torch.cuda.is_available() else -1
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

MAX_INPUT_TOKENS = 1024  # BART max input length

def truncate_to_max_tokens(text, tokenizer, max_tokens=MAX_INPUT_TOKENS):
    tokens = tokenizer.encode(text, truncation=True, max_length=max_tokens)
    return tokenizer.decode(tokens, skip_special_tokens=True)

def summarize_document(text):
    text = truncate_to_max_tokens(text, tokenizer)
    # TL;DR (short summary)
    tldr = summarizer(text, max_length=30, min_length=10, do_sample=False)[0]['summary_text']
    # 100-word summary (approximate with max_length)
    summary = summarizer(text, max_length=130, min_length=80, do_sample=False)[0]['summary_text']
    # Bullet checklist (shorter summary, split into lines)
    checklist_text = summarizer(text, max_length=60, min_length=20, do_sample=False)[0]['summary_text']
    checklist = [line.strip('-• ') for line in checklist_text.split('\n') if line.strip()]
    return {
        'tldr': tldr,
        'simple_summary': summary,
        'checklist': checklist
    } 