import os
import json
import requests
from dotenv import load_dotenv
from pathlib import Path
from typing import Optional

from search_web import buscar_conteudo_web

# Carrega variáveis de ambiente
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3-8b-instruct")

# Carrega base local
BASE_PATH = Path(__file__).resolve().parent / "base.json"
try:
    with open(BASE_PATH, "r", encoding="utf-8") as f:
        base_data = json.load(f)
except Exception:
    base_data = {}

# Carrega prompts JSON
PROMPT_PATH = Path(__file__).resolve().parent / "prompts.json"
with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    PROMPTS = json.load(f)

# Aplica estilo FURIOSO sem prefixos artificiais
def estilo_furioso(resposta: str, tipo: str = "factual") -> str:
    return resposta.strip()

def chamar_openrouter(user_prompt: str, system_prompt: str) -> str:
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.7
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print("❌ Erro ao chamar OpenRouter:", e)
        print("📨 Resposta bruta:", response.text if 'response' in locals() else 'sem resposta')
        return ""

def classificar_pergunta(user_input: str) -> dict:
    user_prompt = f"PERGUNTA:\n{user_input}"
    resposta = chamar_openrouter(user_prompt, PROMPTS["classificador"])

    tipo = "precisa_web"
    modalidade = "geral"

    if "subjetiva" in resposta:
        tipo = "subjetiva"
    elif "factual" in resposta:
        tipo = "factual"

    for mod in ["cs2", "valorant", "lol", "r6"]:
        if mod in resposta:
            modalidade = mod
            break

    print(f"🔍 Tipo: {tipo} | Modalidade: {modalidade}")
    return {"tipo": tipo, "modalidade": modalidade}

def consultar_base_local(pergunta: str) -> Optional[str]:
    pergunta = pergunta.lower()
    for chave, valor in base_data.items():
        if isinstance(valor, str) and chave.lower() in pergunta:
            return valor
    return None

def interpretar_conteudo(pergunta: str, conteudo: str) -> str:
    user_prompt = f"""
--- PERGUNTA ---
{pergunta}

--- CONTEÚDO BRUTO DA WEB ---
{conteudo}
"""
    return chamar_openrouter(user_prompt, PROMPTS["interpretador_web"])

def furioso_responde(pergunta: str, resumo: str) -> str:
    user_prompt = PROMPTS["furioso_response"].format(pergunta=pergunta, resumo=resumo)
    return chamar_openrouter(user_prompt, PROMPTS["furioso_personagem"])

def ajustar_pergunta_para_busca(pergunta: str) -> str:
    pergunta = pergunta.lower().strip()

    if any(p in pergunta for p in ["valorant", "vava"]):
        modalidade = "Valorant"
    elif any(p in pergunta for p in ["lol", "league of legends"]):
        modalidade = "League of Legends"
    elif any(p in pergunta for p in ["r6", "rainbow"]):
        modalidade = "Rainbow Six"
    else:
        modalidade = "CS2"

    if any(p in pergunta for p in ["lineup", "escalação", "formação", "time", "jogadores"]):
        return f"lineup atual da FURIA no {modalidade}"

    if "contratou" in pergunta or "reforço" in pergunta:
        return f"último jogador contratado pela FURIA no {modalidade}"

    if "próximo jogo" in pergunta or "quando a furia joga" in pergunta:
        return f"data e adversário do próximo jogo da FURIA no {modalidade}"

    if "coach" in pergunta or "técnico" in pergunta:
        return f"técnico atual da FURIA no {modalidade}"

    return f"{pergunta} FURIA Esports"

def responder_mensagem(user_input: str, user_id: int) -> str:
    try:
        classificacao = classificar_pergunta(user_input)
        tipo = classificacao["tipo"]
        modalidade = classificacao["modalidade"]

        if tipo == "factual":
            resposta_base = consultar_base_local(user_input)
            if resposta_base:
                return estilo_furioso(resposta_base)
            tipo = "precisa_web"

        if tipo == "subjetiva":
            user_prompt = f"PERGUNTA DO FÃ:\n{user_input}"
            resposta = chamar_openrouter(user_prompt, PROMPTS["furioso_personagem"])
            return estilo_furioso(resposta, tipo="subjetiva")

        if tipo == "precisa_web":
            pergunta_otimizada = ajustar_pergunta_para_busca(user_input)
            conteudo_bruto = buscar_conteudo_web(pergunta_otimizada)

            if not conteudo_bruto or "não encontrei" in conteudo_bruto.lower():
                return "Não achei nada firmeza agora. Mas tô de olho nos portais! 👀"

            resumo = interpretar_conteudo(user_input, conteudo_bruto)
            resposta = furioso_responde(user_input, resumo)
            return resposta.strip()

        return "Buguei aqui... repete aí que eu juro que capto agora! 🌀"

    except Exception as e:
        print("❌ Erro no processamento geral:", e)
        return "⚠️ Algo bugou aqui, mas o FURIOSO não foge da luta! Já volto! 🔧"