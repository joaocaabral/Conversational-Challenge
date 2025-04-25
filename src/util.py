import random

def estilo_furioso(resposta: str) -> str:
    prefixos = [
        "Mano, ó:",
        "Torcedor, se liga:",
        "Fechou então:",
        "Tá ligado?",
        "Seguinte:",
        "Cê vai curtir isso:",
        "Resenha de qualidade, olha só:"  
    ]

    emojis = ["🔥", "🦍", "🖤", "⚡", "🏆", "🎯", "💥"]

    prefixo = random.choice(prefixos)
    emoji_final = random.choice(emojis)

    return f"{prefixo} {resposta.strip()} {emoji_final}"