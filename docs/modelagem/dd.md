# Dicionário de Dados

## Entidades e Atributos

### **Tipo Item**

**Descrição:** Informações referente ao item.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_item | SERIAL | PRIMARY KEY |
| descricao | TEXT | NOT NULL |
| chande_drop | INT | NOT NULL |
| nome | VARCHAR(20) | NOT NULL |
| peso | INT | NOT NULL |
| preco | INT | NOT NULL |

---

### **Armazenamento**

**Descrição:** Itens guardados que podem acessados por um local ou NPC.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_armazenamento | SERIAL | PRIMARY KEY |
| tipo_item | INT | NOT NULL UNIQUE REFERENCES tipo_item(id_item) |
| quantity | INT | NOT NULL CHECK (quantity >= 0) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| tipo_item | tipo_item | id_item |

---


### **Regiao**

**Descrição:** Representa as regiões acessíveis no jogo.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_regiao | SERIAL | PRIMARY KEY |
| nome | VARCHAR(20) | NOT NULL |
| descricao | TEXT | NOT NULL |
| elemento | VARCHAR(5) | NOT NULL |

---

### **Sub Regiao**

**Descrição:** Subconjunto de localidades de cada região.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_subregiao | SERIAL | PRIMARY KEY |
| id_regiao | INT | NOT NULL |
| id_armazenamento | INT | NOT NULL REFERENCES armazenamento(id_armazenamento) |
| nome | VARCHAR(20) | NOT NULL |
| descricao | TEXT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_regiao | regiao | id_regiao |

---

### **Personagem**

**Descrição:** Representa os dados armazenados em cada personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_personagem | SERIAL | PRIMARY KEY |
| id_subregiao | INT | NOT NULL REFERENCES sub_regiao(id_subregiao) |
| nome | VARCHAR(20) | NOT NULL |
| elemento | VARCHAR(5) | NOT NULL |
| conhecimento_arcano | INT | NOT NULL CHECK (conhecimento_arcano >=0) |
| vida_atual | INT | NOT NULL |
| vida_maxima | INT | NOT NULL |
| xp_atual | INT | NOT NULL CHECK (xp_atual >= 0) |
| xp_total | INT | NOT NULL CHECK (xp_total >= 0) |
| energia_arcana_maxima | INT | NOT NULL CHECK (energia_arcana_maxima >= 0) |
| energia_arcana_atual | INT | NOT NULL CHECK (energia_arcana_atual >= 0) |
| inteligencia | INT | NOT NULL CHECK (inteligencia >= 0) |
| moedas | INT | NOT NULL CHECK (moedas >= 0) |
| nivel | INT | NOT NULL CHECK (nivel >= 0) |

---

### **Inventario**

**Descrição:** Tabela de inventário e seu respectivo tipo.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_inventario | SERIAL | PRIMARY KEY |
| id_personagem | INT | NOT NULL REFERENCES personagem(id_personagem) |
| tipo_inventario | VARCHAR(20) | NOT NULL |

---

### **Tipo Npc**

**Descrição:** Representa os dados armazenados na tabela.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_npc | SERIAL | PRIMARY KEY |
| nome | VARCHAR(20) | NOT NULL |
| tipo_npc | VARCHAR(20) | NOT NULL |

---

### **Quester**

**Descrição:** Tipo de NPC que oferece quest aos personagens.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_quester | INT | PRIMARY KEY |
| dialogo | TEXT | NOT NULL |
| num_quests | INT | NOT NULL CHECK (num_quests >= 0) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_quester | tipo_npc | id_npc |

---

### **Quest**

**Descrição:** Representa cada missão ofertada pelos questers.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_quest | SERIAL | PRIMARY KEY |
| quester | INT | NOT NULL |
| id_armazenamento | INT | NOT NULL REFERENCES armazenamento(id_armazenamento) |
| titulo | VARCHAR(20) | NOT NULL |
| descricao | TEXT | NOT NULL |
| recompensa | TEXT | NOT NULL |
| dificuldade | VARCHAR(2) | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| quester | quester | id_quester |

---

### **Quest Instancia**

**Descrição:** Instância de cada quest aceita ou armazenada pelo personagem e quester.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_quest_instancia | SERIAL | PRIMARY KEY |
| id_quest | INT | NOT NULL |
| personagem | INT | NOT NULL |
| status | BIT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_quest | quest | id_quest |
| personagem | personagem | id_personagem |

---

### **Item Instancia**

**Descrição:** Instancia de cada item.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_item_instancia | SERIAL | PRIMARY KEY |
| id_item | INT | NOT NULL |
| id_inventario | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_item | tipo_item | id_item |
| id_inventario | inventario | id_inventario |

---

### **Mercador**

**Descrição:** Tipo de NPC que vende itens ao personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_mercador | INT | UNIQUE NOT NULL |
| id_armazenamento | INT | NOT NULL REFERENCES armazenamento(id_armazenamento) |
| dialogo | TEXT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_mercador | tipo_npc | id_npc |

---

### **Transacao**

**Descrição:** Representa cada compra feita pelo personagem com o mercador.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_transacao | SERIAL | PRIMARY KEY |
| personagem | INT | NOT NULL |
| id_mercador | INT | NOT NULL REFERENCES mercador(id_mercador) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| personagem | personagem | id_personagem |

---

### **Civil**

**Descrição:** Tipo de NPC iteragível, pertecente às cidades.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_civil | INT | NOT NULL |
| id_subregiao | INT | NOT NULL REFERENCES sub_regiao(id_subregiao) |
| descricao | TEXT | - |
| tipo_civil | VARCHAR(20) | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_civil | tipo_npc | id_npc |

---

### **Mochila**

