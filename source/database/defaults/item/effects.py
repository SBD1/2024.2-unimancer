from database import Database
from utils import debug, error
from colorama import Style

def effects(db: Database):
    table_name = Style.BRIGHT + "EFEITO" + Style.NORMAL
    try:
        default = [
            # Botas
            ("Passos Silenciosos", "Reduz o ruído ao caminhar, aumentando a chance de evitar combates.", 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0),  # Botas de couro
            ("Proteção Dracônica", "Concede resistência moderada a ataques físicos.", 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0),  # Botas de dragão
            ("Agilidade das Marés", "Aumenta a velocidade em terrenos aquáticos.", 0.0, 0.1, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0),  # Botas de água
            ("Sombras Protetoras", "Diminui a chance de ser detectado por inimigos.", 0.2, 0.0, 0.1, 0.0, 0.0, 0.2, 0.0, 0.0),  # Botas do crepúsculo
            ("Caminhos Luminosos", "Aumenta a regeneração de energia arcana ao caminhar.", 0.0, 0.0, 0.0, 0.0, 0.3, 0.0, 0.1, 0.0),  # Botas de cristal
            ("Congelamento Ártico", "Reduz o dano recebido de ataques de fogo.", 0.3, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0),  # Botas de gelo
            ("Raízes da Vida", "Aumenta a recuperação de vida em terrenos florestais.", 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.1, 0.0),  # Botas de madeira
            ("Passos Trovejantes", "Causa dano em área ao pular em combate.", 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.1),  # Botas do trovão
            ("Força Óssea", "Aumenta a resistência física e o dano crítico.", 0.4, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0),  # Botas de ossos
            ("Presença Real", "Concede bônus em todas as batalhas e aumenta o ganho de XP.", 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.5, 0.0),  # Botas da Realeza
            # Bracelete
            ("Resiliência Modesta", "Aumenta ligeiramente a resistência física do usuário.", 0.2, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0),  # Bracelete de bronze
            ("Força Ossificada", "Melhora a resistência física e aumenta o dano crítico.", 0.4, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0),  # Bracelete de ossos
            ("Vitalidade Verdejante", "Recupera gradualmente a vida ao longo do tempo.", 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.0),  # Bracelete de grama
            ("Fúria Arcana", "Amplifica o dano de feitiços destrutivos temporariamente.", 0.0, 0.0, 0.4, 0.0, 0.3, 0.0, 0.0, 0.0),  # Bracelete de Plasma Arcano
            ("Reflexo Etéreo", "Concede resistência a ataques mágicos.", 0.2, 0.1, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0),  # Bracelete de Cristal Etéreo
            ("Firmeza Primeva", "Aumenta significativamente a defesa contra ataques físicos.", 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),  # Bracelete da Rocha Primeva
            #Fivela
            ("Resiliência Simples", "Concede uma pequena melhoria na defesa física.", 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),  # Fivela de bronze
            ("Runas Destrutivas", "Amplifica o dano de magias ofensivas temporariamente.", 0.0, 0.3, 0.4, 0.0, 0.2, 0.0, 0.0, 0.0),  # Fivela Rúnica
            ("Energia Maldita", "Aumenta o crítico e reduz ligeiramente a defesa do usuário.", -0.1, 0.0, 0.6, 0.0, 0.3, 0.0, 0.0, 0.0),  # Fivela Obscura
            ("Luz Astral", "Melhora as habilidades de cura e concede resistência a magia.", 0.1, 0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.0),  # Fivela Celestial
            ("Graça do Vento", "Concede maior agilidade e chance de esquiva.", 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.0, 0.0),  # Fivela da Ventania
            ("Proteção Glacial", "Aumenta a defesa física e mágica, protegendo contra o frio.", 0.5, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),  # Fivela do Gelo Inquebrável
            #Bengala
            ('Resistência Natural', 'Aumenta a resistência contra ataques físicos leves.', 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0), # Bengala de Madeira Rústica
            ('Cura do Bosque', 'Concede um pequeno aumento na regeneração de vida.', 0.1, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0), # Bengala de Galho Seco
            ('Passos Ágeis', 'Aumenta ligeiramente a agilidade e a velocidade de movimento.', 0.0, 0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0), # Bengala de Bambteu
            ('Sábia Defesa', 'Aumenta a inteligência e a resistência mágica.', 0.0, 0.3, 0.0, 0.0, 0.2, 0.0, 0.0, 0.1), # Bengala de Carvalho Encantado
            ('Defesa Implacável', 'Aumenta significativamente a resistência física e a defesa mágica.', 0.4, 0.2, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0), # Bengala de Madeira Petrificada
            ('Aço Místico', 'Aumenta a chance de crítico e melhora a defesa contra ataques mágicos.', 0.3, 0.2, 0.5, 0.0, 0.1, 0.0, 0.0, 0.0), # Bengala de Prata Mística
            ('Poder Arcano', 'Amplifica o poder de feitiços mágicos e aumenta a regeneração de energia arcana.', 0.0, 0.4, 0.0, 0.0, 0.3, 0.0, 0.0, 0.1), # Bengala de Cristal Arcano
            ('Força Dracônica', 'Aumenta a resistência física e o dano crítico, além de melhorar a regeneração de vida.', 0.5, 0.0, 0.6, 0.2, 0.0, 0.0, 0.0, 0.2), # Bengala de Ossos Dracônicos
            # Manto
            ('Proteção Básica', 'Aumenta a resistência contra ataques leves.', 0.2, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0), # Manto de Lona Simples
            ('Conforto Leve', 'Aumenta ligeiramente a agilidade e a regeneração de vida.', 0.0, 0.1, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0), # Manto de Algodão Básico
            ('Calor Rústico', 'Aumenta a defesa contra frio e a resistência física.', 0.3, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0), # Manto de Lã Rústica
            ('Resistência Ártica', 'Reduz o dano de ataques baseados em gelo e aumenta a resistência mágica.', 0.2, 0.2, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0), # Manto de Neve Encantado
            ('Fúria Selvagem', 'Aumenta a vida e concede bônus de resistência física em terrenos florestais.', 0.4, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.0), # Manto de Pele de Urso
            ('Elegância Ardente', 'Amplifica o dano de magias de fogo e concede resistência contra queimaduras.', 0.3, 0.4, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0), # Manto de Seda Flamejante
            ('Sombras Celestiais', 'Aumenta a resistência mágica e a sorte do portador.', 0.2, 0.3, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0), # Manto Celestial das Sombras
            ('Renascimento Ardente', 'Recupera vida ao longo do tempo e aumenta o dano crítico.', 0.3, 0.0, 0.5, 0.2, 0.0, 0.0, 0.0, 0.0), # Manto da Fênix Ardente
            ('Fúria Tempestuosa', 'Amplifica o dano de feitiços elétricos e aumenta a chance de crítico.', 0.4, 0.5, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0), # Manto do Vórtice Tempestuoso
            # Colar
            ('Durabilidade Básica', 'Aumenta ligeiramente a resistência física.', 0.1, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0), # Colar de Bronze
            ('Sabedoria Inicial', 'Aumenta a inteligência mágica para aprendizes.', 0.0, 0.2, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0), # Colar de Prata
            ('Chama Potencial', 'Amplifica feitiços de fogo e aumenta dano crítico.', 0.0, 0.4, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0), # Colar da Combustão Arcana
            ('Ventos Ágeis', 'Aumenta a agilidade e o poder de magias de vento.', 0.0, 0.3, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0), # Colar da Brisa Mística
            ('Gelo Eterno', 'Concede resistência ao calor e aumenta a defesa mágica.', 0.3, 0.2, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0), # Colar do Gelo Supremo
            ('Regeneração Vital', 'Auxilia na regeneração de vida e energia.', 0.2, 0.0, 0.0, 0.3, 0.2, 0.0, 0.0, 0.0), # Colar do Vigor Florestal
            ('Luz Brilhante', 'Amplifica feitiços de luz e aumenta a sorte.', 0.0, 0.5, 0.0, 0.0, 0.2, 0.3, 0.0, 0.0), # Colar do Prisma Radiante
            ('Proteção Espiritual', 'Reduz o dano mágico e concede bônus defensivo.', 0.4, 0.3, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0), # Colar do Eco Ancestral
            ('Energia Trovejante', 'Amplifica habilidades elétricas e aumenta crítico.', 0.0, 0.4, 0.5, 0.0, 0.2, 0.0, 0.0, 0.0), # Colar do Raio Furioso
            ('Força Sombria', 'Canaliza poder sombrio e aumenta resistência mágica.', 0.3, 0.4, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0), # Colar do Eclipse Noturno
            ('Agilidade Aquática', 'Aumenta a velocidade e dano de ataques aquáticos.', 0.0, 0.3, 0.2, 0.0, 0.2, 0.0, 0.0, 0.0), # Colar da Maré Mística
            ('Sacrifício Carmesim', 'Converte vida em aumento extremo de poder.', 0.0, 0.6, 0.4, -0.3, 0.5, 0.0, 0.0, 0.0), # Colar Carmesim Profano
            ('Lâminas Invisíveis', 'Aumenta o dano de ataques cortantes e agilidade.', 0.0, 0.2, 0.3, 0.0, 0.0, 0.1, 0.0, 0.0), # Anel de Vento
            ('Poder Régio', 'Aumenta drasticamente o poder mágico e crítico.', 0.3, 0.6, 0.5, 0.0, 0.2, 0.0, 0.0, 0.0), # Anel da Realeza
            # Luvas
            ('Resistência Aquática', 'Protege contra feitiços e magias aquáticas.', 0.1, 0.2, 0.05, 0.0, 0.15, 0.0, 0.0, 0.0),
            ('Amplificação Ígnea', 'Aumenta o poder de feitiços de fogo.', 0.05, 0.3, 0.1, 0.0, 0.25, 0.0, 0.0, 0.0),
            ('Precisão do Vento', 'Aumenta a precisão de ataques de longo alcance.', 0.05, 0.15, 0.2, 0.0, 0.0, 0.05, 0.0, 0.0),
            ('Proteção Sombria', 'Reduz o dano recebido de magias sombrias.', 0.3, 0.1, 0.0, 0.0, 0.15, 0.0, 0.0, 0.0),
            ('Purificação Radiante', 'Cura venenos automaticamente após 2 turnos.', 0.2, 0.2, 0.0, 0.1, 0.1, 0.05, 0.0, 0.0),
            ('Absorção de Marés', 'Absorve parte do dano de magias aquáticas.', 0.25, 0.1, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0),
            ('Intimidação Profana', 'Reduz a chance de acerto dos inimigos.', 0.15, 0.15, 0.05, 0.0, 0.0, 0.05, 0.0, 0.0),
            ('Velocidade Predatória', 'Aumenta a velocidade e esquiva em combate.', 0.2, 0.05, 0.15 0.0, 0.0, 0.1, 0.0, 0.0),
            ('Resistência Gélida', 'Concede resistência ao frio extremo.', 0.3, 0.05, 0.0, 0.0, 0.15, 0.0, 0.0, 0.0),
            ('Tempestade Energizada', 'Amplifica o dano de ataques elétricos.', 0.05, 0.25, 0.2, 0.0, 0.3, 0.0, 0.0, 0.0),
            # Chapeu
            ('Revelação Arcana', 'Aumenta a capacidade de desvendar segredos ocultos.', 0.1, 0.3, 0.05, 0.0, 0.2, 0.05, 0.0, 0.0),
            ('Aura Amaldiçoada', 'Diminui a confiança dos inimigos, gerando incertezas.', 0.15, 0.2, 0.1, 0.0, 0.15, 0.05, 0.0, 0.0),
            ('Sombras Nutridoras', 'Amplifica o poder de feitiços destrutivos.', 0.2, 0.25, 0.15, 0.0, 0.3, 0.0, 0.0, 0.0),
            ('Poder Dracônico', 'Aumenta a força e resistência contra ataques de dragões.', 0.3, 0.2, 0.15, 0.1, 0.2, 0.05, 0.0, 0.0),
            ('Sopro Gélido', 'Reduz a velocidade dos inimigos, causando desconforto.', 0.2, 0.15, 0.05, 0.0, 0.2, 0.05, 0.0, 0.0),
            ('Energia Nefasta', 'Aumenta a regeneração de mana e poder em ambientes sombrios.', 0.15, 0.3, 0.1, 0.0, 0.3, 0.05, 0.0, 0.0),
            ('Luz Purificadora', 'Remove efeitos negativos e reduz o dano recebido de magias.', 0.25, 0.15 0.05, 0.1, 0.2, 0.0, 0.0, 0.0),
            ('Chamas Ardentes', 'Amplifica o dano de ataques de fogo.', 0.15 0.25, 0.2, 0.0, 0.3, 0.05, 0.0, 0.0),
            ('Energia Trovejante', 'Aumenta a velocidade de ataque e precisão.', 0.15 0.2, 0.15 0.0, 0.3, 0.05, 0.0, 0.0),
            ('Coragem Inabalável', 'Concede resistência extra contra ataques críticos.', 0.3, 0.2, 0.1, 0.15 0.2, 0.05, 0.0, 0.0),
            ('Ilusão Arcana', 'Confunde os inimigos, reduzindo sua precisão.', 0.2, 0.25, 0.1, 0.0, 0.15 0.05, 0.0, 0.0),
            ('Ecos Ancestrais', 'Concede bônus de resistência e regeneração.', 0.3, 0.2, 0.1, 0.15 0.2, 0.05, 0.0, 0.0),
            # Calca
            ('Proteção Rústica', 'Concede leve proteção com couro resistente.', 0.02, 0.05, 0.0, 0.1, 0.0, 0.05, 0.0, 0.0),
            ('Força Dracônica', 'Oferece resistência e poder do couro de dragão.', 0.04, 0.08, 0.02, 0.15, 0.0, 0.1, 0.0, 0.0),
            ('Sombras Forjadas', 'Amplifica a resistência com energias das trevas.', 0.06, 0.1, 0.03, 0.2, 0.0, 0.15, 0.0, 0.0),
            ('Cristal Arcano', 'Concede bônus de magia com proteção cristalina.', 0.06, 0.12, 0.04, 0.25, 0.0, 0.2, 0.0, 0.0),
            ('Vigor da Madeira', 'Fornece resistência com a vitalidade da madeira viva.', 0.03, 0.06, 0.02, 0.15, 0.0, 0.1, 0.0, 0.0),
            ('Trovão Potente', 'Aumenta o poder com a força do trovão.', 0.15, 0.2, 0.03, 0.3, 0.0, 0.25, 0.0, 0.0),
            ('Resiliência Óssea', 'Amplifica resistência com ossos de dragão.', 0.2, 0.25, 0.06, 0.35, 0.0, 0.3, 0.0, 0.0),
            ('Glória Real', 'Fornece bônus para magos experientes.', 0.230, 0.3, 0.05, 0.4, 0.0, 0.35, 0.0, 0.0),
            ('Energia Tempestuosa', 'Concede agilidade e força com o poder das tempestades.', 0.25, 0.4, 0.04, 0.45, 0.0, 0.4, 0.0, 0.0),
            ('Instinto Animal', 'Aumenta o vigor com peles mágicas.', 0.3, 0.35, 0.05, 0.5, 0.0, 0.45, 0.0, 0.0),
            ('Tecido Encantado', 'Fornece proteção mágica leve.', 0.32, 0.4, 0.03, 0.55, 0.0, 0.5, 0.0, 0.0),
            ('Elegância Arcana', 'Amplifica poder mágico com seda mágica.', 0.33, 0.45, 0.03, 0.6, 0.0, 0.55, 0.0, 0.0),
            ('Força Gigantesca', 'Concede enorme resistência com ossos de gigante.', 0.34, 0.5, 0.06, 0.65, 0.0, 0.6, 0.0, 0.0),
            ('Maciez Encantada', 'Oferece conforto e proteção mágica.', 0.36, 0.55, 0.04, 0.7, 0.0, 0.65, 0.0, 0.0),
            ('Escamas de Serpente', 'Aumenta a resistência com escamas místicas.', 0.35, 0.6, 0.05, 0.75, 0.0, 0.7, 0.0, 0.0),
            # Meia
            ('Conforto Simples', 'Concede leve proteção com pano comum.', 0.02, 0.03, 0.0, 0.05, 0.0, 0.01, 0.0, 0.0),
            ('Aconchego Natural', 'Fornece calor e proteção com lã de ovelha.', 0.04, 0.05, 0.0, 0.1, 0.0, 0.02, 0.0, 0.0),
            ('Toque Celestial', 'Amplifica habilidades mágicas com seda mágica.', 0.1, 0.15, 0.02, 0.2, 0.0, 0.1, 0.0, 0.0),
            ('Maciez Encantada', 'Oferece bônus mágico com algodão encantado.', 0.11, 0.16, 0.02, 0.22, 0.0, 0.12, 0.0, 0.0),
            ('Esplendor Dourado', 'Aumenta resistência com fios de ouro.', 0.12, 0.18, 0.02, 0.24, 0.0, 0.13, 0.0, 0.0),
            ('Vitalidade Raiz', 'Fornece resistência e energia com raízes mágicas.', 0.13, 0.2, 0.02, 0.26, 0.0, 0.15, 0.0, 0.0),
            ('Sussurros Sombrios', 'Amplifica poder mágico com magia sombria.', 0.15, 0.25, 0.03, 0.3, 0.0, 0.2, 0.0, 0.0),
            # Anel
            ('Brilho Simples', 'Concede leve proteção com um anel de bronze.', 0.05, 0.02, 0.0, 0.1, 0.0, 0.01, 0.0, 0.0),
            ('Aura de Prata', 'Aumenta habilidades mágicas para iniciantes.', 0.2, 0.05, 0.0, 0.14, 0.0, 0.02, 0.0, 0.0),
            ('Resplendor Áureo', 'Oferece grande poder para magos experientes.', 0.23, 0.15, 0.05, 0.3, 0.0, 0.12, 0.0, 0.0),
            ('Encanto Arcano', 'Amplifica magia com propriedades místicas.', 0.37, 0.2, 0.05, 0.5, 0.0, 0.23, 0.0, 0.0),
            ('Maldição Sombria', 'Aumenta poder sombrio, mas é perigoso.', 0.37, 0.3, 0.15, 0.21, 0.0, 0.21, 0.0, 0.0),
            ('Diamante Místico', 'Concede poder incomparável para magos.', 0.51, 0.4, 0.1, 0.5, 0.0, 0.5, 0.0, 0.0),
            ('Força Negra', 'Oferece poder com matéria sombria.', 0.16, 0.1, 0.03, 0.25, 0.0, 0.05, 0.0, 0.0),
            ('Harmonia Natural', 'Fornece equilíbrio com grama mística.', 0.07, 0.03, 0.01, 0.18, 0.0, 0.018, 0.0, 0.0),
            ('Gelo Eterno', 'Amplifica resistência com gelo inquebrável.', 0.4, 0.2, 0.04, 0.5, 0.0, 0.11, 0.0, 0.0),
            ('Emanar Arcano', 'Fortalece energia com fulgor mágico.', 0.28, 0.15, 0.02, 0.4, 0.0, 0.08, 0.0, 0.0),
            ('Espiral Espiritual', 'Atrai espíritos com poder espectral.', 0.33, 0.25, 0.06, 0.45, 0.0, 0.15, 0.0, 0.0),
            ('Lâmina Invisível', 'Proporciona ataques cortantes com vento.', 0.2, 0.1, 0.01, 0.3, 0.0, 0.065, 0.0, 0.0);
        ]

        db.cur.executemany(
            """
            INSERT INTO efeito (nome, descricao, defesa, inteligencia, critico, vida, energia_arcana, sorte, xp, moedas)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, 
            default
        )
        db.conn.commit()

        debug(f"default: {len(default)} {table_name} added successfully!")
        return len(default)
    
    except Exception as e:
        db.conn.rollback()
        error(f"Erro ao adicionar valores na tabela {table_name}: {e}")
