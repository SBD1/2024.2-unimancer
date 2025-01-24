from database import Database
from utils import debug

# adding enemies to database
def default_enemies(db: Database):
    try:
        enemies = [
            ("Rato Selvagem", "Inimigo", "Um pequeno roedor agressivo que se alimenta de restos do vilarejo.", "Terra", 20, 5, 2, 0, 0, 1),
            ("Ladrão de Rua", "Inimigo", "Um criminoso que tenta roubar viajantes desavisados.", "Trevas", 30, 10, 5, 0, 0, 3),
            ("Corvo Guardião", "Inimigo", "Um pássaro grande e territorial que protege os arredores da praça.", "Ar", 25, 8, 3, 0, 0, 2),
            ("Lobo Sombrio", "Inimigo", "Uma criatura ágil que caça à noite na floresta.", "Trevas", 50, 20, 10, 0, 0, 4),
            ("Espírito da Clareira", "Inimigo", "Um espírito pacífico que pode se tornar hostil se perturbado.", "Luz", 40, 15, 0, 10, 20, 5),
            ("Ent Ancião", "Inimigo", "Uma árvore viva que protege os segredos da floresta.", "Terra", 70, 25, 15, 5, 10, 3),
            ("Guardião de Pedra", "Inimigo", "Um golem que defende as ruínas de intrusos.", "Terra", 80, 30, 20, 0, 0, 2),
            ("Serpente das Sombras", "Inimigo", "Uma serpente que se camufla nas ruínas escuras.", "Trevas", 60, 25, 10, 5, 10, 4),
            ("Espectro do Abismo", "Inimigo", "Um fantasma que assombra os corredores das ruínas.", "Trevas", 50, 20, 5, 20, 30, 8),
            ("Escorpião Gigante", "Inimigo", "Um escorpião imenso, armado com uma cauda venenosa.", "Terra", 90, 35, 15, 0, 0, 3),
            ("Djin Traiçoeiro", "Inimigo", "Um espírito do deserto que tenta enganar os viajantes.", "Fogo", 60, 30, 20, 15, 40, 10),
            ("Caravaneiro Corrompido", "Inimigo", "Um comerciante que se tornou hostil após perder tudo.", "Luz", 70, 30, 25, 5, 10, 6),
            ("Golem de Cristal", "Inimigo", "Um golem criado a partir de cristais brilhantes, resistente e difícil de derrotar.", "Terra", 150, 70, 30, 5, 10, 3),
            ("Minerador Fantasma", "Inimigo", "O espírito de um minerador que morreu na caverna, ainda vagando em busca de tesouros.", "Trevas", 80, 50, 20, 15, 30, 6),
            ("Afortunado", "Inimigo", "Uma entidade mágica que protege os cristais mais valiosos da caverna.", "Luz", 100, 60, 40, 20, 40, 10),
            ("Gigante Congelado", "Inimigo", "Um gigante que protege os picos nevados.", "Água", 120, 50, 30, 5, 15, 5),
            ("Águia do Crepúsculo", "Inimigo", "Um pássaro imenso que domina os céus da montanha.", "Ar", 80, 40, 20, 10, 25, 7),
            ("Espírito da Geada", "Inimigo", "Um ser mágico que controla o gelo da montanha.", "Água", 70, 35, 10, 20, 50, 9),
            ("Guerreiro Esqueleto", "Inimigo", "Um esqueleto animado pela magia negra, armado com espadas enferrujadas.", "Trevas", 70, 35, 15, 5, 0, 3),
            ("Feiticeiro Esqueleto", "Inimigo", "Um mago esqueleto que usa feitiços antigos para proteger os segredos da caverna.", "Trevas", 60, 40, 10, 25, 50, 12),
            ("Goblin Zumbi", "Inimigo", "Um goblin reanimado, movido por uma força sombria.", "Trevas", 50, 20, 5, 0, 0, 2),
            ("Guerreiro Corrompido", "Inimigo", "Um antigo herói que foi consumido pelo mal.", "Trevas", 100, 60, 50, 10, 20, 7),
            ("Fera Flamejante", "Inimigo", "Uma criatura ardente que espalha destruição.", "Fogo", 110, 55, 40, 15, 30, 8),
            ("Dragão da Devastação", "Inimigo", "Um dragão imenso, a maior ameaça das terras devastadas.", "Trevas", 200, 100, 100, 50, 100, 20)
        ]

        for enemy in enemies:
            # (temporary solution: adding a item test)
            # db.cur.execute(
            #     """
            #         INSERT INTO item (tipo, descricao, chance_drop, nome, peso, preco)
            #         VALUES (%s, %s, %s, %s, %s, %s)
            #         RETURNING id
            #     """, ("Acessório", "Item genérico para inicialização de armazenamento.", 0, "Placeholder", 0, 0)
            # )\
            # item_result = db.cur.fetchone()
            # if item_result is None:
            #     raise ValueError("Falha ao criar item placeholder.")
            # placeholder_item_id = item_result[0]

            # # (temporary solution: adding a storage)
            # db.cur.execute(
            #     """
            #         INSERT INTO armazenamento (item_id, quantidade)
            #         VALUES (%s, %s)
            #         RETURNING id
            #     """, (placeholder_item_id, 0) # enemy doens't have initial itens
            # )
            # storage_result = db.cur.fetchone()
            # if storage_result is None:
            #     raise ValueError("Falha ao criar armazenamento.")
            # armazenamento_id = storage_result[0]

            # add new NPC  enemy
            db.cur.execute(
                """
                    INSERT INTO npc (nome, tipo)
                    VALUES (%s, %s)
                    RETURNING id
                """, (enemy[0], enemy[1])
            )
            npc_result = db.cur.fetchone()
            npc_id = npc_result
            
            if npc_result is None:
                debug("Falied do reach npc")
                return

            # adding in enemy table
            db.cur.execute(
                """
                    INSERT INTO inimigo (id, armazenamento_id, descricao, elemento, vida_maxima, xp_obtido, moedas_obtidas, conhecimento_arcano, energia_arcana_maxima, inteligencia, dialogo)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (npc_id, None, enemy[2], enemy[3], enemy[4], enemy[5], enemy[6], enemy[7], enemy[8], enemy[9], None)
            )

        db.conn.commit()
        debug("default: enemies added successfully!")
        

    except Exception as e:
        debug(f"default: Error occurred while adding *inimigo* values: {e}")
        db.conn.rollback()
        