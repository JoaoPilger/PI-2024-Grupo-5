from dotenv import load_dotenv # puxar api do arquivo oculto
import os # executar comandos 
import google.generativeai as genai
import json

# aplica a API_KEY para buscar com a IA
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-002")



with open('./flask/sistema/documentos.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

with open('./flask/sistema/data.json', 'r', encoding='utf-8') as formulario:
    form = formulario.read()

prompt = f"Dê uma ideia de um breve treino depois de ler o seguinte conteúdo: {conteudo}\n\nE tenha em mente as seguintes informações do usuário fictício, lembre-se também que ele possui atestado médico para poder realizar exercícios: {form}. Trate o usuário como se estivesse falando diretamente com ele."
print("Carregando... Isso pode levar alguns segundos.")
response = model.generate_content(prompt)
resultado = response.text


# Dicionário que vai virar o dados.json
treino = {
    "treino": resultado
}

path = os.path.join(os.getcwd(), 'flask', 'sistema', 'respostaIA.json')

# Cria o dados.json com a resposta da IA
with open(path, 'w', encoding='utf-8') as arquivo:
    json.dump(treino, arquivo, indent=4, ensure_ascii=False)