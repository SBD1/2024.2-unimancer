from database import Database
from utils import debug, error
from colorama import Style

def effects(db: Database):
    table_name = Style.BRIGHT + "EFEITO" + Style.NORMAL
    try:
        default = [
            # Botas
            ("Passos Silenciosos", "Reduz o ruído ao caminhar, aumentando a chance de evitar combates.", 1.1, 1.0, 1.0, 1.0, 1.0, 1.1, 1.0, 1.0),  # Botas de couro
            ("Proteção Dracônica", "Concede resistência moderada a ataques físicos.", 1.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.0),  # Botas de dragão
            ("Agilidade das Marés", "Aumenta a velocidade em terrenos aquáticos.", 1.0, 1.1, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0),  # Botas de água
            ("Sombras Protetoras", "Diminui a chance de ser detectado por inimigos.", 1.2, 1.0, 1.1, 1.0, 1.0, 1.2, 1.0, 1.0),  # Botas do crepúsculo
            ("Caminhos Luminosos", "Aumenta a regeneração de energia arcana ao caminhar.", 1.0, 1.0, 1.25, 1.0, 1.3, 1.0, 1.1, 1.0),  # Botas de cristal
            ("Congelamento Ártico", "Reduz o dano recebido de ataques de fogo.", 1.3, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0, 1.0),  # Botas de gelo
            ("Raízes da Vida", "Aumenta a recuperação de vida em terrenos florestais.", 1.1, 1.2, 1.0, 1.3, 1.0, 1.0, 1.1, 1.0),  # Botas de madeira
            ("Passos Trovejantes", "Causa dano em área ao pular em combate.", 1.0, 1.0, 1.2, 1.0, 1.0, 1.0, 1.0, 1.1),  # Botas do trovão
            ("Força Óssea", "Aumenta a resistência física e o dano crítico.", 1.4, 1.0, 1.2, 1.0, 1.0, 1.0, 1.0, 1.0),  # Botas de ossos
            ("Presença Real", "Concede bônus em todas as batalhas e aumenta o ganho de XP.", 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.5, 1.0),  # Botas da Realeza
            # Bracelete
            ("Resiliência Modesta", "Aumenta ligeiramente a resistência física do usuário.", 1.2, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0, 1.0),  # Bracelete de bronze
            ("Força Ossificada", "Melhora a resistência física e aumenta o dano crítico.", 1.4, 1.0, 1.2, 1.0, 1.0, 1.0, 1.0, 1.0),  # Bracelete de ossos
            ("Vitalidade Verdejante", "Recupera gradualmente a vida ao longo do tempo.", 1.0, 1.0, 1.0, 1.3, 1.0, 1.0, 1.0, 1.0),  # Bracelete de grama
            ("Fúria Arcana", "Amplifica o dano de feitiços destrutivos temporariamente.", 1.0, 1.0, 1.4, 1.0, 1.3, 1.0, 1.0, 1.0),  # Bracelete de Plasma Arcano
            ("Reflexo Etéreo", "Concede resistência a ataques mágicos.", 1.2, 1.1, 1.0, 1.0, 1.3, 1.0, 1.0, 1.0),  # Bracelete de Cristal Etéreo
            ("Firmeza Primeva", "Aumenta significativamente a defesa contra ataques físicos.", 1.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),  # Bracelete da Rocha Primeva
            #Fivela
            ("Resiliência Simples", "Concede uma pequena melhoria na defesa física.", 1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),  # Fivela de bronze
            ("Runas Destrutivas", "Amplifica o dano de magias ofensivas temporariamente.", 1.0, 1.3, 1.4, 1.0, 1.2, 1.0, 1.0, 1.0),  # Fivela Rúnica
            ("Energia Maldita", "Aumenta o crítico e reduz ligeiramente a defesa do usuário.", 1.1, 1.0, 1.6, 1.0, 1.3, 1.0, 1.0, 1.0),  # Fivela Obscura
            ("Luz Astral", "Melhora as habilidades de cura e concede resistência a magia.", 1.1, 1.2, 1.0, 1.3, 1.0, 1.0, 1.0, 1.0),  # Fivela Celestial
            ("Graça do Vento", "Concede maior agilidade e chance de esquiva.", 1.0, 1.0, 1.0, 1.0, 1.0, 1.4, 1.0, 1.0),  # Fivela da Ventania
            ("Proteção Glacial", "Aumenta a defesa física e mágica, protegendo contra o frio.", 1.5, 1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),  # Fivela do Gelo Inquebrável
            #Bengala
            ('Resistência Natural', 'Aumenta a resistência contra ataques físicos leves.', 1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.0), # Bengala de Madeira Rústica
            ('Cura do Bosque', 'Concede um pequeno aumento na regeneração de vida.', 1.1, 1.0, 1.0, 1.2, 1.0, 1.0, 1.0, 1.0), # Bengala de Galho Seco
            ('Passos Ágeis', 'Aumenta ligeiramente a agilidade e a velocidade de movimento.', 1.0, 1.1, 1.0, 1.0, 1.0, 1.1, 1.0, 1.0), # Bengala de Bambteu
            ('Sábia Defesa', 'Aumenta a inteligência e a resistência mágica.', 1.0, 1.3, 1.0, 1.0, 1.2, 1.0, 1.0, 1.1), # Bengala de Carvalho Encantado
            ('Defesa Implacável', 'Aumenta significativamente a resistência física e a defesa mágica.', 1.4, 1.2, 1.0, 1.1, 1.0, 1.0, 1.0, 1.0), # Bengala de Madeira Petrificada
            ('Aço Místico', 'Aumenta a chance de crítico e melhora a defesa contra ataques mágicos.', 1.3, 1.2, 1.5, 1.0, 1.1, 1.0, 1.0, 1.0), # Bengala de Prata Mística
            ('Poder Arcano', 'Amplifica o poder de feitiços mágicos e aumenta a regeneração de energia arcana.', 1.0, 1.4, 1.0, 1.0, 1.3, 1.0, 1.0, 1.1), # Bengala de Cristal Arcano
            ('Força Dracônica', 'Aumenta a resistência física e o dano crítico, além de melhorar a regeneração de vida.', 1.5, 1.0, 1.6, 1.2, 1.0, 1.0, 1.0, 1.2), # Bengala de Ossos Dracônicos
            # Manto
            ('Proteção Básica', 'Aumenta a resistência contra ataques leves.', 1.2, 1.0, 1.0, 1.0, 1.0, 1.1, 1.0, 1.0), # Manto de Lona Simples
            ('Conforto Leve', 'Aumenta ligeiramente a agilidade e a regeneração de vida.', 1.0, 1.1, 1.0, 1.2, 1.0, 1.0, 1.0, 1.0), # Manto de Algodão Básico
            ('Calor Rústico', 'Aumenta a defesa contra frio e a resistência física.', 1.3, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0, 1.0), # Manto de Lã Rústica
            ('Resistência Ártica', 'Reduz o dano de ataques baseados em gelo e aumenta a resistência mágica.', 1.2, 1.2, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0), # Manto de Neve Encantado
            ('Fúria Selvagem', 'Aumenta a vida e concede bônus de resistência física em terrenos florestais.', 1.4, 1.0, 1.0, 1.3, 1.0, 1.0, 1.0, 1.0), # Manto de Pele de Urso
            ('Elegância Ardente', 'Amplifica o dano de magias de fogo e concede resistência contra queimaduras.', 1.3, 1.4, 1.0, 1.0, 1.2, 1.0, 1.0, 1.0), # Manto de Seda Flamejante
            ('Sombras Celestiais', 'Aumenta a resistência mágica e a sorte do portador.', 1.2, 1.3, 1.0, 1.0, 1.0, 1.3, 1.0, 1.0), # Manto Celestial das Sombras
            ('Renascimento Ardente', 'Recupera vida ao longo do tempo e aumenta o dano crítico.', 1.3, 1.0, 1.5, 1.2, 1.0, 1.0, 1.0, 1.0), # Manto da Fênix Ardente
            ('Fúria Tempestuosa', 'Amplifica o dano de feitiços elétricos e aumenta a chance de crítico.', 1.4, 1.5, 1.6, 1.0, 1.0, 1.0, 1.0, 1.0), # Manto do Vórtice Tempestuoso
            # Colar
            ('Durabilidade Básica', 'Aumenta ligeiramente a resistência física.', 1.1, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0, 1.0), # Colar de Bronze
            ('Sabedoria Inicial', 'Aumenta a inteligência mágica para aprendizes.', 1.0, 1.2, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0), # Colar de Prata
            ('Chama Potencial', 'Amplifica feitiços de fogo e aumenta dano crítico.', 1.0, 1.4, 1.3, 1.0, 1.0, 1.0, 1.0, 1.0), # Colar da Combustão Arcana
            ('Ventos Ágeis', 'Aumenta a agilidade e o poder de magias de vento.', 1.0, 1.3, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0), # Colar da Brisa Mística
            ('Gelo Eterno', 'Concede resistência ao calor e aumenta a defesa mágica.', 1.3, 1.2, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0), # Colar do Gelo Supremo
            ('Regeneração Vital', 'Auxilia na regeneração de vida e energia.', 1.2, 1.0, 1.0, 1.3, 1.2, 1.0, 1.0, 1.0), # Colar do Vigor Florestal
            ('Luz Brilhante', 'Amplifica feitiços de luz e aumenta a sorte.', 1.0, 1.5, 1.0, 1.0, 1.2, 1.3, 1.0, 1.0), # Colar do Prisma Radiante
            ('Proteção Espiritual', 'Reduz o dano mágico e concede bônus defensivo.', 1.4, 1.3, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0), # Colar do Eco Ancestral
            ('Energia Trovejante', 'Amplifica habilidades elétricas e aumenta crítico.', 1.0, 1.4, 1.5, 1.0, 1.2, 1.0, 1.0, 1.0), # Colar do Raio Furioso
            ('Força Sombria', 'Canaliza poder sombrio e aumenta resistência mágica.', 1.3, 1.4, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0), # Colar do Eclipse Noturno
            ('Agilidade Aquática', 'Aumenta a velocidade e dano de ataques aquáticos.', 1.0, 1.3, 1.2, 1.0, 1.2, 1.0, 1.0, 1.0), # Colar da Maré Mística
            ('Sacrifício Carmesim', 'Converte vida em aumento extremo de poder.', 1.0, 1.6, 1.4, 1.3, 1.5, 1.0, 1.0, 1.0), # Colar Carmesim Profano
            ('Lâminas Invisíveis', 'Aumenta o dano de ataques cortantes e agilidade.', 1.0, 1.2, 1.3, 1.0, 1.0, 1.1, 1.0, 1.0), # Anel de Vento
            ('Poder Régio', 'Aumenta drasticamente o poder mágico e crítico.', 1.3, 1.6, 1.5, 1.0, 1.2, 1.0, 1.0, 1.0), # Anel da Realeza
            # Luvas
            ('Resistência Aquática', 'Protege contra feitiços e magias aquáticas.', 1.1, 1.2, 1.05, 1.0, 1.15, 1.0, 1.0, 1.0),
            ('Amplificação Ígnea', 'Aumenta o poder de feitiços de fogo.', 1.05, 1.3, 1.1, 1.0, 1.25, 1.0, 1.0, 1.0),
            ('Precisão do Vento', 'Aumenta a precisão de ataques de longo alcance.', 1.05, 1.15, 1.2, 1.0, 1.0, 1.05, 1.0, 1.0),
            ('Proteção Sombria', 'Reduz o dano recebido de magias sombrias.', 1.3, 1.1, 1.0, 1.0, 1.15, 1.0, 1.0, 1.0),
            ('Purificação Radiante', 'Cura venenos automaticamente após 2 turnos.', 1.2, 1.2, 1.0, 1.1, 1.1, 1.05, 1.0, 1.0),
            ('Absorção de Marés', 'Absorve parte do dano de magias aquáticas.', 1.25, 1.1, 1.0, 1.0, 1.2, 1.0, 1.0, 1.0),
            ('Intimidação Profana', 'Reduz a chance de acerto dos inimigos.', 1.15, 1.15, 1.05, 1.0, 1.0, 1.05, 1.0, 1.0),
            ('Velocidade Predatória', 'Aumenta a velocidade e esquiva em combate.', 1.2, 1.05, 1.15, 1.0, 1.0, 1.1, 1.0, 1.0),
            ('Resistência Gélida', 'Concede resistência ao frio extremo.', 1.3, 1.05, 1.0, 1.0, 1.15, 1.0, 1.0, 1.0),
            ('Tempestade Energizada', 'Amplifica o dano de ataques elétricos.', 1.05, 1.25, 1.2, 1.0, 1.3, 1.0, 1.0, 1.0),
            # Chapeu
            ('Revelação Arcana', 'Aumenta a capacidade de desvendar segredos ocultos.', 1.1, 1.3, 1.05, 1.0, 1.2, 1.05, 1.0, 1.0),
            ('Aura Amaldiçoada', 'Diminui a confiança dos inimigos, gerando incertezas.', 1.15, 1.2, 1.1, 1.0, 1.15, 1.05, 1.0, 1.0),
            ('Sombras Nutridoras', 'Amplifica o poder de feitiços destrutivos.', 1.2, 1.25, 1.15, 1.0, 1.3, 1.0, 1.0, 1.0),
            ('Poder Dracônico', 'Aumenta a força e resistência contra ataques de dragões.', 1.3, 1.2, 1.15, 1.1, 1.2, 1.05, 1.0, 1.0),
            ('Sopro Gélido', 'Reduz a velocidade dos inimigos, causando desconforto.', 1.2, 1.15, 1.05, 1.0, 1.2, 1.05, 1.0, 1.0),
            ('Energia Nefasta', 'Aumenta a regeneração de mana e poder em ambientes sombrios.', 1.15, 1.3, 1.1, 1.0, 1.3, 1.05, 1.0, 1.0),
            ('Luz Purificadora', 'Remove efeitos negativos e reduz o dano recebido de magias.', 1.25, 1.15, 1.05, 1.1, 1.2, 1.0, 1.0, 1.0),
            ('Chamas Ardentes', 'Amplifica o dano de ataques de fogo.', 1.15, 1.25, 1.2, 1.0, 1.3, 1.05, 1.0, 1.0),
            ('Energia Trovejante', 'Aumenta a velocidade de ataque e precisão.', 1.15, 1.2, 1.15, 1.0, 1.3, 1.05, 1.0, 1.0),
            ('Coragem Inabalável', 'Concede resistência extra contra ataques críticos.', 1.3, 1.2, 1.1, 1.15, 1.2, 1.05, 1.0, 1.0),
            ('Ilusão Arcana', 'Confunde os inimigos, reduzindo sua precisão.', 1.2, 1.25, 1.1, 1.0, 1.15, 1.05, 1.0, 1.0),
            ('Ecos Ancestrais', 'Concede bônus de resistência e regeneração.', 1.3, 1.2, 1.1, 1.15, 1.2, 1.05, 1.0, 1.0),
            # Calca
            ('Proteção Rústica', 'Concede leve proteção com couro resistente.', 1.02, 1.05, 1.0, 1.1, 1.0, 1.05, 1.0, 1.0),
            ('Força Dracônica', 'Oferece resistência e poder do couro de dragão.', 1.04, 1.08, 1.02, 1.15, 1.0, 1.1, 1.0, 1.0),
            ('Sombras Forjadas', 'Amplifica a resistência com energias das trevas.', 1.06, 1.1, 1.03, 1.2, 1.0, 1.15, 1.0, 1.0),
            ('Cristal Arcano', 'Concede bônus de magia com proteção cristalina.', 1.06, 1.12, 1.04, 1.25, 1.0, 1.2, 1.0, 1.0),
            ('Vigor da Madeira', 'Fornece resistência com a vitalidade da madeira viva.', 1.03, 1.06, 1.02, 1.15, 1.0, 1.1, 1.0, 1.0),
            ('Trovão Potente', 'Aumenta o poder com a força do trovão.', 1.15, 1.2, 1.03, 1.3, 1.0, 1.25, 1.0, 1.0),
            ('Resiliência Óssea', 'Amplifica resistência com ossos de dragão.', 1.2, 1.25, 1.06, 1.35, 1.0, 1.3, 1.0, 1.0),
            ('Glória Real', 'Fornece bônus para magos experientes.', 1.230, 1.3, 1.05, 1.4, 1.0, 1.35, 1.0, 1.0),
            ('Energia Tempestuosa', 'Concede agilidade e força com o poder das tempestades.', 1.25, 1.4, 1.04, 1.45, 1.0, 1.4, 1.0, 1.0),
            ('Instinto Animal', 'Aumenta o vigor com peles mágicas.', 1.3, 1.35, 1.05, 1.5, 1.0, 1.45, 1.0, 1.0),
            ('Tecido Encantado', 'Fornece proteção mágica leve.', 1.32, 1.4, 1.03, 1.55, 1.0, 1.5, 1.0, 1.0),
            ('Elegância Arcana', 'Amplifica poder mágico com seda mágica.', 1.33, 1.45, 1.03, 1.6, 1.0, 1.55, 1.0, 1.0),
            ('Força Gigantesca', 'Concede enorme resistência com ossos de gigante.', 1.34, 1.5, 1.06, 1.65, 1.0, 1.6, 1.0, 1.0),
            ('Maciez Encantada', 'Oferece conforto e proteção mágica.', 1.36, 1.55, 1.04, 1.7, 1.0, 1.65, 1.0, 1.0),
            ('Escamas de Serpente', 'Aumenta a resistência com escamas místicas.', 1.35, 1.6, 1.05, 1.75, 1.0, 1.7, 1.0, 1.0),
            # Meia
            ('Conforto Simples', 'Concede leve proteção com pano comum.', 1.02, 1.03, 1.0, 1.05, 1.0, 1.01, 1.0, 1.0),
            ('Aconchego Natural', 'Fornece calor e proteção com lã de ovelha.', 1.04, 1.05, 1.0, 1.1, 1.0, 1.02, 1.0, 1.0),
            ('Toque Celestial', 'Amplifica habilidades mágicas com seda mágica.', 1.1, 1.15, 1.02, 1.2, 1.0, 1.1, 1.0, 1.0),
            ('Maciez Encantada', 'Oferece bônus mágico com algodão encantado.', 1.11, 1.16, 1.02, 1.22, 1.0, 1.12, 1.0, 1.0),
            ('Esplendor Dourado', 'Aumenta resistência com fios de ouro.', 1.12, 1.18, 1.02, 1.24, 1.0, 1.13, 1.0, 1.0),
            ('Vitalidade Raiz', 'Fornece resistência e energia com raízes mágicas.', 1.13, 1.2, 1.02, 1.26, 1.0, 1.15, 1.0, 1.0),
            ('Sussurros Sombrios', 'Amplifica poder mágico com magia sombria.', 1.15, 1.25, 1.03, 1.3, 1.0, 1.2, 1.0, 1.0),
            # Anel
            ('Brilho Simples', 'Concede leve proteção com um anel de bronze.', 1.05, 1.02, 1.0, 1.1, 1.0, 1.01, 1.0, 1.0),
            ('Aura de Prata', 'Aumenta habilidades mágicas para iniciantes.', 1.2, 1.05, 1.0, 1.14, 1.0, 1.02, 1.0, 1.0),
            ('Resplendor Áureo', 'Oferece grande poder para magos experientes.', 1.23, 1.15, 1.05, 1.3, 1.0, 1.12, 1.0, 1.0),
            ('Encanto Arcano', 'Amplifica magia com propriedades místicas.', 1.37, 1.2, 1.05, 1.5, 1.0, 1.23, 1.0, 1.0),
            ('Maldição Sombria', 'Aumenta poder sombrio, mas é perigoso.', 1.37, 1.3, 1.15, 1.21, 1.0, 1.21, 1.0, 1.0),
            ('Diamante Místico', 'Concede poder incomparável para magos.', 1.51, 1.4, 1.1, 1.5, 1.0, 1.5, 1.0, 1.0),
            ('Força Negra', 'Oferece poder com matéria sombria.', 1.16, 1.1, 1.03, 1.25, 1.0, 1.05, 1.0, 1.0),
            ('Harmonia Natural', 'Fornece equilíbrio com grama mística.', 1.07, 1.03, 1.01, 1.18, 1.0, 1.018, 1.0, 1.0),
            ('Gelo Eterno', 'Amplifica resistência com gelo inquebrável.', 1.4, 1.2, 1.04, 1.5, 1.0, 1.11, 1.0, 1.0),
            ('Emanar Arcano', 'Fortalece energia com fulgor mágico.', 1.28, 1.15, 1.02, 1.4, 1.0, 1.08, 1.0, 1.0),
            ('Espiral Espiritual', 'Atrai espíritos com poder espectral.', 1.33, 1.25, 1.06, 1.45, 1.0, 1.15, 1.0, 1.0),
            ('Lâmina Invisível', 'Proporciona ataques cortantes com vento.', 1.2, 1.1, 1.01, 1.3, 1.0, 1.065, 1.0, 1.0),
        ]

        for (name, description, intelligence, life, arcana, *_) in default:
            db.cur.execute(
                f"""
                INSERT INTO efeito (nome, descricao, inteligencia, vida, energia_arcana)
                VALUES ('{name}', '{description}', {intelligence}, {life}, {arcana});
                """
            )
        db.conn.commit()

        debug(f"default: {len(default)} {table_name} added successfully!")
        return len(default)
    
    except Exception as e:
        db.conn.rollback()
        error(f"Erro ao adicionar valores na tabela {table_name}: {e}")
