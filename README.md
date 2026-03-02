📘 MiniGuia NotebookLM Generator

🚀 Gerador automatizado de MiniGuias de Estudo em Markdown utilizando Python.
Ideal para estruturar conteúdos e organizar estudos com apoio de IA (como NotebookLM).

🎯 Objetivo

Este projeto permite gerar um caderno estruturado contendo:

📚 Fontes de referência

🎯 Objetivos de estudo

❓ Perguntas estratégicas

🧠 Prompts reutilizáveis

📝 Resumo organizado

📖 Glossário de conceitos

Tudo em formato Markdown, pronto para usar no GitHub, Notion, Obsidian ou qualquer editor.

📂 Estrutura do Projeto
miniguia-notebooklm/
│
├── generate_miniguia.py   🐍 Script principal que gera o MiniGuia
├── config.json            ⚙️ Arquivo opcional para preencher automaticamente
├── MINIGUIA.md            📄 Arquivo gerado com o resultado final
├── README.md              📘 Documentação do projeto
└── requirements.txt       📦 Dependências (somente biblioteca padrão)
🔍 Descrição dos Arquivos
🐍 generate_miniguia.py

Script responsável por montar o MiniGuia em Markdown a partir do tema informado e do arquivo de configuração (opcional).

⚙️ config.json

Arquivo opcional onde você pode definir:

Fontes

Objetivos

Perguntas estratégicas

Prompts reutilizáveis

Resumo estruturado

Glossário

📄 MINIGUIA.md

Arquivo final gerado automaticamente pelo script.

📘 README.md

Documentação e instruções de uso.

📦 requirements.txt

Lista de dependências (não possui bibliotecas externas).

▶️ Como Executar
🔹 Gerar estrutura básica
python generate_miniguia.py --tema "Reserva de Emergência"
🔹 Gerar guia preenchido com config.json
python generate_miniguia.py --tema "Reserva de Emergência" --config config.json

Após executar, será criado automaticamente o arquivo:

MINIGUIA.md
💡 Aplicações

✔ Estudos acadêmicos
✔ Organização de conteúdo técnico
✔ Revisões para provas
✔ Estruturação de conhecimento financeiro
✔ Fluxo de aprendizado com IA

🧠 Tecnologias Utilizadas

Python 3

Dataclasses

Manipulação de arquivos

Geração dinâmica de Markdown

Estrutura orientada a objetos

🚀 Possíveis Melhorias Futuras

Interface Web

Integração com API de IA

Exportação para PDF

Geração automática de conteúdo

Interface gráfica

📄 Licença

Projeto open-source para fins educacionais e profissionais.
