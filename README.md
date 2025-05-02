# 🦁 FURIOSO Bot — o torcedor mais fanático da FURIA

Este é o FURIOSO, um bot que eu desenvolvi para responder torcedores da FURIA Esports no Telegram. Ele conversa como um verdadeiro torcedor: com paixão, informalidade e resenha  como se estivesse num grupo de WhatsApp da torcida. O objetivo foi criar uma experiência conversacional que mistura informação atualizada com o jeitão raiz da comunidade da FURIA.

👉 Teste aqui: [@Furios0Bot](https://t.me/Furios0Bot)

---

## ✨ O que o FURIOSO faz

- Responde perguntas sobre os times da FURIA (CS2, Valorant, LoL, R6)
- Consulta escalações, técnicos, reforços e histórico
- Traz informações atualizadas usando fontes como Liquipedia, Ubisoft, redes sociais oficiais
- Informa sobre próximos jogos com o comando `/agenda`
- Solta frases de resenha com `/resenha`
- Sugere perguntas com o comando `/menu`
- Classifica automaticamente se a pergunta é factual, subjetiva ou exige busca
- Fala como torcedor — sem parecer robô, sem se identificar como IA

---

## ⚙️ Tecnologias usadas

- Python 3.10+
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- Tavily API (busca na web)
- OpenRouter (modelo de linguagem via API)
- Railway (para manter o bot online gratuitamente)

---

## 📦 Como rodar localmente (Caso queira)

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Conversational-Challenge.git
cd Conversational-Challenge
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Rode o bot

```bash
python src/main.py
```

---

## 📁 Estrutura do projeto

```
src/
├── main.py              # Entrada do bot no Telegram
├── agent.py             # Inteligência do bot (classificação, busca, resposta)
├── context.py           # Histórico de mensagens por usuário
├── search_web.py        # Integração com Tavily
├── base.json            # Fontes confiáveis (urls específicas)
├── prompts.json         # Todos os prompts usados pela IA
requirements.txt
Procfile
.env
```

---

## 🧠 Como o FURIOSO pensa

O FURIOSO responde como um torcedor de verdade:
- Nunca se identifica como IA
- Só usa informações confirmadas
- Se for uma pergunta de opinião, ele inventa como qualquer torcedor faria
- Se não souber, assume que ainda não saiu notícia
- Usa emojis e expressões do dia a dia com moderação e estilo

Exemplo de resposta factual:
```
FalleN, YEKINDAR, molodoy, yuurih e KSCERATO. E o comandante é o guerri. Line pesada demais.
```

Exemplo de opinião:
```
O Fallen, sem dúvidas. É o professor, né? Representa tudo que a FURIA virou hoje.
```

---

## 🤝 Sobre

Este projeto foi desenvolvido como parte de um desafio técnico para a FURIA.  