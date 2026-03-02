🎯 Objetivos de estudo

❓ Perguntas estratégicas

🧠 Prompts reutilizáveis

📝 Resumo organizado

📖 Glossário de conceitos

Tudo em formato Markdown, pronto para usar no GitHub, Notion, Obsidian ou qualquer editor.

📂 Estrutura da Pasta
miniguia-notebooklm/
│
├── generate_miniguia.py   🐍 Script principal que gera o MiniGuia
├── config.json            ⚙️ Arquivo opcional para preencher automaticamente o guia
├── MINIGUIA.md            📄 Arquivo gerado com o resultado final
├── README.md              📘 Documentação do projeto
└── requirements.txt       📦 Dependências (usa apenas biblioteca padrão)
🔍 O que é cada arquivo?

🐍 generate_miniguia.py
Script responsável por montar o MiniGuia em Markdown a partir do tema e das configurações.

⚙️ config.json
Arquivo opcional onde você define:

Fontes

Objetivos

Perguntas

Prompts

Resumo estruturado

Glossário

📄 MINIGUIA.md
Arquivo final gerado automaticamente pelo script.

📘 README.md
Documento explicando o funcionamento do projeto.

📦 requirements.txt
Lista de dependências (neste caso, nenhuma externa).

▶️ Como Executar
🔹 Gerar estrutura básica:
python generate_miniguia.py --tema "Reserva de Emergência"
🔹 Gerar guia preenchido com config.json:
python generate_miniguia.py --tema "Reserva de Emergência" --config config.json
💡 Aplicações

✔ Estudos acadêmicos
✔ Organização de conteúdo técnico
✔ Revisões para provas
✔ Estruturação de conhecimento financeiro
✔ Fluxo de aprendizado com IA

🧠 Tecnologias Utilizadas

Python 3

Dataclasses

Geração dinâmica de Markdown

Estruturação orientada a objetos
