# Data Manipulation Language - DML

## Introdução

DML é um conjunto de instruções SQL que permitem consultar, adicionar, editar e excluir dados de tabelas ou visualizações de banco de dados

## DML

### Região

```sql
INSERT INTO regiao (nome, descricao, elemento) VALUES 
    ("Bosques dos Serafins", "Bosque com o alto índice de serafins.", "Fogo"),
    ("Deserto de Obsidiana", "Deserto com areias negras e calor extremo.", "Fogo"),
    ("Lago dos Espelhos", "Lago tranquilo com águas cristalinas.", "Água"),
    ("Planície dos Ventos", "Vasta planície com ventos constantes.", "Ar");
```

### Feitiço

```sql
INSERT INTO feitico (descricao, elemento, countdown, energia_arcana_necessaria, energia_arcana, tipo)
VALUES 
('Feitiço de Fogo que causa dano em um inimigo.', 'Fogo', 5, 10, 5, 'Dano'),
('Feitiço de Cura que recupera vida do personagem.', 'Água', 3, 8, 5, 'Cura'),
('Feitiço de Terra que causa dano em área em múltiplos inimigos.', 'Terra', 6, 15, 10, 'Dano de área'),
('Feitiço de Ar que cria uma barreira de proteção.', 'Ar', 7, 12, 6, 'Dano'),
('Feitiço de Luz que restaura energia arcana.', 'Luz', 4, 10, 7, 'Cura');
```

### Poção

```sql
INSERT INTO item (descricao, chance_drop, nome, peso, preco)
VALUES
('Poção de Cura que recupera 50 pontos de vida.', 80, 'Poção de Cura', 1, 20),
('Poção de Energia que recupera 30 pontos de energia arcana.', 70, 'Poção de Energia', 1, 30),
('Poção de Força que aumenta o dano causado em 10 pontos.', 60, 'Poção de Força', 1, 50),
('Poção de Velocidade que aumenta a agilidade em 15 pontos.', 50, 'Poção de Velocidade', 1, 40),
('Poção de Defesa que reduz o dano recebido em 20 pontos.', 40, 'Poção de Defesa', 1, 60);
```

### Inimigo
```sql
INSERT INTO inimigo (descricao, elemento, vida_maxima, xp_obtido, inteligencia, modas_obtidas, conhecimento_arcano, energia_arcana_maxima, dialogo)
VALUES
('Pequeno inimigo de aparência verde, conhecido por ser astuto e rápido.', 'Terrestre', 100, 50, 10, 20, 15, 50, 'Um goblin pequeno que ataca com golpes rápidos.'),
('Inimigo morto-vivo que carrega uma espada enferrujada.', 'Morte', 150, 60, 15, 30, 20, 40, 'O esqueleto vagueia sem propósito, sempre buscando uma batalha.'),
('Criatura lendária que solta fogo e é temida por todos.', 'Fogo', 500, 300, 50, 100, 75, 200, 'O dragão é imenso e exala fogo em cada respiração.'),
('Inimigo rápido e ágil, atacando em matilhas.', 'Terrestre', 120, 40, 20, 25, 18, 30, 'Lobos selvagens caçam em grupo, tornando-os perigosos.'),
('Inimigo mágico que conjura feitiços poderosos e traiçoeiros.', 'Arcano', 200, 100, 40, 60, 80, 100, 'O feiticeiro sombrio usa feitiços de controle e destruição.');
```

## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 13/01/2024 | Criação   | Grupo |
| `1.1`  | 13/01/2024 | Atualização | Grupo |