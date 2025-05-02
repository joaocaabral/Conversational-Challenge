import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

# Carrega a chave da Tavily
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Carrega os links confiáveis a partir do base.json
BASE_PATH = Path(__file__).resolve().parent / "base.json"
try:
    with open(BASE_PATH, "r", encoding="utf-8") as f:
        base_data = json.load(f)
        fontes = base_data.get("fontes_confiaveis", {})
        urls_confiaveis = list(fontes.values())
        print("🔗 URLs confiáveis usadas:", urls_confiaveis)
except Exception as e:
    print("❌ Erro ao carregar base.json:", e)
    urls_confiaveis = []

def buscar_conteudo_web(pergunta: str) -> str:
    try:
        url = "https://api.tavily.com/search"
        headers = {"Content-Type": "application/json"}
        payload = {
            "api_key": TAVILY_API_KEY,
            "query": pergunta,
            "search_depth": "advanced",
            "include_answer": True,
            "include_raw_content": False,
            "include_images": False,
            "include_urls": urls_confiaveis,
            "max_results": 5
        }

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

        resposta = data.get("answer", "").strip()
        if resposta and len(resposta.split()) >= 10:
            print("✅ Tavily retornou resposta direta")
            return resposta

        print("⚠️ Tavily sem resposta direta. Buscando snippets...")
        for r in data.get("results", []):
            content = r.get("content", "")
            if "furia" in content.lower():
                print("✅ Usando snippet com menção à FURIA")
                return content.strip()

        print("⚠️ Nenhuma resposta confiável encontrada")
        return "Não encontrei nada confiável agora. Melhor conferir no site oficial da FURIA."

    except Exception as e:
        print("❌ Erro ao chamar Tavily:", e)
        return "A web hoje não colaborou... mas tô pronto pra próxima!"