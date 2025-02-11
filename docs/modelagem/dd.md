# Dicionário de Dados

## Tipos

### **TIPO_INVENTARIO**

- 'Mochila';
- 'Grimório'.

### **TIPO_ELEMENTO**

- 'Fogo';
- 'Água';
- 'Terra';
- 'Ar';
- 'Trevas';
- 'Luz'.

### **TIPO_DIFICULDADE**

- 'Iniciante';
- 'Fácil';
- 'Médio';
- 'Difícil';
- 'Legendário'.

### **TIPO_ITEM**

- 'Poção';
- 'Acessório'.

### **TIPO_FEITICO**

- 'Dano';
- 'Dano de área';
- 'Cura'.

### **TIPO_NPC**

- 'Civil';
- 'Inimigo'.

### **TIPO_CIVIL**

- 'Mercador';
- 'Quester'.

### **TIPO_DIRECAO**

- 'Norte';
- 'Sul';
- 'Leste';
- 'Oeste';
- 'Cima';
- 'Baixo'.

### **TIPO_SITUACAO**

- 'Passável';
- 'Não Passável'.

### **TIPO_ACESSORIO**

- 'Anel';
- 'Chapéu';
- 'Colar';
- 'Bracelete';
- 'Fivela';
- 'Luvas';
- 'Botas';
- 'Calça';
- 'Meias';
- 'Bengala';
- 'Manto'.

## Entidades e Atributos

### **Item**

**Descrição:** Informações referente ao item.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| descricao | TEXT | NOT NULL |
| chance_drop | INT | NOT NULL CHECK (chance_drop >= 0) |
| nome | VARCHAR(20) | NOT NULL |
| peso | INT | NOT NULL CHECK (peso >= 0) |
| preco | INT | NOT NULL CHECK (preco >= 0) |

---

### **Armazenamento**

**Descrição:** Itens guardados que podem acessados por um local ou NPC.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| item_id | INT | NOT NULL |
| id | INT | NOT NULL |
| quantidade | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| item_id | item | id |

---

### **Regiao**

**Descrição:** Representa as regiões acessíveis no jogo.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| nome | VARCHAR(50) | NOT NULL |
| descricao | TEXT | NOT NULL |
| elemento | TIPO_ELEMENTO | NOT NULL |

---

### **Sub-Regiao**

**Descrição:** Subconjunto de localidades de cada região.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| regiao_id | INT | NOT NULL |
| armazenamento_id | INT | - |
| nome | VARCHAR(50) | NOT NULL |
| descricao | TEXT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| regiao_id | regiao | id |

### **Sub-Regiao Conexao**

**Descrição:** Conexão entre sub-regiões.~

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| sub_regiao_1 | INT | NOT NULL |
| sub_regiao_2 | INT | NOT NULL |
| descricao | TIPO_DIRECAO | NOT NULL |
| situacao | TIPO_SITUACAO | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| sub_regiao_1 | regiao | id |
| sub_regiao_1 | regiao | id |

---

### **Sub-regiao Acessorio conexão**

**Descrição:**

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| sub_regiao1_id | INT | NOT NULL |
| sub_regiao2_id | INT | NOT NULL |
| acessorio_id | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| sub_regiao1_id | sub_regiao | id |
| sub_regiao2_id | sub_regiao | id |
| acessorio_id | acessorio | id |

---

### **Personagem**

**Descrição:** Representa os dados armazenados em cada personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| sub_regiao_id | INT | NOT NULL |
| nome | VARCHAR(20) | NOT NULL |
| elemento | TIPO_ELEMENTO | NOT NULL |
| conhecimento_arcano | INT | NOT NULL CHECK (conhecimento_arcano >= 0) |
| vida | INT | NOT NULL CHECK (vida >= 0) |
| vida_maxima | INT | NOT NULL CHECK (vida_maxima >= 0) |
| xp | INT | NOT NULL CHECK (xp >= 0) |
| xp_total | INT | NOT NULL CHECK (xp_total >= 0) |
| energia_arcana | INT | NOT NULL CHECK (energia_arcana >= 0) |
| energia_arcana_maxima | INT | NOT NULL CHECK (energia_arcana_maxima >= 0) |
| inteligencia | INT | NOT NULL CHECK (inteligencia >= 0) |
| moedas | INT | NOT NULL CHECK (moedas >= 0) |
| nivel | INT | NOT NULL CHECK (nivel >= 0) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| sub_regiao_id | sub_regiao | id |

---

### **Inventario**

**Descrição:** Tabela de inventário e seu respectivo tipo.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| personagem_id | INT | NOT NULL |
| tipo | TIPO_INVENTARIO | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| personagem_id | personagem | id |


---

### **Npc**

**Descrição:** Representa os dados armazenados na tabela.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| nome | VARCHAR(20) | NOT NULL |
| tipo | TIPO_NPC | NOT NULL |

