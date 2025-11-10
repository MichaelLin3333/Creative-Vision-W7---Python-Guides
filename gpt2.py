# Install necessary libraries
# You can uncomment this line if transformers isn't installed
# !pip install transformers torch

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # You can also use "gpt2-medium", "gpt2-large", etc.
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Due to internet issue, you might not be able to use gpt2 via an API call
# If so, download gpt2 from here https://huggingface.co/openai-community/gpt2
# and use the following code
"""
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_path = ".gpt2_local"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)
"""

# Prepare input prompt
prompt = "Once upon a time in a futuristic world,"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generate text
output = model.generate(
    input_ids,
    max_length=100,       # maximum length of generated text
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    temperature=0.7,
    top_p=0.9,
    top_k=50
)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
