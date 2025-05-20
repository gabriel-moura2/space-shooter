# Galactic Onslaught

**Galactic Onslaught** é um jogo arcade 2D desenvolvido com [Pygame](https://www.pygame.org/), no qual o jogador controla uma pequena nave espacial que se move verticalmente para desviar de inimigos e destruir naves oponentes. O objetivo é sobreviver pelo maior número de fases possível, enfrentando desafios progressivamente mais difíceis.

Este projeto foi criado como uma prática de desenvolvimento e gerenciamento de projetos, e está atualmente em desenvolvimento.

## Pré-visualização

![til](./assets/images/pre-visualização.gif)

## Funcionalidades

- Controles simples (movimento vertical com as setas e disparo com espaço)
- Inimigos variados com padrões de ataque
- Níveis com dificuldade progressiva
- Sistema de pontuação

## Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Instale o Pygame:
```bash
pip install pygame
```
3. Clone este repositório:
```bash
git clone https://github.com/gabriel-moura2/space-shooter.git
cd space-shooter
```
4. Execute o jogo:
```bash
python main.py
```
## Requisitos

- Python 3.x
- Pygame

## Estrutura do Projeto

```bash
space-shooter/
├── assets/           # Imagens, sons, fontes
├── base/             # Classes básicas genéricas
├── core/             # Lógica principal do loop do jogo
├── entities/         # Naves, inimigos, projéteis, etc.
├── scenes/           # Telas e estados do jogo (menu, jogo, game over...)
├── system/           # Sistemas auxiliares (ex: colisão)
├── ui/               # Elementos de interface (textos, HUD)
├── utils/            # Funções utilitárias
├── config.py         # Configurações globais (tamanho da tela, cores, etc)
├── LICENSE
├── main.py           # Arquivo principal do jogo
├── README.md
└── requirements.txt  # Lista de dependências
```

***

> Este jogo é uma prática de projeto individual e serve como laboratório para aplicar conceitos de design, programação e organização em desenvolvimento de jogos.