___

### **Civil**

**Descrição:** Tipo de NPC iteragível, pertecente às cidades.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | NOT NULL |
| sub_regiao_id | INT | NOT NULL|
| descricao | TEXT | NOT NULL |
| tipo_civil | TIPO_CIVIL | - |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id | npc | id |
| sub_regiao_id | sub_regiao | id |

---

### **Quester**

**Descrição:** Tipo de NPC que oferece quest aos personagens.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | PRIMARY KEY |
| dialogo | TEXT | NOT NULL |
| num_quests | INT | NOT NULL CHECK (num_quests >= 0) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id | npc | id |

---

### **Quest**

**Descrição:** Representa cada missão ofertada pelos questers.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| quester_id | INT | NOT NULL |
| armazenamento_id | INT | NOT NULL |
| titulo | VARCHAR(20) | NOT NULL |
| descricao | TEXT | NOT NULL |
| recompensa | TEXT | NOT NULL |
| dificuldade | TIPO_DIFICULDADE | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| quester_id | quester | id |
| armazenamento_id | armazenamento | id |

---

### **Quest Instancia**

**Descrição:** Instância de cada quest aceita ou armazenada pelo personagem e quester.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| quest_id | INT | NOT NULL |
| personagem_id | INT | NOT NULL |
| completed | BOOLEAN | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| quest_id | quest | id |
| personagem_id | personagem | id |

---

### **Item Instancia**

**Descrição:** Instancia de cada item.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| item_id | INT | NOT NULL |
| inventario_id | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| item_id | item | id |
| inventario_id | inventario | id |

---

### **Mercador**

**Descrição:** Tipo de NPC que vende itens ao personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | PRIMARY KEY |
| armazenamento_id | INT | NOT NULL |
| dialogo | TEXT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id | npc | id |
| armazenamento_id | armazenamento | id |

---

### Armazenamento Mercador

**Descrição:** Tabela para armazenar a quantidade de itens do mercador.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| mercador_id | INT | NOT NULL |
| armazenamento_id | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| mercador_id | mercador | id |
| armazenamento_id | armazenamento | id |


### **Transacao**

**Descrição:** Representa cada compra/venda feita pelo personagem com o mercador.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| mercador_id | INT | NOT NULL |
| personagem_id | INT | NOT NULL |
| item_id | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| mercador_id | mercador | id |
| personagem_id | personagem | id |
| item_id | item | id |

---

### **Mochila**

**Descrição:** Tipo de inventário do personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| peso | INT | NOT NULL CHECK (peso <= peso AND peso >= 0) |
| peso_total | INT | NOT NULL CHECK (peso_total >= 0) |

---

### **Feitico**

**Descrição:** Dados do feitico, sendo ele seus requerimentos, energia arcana necessária, elemento e descrição.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| descricao | TEXT | NOT NULL |
| elemento | TIPO_ELEMENTO | NOT NULL |
| countdown | INT | NOT NULL CHECK (countdown >= 0) |
| energia_arcana_necessaria | INT | NOT NULL CHECK (energia_arcana_necessaria >= 0) |
| energia_arcana | INT | NOT NULL CHECK (energia_arcana >= 0) |
| tipo | TIPO_FEITICO | NOT NULL |

---

### **Feitico Requerido**

**Descrição:** O feitico que é requerido para ter outro feitico.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| de_id | INT | NOT NULL |
| para_id | TEXT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| de_id | feitico | id |
| para_id | feitico | id |

___

### **Feitico Dano**

**Descrição:** Tipo de feitiço que concede dano a um inimigo específico.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | PRIMARY KEY |
| dano_total | INT | NOT NULL CHECK (dano_total >= 0) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id | feitico | id |

---

### **Feitico Dano Area**

**Descrição:** Tipo de feitiço que concede dano em área em N inimigos.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | PRIMARY KEY |
| qtd_inimigos_afetados | INT | NOT NULL CHECK (qtd_inimigos_afetados >= 0) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id | feitico | id |

---

### **Feitico Cura**

**Descrição:** Tipo de feitiço que concede cura ao personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | PRIMARY KEY |
| qtd_cura | INT | NOT NULL CHECK (qtd_cura >= 0) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id | feitico | id |

---

### **Grimorio**

**Descrição:** Tipo de inventário dod personagem que contêm seus feitiços.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | PRIMARY KEY |
| num_pag | INT | NOT NULL CHECK (num_pag <= num_pag_maximo AND num_pag >= 0) |
| num_pag_maximo | INT | NOT NULL CHECK (num_pag_maximo >= 0) |


**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id | inventario | id |

___

### **Feitico Aprendido**

**Descrição:** Representa o feitiço aprendido pelo personagem, armazenado em seu grimório.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| inventario_id | INT | NOT NULL |
| feitico_id | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| invetario_id | inventario | id |
| feitico_id | feitico | id |

