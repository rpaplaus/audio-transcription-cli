# Audio Transcription & AI Analysis CLI

## Visão Geral

Este projeto é uma **ferramenta CLI modular** para ingestão, transcrição e análise semântica de áudios usando **Python + IA (LLMs)**.

Ele foi projetado como um **pipeline de produção**, não como um script isolado:
- suporta múltiplos arquivos em lote
- mantém organização por dataset
- gera saídas reutilizáveis (texto, resumos, insights)

O foco é **clareza, automação e entrega prática**.

---

## Por que esse projeto existe

Grande parte do conteúdo de valor (reuniões, entrevistas, podcasts, aulas) ainda nasce em áudio.
Este projeto transforma áudio bruto em:
- texto estruturado
- resumos executivos
- tópicos principais
- insights acionáveis

Tudo isso de forma reproduzível e escalável.

---

## Arquitetura do Pipeline

O pipeline é dividido em três fases independentes:

### 1. Ingest
Responsável por:
- receber um ou mais arquivos de áudio
- organizar cada áudio em sua própria pasta de projeto

### 2. Transcribe
Responsável por:
- transcrever os áudios usando um modelo de speech-to-text
- salvar o texto como `transcript.txt` dentro da pasta do áudio

### 3. Analyze
Responsável por:
- percorrer todas as pastas geradas
- analisar cada `transcript.txt`
- gerar resumos e insights usando um LLM

Cada fase pode ser executada separadamente ou em sequência.

---

## Estrutura de Pastas

```
project/
├── ingest.py
├── transcribe.py
├── analyze.py
├── README.md
├── .env
├── .gitignore
├── input/
│   └── meeting.wav
└── output/
    └── meeting/
        ├── meeting.wav
        ├── transcript.txt
        └── summary.md
```

Cada áudio gera um **dataset fechado**, facilitando revisão, versionamento e reaproveitamento.

---

## Tecnologias Utilizadas

- Python 3.12
- OpenAI API (LLMs)
- Speech-to-Text (Whisper / equivalente)
- `pathlib`, `dotenv`

Projeto pensado para rodar inicialmente em **Windows** e posteriormente em **macOS**.

---

## Execução Básica

1. Criar ambiente virtual
```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instalar dependências
```bash
pip install -r requirements.txt
```

3. Configurar `.env`
```
OPENAI_API_KEY=your_key_here
```

4. Rodar pipeline
```bash
python ingest.py input/*.wav
python transcribe.py
python analyze.py
```

---

## Exemplo de Uso

Após a execução:
- cada áudio terá sua própria pasta
- cada pasta conterá:
  - o áudio original
  - a transcrição
  - o resumo gerado por IA

Isso permite análise individual ou em lote.

---

## Status do Projeto

✔ Pipeline funcional
✔ Suporte a múltiplos arquivos
✔ Organização por dataset
✔ Análise automatizada com IA

Próximos passos planejados:
- flags CLI (`--only`, `--force`)
- saída estruturada em JSON
- geração de HTML para visualização

---

## Sobre o Autor

Projeto desenvolvido por **Rodrigo Paplauskas**.

Creative Technologist com mais de 30 anos de experiência em sistemas de áudio, workflows de produção e, mais recentemente, engenharia de software e IA.

Este projeto reflete uma abordagem prática, sistêmica e orientada a resultado.

