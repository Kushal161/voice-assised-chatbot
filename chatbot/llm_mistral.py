from langchain.llms import Ollama
from STT import text
ollama = Ollama(base_url='http://localhost:11434',model='llama2')

B = ollama.invoke(text)
print(B)