---

### **Pergaminho**

**Descrição:** Item do tipo consumível que ensina um feitiço para o personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | PRIMARY KEY |
| cor | VARCHAR(10) | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id | item | id |

___

### **Feitiço escrito**

**Descrição:** Representa o tipo de feitico presente em algum item.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| item_id | INT | NOT NULL |
| feitico_id | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| item_id | item | id |
| feitico_id | feitico | id |

---

### **Efeito**

**Descrição:** Efeitos que podem ser aplicados.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| nome | VARCHAR(20) | NOT NULL |
| descricao | TEXT | NOT NULL |
| critico | DECIMAL(1, 3) | NOT NULL |
| defesa | DECIMAL(1, 3) | NOT NULL |
| inteligencia | DECIMAL(1, 3) | NOT NULL 
| vida | DECIMAL(1, 3) | NOT NULL |
| energia_arcana | DECIMAL(1, 3) | NOT NULL |
| sorte | DECIMAL(1, 3) | NOT NULL |
| xp | DECIMAL(1, 3) | NOT NULL |
| moedas | DECIMAL(1, 3) | NOT NULL |

---

### **Acessorio**

**Descrição:** Tipo de item equipável que concede atributos ao personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | PRIMARY KEY |
| tipo | TIPO_ACESSORIO | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id | item | id |

---

### **Acessorio Efeito**

**Descrição:** Efeito que um acessório possui.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| acessorio_id | INT | NOT NULL |
| efeito_id | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| acessorio_id | item | id |
| efeito_id | efeito | id |

---

### **Pocao**

**Descrição:** Tipo de item consumível que causa algum efeito ao personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | PRIMARY KEY |
| turnos | INT | NOT NULL CHECK (duracao >= 0) |
| usado | BOOL | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id | item | id |

___

### **Pocao Efeito**

**Descrição:** Efeito que poção possui.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| pocao_id | INT | NOT NULL |
| efeito_id | DECIMAL(1,3) | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| pocao_id | pocao | id |
| efeito_id | efeito | id |

---

### **Inimigo**

**Descrição:** Representa os dados armazenados do NPC do tipo Inimigo.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | INT | NOT NULL UNIQUE |
| armazenamento_id | INT | NOT NULL |
| descricao | TEXT | NOT NULL |
| elemento | TIPO_ELEMENTO | NOT NULL |
| vida_maxima | INT | NOT NULL CHECK (vida_maxima >= 0) |
| xp_obtido | INT | NOT NULL CHECK (xp_obtido >= 0) |
| inteligencia | INT | NOT NULL CHECK (inteligencia >= 0) |
| modas_obtidas | INT | NOT NULL CHECK (moedas_obtidas >= 0) |
| conhecimento_arcano | INT | NOT NULL CHECK (conhecimento_arcano >= 0) |
| energia_arcana_maxima | INT | NOT NULL CHECK (energia_arcana_maxima >= 0) |
| dialogo | TEXT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| id_inimigo | tipo_npc | id_npc |
| armazenamento_id | armazenamento | id |

---

### Armazenamento Inimigo

**Descrição:** Armanezamento de itens do inimigo.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| inimigo_id | INT | NOT NULL |
| armazenamento_id | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| inimigo_id | inimigo | id |
| armazenamento_id | armazenamento | id |

---

### **Feitico Inimigo**

**Descrição:** Feitiços que inimigo possui.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| inimigo_id | INT | NOT NULL |
| efeito_id | INT | NOT NULL |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| inimigo_id | inimigo | id |
| efeito_id | efeito | id |

---

### **Inimigo Instancia**

**Descrição:** Instancia de um Inimigo.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| id | SERIAL | PRIMARY KEY |
| inimigo_id | INT | NOT NULL |
| sub_regiao_id | INT | NOT NULL |
| vida | INT | NOT NULL CHECK (vida >=0 ) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| inimigo_id | inimigo | id |
| sub_regiao_id | sub_regiao | id |

---

### **Combate**

**Descrição:** Representa o combate entre um inimigo e o personagem.

| Nome | Tipo de Dado | Restrições |
|------|--------------|------------|
| inimigo_instancia_id | INT | NOT NULL |
| personagem_id | INT | NOT NULL |
| dano_causado | INT | NOT NULL CHECK (dano_causado >= 0) |
| dano_recebido | INT | NOT NULL CHECK (dano_recebido >= 0) |

**Chaves Estrangeiras:**

| Coluna | Referencia Tabela | Referencia Coluna |
|--------|--------------------|-------------------|
| inimigo_instancia_id | inimigo_instancia | id |
| personagem_id | personagem | id |

---

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 25/11/2024 | Criação   | Grupo |
| `1.1`  | 04/01/2025 | Arrumando entidades e restrições   | Grupo |
| `3.0`  | 12/01/2025 | Arrumando entidades e restrições   | Grupo |
