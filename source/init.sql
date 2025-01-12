CREATE TYPE TIPO_INVENTARIO AS ENUM ('mochila', 'grimorio');
CREATE TYPE TIPO_ELEMENTO AS ENUM ('fogo', 'agua', 'terra', 'ar', 'trevas', 'luz');
CREATE TYPE TIPO_DIFICULDADE AS ENUM ('iniciante', 'facil', 'medio', 'dificil', 'legendario');
CREATE TYPE TIPO_ITEM AS ENUM ('pocao', 'acessorio');
CREATE TYPE TIPO_FEITICO AS ENUM ('dano', 'dano_area', 'cura');
CREATE TYPE TIPO_NPC AS ENUM ('civil', 'inimigo');
CREATE TYPE TIPO_CIVIL AS ENUM ('mercador', 'quester');

CREATE TABLE item (
    id SERIAL PRIMARY KEY,
    descricao TEXT NOT NULL,
	chance_drop INT NOT NULL CHECK (chance_drop >= 0),
	nome VARCHAR(20) NOT NULL,
	peso INT NOT NULL CHECK (peso >= 0),
	preco INT NOT NULL CHECK (preco >= 0)
);

CREATE TABLE armazenamento (
    id SERIAL PRIMARY KEY,
    item_id INT NOT NULL REFERENCES item(id),
    quantity INT NOT NULL CHECK (quantity >= 0)    
);

CREATE TABLE regiao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL,
    elemento VARCHAR(5) NOT NULL
);

CREATE TABLE sub_regiao (
    id SERIAL PRIMARY KEY,
    regiao_id INT NOT NULL REFERENCES regiao(id),
    armazenamento_id INT REFERENCES armazenamento(id),
    norte_id INT REFERENCES sub_regiao(id),
    leste_id INT REFERENCES sub_regiao(id),
    oeste_id INT REFERENCES sub_regiao(id),
    sul_id INT REFERENCES sub_regiao(id),
    nome VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL
);

CREATE TABLE personagem (
    id SERIAL PRIMARY KEY,
	sub_regiao_id INT NOT NULL REFERENCES sub_regiao(id),
	nome VARCHAR(20) NOT NULL,
    elemento TIPO_ELEMENTO NOT NULL,
    conhecimento_arcano INT NOT NULL CHECK (conhecimento_arcano >= 0),
    vida_atual INT NOT NULL CHECK (vida_atual >= 0),
	vida_maxima INT NOT NULL CHECK (vida_maxima >= 0),
	xp_atual INT NOT NULL CHECK (xp_atual >= 0),
    xp_total INT NOT NULL CHECK (xp_total >= 0),
    energia_arcana_maxima INT NOT NULL CHECK (energia_arcana_maxima >= 0),
    energia_arcana_atual INT NOT NULL CHECK (energia_arcana_atual >= 0),
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
	nome VARCHAR(20) NOT NULL,
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
    dialogo TEXT,
    num_quests INT NOT NULL CHECK (num_quests >= 0)
);

CREATE TABLE quest (
    id SERIAL PRIMARY KEY,
    quester INT NOT NULL REFERENCES quester(id),
    armazenamento_id INT NOT NULL REFERENCES armazenamento(id),
    titulo VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL,
    recompensa TEXT NOT NULL,
    dificuldade VARCHAR(2) NOT NULL
);

CREATE TABLE quest_instancia (
    id SERIAL PRIMARY KEY,
    personagem_id INT NOT NULL REFERENCES personagem(id),
    quest_id INT NOT NULL REFERENCES quest(id),
    completed BOOLEAN NOT NULL
);

CREATE TABLE item_instancia (
    id SERIAL PRIMARY KEY,
    item_id INT NOT NULL REFERENCES item(id),
    inventario_id INT NOT NULL REFERENCES inventario(id)
);

CREATE TABLE mercador (
    id INT NOT NULL PRIMARY KEY REFERENCES npc(id),
    armazenamento_id INT NOT NULL REFERENCES armazenamento(id),
    dialogo TEXT NOT NULL
);

CREATE TABLE transacao (
    id SERIAL PRIMARY KEY,
    mercador_id INT NOT NULL REFERENCES mercador(id),
    personagem_id INT NOT NULL REFERENCES personagem(id),
    item_id INT NOT NULL REFERENCES item(id)
);

