# Data Manipulation Language - DML

## Introdução

DML é um conjunto de instruções SQL que permitem consultar, adicionar, editar e excluir dados de tabelas ou visualizações de banco de dados

## DML

### Região
??? "DML Região"
    ```python
    ## adiciona regiao
    regions = [
            ("Vilarejo do Amanhecer", "Uma vila tranquila, onde os primeiros raios de sol tocam a terra.", "Água"),
            ("Floresta Eterna", "Uma floresta densa e mística, habitada por espíritos antigos.", "Terra"),
            ("Ruínas do Abismo", "Ruínas ancestrais com segredos esquecidos.", "Trevas"),
            ("Deserto de Areias Infinitas", "Um deserto vasto e sem fim, onde segredos estão enterrados sob a areia.", "Fogo"),
            ("Montanha do Crepúsculo", "Uma montanha alta e gélida, coberta de mistérios e perigos.", "Ar"),
            ("Terras Devastadas", "Um lugar sombrio e inóspito, marcado pela destruição e caos.", "Trevas"),
            ("Caverna Cristalizada", "Uma caverna mágica repleta de cristais brilhantes e perigos ocultos.", "Luz"),
            ("Caverna Soterrada", "Uma caverna misteriosa enterrada sob as montanhas, cheia de segredos antigos.", "Terra")
            ]
            db.cur.executemany(
                """
                INSERT INTO regiao (nome, descricao, elemento)
                VALUES (%s, %s, %s)
                """, regions
            )

    ## adiciona subregiao
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

    ## adiciona as conexoes das subregioes
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
    ```

