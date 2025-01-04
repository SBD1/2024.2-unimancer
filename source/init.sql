-- Tabela tipo_item
CREATE TABLE tipo_item (
    id_item SERIAL PRIMARY KEY,
    descricao TEXT NOT NULL,
	chande_drop INT NOT NULL,
	nome VARCHAR(20) NOT NULL,
	peso INT NOT NULL,
	preco INT NOT NULL
);

--Tabela armazenamento
CREATE TABLE armazenamento(
	id_armazenamento SERIAL PRIMARY KEY,
	tipo_item INT NOT NULL UNIQUE REFERENCES tipo_item(id_item),
	quantity INT NOT NULL CHECK (quantity >= 0)
);

-- Tabela regiao
CREATE TABLE regiao (
    id_regiao SERIAL PRIMARY KEY,
    nome VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL,
    elemento VARCHAR(5) NOT NULL
);

-- Tabela sub_regiao
CREATE TABLE sub_regiao (
    id_subregiao SERIAL PRIMARY KEY,
    id_regiao INT NOT NULL,
    id_armazenamento INT NOT NULL REFERENCES armazenamento(id_armazenamento),
    nome VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (id_regiao) REFERENCES regiao(id_regiao)
);

-- Tabela personagem
CREATE TABLE personagem (
    id_personagem SERIAL PRIMARY KEY,
	id_subregiao INT NOT NULL REFERENCES sub_regiao(id_subregiao),
	nome VARCHAR(20) NOT NULL,
    elemento VARCHAR(5) NOT NULL,
    conhecimento_arcano INT NOT NULL CHECK (conhecimento_arcano >= 0),
    vida_atual INT NOT NULL,
	vida_maxima INT NOT NULL,
	xp_atual INT NOT NULL CHECK (xp_atual >= 0),
    xp_total INT NOT NULL CHECK (xp_total >= 0),
    energia_arcana_maxima INT NOT NULL CHECK (energia_arcana_maxima >= 0),
    energia_arcana_atual INT NOT NULL CHECK (energia_arcana_atual >= 0),
    inteligencia INT NOT NULL CHECK (inteligencia >= 0),
    moedas INT NOT NULL CHECK (moedas >= 0),
    nivel INT NOT NULL CHECK (nivel >= 0)
);


-- Tabela inventario
CREATE TABLE inventario (
    id_inventario SERIAL PRIMARY KEY,
    id_personagem INT NOT NULL REFERENCES personagem(id_personagem),
	tipo_inventario VARCHAR(20) NOT NULL
);

-- Tabela tipo_npc
CREATE TABLE tipo_npc (
    id_npc SERIAL PRIMARY KEY,
	nome VARCHAR(20) NOT NULL,
    tipo_npc VARCHAR(20) NOT NULL
);

-- Tabela quester
CREATE TABLE quester (
    id_quester INT PRIMARY KEY,
    dialogo TEXT,
    num_quests INT NOT NULL CHECK (num_quests >= 0),
    FOREIGN KEY (id_quester) REFERENCES tipo_npc(id_npc)
);

-- Tabela quest
CREATE TABLE quest (
    id_quest SERIAL PRIMARY KEY,
    quester INT NOT NULL,
    id_armazenamento INT NOT NULL REFERENCES armazenamento(id_armazenamento),
    titulo VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL,
    recompensa TEXT NOT NULL,
    dificuldade VARCHAR(2) NOT NULL,
    FOREIGN KEY (quester) REFERENCES quester(id_quester)
);

-- Tabela quest_instancia
CREATE TABLE quest_instancia (
    id_quest_instancia SERIAL PRIMARY KEY,
    id_quest INT NOT NULL,
    personagem INT NOT NULL,
    status BIT NOT NULL,
    FOREIGN KEY (id_quest) REFERENCES quest(id_quest),
    FOREIGN KEY (personagem) REFERENCES personagem(id_personagem)
);

-- Tabela item_instancia
CREATE TABLE item_instancia (
    id_item_instancia SERIAL PRIMARY KEY,
    id_item INT NOT NULL,
    id_inventario INT NOT NULL,
    FOREIGN KEY (id_item) REFERENCES tipo_item(id_item),
    FOREIGN KEY (id_inventario) REFERENCES inventario(id_inventario)
);

-- Tabela mercador
CREATE TABLE mercador (
    id_mercador INT UNIQUE NOT NULL,
    id_armazenamento INT NOT NULL REFERENCES armazenamento(id_armazenamento),
    dialogo TEXT NOT NULL,
    FOREIGN KEY (id_mercador) REFERENCES tipo_npc(id_npc)
);

-- Tabela transacao
CREATE TABLE transacao (
    id_transacao SERIAL PRIMARY KEY,
    personagem INT NOT NULL,
	id_mercador INT NOT NULL REFERENCES mercador(id_mercador),
    FOREIGN KEY (personagem) REFERENCES personagem(id_personagem)
);

-- Tabela civil
CREATE TABLE civil (
    id_civil INT NOT NULL,
    id_subregiao INT NOT NULL REFERENCES sub_regiao(id_subregiao),
    descricao TEXT,
    tipo_civil VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_civil) REFERENCES tipo_npc(id_npc)
);

