from langchain.llms import Ollama
Model = "codellama"
ollama = Ollama(base_url='http://localhost:11434',model=Model)
B = input("enter your question?\n")
print("processing......")
print(ollama.invoke(B))
