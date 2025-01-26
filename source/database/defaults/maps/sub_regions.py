from database import Database
from utils import debug, error

def sub_regions(db: Database):
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
            
        # add subregions to each region
        sub_regions = [
             # Vilarejo do Amanhecer
            (regioes["Vilarejo do Amanhecer"], None, "Ferraria Albnur", "Local de trabalho árduo onde ferramentas e armas são forjadas."),
            (regioes["Vilarejo do Amanhecer"], None, "Praça Central", "O coração do vilarejo, cheio de vida e comércio."),
            (regioes["Vilarejo do Amanhecer"], None, "Casa do Ancião", "Uma casa tranquila que guarda histórias e conselhos sábios."),
            (regioes["Vilarejo do Amanhecer"], None, "Taberna da Caneca Partida", "Um refúgio caloroso para diversão e descanso."),

            # Floresta Eterna
            (regioes["Floresta Eterna"], None, "Clareira dos Espíritos", "Um lugar sereno, onde espíritos vagam em paz."),
            (regioes["Floresta Eterna"], None, "Bosque Sombrio", "Uma área escura e densa, onde o perigo espreita."),
            (regioes["Floresta Eterna"], None, "Lago da Serenidade", "Águas calmas e cristalinas que refletem a lua."),
            (regioes["Floresta Eterna"], None, "Ruínas Perdidas", "Restos de uma antiga civilização, esquecidos pelo tempo."),

            # Ruínas do Abismo
            (regioes["Ruínas do Abismo"], None, "Fenda do Abismo", "Uma fissura que leva às profundezas da ruína."),
            (regioes["Ruínas do Abismo"], None, "Praça das Estátuas", "Estátuas antigas que contam histórias de heróis do passado."),
            (regioes["Ruínas do Abismo"], None, "Entrada da Ruína", "A entrada principal para as ruínas ancestrais."),
            (regioes["Ruínas do Abismo"], None, "Santuário Perdido", "Um lugar sagrado, protegido por antigos guardiões."),

            # Deserto de Areias Infinitas
            (regioes["Deserto de Areias Infinitas"], None, "Oásis dos Mercadores", "Um lugar pacífico onde viajantes descansam e negociam."),
            (regioes["Deserto de Areias Infinitas"], None, "Vale das Serpentes", "Um vale perigoso, cheio de serpentes mortais."),
            (regioes["Deserto de Areias Infinitas"], None, "Ruínas Submersas", "Ruínas antigas parcialmente enterradas na areia."),
            (regioes["Deserto de Areias Infinitas"], None, "Caverna de Cristal", "Uma caverna brilhante repleta de cristais reluzentes."),

            # Caverna Cristalizada
            (regioes["Caverna Cristalizada"], None, "Trono Cristalizado", "Um trono majestoso, feito inteiramente de cristais."),
            (regioes["Caverna Cristalizada"], None, "Núcleo Cristalino", "O coração pulsante da caverna, cheio de energia."),
            (regioes["Caverna Cristalizada"], None, "Vale da Fortuna", "Um vale repleto de riquezas escondidas."),
            (regioes["Caverna Cristalizada"], None, "Entrada Cristalizada", "A entrada principal para a caverna brilhante."),

            # Montanha do Crepúsculo
            (regioes["Montanha do Crepúsculo"], None, "Pico Congelado", "O ponto mais alto da montanha, coberto por neve eterna."),
            (regioes["Montanha do Crepúsculo"], None, "Vilarejo dos Gigantes", "Uma vila antiga habitada por criaturas gigantes."),
            (regioes["Montanha do Crepúsculo"], None, "Ponte Suspensa", "Uma ponte precária que conecta picos distantes."),
            (regioes["Montanha do Crepúsculo"], None, "Cavernas Ecoantes", "Um labirinto de cavernas onde cada som é amplificado."),

            # Caverna Soterrada
            (regioes["Caverna Soterrada"], None, "Vila Esquecida", "Uma vila perdida no tempo, enterrada nas profundezas."),
            (regioes["Caverna Soterrada"], None, "Bosque Perdido", "Um bosque sombrio e labiríntico."),
            (regioes["Caverna Soterrada"], None, "Monte Caído", "Uma montanha desmoronada que guarda segredos."),
            (regioes["Caverna Soterrada"], None, "Jardim de Ossos", "Um jardim macabro, repleto de ossos antigos."),
        
            # Terras Devastadas
            (regioes["Terras Devastadas"], None, "Catedral Queimada", "Uma catedral em ruínas, marcada por chamas antigas."),
            (regioes["Terras Devastadas"], None, "Planícies de Cinzas", "Um campo vasto e desolado, coberto de cinzas."),
            (regioes["Terras Devastadas"], None, "Fenda Arcana", "Uma fenda mágica que emana energia arcana."),
            (regioes["Terras Devastadas"], None, "Cemitério", "Um lugar assombrado, onde os mortos descansam inquietos."),

        ]
        db.cur.executemany(
            """
            INSERT INTO sub_regiao (regiao_id, armazenamento_id, nome, descricao)
            VALUES (%s, %s, %s, %s)
            """, sub_regions
        )
        db.conn.commit()
        debug("default: sub-regions added successfully!")

    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding *sub-regions* values: {e}")