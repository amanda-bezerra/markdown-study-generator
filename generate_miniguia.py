#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import json

@dataclass
class MiniGuia:
    tema: str
    fontes: list[str] = field(default_factory=list)
    objetivos: list[str] = field(default_factory=list)
    perguntas_estrategicas: list[str] = field(default_factory=list)
    prompts: dict[str, list[str]] = field(default_factory=dict)
    glossario: dict[str, str] = field(default_factory=dict)
    resumo_topicos: list[tuple[str, list[str]]] = field(default_factory=list)

    def to_markdown(self) -> str:
        hoje = datetime.now().strftime("%Y-%m-%d")
        md = []

        md.append(f"# MiniGuia de Estudo – {self.tema}\n")
        md.append(f"> Gerado em **{hoje}**\n")

        md.append("## 1) Fontes (3–5)\n")
        for i, f in enumerate(self.fontes, 1):
            md.append(f"{i}. {f}")
        md.append("")

        md.append("## 2) Objetivos de estudo\n")
        for o in self.objetivos:
            md.append(f"- {o}")
        md.append("")

        md.append("## 3) Perguntas estratégicas (para NotebookLM)\n")
        for p in self.perguntas_estrategicas:
            md.append(f"- {p}")
        md.append("")

        md.append("## 4) Prompts reutilizáveis (variações)\n")
        for categoria, itens in self.prompts.items():
            md.append(f"### {categoria}")
            for i, pr in enumerate(itens, 1):
                md.append(f"{i}. {pr}")
            md.append("")

        md.append("## 5) Resumo estruturado\n")
        for titulo, bullets in self.resumo_topicos:
            md.append(f"### {titulo}")
            for b in bullets:
                md.append(f"- {b}")
            md.append("")

        md.append("## 6) Glossário\n")
        for termo, definicao in self.glossario.items():
            md.append(f"- **{termo}**: {definicao}")
        md.append("")

        return "\n".join(md)

def parse_args():
    ap = argparse.ArgumentParser(description="Gera um MiniGuia de Estudo (Markdown).")
    ap.add_argument("--tema", required=True, help="Tema do miniguia.")
    ap.add_argument("--out", default="MINIGUIA.md", help="Arquivo de saída Markdown.")
    ap.add_argument("--config", help="Arquivo JSON opcional.")
    return ap.parse_args()

def load_config_json(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))

def main():
    args = parse_args()
    guia = MiniGuia(tema=args.tema)

    if args.config:
        cfg = load_config_json(args.config)
        guia.fontes = cfg.get("fontes", [])
        guia.objetivos = cfg.get("objetivos", [])
        guia.perguntas_estrategicas = cfg.get("perguntas_estrategicas", [])
        guia.prompts = cfg.get("prompts", {})
        guia.glossario = cfg.get("glossario", {})
        resumo = cfg.get("resumo_topicos", [])
        guia.resumo_topicos = [
            (item.get("titulo", "Tópico"), item.get("bullets", []))
            for item in resumo if isinstance(item, dict)
        ]

    md = guia.to_markdown()
    Path(args.out).write_text(md, encoding="utf-8")
    print(f"MiniGuia gerado em: {args.out}")

if __name__ == "__main__":
    main()
