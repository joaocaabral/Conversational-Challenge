import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from search_web import buscar_conteudo_web
from conhecimento import consultar_base
from util import estilo_furioso

# Carrega variáveis do .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Lê o prompt do personagem FURIOSO
prompt_path = Path(__file__).resolve().parent / "prompt" / "torcedor_prompt.txt"
with open(prompt_path, "r", encoding="utf-8") as f:
    prompt_furioso = f.read()

# Função principal do agente

def responder_mensagem(user_input: str) -> str:
    try:
        # Primeiro tenta responder com base no conhecimento interno
        resposta_local = consultar_base(user_input)
        if resposta_local:
            return estilo_furioso(resposta_local)

        # Se não encontrar, busca na web
        contexto_web = buscar_conteudo_web(user_input)

        # Monta o prompt completo
        pergunta_completa = f"""
Você é o FURIOSO, torcedor mais fanático da FURIA Esports. Responda como torcedor, com emoção e resenha, estilo informal.

=== CONTEXTO FIXO ===
{prompt_furioso}

=== DADO ATUAL DA WEB ===
{contexto_web}

=== PERGUNTA ===
{user_input}
"""

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "cognitive/completion",
            "messages": [
                {"role": "user", "content": pergunta_completa}
            ],
            "temperature": 0.7
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()

        resposta_gerada = response.json()['choices'][0]['message']['content'].strip()
        return estilo_furioso(resposta_gerada)

    except Exception as e:
        print("Erro:", e)
        return "⚠️ Buguei aqui, mas já volto pra zoar o rival! 🛠️"