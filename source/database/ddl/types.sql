CREATE TYPE TIPO_INVENTARIO AS ENUM ('Mochila', 'Grimório');
CREATE TYPE TIPO_ELEMENTO AS ENUM ('Fogo', 'Água', 'Terra', 'Ar', 'Trevas', 'Luz');
CREATE TYPE TIPO_DIFICULDADE AS ENUM ('Iniciante', 'Fácil', 'Médio', 'Difícil', 'Legendário');
CREATE TYPE TIPO_ITEM AS ENUM ('Poção', 'Acessório', 'Pergaminho');
CREATE TYPE TIPO_FEITICO AS ENUM ('Dano', 'Dano de área', 'Cura');
CREATE TYPE TIPO_NPC AS ENUM ('Civil', 'Inimigo');
CREATE TYPE TIPO_CIVIL AS ENUM ('Mercador', 'Quester', 'Civil');
CREATE TYPE TIPO_DIRECAO AS ENUM ('Norte', 'Sul', 'Leste', 'Oeste');
CREATE TYPE TIPO_SITUACAO AS ENUM ('Passável', 'Não Passável');
CREATE TYPE TIPO_ACESSORIO AS ENUM (
    'Anel',
    'Chapéu',
    'Colar',
    'Bracelete',
    'Fivela',
    'Luvas',
    'Botas',
    'Calça',
    'Meias',
    'Bengala',

CREATE TYPE TIPO_COR AS ENUM (
    'Ruby',
    'Ciano',
    'Arco-íris',
    'Prata',
    'Dourado',
    'Bronze',
    'Índigo',
    'Turquesa',
    'Magenta',
    'Esmeralda',
    'Cobre',
    'Púrpura'
);