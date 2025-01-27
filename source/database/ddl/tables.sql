CREATE TABLE item (
    id SERIAL PRIMARY KEY,
    tipo TIPO_ITEM NOT NULL,
    descricao TEXT NOT NULL,
    -- É o numero de inimigos que você tem que matar para conseguir o item.
    -- Chance de drop: O cálculo é: 1 / enemies_average.
	drop_inimigos_media INT NOT NULL CHECK (drop_inimigos_media >= 0),
	nome VARCHAR(50) NOT NULL,
	peso INT NOT NULL CHECK (peso >= 0),
	preco INT NOT NULL CHECK (preco >= 0)
);

CREATE TABLE armazenamento (
    id SERIAL PRIMARY KEY,
    item_id INT NOT NULL REFERENCES item(id),
    quantidade INT NOT NULL
);

CREATE TABLE regiao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao TEXT NOT NULL,
    elemento TIPO_ELEMENTO NOT NULL
);

CREATE TABLE sub_regiao (
    id SERIAL PRIMARY KEY,
    regiao_id INT NOT NULL REFERENCES regiao(id),
    armazenamento_id INT REFERENCES armazenamento(id),
    nome VARCHAR(50) NOT NULL,
    descricao TEXT NOT NULL
);

CREATE TABLE sub_regiao_conexao (
    sub_regiao_1 INT NOT NULL REFERENCES sub_regiao(id),
    sub_regiao_2 INT NOT NULL REFERENCES sub_regiao(id),
    direcao TIPO_DIRECAO NOT NULL,
    situacao TIPO_SITUACAO NOT NULL
);

CREATE TABLE personagem (
    id SERIAL PRIMARY KEY,
	sub_regiao_id INT NOT NULL REFERENCES sub_regiao(id),
	nome VARCHAR(20) NOT NULL,
    elemento TIPO_ELEMENTO NOT NULL,
    conhecimento_arcano INT NOT NULL CHECK (conhecimento_arcano >= 0),
    vida INT NOT NULL CHECK (vida >= 0),
	vida_maxima INT NOT NULL CHECK (vida_maxima >= 0),
	xp INT NOT NULL CHECK (xp >= 0),
    xp_total INT NOT NULL CHECK (xp_total >= 0),
    energia_arcana INT NOT NULL CHECK (energia_arcana >= 0),
    energia_arcana_maxima INT NOT NULL CHECK (energia_arcana_maxima >= 0),
    inteligencia INT NOT NULL CHECK (inteligencia >= 0),
    moedas INT NOT NULL CHECK (moedas >= 0),
    nivel INT NOT NULL CHECK (nivel >= 0)
);

CREATE TABLE inventario (
    id SERIAL PRIMARY KEY,
    personagem_id INT NOT NULL REFERENCES personagem(id),
	tipo TIPO_INVENTARIO NOT NULL
);

CREATE TABLE npc (
    id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
    tipo TIPO_NPC NOT NULL
);

CREATE TABLE civil (
    id INT NOT NULL PRIMARY KEY REFERENCES npc(id),
    sub_regiao_id INT NOT NULL REFERENCES sub_regiao(id),
    descricao TEXT NOT NULL,
    tipo TIPO_CIVIL NOT NULL
);

CREATE TABLE quester (
    id INT NOT NULL PRIMARY KEY REFERENCES npc(id),
    dialogo TEXT NOT NULL,
    num_quests INT NOT NULL CHECK (num_quests >= 0)
);

CREATE TABLE quest (
    id SERIAL PRIMARY KEY,
    quester_id INT NOT NULL REFERENCES quester(id),
    armazenamento_id INT NOT NULL REFERENCES armazenamento(id),
    titulo VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL,
    recompensa TEXT NOT NULL,
    dificuldade TIPO_DIFICULDADE NOT NULL
);

CREATE TABLE quest_instancia (
    id SERIAL PRIMARY KEY,
    quest_id INT NOT NULL REFERENCES quest(id),
    personagem_id INT NOT NULL REFERENCES personagem(id),
    completed BOOLEAN NOT NULL
);

CREATE TABLE item_instancia (
    id SERIAL PRIMARY KEY,
    item_id INT NOT NULL REFERENCES item(id),
    inventario_id INT NOT NULL REFERENCES inventario(id)
);

CREATE TABLE mercador (
    id INT NOT NULL PRIMARY KEY REFERENCES npc(id),
    armazenamento_id INT REFERENCES armazenamento(id),
    dialogo TEXT NOT NULL
);

CREATE TABLE armazenamento_mercador (
    mercador_id INT NOT NULL REFERENCES mercador(id),
    armazenamento_id INT NOT NULL REFERENCES armazenamento(id)
);

CREATE TABLE transacao (
    id SERIAL PRIMARY KEY,
    mercador_id INT NOT NULL REFERENCES mercador(id),
    personagem_id INT NOT NULL REFERENCES personagem(id),
    item_id INT NOT NULL REFERENCES item(id)
);

CREATE TABLE mochila (
	id INT NOT NULL PRIMARY KEY REFERENCES inventario(id),
	peso INT NOT NULL CHECK (peso <= peso_total AND peso >= 0),
	peso_total INT NOT NULL CHECK (peso_total >= 0)
);

CREATE TABLE feitico (
    id SERIAL PRIMARY KEY,
    descricao TEXT NOT NULL,
    elemento TIPO_ELEMENTO NOT NULL,
    countdown INT NOT NULL CHECK (countdown >= 0),
    conhecimento_arcano_necessario INT NOT NULL CHECK (conhecimento_arcano_necessario >= 0),
    energia_arcana INT NOT NULL CHECK (energia_arcana >= 0),
    tipo TIPO_FEITICO NOT NULL
);

