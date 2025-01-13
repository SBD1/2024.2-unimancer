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
WHERE ii.inventario_id = (SELECT id FROM inventario WHERE personagem_id = ?);
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
WHERE sr.regiao_id = ?;
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
SELECT * FROM personagem WHERE id = ?;
```

#### Consultar inventários de um personagem
```sql
SELECT * 
FROM inventario 
WHERE personagem_id = ?;
```

---

### 4. NPCs e Interações

#### Listar NPCs em uma sub-região
```sql
SELECT n.id, n.nome, n.tipo 
FROM npc n
JOIN civil c ON c.id = n.id
WHERE c.sub_regiao_id = ?;
```

#### Listar mercadores e seus itens disponíveis
```sql
SELECT m.id, m.dialogo, i.nome, a.quantidade 
FROM mercador m
JOIN armazenamento_mercador am ON am.mercador_id = m.id
JOIN armazenamento a ON a.id = am.armazenamento_id
JOIN item i ON i.id = a.item_id;
```

---

### 5. Feitiços e Grimórios

#### Listar feitiços aprendidos por um personagem
```sql
SELECT f.id, f.descricao, f.elemento, f.tipo 
FROM feitico_aprendido fa
JOIN feitico f ON fa.feitico_id = f.id
WHERE fa.inventario_id = (SELECT id FROM inventario WHERE personagem_id = ?);
```

#### Consultar feitiços em pergaminhos
```sql
SELECT p.id, p.cor, f.descricao, f.elemento 
FROM pergaminho p
JOIN feitico_escrito fe ON fe.item_id = p.id
JOIN feitico f ON fe.feitico_id = f.id;
```

---

### 6. Quests

#### Listar quests disponíveis por um Quester
```sql
SELECT q.id, q.titulo, q.descricao, q.dificuldade 
FROM quest q
WHERE q.quester_id = ?;
```

#### Consultar progresso de quests de um personagem
```sql
SELECT qi.id, q.titulo, qi.completed 
FROM quest_instancia qi
JOIN quest q ON qi.quest_id = q.id
WHERE qi.personagem_id = ?;
```

---

### 7. Combates

#### Consultar histórico de combates de um personagem
```sql
SELECT c.inimigo_instancia_id, c.dano_causado, c.dano_recebido 
FROM combate c
WHERE c.personagem_id = ?;
```

#### Listar inimigos em uma sub-região
```sql
SELECT ii.id, i.nome, ii.vida 
FROM inimigo_instancia ii
JOIN inimigo i ON ii.inimigo_id = i.id
WHERE ii.sub_regiao_id = ?;
```

## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 13/01/2024 | Criação   | Grupo |