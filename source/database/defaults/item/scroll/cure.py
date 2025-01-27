from database import Database
from utils import debug, error
from colorama import Style

def cure_spells(db: Database):
    
    table_name = Style.BRIGHT + "FEITICO_CURA" + Style.NORMAL

    try:
        default_values = [
            # Água
            (
                "Cura Áquatica: Canaliza a energia das águas para restaurar a vida de aliados dentro da área de efeito.",
                "Água",
                3,
                8,
                10,
                25 
            ),
            (
                "Manto Revitalizante: Envolve os aliados com um manto de água curativa, regenerando sua vida e energia arcana ao longo do tempo.",
                "Água",
                6,
                15,
                20,
                40 
            ),

            # Fogo
            (
                "Flama Curativa: Utiliza o calor das chamas para aquecer e curar ferimentos de aliados próximos.",
                "Fogo",
                3,
                8,
                10,
                25 
            ),
            (
                "Fogo Vigoroso: Invoca chamas benéficas que envolvem os aliados, restaurando sua vida e aumentando sua resistência arcana.",
                "Fogo",
                6,
                15,
                20,
                40 
            ),

            # Terra
            (
                "Regeneração Terrena: Conecta-se com a energia da terra para regenerar a vida dos aliados na área afetada.",
                "Terra",
                3,
                8,
                10,
                25 
            ),
            (
                "Escudo Vital: Forma um escudo de terra que protege e cura os aliados, absorvendo danos e restaurando sua vitalidade.",
                "Terra",
                6,
                15,
                20,
                40 
            ),

            # Ar
            (
                "Brisa Curativa: Convoca uma brisa suave que revitaliza e cura os aliados dentro de sua trajetória.",
                "Ar",
                3,
                8,
                10,
                25 
            ),
            (
                "Vórtice Revigorante: Cria um vórtice de ar que circunda os aliados, restaurando sua vida e energias arcanas continuamente.",
                "Ar",
                6,
                15,
                20,
                40 
            ),

            # Luz
            (
                "Luz Restauradora: Emite uma luz pura que cura ferimentos e restaura a energia arcana dos aliados na área iluminada.",
                "Luz",
                3,
                8,
                10,
                25 
            ),
            (
                "Aura Divina: Envolve os aliados com uma aura de luz celestial, proporcionando cura contínua e proteção contra energias negativas.",
                "Luz",
                6,
                15,
                20,
                40 
            ),

            # Trevas
            (
                "Sombra Curativa: Manipula as sombras para curar os aliados, ocultando-os enquanto restaura sua vitalidade.",
                "Trevas",
                3,
                8,
                10,
                25 
            ),
            (
                "Véu das Trevas: Cria um véu sombrio que não apenas protege os aliados, mas também cura suas feridas e renova sua energia arcana.",
                "Trevas",
                6,
                15,
                20,
                40 
            ),
        ]

        db.cur.executemany(
            """
            SELECT criar_feitico_cura(%s, %s, %s, %s, %s, %s)
            """,
            default_values
        )
        db.conn.commit()
        debug(f"default: {len(default_values)} {table_name} added successfully!")
        
        return len(default_values)
    
    except Exception as e:
        db.conn.rollback()
        error(f"default: error occurred while adding {table_name}s values:\n{e}")