### Feitiço
??? "DML Feitiço"
    ```python
    ## Feitico de dano
            default_values = [
                # Água
                (
                    "Jato de Água",
                    "Lança um jato de água pressurizada que causa danos moderados a um único inimigo.",
                    "Água",
                    2,
                    5,
                    10,
                    15  
                ),
                (
                    "Maremoto",
                    "Invoca uma grande onda que atinge vários inimigos, causando danos elevados.",
                    "Água",
                    5,
                    12,
                    20,
                    30
                ),
                (
                    "Tsunami",
                    "Desencadeia um tsunami devastador que causa danos massivos e empurra os inimigos para longe.",
                    "Água",
                    8,
                    20,
                    30,
                    50
                ),

                # Fogo
                (
                    "Bola de Fogo",
                    "Lança uma bola de fogo explosiva que causa danos intensos a todos os inimigos em uma área.",
                    "Fogo",
                    2,
                    5,
                    10,
                    20
                ),
                (
                    "Chuva de Fogo",
                    "Desce uma chuva de chamas sobre a área alvo, causando danos contínuos aos inimigos.",
                    "Fogo",
                    5,
                    12,
                    20,
                    35
                ),
                (
                    "Inferno Abrasador",
                    "Cria um inferno que queima intensamente, causando danos massivos e queimaduras persistentes.",
                    "Fogo",
                    8,
                    20,
                    30,
                    60
                ),

                # Terra
                (
                    "Saco de Pedra",
                    "Arremessa grandes pedras contra os inimigos, causando danos pesados a um único alvo.",
                    "Terra",
                    2,
                    5,
                    10,
                    18
                ),
                (
                    "Terremoto",
                    "Provoca um terremoto que atinge múltiplos inimigos, causando danos significativos e desequilibrando suas posições.",
                    "Terra",
                    5,
                    12,
                    20,
                    35
                ),
                (
                    "Coluna de Terra",
                    "Erige uma coluna gigante de terra que danifica severamente todos os inimigos ao seu redor.",
                    "Terra",
                    8,
                    20,
                    30,
                    50
                ),

                # Ar
                (
                    "Rajada Voadora",
                    "Lança uma forte rajada de vento que causa danos e empurra os inimigos para trás.",
                    "Ar",
                    2,
                    5,
                    10,
                    15
                ),
                (
                    "Tempestade de Vento",
                    "Invoca uma tempestade de vento que atinge vários inimigos, causando danos contínuos.",
                    "Ar",
                    5,
                    12,
                    20,
                    30
                ),
                (
                    "Furacão Violento",
                    "Desencadeia um furacão poderoso que causa danos massivos e desorienta todos os inimigos na área afetada.",
                    "Ar",
                    8,
                    20,
                    30,
                    50
                ),

                # Luz
                (
                    "Raio Luminoso",
                    "Dispara um raio de luz intensa que causa danos a um único inimigo.",
                    "Luz",
                    2,
                    5,
                    10,
                    15
                ),
                (
                    "Explosão Solar",
                    "Cria uma explosão de luz solar que atinge vários inimigos, causando danos elevados.",
                    "Luz",
                    5,
                    12,
                    20,
                    30
                ),
                (
                    "Eclipse Radiante",
                    "Invoca um eclipse de luz que causa danos massivos e cega temporariamente os inimigos na área.",
                    "Luz",
                    8,
                    20,
                    30,
                    50
                ),

                # Trevas
                (
                    "Sombras Cortantes",
                    "Lança sombras afiadas que causam danos contínuos a múltiplos inimigos.",
                    "Trevas",
                    2,
                    5,
                    10,
                    15
                ),
                (
                    "Torretas Obscuras",
                    "Invoca torretas de trevas que atacam automaticamente os inimigos nas proximidades, causando danos regulares.",
                    "Trevas",
                    5,
                    12,
                    20,
                    30
                ),
                (
                    "Tempestade Sombria",
                    "Desencadeia uma tempestade de trevas que envolve a área, causando danos intensos e drenando a energia arcana dos inimigos.",
                    "Trevas",
                    8,
                    20,
                    30,
                    50
                ),
            ]

            db.cur.executemany(
                """
                SELECT criar_feitico_dano(%s, %s, %s, %s, %s, %s, %s)
                """,
                default_values
            )

    ## Feitico de cura
            default_values = [
                # Água
                (
                    "Cura Áquatica",
                    "Canaliza a energia das águas para restaurar a vida de aliados dentro da área de efeito.",
                    "Água",
                    3,
                    8,
                    10,
                    25 
                ),
                (
                    "Manto Revitalizante",
                    "Envolve os aliados com um manto de água curativa, regenerando sua vida e energia arcana ao longo do tempo.",
                    "Água",
                    6,
                    15,
                    20,
                    40 
                ),

                # Fogo
                (
                    "Flama Curativa",
                    "Utiliza o calor das chamas para aquecer e curar ferimentos de aliados próximos.",
                    "Fogo",
                    3,
                    8,
                    10,
                    25 
                ),
                (
                    "Fogo Vigoroso",
                    "Invoca chamas benéficas que envolvem os aliados, restaurando sua vida e aumentando sua resistência arcana.",
                    "Fogo",
                    6,
                    15,
                    20,
                    40 
                ),

                # Terra
                (
                    "Regeneração Terrena",
                    "Conecta-se com a energia da terra para regenerar a vida dos aliados na área afetada.",
                    "Terra",
                    3,
                    8,
                    10,
                    25 
                ),
                (
                    "Escudo Vital",
                    "Forma um escudo de terra que protege e cura os aliados, absorvendo danos e restaurando sua vitalidade.",
                    "Terra",
                    6,
                    15,
                    20,
                    40 
                ),

                # Ar
                (
                    "Brisa Curativa",
                    "Convoca uma brisa suave que revitaliza e cura os aliados dentro de sua trajetória.",
                    "Ar",
                    3,
                    8,
                    10,
                    25 
                ),
                (
                    "Vórtice Revigorante",
                    "Cria um vórtice de ar que circunda os aliados, restaurando sua vida e energias arcanas continuamente.",
                    "Ar",
                    6,
                    15,
                    20,
                    40 
                ),

                # Luz
                (
                    "Luz Restauradora",
                    "Emite uma luz pura que cura ferimentos e restaura a energia arcana dos aliados na área iluminada.",
                    "Luz",
                    3,
                    8,
                    10,
                    25 
                ),
                (
                    "Aura Divina",
                    "Envolve os aliados com uma aura de luz celestial, proporcionando cura contínua e proteção contra energias negativas.",
                    "Luz",
                    6,
                    15,
                    20,
                    40 
                ),

                # Trevas
                (
                    "Sombra Curativa",
                    "Manipula as sombras para curar os aliados, ocultando-os enquanto restaura sua vitalidade.",
                    "Trevas",
                    3,
                    8,
                    10,
                    25 
                ),
                (
                    "Véu das Trevas",
                    "Cria um véu sombrio que não apenas protege os aliados, mas também cura suas feridas e renova sua energia arcana.",
                    "Trevas",
                    6,
                    15,
                    20,
                    40 
                ),
            ]

            db.cur.executemany(
                """
                SELECT criar_feitico_cura(%s, %s, %s, %s, %s, %s, %s)
                """,
                default_values
            )

    ## Feitico de dano em area
            default_values = [
                # Água
                (
                    "Sopro Congelante",
                    "Exala um vento gelado que congela os inimigos em uma ampla área, causando dano e reduzindo sua velocidade.",
                    "Água",
                    2,
                    5,
                    5,
                    10,   
                    3     
                ),
                (
                    "Muralha Gélida",
                    "Cria uma barreira de gelo ao redor do mago, danificando e desacelerando todos os inimigos que a atravessam.",
                    "Água",
                    4,
                    10,
                    8,
                    20,
                    5
                ),
                (
                    "Nevasca Intensa",
                    "Invoca uma tempestade de neve que causa dano contínuo aos inimigos dentro de sua área de efeito.",
                    "Água",
                    6,
                    15,
                    12,
                    25,
                    6
                ),
                (
                    "Tempestade Glacial",
                    "Desencadeia uma poderosa tempestade de gelo que atinge múltiplos inimigos, causando elevados danos e podendo congelá-los.",
                    "Água",
                    8,
                    20,
                    16,
                    35,
                    7
                ),
                (
                    "Dilúvio Ártico",
                    "Inunda a área com águas geladas, causando danos massivos e drenando a energia arcana dos inimigos afetados.",
                    "Água",
                    10,
                    25,
                    20,
                    50,
                    10
                ),

                # Fogo
                (
                    "Labareda Inicial",
                    "Lança chamas suaves que atingem uma área moderada, causando danos contínuos aos inimigos presentes.",
                    "Fogo",
                    2,
                    5,
                    5,
                    10,
                    3
                ),
                (
                    "Explosão Ígnea",
                    "Detona uma explosão de fogo que causa dano elevado a todos os inimigos em uma grande área.",
                    "Fogo",
                    4,
                    10,
                    8,
                    20,
                    5
                ),
                (
                    "Chamas Medonhas",
                    "Invoca chamas negras que envolvem a área alvo, causando dano constante e reduzindo a resistência dos inimigos.",
                    "Fogo",
                    6,
                    15,
                    12,
                    25,
                    6
                ),
                (
                    "Inferno Crescente",
                    "Desencadeia um inferno que se expande progressivamente, aumentando o dano conforme avança sobre os inimigos.",
                    "Fogo",
                    8,
                    20,
                    16,
                    35,
                    7
                ),
                (
                    "Apocalipse de Fogo",
                    "Invoca uma catástrofe de chamas que devasta uma vasta área, causando danos massivos e incendiando o terreno.",
                    "Fogo",
                    10,
                    25,
                    20,
                    50,
                    10
                ),

                # Terra
                (
                    "Tremor Raso",
                    "Provoca um leve tremor que atinge todos os inimigos próximos, causando danos moderados e desequilibrando suas defesas.",
                    "Terra",
                    2,
                    5,
                    5,
                    10,
                    3
                ),
                (
                    "Ondas Sísmicas",
                    "Envia ondas de choque pelo solo, danificando e desestabilizando múltiplos inimigos na área.",
                    "Terra",
                    4,
                    10,
                    8,
                    20,
                    5
                ),
                (
                    "Espiral Rochosa",
                    "Invoca espinhos de pedra que giram em torno do mago, atingindo todos os inimigos presentes na área de efeito.",
                    "Terra",
                    6,
                    15,
                    12,
                    25,
                    6
                ),
                (
                    "Avalanche Subterrânea",
                    "Desencadeia uma avalanche de pedras e terra que esmagam e causam danos severos aos inimigos na região afetada.",
                    "Terra",
                    8,
                    20,
                    16,
                    35,
                    7
                ),
                (
                    "Cataclismo Terrestre",
                    "Provoca uma devastadora ruptura na terra, causando danos massivos e alterando a topografia da área de combate.",
                    "Terra",
                    10,
                    25,
                    20,
                    50,
                    10
                ),

                # Ar
                (
                    "Vento Cortante",
                    "Lança rajadas de vento afiadas que cortam e causam danos a todos os inimigos na área alvo.",
                    "Ar",
                    2,
                    5,
                    5,
                    10,
                    3
                ),
                (
                    "Tornado Enfurecido",
                    "Invoca um tornado violento que percorre a área, causando danos constantes e desorganizando as formações inimigas.",
                    "Ar",
                    4,
                    10,
                    8,
                    20,
                    5
                ),
                (
                    "Furacão Impiedoso",
                    "Desencadeia um furacão devastador que arrasta e fere todos os inimigos atingidos dentro de sua vasta área de impacto.",
                    "Ar",
                    6,
                    15,
                    12,
                    25,
                    6
                ),
                (
                    "Ciclone Ascendente",
                    "Cria um ciclone poderoso que sobe rapidamente, causando danos intensos e espalhando destruição por toda a área afetada.",
                    "Ar",
                    8,
                    20,
                    16,
                    35,
                    7
                ),
                (
                    "Tempestade Celeste",
                    "Invoca uma tempestade de ventos celestiais que atinge múltiplos inimigos com rajadas de ar cortante e relâmpagos.",
                    "Ar",
                    10,
                    25,
                    20,
                    50,
                    10
                ),

                # Luz
                (
                    "Clarão Ofuscante",
                    "Emite um brilho intenso que cega e causa danos leves a todos os inimigos na área alvo.",
                    "Luz",
                    2,
                    5,
                    5,
                    10,
                    3
                ),
                (
                    "Arco Luminoso",
                    "Cria um arco de luz brilhante que dispara feixes de energia luminosa, danificando múltiplos inimigos.",
                    "Luz",
                    4,
                    10,
                    8,
                    20,
                    5
                ),
                (
                    "Chuva Reluzente",
                    "Desce uma chuva de raios de luz que atinge uma área ampla, causando danos contínuos e curando aliados próximos.",
                    "Luz",
                    6,
                    15,
                    12,
                    25,
                    6
                ),
                (
                    "Brilho Divino",
                    "Envolve a área com uma aura divina que causa danos elevados aos inimigos e aumenta a resistência dos aliados.",
                    "Luz",
                    8,
                    20,
                    16,
                    35,
                    7
                ),
                (
                    "Êxtase Solar",
                    "Libera um poderoso estalo de luz solar que incendeia e causa danos massivos a todos os inimigos na área de efeito.",
                    "Luz",
                    10,
                    25,
                    20,
                    50,
                    10
                ),

                # Trevas
                (
                    "Sussurro das Sombras",
                    "Murmura palavras sombrias que envolvem a área, causando danos leves e enfraquecendo a moral dos inimigos.",
                    "Trevas",
                    2,
                    5,
                    5,
                    10,
                    3
                ),
                (
                    "Poço Profano",
                    "Cria um vórtice de trevas que atrai e danifica todos os inimigos que se aproximam, drenando sua energia vital.",
                    "Trevas",
                    4,
                    10,
                    8,
                    20,
                    5
                ),
                (
                    "Aura Maldita",
                    "Propaga uma aura de maldição que causa danos contínuos e reduz a eficácia das habilidades dos inimigos na área.",
                    "Trevas",
                    6,
                    15,
                    12,
                    25,
                    6
                ),
                (
                    "Tormenta Sombria",
                    "Desencadeia uma tempestade de trevas que atinge múltiplos inimigos, causando danos intensos e drenando sua energia arcana.",
                    "Trevas",
                    8,
                    20,
                    16,
                    35,
                    7
                ),
                (
                    "Abismo Final",
                    "Invoca um abismo de trevas que consome tudo ao seu redor, causando danos devastadores e eliminando inimigos em grande número.",
                    "Trevas",
                    10,
                    25,
                    20,
                    50,
                    10
                ),
            ]

            db.cur.executemany(
                """
                SELECT criar_feitico_dano_area(%s, %s, %s, %s::INT, %s::INT, %s::INT, %s::INT, %s::INT)
                """,
                default_values
            )
    ```

