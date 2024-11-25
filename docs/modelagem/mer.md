# Modelo Entidade Relacionamento – MER 

## Introducao 

O Modelo Entidade-Relacionamento (MER) é uma ferramenta utilizada para representar elementos do mundo real por meio de entidades, que possuem características chamadas atributos, e das conexões entre elas, que são os relacionamentos. 

## Entidades 

- CRIATURA
    - Personagem
    - Instância de Inimigo
- NPC
    - Inimigo 
    - Civil
        - Quester 
        - Mercador 
- ITEM
    - Consumível
        - Poção
        - Pergaminho
    - Não-Consumível
- INSTÂNCIA DE ITEM
- INVENTARIO
    - Grimório
    - Mochila
- QUEST
- INSTANCIA DE QUEST
- FEITIÇO
    - Dano
    - Dano_em_area
    - Cura
- REGIÃO
- LOCAL

## Atributos

- CRIATURA:{ <u>id</u>, moedas, pontos_de_vida, *nivel*:{ xp, pontos_vida_maximo, energia_arcana_maxima } }
    - Personagem:{ <u>nome</u>, elemento, conhecimento_arcano, pontos_vida_atual, energia_arcana_atual, inteligencia, *progresso*:{ quests_realizadas, nr_inimigos_derrotados } }
    - Instância de Inimigo
- NPC:{ <u>id</u>, nome, dialogo }
    - Inimigo:{ <u>id</u>, nome, elemento, pontos_vida_total, inteligencia }
    - Civil
        - Quester 
        - Mercador:{ <u>id</u>, vendas, elemento }
- ITEM:{ <u>id</u>, chance_drop, nome, peso, preco }
    - Consumível
        - Poção:{ efeito, duracao }
        - Pergaminho:{ cor, descricao }
    - Não-Consumível:{ buff, debuff }
- INSTÂNCIA DE ITEM:{ <u>id</u> }
- INVENTARIO:{ <u>id</u> }
    - Grimório:{ nr_paginas }
    - Mochila:{ peso_maximo, peso_atual }
- QUEST:{ <u>id</u>, titulo, descricao, recompensa, dificuldade }
- INSTÂNCIA DE QUEST:{ <u>id</u>, recompensa_moedas, status }
- FEITIÇO:{ <u>nome</u>, elemento, energia_arcana_necessaria }
    - Dano:{ dano_total }
    - Dano_em_area:{ qtd_inimigos_afetados }
    - Cura:{ qtd_cura }
- REGIÃO:{ <u>id</u>, nome, descricao, elemento_regiao }
- LOCAL:{ <u>id</u>, nome, descricao }

## Relacionamentos
- Criatura **Habita** Local
- Personagem **Contém** Inventário
- Personagem **Transaciona** com Mercador uma Instância de Item??????
- Personagem **Confronta** Instância de Inimigo
- Inimigo **Tem** Instância de Inimigo
- Inimigo **Fornece** Item
- Civel **Habita** Local
- Quester **Oferta** Instância de Quest
- Mercador **Fornece** Item
- Item **Tem** Instância de Item
- Pergaminho **Contém** Feitiço
- Grimório **Contém** Feitiço
- Mochila **Contém** Instância de Item
- Quest **Tem** Instância de Quest
- Feitiço **Requer** Feitiço
- Região **Contém** Local
- Local **Contém** Instancia de Item
- Local **Contém** Local

## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 24/11/2024 | Criação do MER  | Grupo |
 