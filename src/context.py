from collections import defaultdict, deque

# Armazena últimas mensagens por usuário (por padrão, 3)
historico_usuarios = defaultdict(lambda: deque(maxlen=3))

def registrar_mensagem(user_id: int, mensagem: str):
    """
    Adiciona uma nova mensagem ao histórico do usuário.
    """
    historico_usuarios[user_id].append(mensagem)

def obter_contexto(user_id: int) -> list[str]:
    """
    Retorna a lista das últimas mensagens do usuário.
    """
    return list(historico_usuarios[user_id])