### Poção
??? "DML poção"
    ```python
            values = [
                ("Elixir da Vida", 4, "Cura Pequena", 1, 50), 
                ("Mana Líquida", 5, "Recuperação Arcana", 1, 75),
                ("Poção da Força Titânica", 4, "Aumento de Força", 2, 100),
                ("Poção do Vento Celeste", 3, "Velocidade Extra", 1, 90),
                ("Poção da Pele de Pedra", 5, "Defesa Temporária", 2, 120),
                ("Lágrima do Dragão", 6, "Regeneração Poderosa", 2, 200),
                ("Sangue do Fênix", 9, "Ressurreição", 3, 500),
                ("Poção do Tempo Congelado", 10, "Paralisação Temporal", 3, 350),
                ("Elixir da Perdição", 10, "Dano Sombrio", 5, 180),
                ("Néctar do Destino", 14, "Sorte Abençoada", 4, 150)
            ]
            for (name, p_drop_inimigos_media, description, weight, price) in values:
                db.cur.execute(
                    f"""
                    SELECT criar_pocao (
                        '{description}',
                        {p_drop_inimigos_media},
                        '{name}',
                        {weight},
                        {price}
                    );
                    """
                )

    ```

### Inimigo
??? "DML inimigo"
    ```python
            enemies = [
                ("🐭", "Rato Selvagem", "Um pequeno roedor agressivo que se alimenta de restos do vilarejo.", "Terra", 20, 5, 2, 0, 0, 1),
                ("🕴️", "Ladrão de Rua", "Um criminoso que tenta roubar viajantes desavisados.", "Trevas", 30, 10, 5, 0, 0, 3),
                ("🐦", "Corvo Guardião", "Um pássaro grande e territorial que protege os arredores da praça.", "Ar", 25, 8, 3, 0, 0, 2),
                ("🐺", "Lobo Sombrio", "Uma criatura ágil que caça à noite na floresta.", "Trevas", 50, 20, 10, 0, 0, 4),
                ("✨", "Espírito da Clareira", "Um espírito pacífico que pode se tornar hostil se perturbado.", "Luz", 40, 15, 0, 10, 20, 5),
                ("🌳", "Ent Ancião", "Uma árvore viva que protege os segredos da floresta.", "Terra", 70, 25, 15, 5, 10, 3),
                ("🗿", "Guardião de Pedra", "Um golem que defende as ruínas de intrusos.", "Terra", 80, 30, 20, 0, 0, 2),
                ("🐍", "Serpente das Sombras", "Uma serpente que se camufla nas ruínas escuras.", "Trevas", 60, 25, 10, 5, 10, 4),
                ("👻", "Espectro do Abismo", "Um fantasma que assombra os corredores das ruínas.", "Trevas", 50, 20, 5, 20, 30, 8),
                ("🦂", "Escorpião Gigante", "Um escorpião imenso, armado com uma cauda venenosa.", "Terra", 90, 35, 15, 0, 0, 3),
                ("🧞", "Djin Traiçoeiro", "Um espírito do deserto que tenta enganar os viajantes.", "Fogo", 60, 30, 20, 15, 40, 10),
                ("🧳", "Caravaneiro Corrompido", "Um comerciante que se tornou hostil após perder tudo.", "Luz", 70, 30, 25, 5, 10, 6),
                ("💎", "Golem de Cristal", "Um golem criado a partir de cristais brilhantes, resistente e difícil de derrotar.", "Terra", 150, 70, 30, 5, 10, 3),
                ("⛏️", "Minerador Fantasma", "O espírito de um minerador que morreu na caverna, ainda vagando em busca de tesouros.", "Trevas", 80, 50, 20, 15, 30, 6),
                ("🍀", "Afortunado", "Uma entidade mágica que protege os cristais mais valiosos da caverna.", "Luz", 100, 60, 40, 20, 40, 10),
                ("❄️", "Gigante Congelado", "Um gigante que protege os picos nevados.", "Água", 120, 50, 30, 5, 15, 5),
                ("🦅", "Águia do Crepúsculo", "Um pássaro imenso que domina os céus da montanha.", "Ar", 80, 40, 20, 10, 25, 7),
                ("❄️👻", "Espírito da Geada", "Um ser mágico que controla o gelo da montanha.", "Água", 70, 35, 10, 20, 50, 9),
                ("💀⚔️", "Guerreiro Esqueleto", "Um esqueleto animado pela magia negra, armado com espadas enferrujadas.", "Trevas", 70, 35, 15, 5, 0, 3),
                ("💀🧙", "Feiticeiro Esqueleto", "Um mago esqueleto que usa feitiços antigos para proteger os segredos da caverna.", "Trevas", 60, 40, 10, 25, 50, 12),
                ("🧟", "Goblin Zumbi", "Um goblin reanimado, movido por uma força sombria.", "Trevas", 50, 20, 5, 0, 0, 2),
                ("⚔️😈", "Guerreiro Corrompido", "Um antigo herói que foi consumido pelo mal.", "Trevas", 100, 60, 50, 10, 20, 7),
                ("🔥🐾", "Fera Flamejante", "Uma criatura ardente que espalha destruição.", "Fogo", 110, 55, 40, 15, 30, 8),
                ("🐉", "Dragão da Devastação", "Um dragão imenso, a maior ameaça das terras devastadas.", "Trevas", 200, 100, 100, 50, 100, 20),
                ("🧙‍♀️🔥", "Abgail", "Entidade de uma grande maga que pagou o preço por conhecer todas as verdades.", "Fogo", 150, 60, 75, 100, 100, 12),
                ("🌟", "Lumina", "Lumina é uma figura radiante, simbolizando a pureza e o poder da luz. Sua presença ilumina até as sombras mais profundas, e ela tem a capacidade de curar aliados ou desintegrar inimigos com feitos de luz concentrados.", "Luz", 180, 75, 90, 120, 90, 15),
                ("💀🔥", "Necromante", "O Necromante é um mestre das artes negras, comandando os mortos e manipulando as trevas para enfraquecer seus inimigos.", "Trevas", 200, 85, 100, 110, 120, 14),
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
    ```

## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 13/01/2024 | Criação   | Grupo |
| `1.1`  | 13/01/2024 | Atualização | Grupo |
| `1.2`  | 03/02/2025 | Atualização entrega 3 | Grupo |