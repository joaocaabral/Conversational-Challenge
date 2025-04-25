from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests

# Busca conteúdo relevante de uma página encontrada via DuckDuckGo

def buscar_conteudo_web(query: str) -> str:
    try:
        with DDGS() as ddgs:
            resultados = list(ddgs.text(query, region="br-pt", max_results=1))

        if not resultados:
            return "Não encontrei nada confiável agora."

        url = resultados[0]['href']
        html = requests.get(url, timeout=10).text
        soup = BeautifulSoup(html, 'html.parser')
        textos = soup.find_all(['p', 'li'])
        texto_extraido = "\n".join(t.get_text() for t in textos)

        return texto_extraido[:3000]  # Limita o conteúdo para não sobrecarregar o modelo

    except Exception as e:
        print("Erro ao buscar conteúdo web:", e)
        return "Não consegui carregar informações atualizadas no momento."