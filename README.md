# 🤖 FURIOSO Bot - Desafio Conversacional FURIA

Este projeto é a entrega do **Desafio Técnico #1 - Experiência Conversacional** para a vaga de Assistente de Engenharia de Software na FURIA Tech.

O bot simula um torcedor fanático da FURIA, o **FURIOSO**, que interage com outros fãs no Telegram com informações atualizadas, resenha e paixão pelos times.

---

## 🎯 Objetivo

Criar um bot conversacional para torcedores da FURIA Esports, com foco no time de **CS2**, mas também cobrindo Valorant, R6, LoL, campanhas históricas e produtos.

---

## ✅ Funcionalidades

- Bot Telegram funcional com linguagem de torcida  
- Respostas com gírias, emoção e emojis  
- Consulta rápida a conhecimento fixo (lineups, títulos, técnicos)  
- Busca em tempo real com **Tavily API**  
- Geração de respostas via **OpenRouter API**  
- Fallbacks opinativos para perguntas subjetivas  
- Modular, escalável e fácil de manter  

---

## 📦 Estrutura de Pastas

```
Conversational-Challenge/
├── .env.example
├── requirements.txt
├── README.md
├── conhecimento/
│   └── base.json
├── prompt/
│   └── torcedor_prompt.txt
├── src/
│   ├── main.py
│   ├── agent.py
│   ├── conhecimento.py
│   ├── search_web.py
│   └── util.py
```

---

## 🚀 Como rodar

### 1. Clone o projeto

```bash
git clone https://github.com/seunome/furioso-bot.git
cd furioso-bot
```

### 2. Crie um arquivo `.env` com suas chaves

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo (ou use o `.env.example` como base):

```env
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxx
TELEGRAM_TOKEN=123456789:ABCDEF_seu_token_aqui
```

### 3. Instale as dependências

Se estiver usando ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Execute o bot

```bash
python src/main.py
```

Ao iniciar, o terminal mostrará:

```
🔥 Bot está rodando... Ctrl+C para parar.
```

Agora é só abrir o Telegram e conversar com o seu FURIOSO 🦍🔥

---

## 💬 Exemplos de perguntas

- "Qual a lineup de CS2?"
- "Quem é o técnico do Valorant?"
- "Quais títulos da FURIA no R6?"
- "Qual foi a melhor campanha da FURIA?"
- "Você prefere o FalleN ou o arT?"

---

## 🧠 Como funciona

- Se a pergunta for factual → responde da base (`base.json`)  
- Se for subjetiva → responde com frases opinativas no estilo FURIOSO  
- Se for informativa mas dinâmica → busca na web com Tavily e envia para o modelo  
- Todas as respostas passam pelo `estilo_furioso()` com gírias e emojis  

---

## 📽️ Demonstração

[⚠️ Link do vídeo aqui se gravado]

---

## 🔮 Melhorias futuras

- Adicionar memória longa (ex: com Redis ou MongoDB)  
- Integração com calendário de jogos em tempo real  
- Comando /partida ou /agenda com próximos confrontos  
- Versão web com interface animada  

---