--Tabela mochila
CREATE TABLE mochila(
	id_mochila SERIAL PRIMARY KEY,
	id_personagem INT NOT NULL REFERENCES personagem(id_personagem),
	id_item_instancia INT NOT NULL REFERENCES item_instancia(id_item_instancia),
	peso_atual INT NOT NULL CHECK (peso_atual <= peso_total AND peso_atual >= 0),
	peso_total INT NOT NULL CHECK (peso_total >= 0)
);

-- Tabela feitico
CREATE TABLE feitico (
    id_feitico SERIAL PRIMARY KEY,
    descricao TEXT NOT NULL,
    elemento VARCHAR(5) NOT NULL,
    feitico_requerido VARCHAR(20) NOT NULL,
    energia_arcana_necessaria INT NOT NULL CHECK (energia_arcana_necessaria >= 0)
);


-- Tabela grimorio
CREATE TABLE grimorio (
    id_grimorio INT PRIMARY KEY,
	id_personagem INT NOT NULL REFERENCES personagem(id_personagem),
	id_feitico INT NOT NULL REFERENCES feitico(id_feitico),
	num_pag_atual INT NOT NULL,
    num_pag_maximo INT NOT NULL
);



-- Tabela feitico_dano
CREATE TABLE feitico_dano (
    id_feitico INT PRIMARY KEY,
    dano_total INT NOT NULL,
    FOREIGN KEY (id_feitico) REFERENCES feitico(id_feitico)
);

-- Tabela feitico_dano_area
CREATE TABLE feitico_dano_area (
    id_feitico INT PRIMARY KEY,
    qtd_inimigos_afetados INT NOT NULL,
    FOREIGN KEY (id_feitico) REFERENCES feitico(id_feitico)
);

-- Tabela feitico_cura
CREATE TABLE feitico_cura (
    id_feitico INT PRIMARY KEY,
    qtd_cura INT NOT NULL,
    FOREIGN KEY (id_feitico) REFERENCES feitico(id_feitico)
);


-- Tabela pergaminho
CREATE TABLE pergaminho (
    id_item INT PRIMARY KEY,
    id_feitico INT NOT NULL,
    chance_drop DECIMAL(2,3) NOT NULL CHECK (chance_drop >= 0),
    nome VARCHAR(20) NOT NULL,
    peso INT NOT NULL,
    preco INT NOT NULL CHECK (preco >= 0),
    cor VARCHAR(10) NOT NULL,
    FOREIGN KEY (id_item) REFERENCES tipo_item(id_item),
    FOREIGN KEY (id_feitico) REFERENCES feitico(id_feitico)
);

-- Tabela acessorio
CREATE TABLE acessorio (
    id_item INT PRIMARY KEY,
    efeito DECIMAL(1,3) NOT NULL,
    debuff DECIMAL(1,3) NOT NULL,
    FOREIGN KEY (id_item) REFERENCES tipo_item(id_item)
);

-- Tabela pocao
CREATE TABLE pocao (
    id_item INT PRIMARY KEY,
    efeito DECIMAL(1,3) NOT NULL,
    duracao INT NOT NULL CHECK (duracao >= 0),
    FOREIGN KEY (id_item) REFERENCES tipo_item(id_item)
);

-- Tabela inimigo
CREATE TABLE inimigo (
    id_inimigo INT NOT NULL UNIQUE,
    id_armazenamento INT NOT NULL REFERENCES armazenamento(id_armazenamento),
    elemento VARCHAR(5) NOT NULL,
    descricao TEXT NOT NULL,
    vida_maxima INT NOT NULL,
    xp_obtido INT NOT NULL,
    inteligencia INT NOT NULL,
    dialogo TEXT NOT NULL,
    FOREIGN KEY (id_inimigo) REFERENCES tipo_npc(id_npc)
);

-- Tabela inimigo_instancia
CREATE TABLE inimigo_instancia (
    id_inimigo_instancia SERIAL PRIMARY KEY,
    id_npc INT NOT NULL,
    id_subregiao INT NOT NULL REFERENCES sub_regiao(id_subregiao),
    vida_atual INT NOT NULL,
    FOREIGN KEY (id_npc) REFERENCES inimigo(id_inimigo)
);

-- Tabela combate
CREATE TABLE combate (
    id_inimigo_instancia INT NOT NULL,
    id_personagem INT NOT NULL,
    dano_causado INT NOT NULL,
    dano_recebido INT NOT NULL,
    PRIMARY KEY (id_inimigo_instancia, id_personagem),
    FOREIGN KEY (id_inimigo_instancia) REFERENCES inimigo_instancia(id_inimigo_instancia),
    FOREIGN KEY (id_personagem) REFERENCES personagem(id_personagem)
);



--Tabela feitico escrito
CREATE TABLE feitico_escrito(
	id_item INT NOT NULL REFERENCES tipo_item(id_item),
	id_feitico INT NOT NULL REFERENCES feitico(id_feitico),
	PRIMARY KEY (id_item, id_feitico)
);

-- Tabela feitico_aprendido
CREATE TABLE feitico_aprendido (
    id_inventario INT NOT NULL,
    id_feitico INT NOT NULL,
    PRIMARY KEY (id_inventario, id_feitico),
    FOREIGN KEY (id_inventario) REFERENCES inventario(id_inventario),
    FOREIGN KEY (id_feitico) REFERENCES feitico(id_feitico)
);

