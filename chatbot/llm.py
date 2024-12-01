import warnings
from langchain.llms import Ollama
Model = "llama2"
ollama = Ollama(base_url='http://localhost:11434',model=Model)
A = True
while A:
    B = input("enter your question?\n")
    if B=="bye":
        A = False
    else:
        print(ollama.invoke(B))
