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

## 🤝 Sobre

Este projeto foi desenvolvido por mim como parte de um desafio técnico para a FURIA Esports.

A proposta era criar uma experiência conversacional voltada para fãs da organização, com tom torcedor e linguagem natural.

### 🔧 Como o bot funciona por dentro

1. **Classificação da pergunta**  
   Cada mensagem recebida é analisada por um modelo de linguagem (via OpenRouter) para determinar:
   - Se é factual, subjetiva ou precisa buscar na web
   - Qual modalidade está sendo mencionada (CS2, Valorant, LoL, R6, geral)

2. **Respostas subjetivas**  
   Quando a pergunta é de opinião, o bot gera diretamente uma resposta como personagem, no estilo do torcedor “FURIOSO”, com tom apaixonado, informal e espontâneo.

3. **Respostas factuais**  
   Se a pergunta for objetiva e coberta pela base local (`base.json`), a resposta é recuperada de lá imediatamente.

4. **Busca na web (com precisão)**  
   Se a resposta precisa ser atualizada:
   - A pergunta é otimizada para ser mais específica (ex: “lineup atual da FURIA no CS2”)
   - É feita uma busca via Tavily, priorizando links definidos manualmente no `base.json` (como páginas da Liquipedia e da Ubisoft)
   - O conteúdo retornado é passado por uma segunda IA que organiza e interpreta os dados
   - Em seguida, uma terceira IA responde ao fã no estilo torcedor, com base nesse conteúdo

5. **Histórico e contexto**  
   O bot inicialmente usava contexto de conversas anteriores, mas após testes removi essa funcionalidade para evitar confusões. Agora ele interpreta cada pergunta de forma isolada, o que tornou as respostas mais precisas.

### 🧱 Estrutura modular e escalável

- Toda a lógica está separada em arquivos específicos (classificação, busca, resposta)
- Os prompts estão centralizados num único `prompts.json`, o que facilita ajustes e iteração
- As fontes confiáveis estão no `base.json`, permitindo atualizar os links sem mexer no código
- O deploy está configurado para rodar 24h/dia no Railway

---