import json
from pathlib import Path

# Caminho para o arquivo de conhecimento
base_path = Path(__file__).resolve().parent.parent / "conhecimento" / "base.json"

# Carrega a base de conhecimento
with open(base_path, "r", encoding="utf-8") as f:
    base = json.load(f)

# Dicionário de sinônimos para cada tipo de dado
aliases = {
    "lineup": ["line", "lineup", "escalação", "time", "jogadores", "elenco"],
    "coach": ["coach", "técnico", "treinador"],
    "titulos": ["títulos", "conquistas", "troféus"],
    "campeonatos_disputados": ["campeonatos", "torneios", "disputas", "participações"]
}

def match_alias(key, pergunta):
    if key not in aliases:
        return False
    return any(alias in pergunta for alias in aliases[key])

def consultar_base(pergunta: str) -> str:
    pergunta = pergunta.lower()

    # Match direto com chaves simples
    for chave, valor in base.items():
        if isinstance(valor, str):
            if chave.replace("_", " ") in pergunta:
                return valor

    # Verifica listas ou dicionários com base em alias e categoria
    for chave, grupo in base.items():
        if isinstance(grupo, dict):
            if match_alias(chave, pergunta):
                for modalidade, itens in grupo.items():
                    if modalidade in pergunta:
                        resposta = f"{chave.replace('_', ' ').capitalize()} ({modalidade}):\n- " + "\n- ".join(itens)
                        return resposta

    # Lineups e coaches como entrada especial
    for chave, valor in base.items():
        if isinstance(valor, str):
            for tipo in ["lineup", "coach"]:
                if chave.startswith(tipo):
                    modalidade = chave.replace(f"{tipo}_", "")
                    if match_alias(tipo, pergunta) and modalidade in pergunta:
                        return valor

    return ""