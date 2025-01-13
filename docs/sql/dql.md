# Data Query Language - DQL

## Introdução

DQL é um conjunto de comandos que permitem consultar e recuperar dados de um banco de dados relacional.


## DQL

### 1. Itens e Armazenamento

#### Listar todos os itens disponíveis no jogo
```sql
SELECT * FROM item;
```

#### Consultar itens armazenados em um local específico
```sql
SELECT a.id, i.nome, a.quantidade 
FROM armazenamento a
JOIN item i ON a.item_id = i.id;
```

#### Verificar itens no inventário de um personagem
```sql
SELECT ii.id, i.nome, i.tipo 
FROM item_instancia ii
JOIN item i ON ii.item_id = i.id
WHERE ii.inventario_id = (SELECT id FROM inventario WHERE personagem_id = $1);
```

---

### 2. Regiões e Sub-regiões

#### Listar todas as regiões e seus elementos
```sql
SELECT * FROM regiao;
```

#### Listar sub-regiões de uma região específica
```sql
SELECT sr.id, sr.nome, sr.descricao 
FROM sub_regiao sr
WHERE sr.regiao_id = $1;
```

#### Consultar conexões entre sub-regiões
```sql
SELECT src.sub_regiao_1, src.sub_regiao_2, src.direcao, src.situacao 
FROM sub_regiao_conexao src;
```

---

### 3. Personagens e Inventários

#### Detalhes de um personagem
```sql
SELECT * FROM personagem WHERE id = $1;
```

#### Consultar a mochila e o peso da mochila de um personagem
``` sql
SELECT m.id, m.peso, m.peso_total
FROM mochila m
JOIN inventario inv ON m.id = inv.id
WHERE inv.personagem_id = $1;
```

#### Consultar itens de um personagem
```sql
SELECT i.nome, i.descricao, ii.quantidade
FROM inventario inv
JOIN item_instancia ii ON inv.id = ii.inventario_id
JOIN item i ON ii.item_id = i.id
WHERE inv.personagem_id = $1;
```

#### Consultar poções do inventário de um personagem
```sql
SELECT p.id, p.turnos, p.usado, i.nome AS item_nome
FROM pocao p
JOIN item i ON p.id = i.id
JOIN item_instancia ii ON i.id - ii.item_id
JOIN inventario inv ON ii.inventario_id = inv.id
WHERE inv.personagem_id = $1;
```

#### Consultar os feitiços aprendidos
```sql
SELECT f.descricao, f.elemento, f.tipo
FROM feitico f
JOIN feitico_aprendido fa ON f.id = fa.feitico_id
WHERE fa.inventario_id = $1; -- $1 is iventory id's
```

#### Consultar os efeitos de um acessório
```sql
SELECT e.nome, e.descricao, e.defesa, e.inteligencia, e.critico
FROM efeito e
JOIN acessorio_efeito ae ON e.id = ae.efeito_id
JOIN acessorio a ON ae.acessorio_id = a.id
JOIN item_instancia ii ON a.id = ii.item_id
JOIN inventario inv ON ii.inventario_id = inv.id
WHERE inv.personagem_id = $1;
```

#### Consultar todas as subregiões que um personagem pode ir
``` sql
SELECT sr2.nome AS sub_regiao_destino, src.direcao, src.situacao
FROM sub_regiao_conexao src
JOIN sub_regiao sr1 ON src.sub_regiao_1 = sr1.id
JOIN sub_regiao sr2 ON src.sub_regiao_2 = sr2.id
WHERE sr1.id = $1; 
```

---

### 4. NPCs e Interações

#### Listar NPCs em uma sub-região
```sql
SELECT n.id, n.nome, n.tipo 
FROM npc n
JOIN civil c ON c.id = n.id
WHERE c.sub_regiao_id = $1;
```

#### Listar mercadores e seus itens disponíveis
```sql
SELECT m.id, m.dialogo, i.nome, a.quantidade 
FROM mercador m
JOIN armazenamento_mercador am ON am.mercador_id = m.id
JOIN armazenamento a ON a.id = am.armazenamento_id
JOIN item i ON i.id = a.item_id;
```

#### Listar diálogos dos mercadores
```sql
SELECT m.id, m.dialogo
FROM mercador m;
```

#### Consultar transações entre mercador e personagem
```sql
SELECT t.id, m.dialogo AS mercador, p.nome AS personagem, i.nome AS item
FROM transcoes t
JOIN mercador m ON t.mercador_id = m.id
JOIN personagem p ON t.personagem_id = p.id
JOIN item i ON t.item_id = i.id;
```

---

### 5. Feitiços e Grimórios

#### Listar feitiços aprendidos por um personagem
```sql
SELECT f.id, f.descricao, f.elemento, f.tipo 
FROM feitico_aprendido fa
JOIN feitico f ON fa.feitico_id = f.id
WHERE fa.inventario_id = (SELECT id FROM inventario WHERE personagem_id = $1);
```

#### Consultar feitiços em pergaminhos
```sql
SELECT p.id, p.cor, f.descricao, f.elemento 
FROM pergaminho p
JOIN feitico_escrito fe ON fe.item_id = p.id
JOIN feitico f ON fe.feitico_id = f.id;
```


#### Listar feitiços de Dano em área
```sql
SELECT f.descricao, f.elemento, f.energia_arcana, fda.qtd_inimigos_afetados
FROM feitico f
JOIN feitico_dano_area fda ON f.id = fta.id;
```

#### Listar feitiços de Dano
```sql
SELECT f.descricao, f.elemento, f.energia_arcana, fd.dano_total
FROM feitico f
JOIN feitico_dano fd ON f.id = fd.id;
```

#### Listar feitiços de Cura
```sql
SELECT f.descricao, f.elemento, f.energia_arcana, fc.qtd_cura
FROM feitico f
JOIN feitico_dano fc ON f.id = fc.id;
```

---

### 6. Quests

#### Listar quests disponíveis por um Quester
```sql
SELECT q.id, q.titulo, q.descricao, q.dificuldade, q.recompensa 
FROM quest q
WHERE q.quester_id = $1;
```

#### Consultar progresso de quests de um personagem
```sql
SELECT qi.id, q.titulo, qi.completed 
FROM quest_instancia qi
JOIN quest q ON qi.quest_id = q.id
WHERE qi.personagem_id = $1;
```

---

### 7. Combates

#### Consultar histórico de combates de um personagem
```sql
SELECT c.inimigo_instancia_id, c.dano_causado, c.dano_recebido 
FROM combate c
WHERE c.personagem_id = $1;
```

#### Listar inimigos em uma sub-região
```sql
SELECT ii.id, i.nome, ii.vida 
FROM inimigo_instancia ii
JOIN inimigo i ON ii.inimigo_id = i.id
WHERE ii.sub_regiao_id = $1;
```

## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 13/01/2024 | Criação   | Grupo |
| `1.1`  | 13/01/2024 | Correções e Adições | Grupo |