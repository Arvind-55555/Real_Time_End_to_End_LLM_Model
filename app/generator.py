from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from .config import settings

_tokenizer = None
_model = None

def load_generator():
    global _tokenizer, _model
    if _tokenizer is None:
        _tokenizer = AutoTokenizer.from_pretrained(settings.GEN_MODEL)
        _model = AutoModelForCausalLM.from_pretrained(settings.GEN_MODEL).to(settings.DEVICE)
    return _tokenizer, _model

def generate_answer(prompt, max_new_tokens=None, temperature=0.7, top_p=0.9):
    tok, model = load_generator()
    max_new_tokens = max_new_tokens or settings.MAX_GEN_TOKENS
    inputs = tok(prompt, return_tensors="pt", truncation=True).to(settings.DEVICE)
    out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=True, temperature=temperature, top_p=top_p)
    return tok.decode(out[0], skip_special_tokens=True)
