from database import Database
from utils import debug, error
from colorama import Style

def scrolls(db: Database):
    table_name = Style.BRIGHT + "PERGAMINHO" + Style.NORMAL
    try:
        default_values = [
            (
                "Pergaminho dos Elementos Unidos: Contém feitiços de múltiplos elementos, permitindo combinações poderosas.",
                25,  # chance_drop
                "Elementos Unidos",
                2,    # peso
                300,  # preco
                "Arco-íris"  # cor
            ),
            (
                "Pergaminho da Harmonia Arcana: Facilita a execução de feitiços de diferentes escolas de magia simultaneamente.",
                20,
                "Harmonia Arcana",
                3,
                250,
                "Prata"
            ),
            (
                "Pergaminho dos Encantos Mistos: Permite a combinação de feitiços de ataque e cura em um único lançamento.",
                15,
                "Encantos Mistos",
                2,
                220,
                "Dourado"
            ),
            (
                "Pergaminho da Versatilidade Mágica: Amplia a variedade de feitiços que o usuário pode lançar a partir de um único pergaminho.",
                10,
                "Versatilidade Mágica",
                2,
                200,
                "Bronze"
            ),

            (
                "Pergaminho da Convergência Elemental: Une forças de diferentes elementos para criar efeitos únicos e devastadores.",
                25,
                "Convergência Elemental",
                2,
                300,
                "Índigo"
            ),
            (
                "Pergaminho da Sinergia Arcana: Aumenta a eficácia quando múltiplos feitiços são lançados em rápida sucessão.",
                20,
                "Sinergia Arcana",
                3,
                250,
                "Turquesa"
            ),
            (
                "Pergaminho dos Feitiços Múltiplos: Guarda uma seleção variada de feitiços, permitindo escolha dinâmica durante o combate.",
                15,
                "Feitiços Múltiplos",
                2,
                220,
                "Magenta"
            ),
            (
                "Pergaminho da Dualidade Mágica: Permite ao usuário alternar entre dois feitiços diferentes instantaneamente.",
                10,
                "Dualidade Mágica",
                2,
                200,
                "Esmeralda"
            ),

            (
                "Pergaminho do Poder Compartilhado: Divida o poder mágico entre vários feitiços para maximizar o impacto.",
                25,
                "Poder Compartilhado",
                2,
                300,
                "Bronze"
            ),
            (
                "Pergaminho da Amplificação Mágica: Potencializa os feitiços lançados a partir deste pergaminho, aumentando seu alcance e dano.",
                20,
                "Amplificação Mágica",
                3,
                250,
                "Prata"
            ),
            (
                "Pergaminho da Adaptação Arcana: Ajusta automaticamente os feitiços conforme a situação, proporcionando flexibilidade ao usuário.",
                15,
                "Adaptação Arcana",
                2,
                220,
                "Bronze"
            ),
            (
                "Pergaminho das Energias Combinadas: Combina diferentes fontes de energia mágica para criar efeitos únicos e incomuns.",
                10,
                "Energias Combinadas",
                2,
                200,
                "Dourado"
            ),

            (
                "Pergaminho da Resiliência Mágica: Aumenta a resistência contra magias adversárias enquanto utiliza feitiços do pergaminho.",
                25,
                "Resiliência Mágica",
                2,
                300,
                "Púrpura"
            ),
            (
                "Pergaminho do Fluxo Mágico: Melhora a eficiência do uso de energia arcana durante a execução de múltiplos feitiços.",
                20,
                "Fluxo Mágico",
                3,
                250,
                "Ciano"
            ),
            (
                "Pergaminho da Estabilidade Arcana: Garante a estabilidade dos feitiços lançados, reduzindo falhas e efeitos colaterais.",
                15,
                "Estabilidade Arcana",
                2,
                220,
                "Púrpura"
            ),
            (
                "Pergaminho da Manipulação Mágica: Permite ao usuário controlar e direcionar feitiços com maior precisão e deliberadamente.",
                10,
                "Manipulação Mágica",
                2,
                200,
                "Esmeralda"
            ),

            (
                "Pergaminho da Expansão de Feitiços: Aumenta a área de efeito dos feitiços lançados através deste pergaminho.",
                25,
                "Expansão de Feitiços",
                2,
                300,
                "Ciano"
            ),
            (
                "Pergaminho da Intensificação: Multiplica a intensidade dos feitiços, tornando-os mais potentes e duradouros.",
                20,
                "Intensificação",
                3,
                250,
                "Dourado"
            ),
            (
                "Pergaminho da Diversificação: Introduz variedade nos feitiços, permitindo o uso de diferentes tipos em situações variadas.",
                15,
                "Diversificação",
                2,
                220,
                "Ruby"
            ),
            (
                "Pergaminho da Conjuração Mista: Facilita a conjuração simultânea de feitiços de diferentes categorias, como ataque e defesa.",
                10,
                "Conjuração Mista",
                2,
                200,
                "Prata"
            ),
        ]

        db.cur.executemany(
            """
            SELECT criar_pergaminho(%s, %s::INT, %s, %s::INT, %s::INT, %s)
            """,
            default_values
        )
        db.conn.commit()
        debug(f"default: {len(default_values)} {table_name} added successfully!")
        
        return len(default_values)
    
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values:\n{e}")