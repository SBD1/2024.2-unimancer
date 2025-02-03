from database import Database
from utils import debug, error
from colorama import Style

# adding enemies to database
def default_enemies(db: Database):
    
    table_name = Style.BRIGHT + "INIMIGO" + Style.NORMAL
    
    try:
        enemies = [
            ("", "Rato Selvagem", "Um pequeno roedor agressivo que se alimenta de restos do vilarejo.", "Terra", 20, 5, 2, 0, 0, 1),
            ("", "Ladrão de Rua", "Um criminoso que tenta roubar viajantes desavisados.", "Trevas", 30, 10, 5, 0, 0, 3),
            ("", "Corvo Guardião", "Um pássaro grande e territorial que protege os arredores da praça.", "Ar", 25, 8, 3, 0, 0, 2),
            ("🐺", "Lobo Sombrio", "Uma criatura ágil que caça à noite na floresta.", "Trevas", 50, 20, 10, 0, 0, 4),
            ("", "Espírito da Clareira", "Um espírito pacífico que pode se tornar hostil se perturbado.", "Luz", 40, 15, 0, 10, 20, 5),
            ("", "Ent Ancião", "Uma árvore viva que protege os segredos da floresta.", "Terra", 70, 25, 15, 5, 10, 3),
            ("", "Guardião de Pedra", "Um golem que defende as ruínas de intrusos.", "Terra", 80, 30, 20, 0, 0, 2),
            ("", "Serpente das Sombras", "Uma serpente que se camufla nas ruínas escuras.", "Trevas", 60, 25, 10, 5, 10, 4),
            ("", "Espectro do Abismo", "Um fantasma que assombra os corredores das ruínas.", "Trevas", 50, 20, 5, 20, 30, 8),
            ("", "Escorpião Gigante", "Um escorpião imenso, armado com uma cauda venenosa.", "Terra", 90, 35, 15, 0, 0, 3),
            ("", "Djin Traiçoeiro", "Um espírito do deserto que tenta enganar os viajantes.", "Fogo", 60, 30, 20, 15, 40, 10),
            ("", "Caravaneiro Corrompido", "Um comerciante que se tornou hostil após perder tudo.", "Luz", 70, 30, 25, 5, 10, 6),
            ("", "Golem de Cristal", "Um golem criado a partir de cristais brilhantes, resistente e difícil de derrotar.", "Terra", 150, 70, 30, 5, 10, 3),
            ("", "Minerador Fantasma", "O espírito de um minerador que morreu na caverna, ainda vagando em busca de tesouros.", "Trevas", 80, 50, 20, 15, 30, 6),
            ("", "Afortunado", "Uma entidade mágica que protege os cristais mais valiosos da caverna.", "Luz", 100, 60, 40, 20, 40, 10),
            ("", "Gigante Congelado", "Um gigante que protege os picos nevados.", "Água", 120, 50, 30, 5, 15, 5),
            ("", "Águia do Crepúsculo", "Um pássaro imenso que domina os céus da montanha.", "Ar", 80, 40, 20, 10, 25, 7),
            ("", "Espírito da Geada", "Um ser mágico que controla o gelo da montanha.", "Água", 70, 35, 10, 20, 50, 9),
            ("", "Guerreiro Esqueleto", "Um esqueleto animado pela magia negra, armado com espadas enferrujadas.", "Trevas", 70, 35, 15, 5, 0, 3),
            ("", "Feiticeiro Esqueleto", "Um mago esqueleto que usa feitiços antigos para proteger os segredos da caverna.", "Trevas", 60, 40, 10, 25, 50, 12),
            ("", "Goblin Zumbi", "Um goblin reanimado, movido por uma força sombria.", "Trevas", 50, 20, 5, 0, 0, 2),
            ("", "Guerreiro Corrompido", "Um antigo herói que foi consumido pelo mal.", "Trevas", 100, 60, 50, 10, 20, 7),
            ("", "Fera Flamejante", "Uma criatura ardente que espalha destruição.", "Fogo", 110, 55, 40, 15, 30, 8),
            ("🐉", "Dragão da Devastação", "Um dragão imenso, a maior ameaça das terras devastadas.", "Trevas", 200, 100, 100, 50, 100, 20),
            ("", "Abgail", "Entidade de uma grande maga que pagou o preço por conhecer todas as verdades.", "Fogo", 150, 60, 75, 100, 100, 12),
            ("", "Lumina", "Lumina é uma figura radiante, simbolizando a pureza e o poder da luz. Sua presença ilumina até as sombras mais profundas, e ela tem a capacidade de curar aliados ou desintegrar inimigos com feixes de luz concentrados.", "Luz", 180, 75, 90, 120, 90, 15),
            ("", "Necromante", "O Necromante é um mestre das artes negras, comandando os mortos e manipulando as trevas para enfraquecer seus inimigos.", "Trevas", 200, 85, 100, 110, 120, 14),
            (
                "",
                "Nosferus",
                "Antigo Unimancer que abandonou sua humanidade em busca de mais poder, e aprender a controlar outros elementos.",
                "Trevas",
                220,
                100,
                125,
                130,
                80,
                18
            )
        ]
        
        for enemy in enemies:
            emoji, name, description, element, max_hp, xp, inteligence, coins, arcana, energy = enemy
            db.cur.execute(
                f"""
                SELECT criar_inimigo(
                    '{emoji}',
                    '{name}',
                    '{description}',
                    '{element}',
                    {max_hp},
                    {xp},
                    {inteligence},
                    {coins},
                    {arcana},
                    {energy},
                    '.....dialogo inimigo....'
                )
                """
            )

        db.conn.commit()
        debug(f"default: {len(enemies)} {table_name} added successfully!")
       
        return len(enemies) 

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name} values: {e}")