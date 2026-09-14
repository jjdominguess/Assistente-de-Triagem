# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="Assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>


# Graduação ON em Inteligência Artificial #

# Fire Guard AI #

## 📜 Descrição

O **Fire Guard AI** é uma solução integrada de Inteligência Artificial para detecção de incêndios em áreas florestais, combinando Visão Computacional, Machine Learning e IA Generativa para monitoramento ambiental e preservação de biomas vulneráveis.

Este projeto demonstra a aplicação prática de **técnicas avançadas de IA**, contemplando:

- **Visão Computacional**: Arquitetura MobileNetV2 com Transfer Learning
- **Dataset de Treinamento**: ~2.700 imagens de incêndios e áreas sem fogo
- **Performance do Modelo**: 90% de acurácia no conjunto de testes
- **Interface Web**: Streamlit para análise em tempo real de imagens
- **IA Generativa**: LLM Ollama para geração de relatórios em linguagem natural
- **Integração Disciplinar**: Fusão de múltiplas competências do curso

O sistema processa imagens enviadas pelo usuário, identifica probabilidade de ocorrência de incêndio e gera relatórios técnicos acessíveis, demonstrando como tecnologias de IA podem contribuir para iniciativas de sustentabilidade e proteção ambiental.


## 🎯 Objetivo

Este projeto visa demonstrar a aplicação integrada de Inteligência Artificial para detecção de incêndios florestais, garantindo:

- 📌 Detecção inteligente de incêndios com 90% de acurácia
- 📌 Integração de Visão Computacional (Transfer Learning com MobileNetV2)
- 📌 Interface acessível para análise em tempo real com Streamlit
- 📌 IA Generativa para geração de relatórios técnicos em linguagem natural
- 📌 Monitoramento ambiental e proteção de biomas vulneráveis

## 🧠 Estrutura Macro do Repositório

```bash
📂 FIRE-GUARD-AI
│
├── 📂 AI_GENERATIVE
│   └── 📜 generative.py
│
├── 📂 ASSETS
│   └── 📜 logo-fiap.png
│
├── 📂 BOARD
│   └── 📜 app.py
│
├── 📂 DATASET
│   ├── 📂 train/
│   │   ├── 📂 fire/
│   │   └── 📂 nofire/
│   ├── 📂 val/
│   │   ├── 📂 fire/
│   │   └── 📂 nofire/
│   ├── 📂 test/
│   │   ├── 📂 fire/
│   │   └── 📂 nofire/
│   └── 📂 test2/
│
├── 📂 DOCS
│   └── 📜 fire_guard_AI.drawio
│
├── 📂 MODELS
│   ├── 📜 __init__.py
│   ├── 📜 train_model.py
│   ├── 📜 predict.py
│   ├── 📜 generator.py
│   └── 📜 fire_guard_model.keras
│
├── 📂 SUPPORT_FILES
│   └── 📜 remove_corrupted_images.py
│
├── 📜 README.md
├── 📜 requirements.txt
└── 📂 venv/
```

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

> Projeto desenvolvido para fins acadêmicos, seguindo boas práticas de ciência de dados e aprendizado de máquina.
