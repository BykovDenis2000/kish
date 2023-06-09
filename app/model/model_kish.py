import numpy as np
#import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

np.random.seed(42)
#torch.manual_seed(42)
def predict_kish(text):
    tokenizer = GPT2Tokenizer.from_pretrained("model/models/essays")
    model = GPT2LMHeadModel.from_pretrained("model/models/essays")
    inpt = tokenizer.encode(text, return_tensors="pt")
    out = model.generate(inpt,
                     max_length=100,
                     repetition_penalty=6.0,
                     do_sample=True,
                     top_k=5,
                     top_p=0.95,
                     temperature=1,
                     no_repeat_ngram_size=2,
                     pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(out[0],skip_special_tokens=True)
