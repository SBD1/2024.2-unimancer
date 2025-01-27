from database import Database
from utils import debug, error
from colorama import Style

# Add something in the database.
def sub_regions_connections(db: Database):
    
    table_name = Style.BRIGHT + "SUB_REGIAO_CONEXAO" + Style.NORMAL
    
    try:
        # consult IDs of every region
        db.cur.execute("SELECT id, nome FROM regiao")
        regioes = {regiao[1]: regiao[0] for regiao in db.cur.fetchall()}

        # verify if regions are in database
        expected_regions = [
            "Vilarejo do Amanhecer",
            "Floresta Eterna",
            "Ruínas do Abismo",
            "Deserto de Areias Infinitas",
            "Montanha do Crepúsculo",
            "Terras Devastadas",
            "Caverna Cristalizada",
            "Caverna Soterrada"
        ]

        for region in expected_regions:
            if region not in regioes:
                raise ValueError(f"Region: {region} not found!")
        
        # Getting all subregions
        connections = []
        db.cur.execute(f"SELECT id, nome FROM sub_regiao WHERE regiao_id = {regioes['Vilarejo do Amanhecer']}")
        vilarejo_subs = {row[1]: row[0] for row in db.cur.fetchall()}
        
        db.cur.execute(f"SELECT id, nome FROM sub_regiao WHERE regiao_id ={regioes['Floresta Eterna']}")
        floresta_subs = {row[1]: row[0] for row in db.cur.fetchall()}

        db.cur.execute(f"SELECT id, nome FROM sub_regiao WHERE regiao_id ={regioes['Ruínas do Abismo']}")
        ruinas_subs = {row[1]: row[0] for row in db.cur.fetchall()}

        db.cur.execute(f"SELECT id, nome FROM sub_regiao WHERE regiao_id ={regioes['Deserto de Areias Infinitas']}")
        deserto_subs = {row[1]: row[0] for row in db.cur.fetchall()}

        db.cur.execute(f"SELECT id, nome FROM sub_regiao WHERE regiao_id ={regioes['Montanha do Crepúsculo']}")
        montanhas_subs = {row[1]: row[0] for row in db.cur.fetchall()}

        db.cur.execute(f"SELECT id, nome FROM sub_regiao WHERE regiao_id ={regioes['Terras Devastadas']}")
        terras_subs = {row[1]: row[0] for row in db.cur.fetchall()}

        db.cur.execute(f"SELECT id, nome FROM sub_regiao WHERE regiao_id ={regioes['Caverna Cristalizada']}")
        caverna_cristal_subs = {row[1]: row[0] for row in db.cur.fetchall()}

        db.cur.execute(f"SELECT id, nome FROM sub_regiao WHERE regiao_id ={regioes['Caverna Soterrada']}")
        caverna_soterrada_subs = {row[1]: row[0] for row in db.cur.fetchall()}

        # 1. Vilarejo do Amanhecer
        connections += [
            (vilarejo_subs["Ferraria Albnur"], vilarejo_subs["Praça Central"], "Sul", "Passável"),
            (vilarejo_subs["Praça Central"], vilarejo_subs["Ferraria Albnur"], "Norte", "Passável"),
            (vilarejo_subs["Praça Central"], vilarejo_subs["Casa do Ancião"], "Oeste", "Passável"),
            (vilarejo_subs["Casa do Ancião"], vilarejo_subs["Praça Central"], "Leste", "Passável"),
            (vilarejo_subs["Praça Central"], vilarejo_subs["Taberna da Caneca Partida"], "Leste", "Passável"),
            (vilarejo_subs["Taberna da Caneca Partida"], vilarejo_subs["Praça Central"], "Oeste", "Passável"),
            (vilarejo_subs["Casa do Ancião"], floresta_subs["Lago da Serenidade"], "Oeste", "Não Passável"),
            (floresta_subs["Lago da Serenidade"], vilarejo_subs["Casa do Ancião"], "Leste", "Passável")
        ]

        # 2. Floresta Eterna
        connections += [
            (floresta_subs["Clareira dos Espíritos"], floresta_subs["Bosque Sombrio"], "Sul", "Passável"),
            (floresta_subs["Bosque Sombrio"], floresta_subs["Clareira dos Espíritos"], "Norte", "Passável"),
            (floresta_subs["Bosque Sombrio"], floresta_subs["Ruínas Perdidas"], "Oeste", "Passável"),
            (floresta_subs["Ruínas Perdidas"], floresta_subs["Bosque Sombrio"], "Leste", "Passável"),
            (floresta_subs["Bosque Sombrio"], floresta_subs["Lago da Serenidade"], "Leste", "Passável"),
            (floresta_subs["Lago da Serenidade"], floresta_subs["Bosque Sombrio"],  "Oeste", "Passável"),
            (floresta_subs["Bosque Sombrio"], floresta_subs["Ruínas Perdidas"], "Oeste", "Passável"),
            (floresta_subs["Ruínas Perdidas"],  floresta_subs["Bosque Sombrio"], "Leste", "Passável"),
            (floresta_subs["Ruínas Perdidas"],  ruinas_subs["Entrada da Ruína"], "Oeste", "Passável"),
            (ruinas_subs["Entrada da Ruína"], floresta_subs["Ruínas Perdidas"], "Leste", "Passável")
        ]

        # 2.1. Ruínas do Abismo
        connections += [
            (ruinas_subs["Fenda do Abismo"], ruinas_subs["Praça das Estátuas"], "Sul", "Passável"),
            (ruinas_subs["Praça das Estátuas"], ruinas_subs["Fenda do Abismo"], "Norte", "Não Passável"),
            (ruinas_subs["Praça das Estátuas"], ruinas_subs["Santuário Perdido"], "Oeste", "Passável"),
            (ruinas_subs["Santuário Perdido"], ruinas_subs["Praça das Estátuas"], "Leste", "Passável"),
            (ruinas_subs["Praça das Estátuas"], ruinas_subs["Entrada da Ruína"], "Leste", "Passável"),
            (ruinas_subs["Entrada da Ruína"], ruinas_subs["Praça das Estátuas"],  "Oeste", "Passável"),
            (ruinas_subs["Praça das Estátuas"], ruinas_subs["Santuário Perdido"], "Oeste", "Passável"),
            (ruinas_subs["Santuário Perdido"],  ruinas_subs["Praça das Estátuas"], "Leste", "Passável")
        ]

        # 3. Deserto de Areias Infinitas
        connections += [
            (deserto_subs["Oásis dos Mercadores"], deserto_subs["Vale das Serpentes"], "Sul", "Passável"),
            (deserto_subs["Oásis dos Mercadores"], montanhas_subs["Vilarejo dos Gigantes"], "Leste", "Não Passável"),
            # Voltar para deserto também ????
            (deserto_subs["Vale das Serpentes"], deserto_subs["Oásis dos Mercadores"], "Norte", "Passável"),
            (deserto_subs["Vale das Serpentes"], deserto_subs["Caverna de Cristal"], "Oeste", "Passável"),
            (deserto_subs["Caverna de Cristal"], deserto_subs["Vale das Serpentes"], "Leste", "Passável"),
            (deserto_subs["Caverna de Cristal"], caverna_cristal_subs["Entrada Cristalizada"], "Oeste", "Passável"),
            (caverna_cristal_subs["Entrada Cristalizada"], deserto_subs["Caverna de Cristal"], "Norte", "Passável"),
            (deserto_subs["Vale das Serpentes"], deserto_subs["Ruínas Submersas"], "Leste", "Passável"),
            (deserto_subs["Ruínas Submersas"], deserto_subs["Vale das Serpentes"],  "Oeste", "Passável"),
            (deserto_subs["Vale das Serpentes"], deserto_subs["Caverna de Cristal"], "Oeste", "Passável"),
            (deserto_subs["Caverna de Cristal"],  deserto_subs["Vale das Serpentes"], "Leste", "Passável")
        ]

        # 3.1. Caverna Cristalizada
        connections += [
            (caverna_cristal_subs["Trono Cristalizado"], caverna_cristal_subs["Núcleo Cristalino"], "Sul", "Passável"),
            (caverna_cristal_subs["Núcleo Cristalino"], caverna_cristal_subs["Trono Cristalizado"], "Norte", "Passável"),
            (caverna_cristal_subs["Núcleo Cristalino"], caverna_cristal_subs["Entrada Cristalizada"], "Oeste", "Passável"),
            (caverna_cristal_subs["Entrada Cristalizada"], caverna_cristal_subs["Núcleo Cristalino"], "Leste", "Passável"),
            (caverna_cristal_subs["Núcleo Cristalino"], caverna_cristal_subs["Vale da Fortuna"], "Leste", "Passável"),
            (caverna_cristal_subs["Vale da Fortuna"], caverna_cristal_subs["Núcleo Cristalino"],  "Oeste", "Passável"),
        ]

        # 4. Montanhas do Crepúsculo
        connections += [
            (montanhas_subs["Pico Congelado"], montanhas_subs["Vilarejo dos Gigantes"], "Sul", "Passável"),
            (montanhas_subs["Vilarejo dos Gigantes"], montanhas_subs["Pico Congelado"], "Norte", "Passável"),
            (montanhas_subs["Vilarejo dos Gigantes"], montanhas_subs["Cavernas Ecoantes"], "Oeste", "Passável"),
            (montanhas_subs["Cavernas Ecoantes"], montanhas_subs["Vilarejo dos Gigantes"], "Leste", "Passável"),
            (montanhas_subs["Vilarejo dos Gigantes"], montanhas_subs["Ponte Suspensa"], "Leste", "Passável"),
            (montanhas_subs["Ponte Suspensa"], montanhas_subs["Vilarejo dos Gigantes"],  "Oeste", "Passável"),
            (montanhas_subs["Vilarejo dos Gigantes"], montanhas_subs["Cavernas Ecoantes"], "Oeste", "Passável"),
            (montanhas_subs["Cavernas Ecoantes"],  montanhas_subs["Vilarejo dos Gigantes"], "Leste", "Passável"),
            (montanhas_subs["Cavernas Ecoantes"],  caverna_soterrada_subs["Bosque Perdido"], "Oeste", "Passável"),
            (caverna_soterrada_subs["Bosque Perdido"], montanhas_subs["Cavernas Ecoantes"], "Sul", "Passável")
        ]

        # 4.1 Caverna Soterrada
        connections += [
            (caverna_soterrada_subs["Vila Esquecida"], caverna_soterrada_subs["Bosque Perdido"], "Sul", "Passável"),
            (caverna_soterrada_subs["Bosque Perdido"], caverna_soterrada_subs["Vila Esquecida"], "Norte", "Passável"),
            (caverna_soterrada_subs["Bosque Perdido"], caverna_soterrada_subs["Jardim de Ossos"], "Oeste", "Passável"),
            (caverna_soterrada_subs["Jardim de Ossos"], caverna_soterrada_subs["Bosque Perdido"], "Leste", "Passável"),
            (caverna_soterrada_subs["Bosque Perdido"], caverna_soterrada_subs["Monte Caído"], "Leste", "Não Passável"),
            (caverna_soterrada_subs["Monte Caído"], caverna_soterrada_subs["Bosque Perdido"],  "Oeste", "Passável"),
            (caverna_soterrada_subs["Monte Caído"], terras_subs["Planícies de Cinzas"],  "Leste", "Passável"),
            (terras_subs["Planícies de Cinzas"], caverna_soterrada_subs["Monte Caído"], "Sul", "Passável"),
            (caverna_soterrada_subs["Bosque Perdido"], caverna_soterrada_subs["Jardim de Ossos"], "Oeste", "Passável"),
            (caverna_soterrada_subs["Jardim de Ossos"],  caverna_soterrada_subs["Bosque Perdido"], "Leste", "Passável")
        ]

        # 5. Terras Devastadas
        connections += [
            (terras_subs["Catedral Queimada"], terras_subs["Planícies de Cinzas"], "Sul", "Passável"),
            (terras_subs["Planícies de Cinzas"], terras_subs["Catedral Queimada"], "Norte", "Não Passável"),
            (terras_subs["Planícies de Cinzas"], terras_subs["Cemitério"], "Oeste", "Passável"),
            (terras_subs["Cemitério"], terras_subs["Planícies de Cinzas"], "Leste", "Passável"),
            (terras_subs["Planícies de Cinzas"], terras_subs["Fenda Arcana"], "Leste", "Passável"),
            (terras_subs["Fenda Arcana"], terras_subs["Planícies de Cinzas"],  "Oeste", "Passável"),
        ]
        
        db.cur.executemany(
            """
            INSERT INTO sub_regiao_conexao (sub_regiao_1, sub_regiao_2, direcao, situacao)
            VALUES (%s, %s, %s, %s)
            """, connections
        )
        db.conn.commit()
        debug(f"default: {len(table_name)} {table_name} added successfully!")
        
        return len(table_name)

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values: {e}")
