# 🎯 Guess Number — Jogo de Adivinhação (CLI)

Jogo interativo de adivinhação numérica desenvolvido em Python para execução no terminal, onde o jogador define o limite máximo do desafio e recebe dicas a cada palpite até descobrir o número sorteado.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📋 Sobre o Projeto

Projeto desenvolvido para praticar lógica de programação, estruturas de repetição (`while`), controle de fluxo condicional (`if/elif/else`), tratamento e validação de entradas do usuário (`isdigit()`) e geração de números aleatórios com a biblioteca nativa `random`.

### ✨ Funcionalidades
- **Dificuldade Personalizável:** O jogador escolhe o número teto do desafio, definindo o intervalo de sorteio (`0` até o número escolhido).
- **Sistema de Dicas:** A cada tentativa incorreta, o programa informa se o palpite foi maior ou menor do que o número secreto.
- **Validação de Entradas:** Verifica se os valores digitados são numéricos tanto na definição do teto quanto durante os palpites, evitando falhas na execução.
- **Contador de Tentativas:** Registra e exibe ao final da partida quantas tentativas foram necessárias para acertar.