**Descrição:** Tipo de inventário do personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_mochila | SERIAL | PRIMARY KEY |
| id_personagem | INT | NOT NULL REFERENCES personagem(id_personagem) |
| id_instancia_item | INT | NOT NULL REFERENCES item_instancia(id_item_instancia) |
| peso_atual | INT | NOT NULL CHECK (peso_atual <= peso_total AND peso_atual >= 0) |
| peso_total | INT | NOT NULL CHECK (peso_total >= 0) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_personagem | personagem | id_personagem |
| id_instancia_item | instancia_item | id_instancia_item |

---

### **Feitico**

**Descrição:** Dados do feitico, sendo ele seus requerimentos, energia arcana necessária, elemento e descrição.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_feitico | SERIAL | PRIMARY KEY |
| descricao | TEXT | NOT NULL |
| elemento | VARCHAR(5) | NOT NULL |
| feitico_requerido | VARCHAR(20) | NOT NULL |
| energia_arcana_necessaria | INT | NOT NULL CHECK (energia_arcana_necessaria >= 0) |

---

### **Grimorio**

**Descrição:** Tipo de inventário dod personagem que contêm seus feitiços.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_grimorio | INT | PRIMARY KEY |
| id_personagem | INT | NOT NULL REFERENCES personagem(id_personagem) |
| id_feitico | INT | NOT NULL REFERENCES feitico(id_feitico) |
| num_pag_atual | INT | NOT NULL |
| num_pag_maximo | INT | NOT NULL |

---

### **Feitico Dano**

**Descrição:** Tipo de feitiço que concede dano a um inimigo específico.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_feitico | INT | PRIMARY KEY |
| dano_total | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_feitico | feitico | id_feitico |

---

### **Feitico Dano Area**

**Descrição:** Tipo de feitiço que concede dano em área em N inimigos.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_feitico | INT | PRIMARY KEY |
| qtd_inimigos_afetados | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_feitico | feitico | id_feitico |

---

### **Feitico Cura**

**Descrição:** Tipo de feitiço que concede cura ao personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_feitico | INT | PRIMARY KEY |
| qtd_cura | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_feitico | feitico | id_feitico |

---

### **Pergaminho**

**Descrição:** Item do tipo consumível que ensina um feitiço para o personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_item | INT | PRIMARY KEY |
| id_feitico | INT | NOT NULL |
| chance_drop | DECIMAL | NOT NULL CHECK (chance_drop >= 0) |
| nome | VARCHAR(20) | NOT NULL |
| peso | INT | NOT NULL |
| preco | INT | NOT NULL CHECK (preco >= 0) |
| cor | VARCHAR(10) | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_item | tipo_item | id_item |
| id_feitico | feitico | id_feitico |

---

### **Acessorio**

**Descrição:** Tipo de item equipável que concede algum debuff ao inimigo.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_item | INT | PRIMARY KEY |
| efeito | DECIMAL(1,3) | NOT NULL |
| debuff | DECIMAL(1,3) | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_item | tipo_item | id_item |

---

### **Pocao**

**Descrição:** Tipo de item consumível que causa algum efeito ao personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_item | INT | PRIMARY KEY |
| efeito | DECIMAL(1,3) | NOT NULL |
| duracao | INT | NOT NULL CHECK (duracao >= 0) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_item | tipo_item | id_item |

---

### **Inimigo**

**Descrição:** Representa os dados armazenados do NPC do tipo Inimigo.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_inimigo | INT | NOT NULL UNIQUE |
| id_armazenamento | INT | NOT NULL REFERENCES armazenamento(id_armazenamento) |
| elemento | VARCHAR(5) | NOT NULL |
| descricao | TEXT | NOT NULL |
| vida_maxima | INT | NOT NULL |
| xp_obtido | INT | NOT NULL |
| inteligencia | INT | NOT NULL |
| dialogo | TEXT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_inimigo | tipo_npc | id_npc |

---

### **Inimigo Instancia**

**Descrição:** Instancia de um Inimigo.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_inimigo_instancia | SERIAL | PRIMARY KEY |
| id_npc | INT | NOT NULL |
| id_subregiao | INT | NOT NULL REFERENCES sub_regiao(id_subregiao) |
| vida_atual | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_npc | inimigo | id_inimigo |

---

### **Combate**

**Descrição:** Representa o combate entre um inimigo e o personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_inimigo_instancia | INT | NOT NULL |
| id_personagem | INT | NOT NULL |
| dano_causado | INT | NOT NULL |
| dano_recebido | INT | NOT NULL |
| PRIMARY | KEY | (id_inimigo_instancia, id_personagem) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_inimigo_instancia | inimigo_instancia | id_inimigo_instancia |
| id_personagem | personagem | id_personagem |

---

### **Feitiço escrito**

**Descrição:** Representa o tipo de feitico presente em algum item.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_item | INT | NOT NULL REFERENCES tipo_item(id_item) |
| id_feitico | INT | NOT NULL |
| dano_causado | INT | NOT NULL REFERENCES feitico(id_feitico) |
| PRIMARY | KEY | (id_item, id_feitico) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_item | tipo_item | id_item |
| id_feitico | feitico | id_feitico |

---

### **Feitico Aprendido**

**Descrição:** Representa o feitiço aprendido pelo personagem, armazenado em seu grimório.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id_inventario | INT | NOT NULL |
| id_feitico | INT | NOT NULL |
| PRIMARY | KEY | (id_inventario, id_feitico) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_inventario | inventario | id_inventario |
| id_feitico | feitico | id_feitico |

---

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 25/11/2024 | Criação   | Grupo |
| `1.1`  | 04/01/2025 | Arrumando entidades e restrições   | Grupo |