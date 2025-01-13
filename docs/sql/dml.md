# Data Manipulation Language - DML

## Introdução

DML é um conjunto de instruções SQL que permitem consultar, adicionar, editar e excluir dados de tabelas ou visualizações de banco de dados

## DML

### Região

```sql
-- adiciona regiao
INSERT INTO regiao (nome, descricao, elemento) VALUES 
    ("Vilarejo do Amanhecer", "Região inicial do jogador, um vilarejo tranquilo, esbelto...", "Água")

-- adiciona subregiao
INSERT INTO subregiao (regiao_id, parent_id, nome, descricao)
VALUES
    ((SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer'), NULL, 'Ferraria Albnur', 'Local de trabalho árduo onde ferramentas e armas são forjadas.'),
    ((SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer'), NULL, 'Praça Central', 'O coração do vilarejo, cheio de vida e comércio.'),
    ((SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer'), NULL, 'Casa do Ancião', 'Uma casa tranquila que guarda histórias e conselhos sábios.'),
    ((SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer'), NULL, 'Taberna da Caneca Partida', 'Um refúgio caloroso para diversão e descanso.');

-- adiciona as conexoes das subregioes
INSERT INTO sub_regiao_conexao (sub_regiao_1, sub_regiao_2, direcao, situacao)
VALUES
    ((SELECT id FROM sub_regiao WHERE nome = 'Ferraria Albnur' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')),
     (SELECT id FROM sub_regiao WHERE nome = 'Praça Central' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')), 'Sul', 'Passável'),
    ((SELECT id FROM sub_regiao WHERE nome = 'Praça Central' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')),
     (SELECT id FROM sub_regiao WHERE nome = 'Ferraria Albnur' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')), 'Norte', 'Passável'),
    ((SELECT id FROM sub_regiao WHERE nome = 'Praça Central' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')),
     (SELECT id FROM sub_regiao WHERE nome = 'Casa do Ancião' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')), 'Oeste', 'Passável'),
    ((SELECT id FROM sub_regiao WHERE nome = 'Casa do Ancião' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')),
     (SELECT id FROM sub_regiao WHERE nome = 'Praça Central' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')), 'Leste', 'Passável'),
    ((SELECT id FROM sub_regiao WHERE nome = 'Praça Central' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')),
     (SELECT id FROM sub_regiao WHERE nome = 'Taberna da Caneca Partida' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')), 'Leste', 'Passável'),
    ((SELECT id FROM sub_regiao WHERE nome = 'Taberna da Caneca Partida' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')),
     (SELECT id FROM sub_regiao WHERE nome = 'Praça Central' AND regiao_id = (SELECT id FROM regiao WHERE nome = 'Vilarejo do Amanhecer')), 'Oeste', 'Passável');
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