CREATE TABLE mochila (
	id INT NOT NULL PRIMARY KEY REFERENCES inventario(id),
	personagem_id INT NOT NULL REFERENCES personagem(id),
	peso_atual INT NOT NULL CHECK (peso_atual <= peso_total AND peso_atual >= 0),
	peso_total INT NOT NULL CHECK (peso_total >= 0)
);

CREATE TABLE feitico (
    id SERIAL PRIMARY KEY,
    feitico_requerido INT NOT NULL REFERENCES feitico(id),
    descricao TEXT NOT NULL,
    elemento TIPO_ELEMENTO NOT NULL,
    countdown INT NOT NULL CHECK (countdown >= 0),
    energia_arcana_necessaria INT NOT NULL CHECK (energia_arcana_necessaria >= 0)
);

CREATE TABLE feitico_dano (
    id INT PRIMARY KEY REFERENCES feitico(id),
    dano_total INT NOT NULL CHECK (dano_total >= 0)
);

CREATE TABLE feitico_dano_area (
    id INT PRIMARY KEY REFERENCES feitico(id),
    qtd_inimigos_afetados INT NOT NULL CHECK (qtd_inimigos_afetados >= 0)
);

CREATE TABLE feitico_cura (
    id INT PRIMARY KEY REFERENCES feitico(id),
    qtd_cura INT NOT NULL CHECK (qtd_cura >= 0)
);

CREATE TABLE grimorio (
    id INT NOT NULL PRIMARY KEY REFERENCES inventario(id),
	personagem_id INT NOT NULL REFERENCES personagem(id),
	num_pag_atual INT NOT NULL CHECK (num_pag_atual <= num_pag_maximo AND num_pag_atual >= 0),
    num_pag_maximo INT NOT NULL CHECK (num_pag_maximo >= 0)
);

CREATE TABLE feitico_aprendido (
    inventario_id INT NOT NULL REFERENCES inventario(id),
    feitico_id INT NOT NULL REFERENCES feitico(id)
);

CREATE TABLE pergaminho (
    id INT PRIMARY KEY REFERENCES item(id),
    descricao TEXT NOT NULL,
    chance_drop INT NOT NULL CHECK (chance_drop >= 0),
    nome VARCHAR(20) NOT NULL,
    peso INT NOT NULL CHECK (peso >= 0),
    preco INT NOT NULL CHECK (preco >= 0),
    cor VARCHAR(10) NOT NULL
);

CREATE TABLE feitico_escrito(
	item_id INT NOT NULL REFERENCES item(id),
	feitico_id INT NOT NULL REFERENCES feitico(id)
);

CREATE TABLE acessorio (
    id INT PRIMARY KEY REFERENCES item(id),
    efeito VARCHAR(10) NOT NULL,
    debuff VARCHAR(10) NOT NULL
);

CREATE TABLE pocao (
    id INT PRIMARY KEY REFERENCES item(id),
    efeito VARCHAR(10) NOT NULL,
    duracao INT NOT NULL CHECK (duracao >= 0)
);

CREATE TABLE inimigo (
    id INT NOT NULL PRIMARY KEY REFERENCES npc(id),
    armazenamento_id INT NOT NULL REFERENCES armazenamento(id),
    descricao TEXT NOT NULL,
    elemento VARCHAR(5) NOT NULL,
    vida_maxima INT NOT NULL CHECK (vida_maxima >= 0),
    xp_obtido INT NOT NULL CHECK (xp_obtido >= 0),
    inteligencia INT NOT NULL CHECK (inteligencia >= 0),
    moedas_obtidas INT NOT NULL CHECK (moedas_obtidas >= 0),
    dialogo TEXT NOT NULL
);

CREATE TABLE inimigo_instancia (
    id SERIAL PRIMARY KEY,
    inimigo_id INT NOT NULL REFERENCES inimigo(id),
    sub_regiao_id INT NOT NULL REFERENCES sub_regiao(id),
    vida_atual INT NOT NULL CHECK (vida_atual >= 0)
);

CREATE TABLE combate (
    inimigo_instancia_id INT NOT NULL REFERENCES inimigo_instancia(id),
    personagem_id INT NOT NULL REFERENCES personagem(id),
    dano_causado INT NOT NULL CHECK (dano_causado >= 0),
    dano_recebido INT NOT NULL CHECK (dano_recebido >= 0)
);