## APIs

An API, or Application Programming Interface, is a set of rules that allows different software programs to communicate with each other.

A commonly known API may include APIs for LLM Chatbots (e.g. GPT5, Gemini, LLaMA4, etc.)
Others may include websites (e.g. Bilibili, YouTube, etc.)

These APIs enable both users and developers to use the tools available by these corporations.

As such, they are very important for project building, as it saves a lot of time and provides a level of abstraction.

You might explore more API usage in the future, but for now, we are considering a library called `transformer` in Python.

## Transformer

"Transformers acts as the model-definition framework for state-of-the-art machine learning models in text, computer vision, audio, video, and multimodal model, for both inference and training."

Think of it as a large tool bag that contains all the AI models for use, not just LLMs. 

It is developed and maintained by HuggingFace🤗 (HF). It is one of the most popular online community for AI. Like GitHub for coders, people post their models in HF.

As a result, you could assess both open sourced models or transformer models through the `transformer` library. Normally, you would not need to download the model, sending a call to HF via `transformer` would do.

To then get started, go to this example [python script](gpt2.py). Follow the links there.

After you have successfully managed to get a gpt2 output, you are free to explore more models!