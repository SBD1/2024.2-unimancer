-- 1. consult all sub-regions where the character can go
SELECT sr2.nome AS sub_regiao_destino, src.direcao, src.situacao
FROM sub_regiao_conexao src
JOIN sub_regiao sr1 ON src.sub_regiao_1 = sr1.id
JOIN sub_regiao sr2 ON src.sub_regiao_2 = sr2.id
WHERE sr1.id = $1;  -- $1 is the actual subregion's ID 

-- 2. List all character
SELECT * FROM personagem;

-- 3. Consult itens from character's inventory
SELECT i.nome, i.descricao, ii.quantidade
FROM inventario inv
JOIN item_instancia ii ON inv.id = ii.inventario_id
JOIN item i ON ii.item_id = i.id
WHERE inv.personagem_id = $1; -- $1 is the character's ID 

-- 4. List all NPCs of a subregion
SELECT n.nome, n.tipo
FROM npc n
JOIN civil c ON n.id = c.id
WHERE c.sub_regiao_id = $1; -- $1 is the subregion's ID

-- 5. get all quest avaibles from a quester
SELECT q.titulo, q.descricao, q.recompensa, q.dificuldade
FROM quest q
JOIN quest_instancia qi ON q.id = qi.quest_id
WHERE qi.personagem_id = $1 AND qi.completed = FALSE; -- $1 is quester ID

-- 6. All spells learned 
SELECT f.descricao, f.elemento, f.tipo
FROM feitico f
JOIN feitico_aprendido fa ON f.id = fa.feitico_id
WHERE fa.inventario_id = $1; -- $1 is iventory id's

-- 7. get enemys from a subregion
SELECT i.descricao, i.elemento, i.vida_maxima, i.xp_obtido, i.moedas_obtidas
FROM inimigo i
JOIN inimigo_instancia ii ON i.id = ii.inimigo_id
WHERE ii.sub_regiao_id = $1; -- $1 subregion's ID

-- 8. Consultar transações entre mercadores e personagens (colocar em ingles)
SELECT t.id, m.dialogo AS mercador, p.nome AS personagem, i.nome AS item
FROM transcoes t
JOIN mercador m ON t.mercador_id = m.id
JOIN personagem p ON t.personagem_id = p.id
JOIN item i ON t.item_id = i.id;

-- 9. get effects from character's acessories
SELECT e.nome, e.descricao, e.defesa, e.inteligencia, e.critico
FROM efeito e
JOIN acessorio_efeito ae ON e.id = ae.efeito_id
JOIN acessorio a ON ae.acessorio_id = a.id
JOIN item_instancia ii ON a.id = ii.item_id
JOIN inventario inv ON ii.inventario_id = inv.id
WHERE inv.personagem_id = $1; -- $1 character's ID

-- 10. get spells 'dano em area'
SELECT f.descricao, f.elemento, f.energia_arcana, fda.qtd_inimigos_afetados
FROM feitico f
JOIN feitico_dano_area fda ON f.id = fta.id;

-- 11. get spells 'dano'
SELECT f.descricao, f.elemento, f.energia_arcana, fd.dano_total
FROM feitico f
JOIN feitico_dano fd ON f.id = fd.id;

-- 12. get spells 'cura'
SELECT f.descricao, f.elemento, f.energia_arcana, fc.qtd_cura
FROM feitico f
JOIN feitico_dano fc ON f.id = fc.id;

-- 13. get regions and your elements
SELECT r.nome, r.elemento, r.descricao
FROM regiao r;

-- 14. get potions avaible in caharcter's inventory
SELECT p.id, p.turnos, p.usado, i.nome AS item_nome
FROM pocao p
JOIN item i ON p.id = i.id
JOIN item_instancia ii ON i.id - ii.item_id
JOIN inventario inv ON ii.inventario_id = inv.id
WHERE inv.personagem_id = $1; -- $1 is character's id

-- 15. get all subregions from a region
SELECT sr.nome, sr.descricao
FROM sub_regiao sr
WHERE sr.regiao_id = $1; -- $1 is region's id

-- 16. backpack and weight
SELECT m.id, m.peso, m.peso_total
FROM mochila m
JOIN inventario inv ON m.id = inv.id
WHERE inv.personagem_id = $1; -- $1 character's id

-- 17. spells avaible in a 'pergaminho'
SELECT f.descricao, f.elemento
FROM feitico f
JOIN feitico_escrito fe ON f.id = fe.feitico_id
JOIN pergaminho p ON fe.item_id = p.id
WHERE p.id = $1; -- $1 is pergaminho's ID

-- 18. get combat from a character and a enemy
SELECT c.inimigo_instancia_id, c.personagem_id, c.dano_causado, c.dano_recebido
FROM combate c;

-- 19. Merchant and dialogues
SELECT m.id, m.dialogo
FROM mercador m;

-- 20. get all itens storaged by a merchant
SELECT i.nome, am.quantidade
FROM armazenamento_mercador am
JOIN armazenamento a ON am.armazenamento_id = a.id
JOIN item i ON a.item_id = i.id
WHERE am.mercador_id = $1; -- $1 is merchant's id

-- 21. get itens from a 'armazenamento' (storage?)
SELECT i.nome, i.descricao, a.quantidade
FROM armazenamento a
JOIN item i ON a.item_id = i.id
WHERE a.id = $1; -- $1 is the 'armazenamento' (storage's) ID