CREATE TABLE feitico_requerimento (
    de_id INT NOT NULL REFERENCES feitico(id),
    para_id INT NOT NULL REFERENCES feitico(id)
);

CREATE TABLE feitico_dano (
    id INT PRIMARY KEY REFERENCES feitico(id),
    dano_total INT NOT NULL CHECK (dano_total >= 0)
);

CREATE TABLE feitico_dano_area (
    id INT PRIMARY KEY REFERENCES feitico(id),
    dano INT NOT NULL CHECK (dano >= 0),
    qtd_inimigos_afetados INT NOT NULL CHECK (qtd_inimigos_afetados >= 0)
);

CREATE TABLE feitico_cura (
    id INT PRIMARY KEY REFERENCES feitico(id),
    qtd_cura INT NOT NULL CHECK (qtd_cura >= 0)
);

CREATE TABLE grimorio (
    id INT NOT NULL PRIMARY KEY REFERENCES inventario(id),
	num_pag INT NOT NULL CHECK (num_pag <= num_pag_maximo AND num_pag >= 0),
    num_pag_maximo INT NOT NULL CHECK (num_pag_maximo >= 0)
);

CREATE TABLE feitico_aprendido (
    inventario_id INT NOT NULL REFERENCES inventario(id),
    feitico_id INT NOT NULL REFERENCES feitico(id)
);

CREATE TABLE pergaminho (
    id INT PRIMARY KEY REFERENCES item(id),
    cor VARCHAR(10) NOT NULL
);

CREATE TABLE feitico_escrito (
	item_id INT NOT NULL REFERENCES pergaminho(id),
	feitico_id INT NOT NULL REFERENCES feitico(id)
);

CREATE TABLE efeito (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL,
    defesa DECIMAL(1, 3) NOT NULL CHECK (defesa >= 0),
    inteligencia DECIMAL(1, 3) NOT NULL CHECK (inteligencia >= 0),
    critico DECIMAL(1, 3) NOT NULL CHECK (critico >= 0),
    vida DECIMAL(1, 3) NOT NULL CHECK (vida >= 0),
    energia_arcana DECIMAL(1, 3) NOT NULL CHECK (energia_arcana >= 0),
    sorte DECIMAL(1, 3) NOT NULL CHECK (sorte >= 0),
    xp DECIMAL(1, 3) NOT NULL CHECK (xp >= 0),
    moedas DECIMAL(1, 3) NOT NULL CHECK (moedas >= 0)
);

CREATE TABLE acessorio (
    id INT PRIMARY KEY REFERENCES item(id),
    tipo TIPO_ACESSORIO NOT NULL
);

CREATE TABLE sub_regiao_acessorio_conexao (
    sub_regiao1_id INT NOT NULL REFERENCES sub_regiao(id),
    sub_regiao2_id INT NOT NULL REFERENCES sub_regiao(id),
    acessorio_id INT NOT NULL REFERENCES acessorio(id)
);

CREATE TABLE acessorio_efeito (
    acessorio_id INT NOT NULL REFERENCES acessorio(id),
    efeito_id INT NOT NULL REFERENCES efeito(id)
);

CREATE TABLE pocao (
    id INT PRIMARY KEY REFERENCES item(id),
    turnos INT NOT NULL CHECK (turnos >= 0),
    usado BOOLEAN NOT NULL
);

CREATE TABLE pocao_efeito (
    pocao_id INT NOT NULL REFERENCES pocao(id),
    efeito_id INT NOT NULL REFERENCES efeito(id)
);

CREATE TABLE inimigo (
    id INT NOT NULL PRIMARY KEY REFERENCES npc(id),
    armazenamento_id INT REFERENCES armazenamento(id), -- To-do: change to not null
    descricao TEXT NOT NULL,
    elemento TIPO_ELEMENTO NOT NULL,
    vida_maxima INT NOT NULL CHECK (vida_maxima >= 0),
    xp_obtido INT NOT NULL CHECK (xp_obtido >= 0),
    inteligencia INT NOT NULL CHECK (inteligencia >= 0),
    moedas_obtidas INT NOT NULL CHECK (moedas_obtidas >= 0),
    conhecimento_arcano INT NOT NULL CHECK (conhecimento_arcano >= 0),
    energia_arcana_maxima INT NOT NULL CHECK (energia_arcana_maxima >= 0),
    dialogo TEXT -- To-do: change to not null
);

CREATE TABLE armazenamento_inimigo (
    inimigo_id INT NOT NULL REFERENCES inimigo(id),
    armazenamento_id INT NOT NULL REFERENCES armazenamento(id)
);

CREATE TABLE inimigo_instancia (
    id SERIAL PRIMARY KEY,
    inimigo_id INT NOT NULL REFERENCES inimigo(id),
    sub_regiao_id INT NOT NULL REFERENCES sub_regiao(id),
    vida INT NOT NULL CHECK (vida >= 0)
);

-- CREATE TABLE combate (
--     inimigo_instancia_id INT NOT NULL REFERENCES inimigo_instancia(id),
--     personagem_id INT NOT NULL REFERENCES personagem(id),
--     dano_causado INT NOT NULL CHECK (dano_causado >= 0),
--     dano_recebido INT NOT NULL CHECK (dano_recebido >= 0)
-- );