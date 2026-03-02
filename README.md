# 📘 MiniGuia NotebookLM Generator

🚀 Gerador automatizado de **MiniGuias de Estudo em Markdown** utilizando Python.  
Ideal para estruturar conteúdos e organizar estudos com apoio de IA (como NotebookLM).

---

## 🎯 Objetivo

Este projeto permite gerar um caderno estruturado contendo:

- 📚 Fontes de referência  
- 🎯 Objetivos de estudo  
- ❓ Perguntas estratégicas  
- 🧠 Prompts reutilizáveis  
- 📝 Resumo organizado  
- 📖 Glossário de conceitos  

Tudo em formato **Markdown**, pronto para usar no GitHub, Notion, Obsidian ou qualquer editor.

---

## 📂 Estrutura do Projeto

miniguia-notebooklm/
│
├── generate_miniguia.py 🐍 Script principal que gera o MiniGuia
├── config.json ⚙️ Arquivo opcional para preencher automaticamente
├── MINIGUIA.md 📄 Arquivo gerado com o resultado final
├── README.md 📘 Documentação do projeto
└── requirements.txt 📦 Dependências (somente biblioteca padrão)


---

## 🔍 Descrição dos Arquivos

### 🐍 generate_miniguia.py  
Script responsável por montar o MiniGuia em Markdown a partir do tema informado e do arquivo de configuração (opcional).

### ⚙️ config.json  
Arquivo opcional onde você pode definir:

- Fontes
- Objetivos
- Perguntas estratégicas
- Prompts reutilizáveis
- Resumo estruturado
- Glossário

### 📄 MINIGUIA.md  
Arquivo final gerado automaticamente pelo script.

### 📘 README.md  
Documentação e instruções de uso.

### 📦 requirements.txt  
Lista de dependências (não possui bibliotecas externas).

---

## ▶️ Como Executar

### 🔹 Gerar estrutura básica

```bash
python generate_miniguia.py --tema "Reserva de Emergência"
