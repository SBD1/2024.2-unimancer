# Dicionário de Dados

## Entidades e Atributos

### **1. Personagem**

**Descrição:** Representa os personagens do jogo, contendo atributos básicos e progressos.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idPersonagem|Identificador único do personagem|INT|-|PRIMARY KEY, IDENTITY|
|idInstanciaCriatura|Relacionamento com uma criatura|INT|-|FOREIGN KEY REFERENCES `Instancia_Criatura`|
|idProgresso|Relacionamento com progresso|INT|-|FOREIGN KEY REFERENCES `Progresso_personagem`|
|nome|Nome do personagem|VARCHAR|100|NOT NULL|
|elemento|Elemento associado ao personagem|VARCHAR|50|CHECK (elemento IN ('Fogo', 'Água', etc.))|
|nivel|Nível atual do personagem|INT|-|NOT NULL, CHECK (nivel >= 1)|
|pontosDeVidaAtual|Pontos de vida restantes|INT|-|DEFAULT 0, CHECK (pontosDeVidaAtual >= 0)|
|energiaArcanaAtual|Energia mágica disponível|INT|-|DEFAULT 0, CHECK (energiaArcanaAtual >= 0)|
|conhecimentoArcano|Conhecimento arcano disponível|INT|-|DEFAULT 0, CHECK (conhecimentoArcano >= 0)|
|inteligencia|Inteligência do personagem|INT|-|DEFAULT 0, CHECK (inteligencia >= 0)|
|moedas|Quantidade de moedas disponíveis|INT|-|DEFAULT 0, CHECK (moedas >= 0)|

---

### **2. Criatura**

**Descrição:** Define as criaturas do jogo, incluindo seus atributos principais.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idCriatura|Identificador único da criatura|INT|-|PRIMARY KEY, IDENTITY|
|pontosDeVidaMaximos|Pontos de vida máximos da criatura|INT|-|NOT NULL, CHECK (pontosDeVidaMaximos >= 0)|
|nivel|Nível da criatura|INT|-|NOT NULL, CHECK (nivel >= 0)|
|energiaArcanaMaxima|Energia mágica máxima da criatura|INT|-|DEFAULT 0, CHECK (energiaArcanaMaxima >= 0)|
|XP|XP da criatura|INT|-|DEFAULT 0, CHECK (XP >= 0)|
|pontosDeVida|Energia pontos de vida da criatura|INT|-|DEFAULT 0, CHECK (pontosDeVida >= 0)|
|moedas|Quantidade de moedas disponíveis|INT|-|DEFAULT 0, CHECK (moedas >= 0)|

---

### **3. Inventário**

**Descrição:** Representa o inventário de itens associados a um personagem.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idInventario|Identificador único do inventário|INT|-|PRIMARY KEY, IDENTITY|
|idPersonagem|Identificador do personagem|INT|-|FOREIGN KEY REFERENCES `Personagem`|

---

### **4. Item**

**Descrição:** Representa itens que podem ser armazenados no inventário.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idItem|Identificador único do item|INT|-|PRIMARY KEY, IDENTITY|
|idInventario|Identificador do inventário|INT|-|FOREIGN KEY REFERENCES `Inventário`|
|nome|Nome do item|VARCHAR|100|NOT NULL|
|peso|Peso do item|FLOAT|-|DEFAULT 0, CHECK (peso >= 0)|
|preco|Preço do item|FLOAT|-|DEFAULT 0, CHECK (preco >= 0)|
|chanceDrop|chance de drop do item|INT|-|DEFAULT 0, CHECK (chanceDrop >= 0)|

---

### **5. Mochila**

**Descrição:** Representa mochilas que armazenam itens e possuem limite de peso.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idMochila|Identificador único da mochila|INT|-|PRIMARY KEY, IDENTITY|
|idInventario|Relacionamento com inventário|INT|-|FOREIGN KEY REFERENCES `Inventário`|
|pesoMaximo|Peso máximo suportado pela mochila|FLOAT|-|NOT NULL, CHECK (pesoMaximo >= 0)|
|pesoAtual|Peso atual da mochila|FLOAT|-|NOT NULL, CHECK (pesoAtual >= 0)|

---

### **6. Região**

**Descrição:** Representa regiões do mapa onde locais podem ser encontrados.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idRegiao|Identificador único da região|INT|-|PRIMARY KEY, IDENTITY|
|nome|Nome da região|VARCHAR|100|NOT NULL|
|descricao|Descrição da região|TEXT|-|-|
|elementoRegiao|Elemento da região|TEXT|-|CHECK (elemento IN ('Fogo', 'Água', etc.))|

---

### **7. Local**

**Descrição:** Representa locais onde os jogadores podem interagir.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idLocal|Identificador único do local|INT|-|PRIMARY KEY, IDENTITY|
|idRegiao|Identificador da região|INT|-|FOREIGN KEY REFERENCES `Regiao`|
|idInstanciaItem|Identificador da instancia de item|INT|-|FOREIGN KEY REFERENCES `Instancia_item`|
|nome|Nome do local|VARCHAR|100|NOT NULL|
|descricao|Descrição do local|TEXT|-|-|

---

### **8. NPC**

**Descrição:** Representa personagens não jogáveis.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idNPC|Identificador único do NPC|INT|-|PRIMARY KEY, IDENTITY|
|idLocal|Relacionamento com local|INT|-|FOREIGN KEY REFERENCES `Local`|
|nome|Nome do NPC|VARCHAR|100|NOT NULL|
|dialogo|Texto de diálogo do NPC|TEXT|-|-|

### **9. Grimório**

**Descrição:** Representa grimórios que podem ser encontrados e usados para adquirir novas habilidades.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idGrimorio|Identificador único do grimório|INT|-|PRIMARY KEY, IDENTITY|
|idInventario|Relacionamento com inventário|INT|-|FOREIGN KEY REFERENCES `Inventário`|
|numPaginas|Número de páginas do grimório|INT|-|NOT NULL, CHECK (numPaginas > 0)|

---

### **10. Poção**

**Descrição:** Representa itens consumíveis do tipo poção.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idPocao|Identificador único da poção|INT|-|PRIMARY KEY, IDENTITY|
|idItemConsumivel|Relacionamento com item consumível|INT|-|FOREIGN KEY REFERENCES `item_nao_consumivel`|
|efeito|Efeito da poção|TEXT|-|NOT NULL|
|duracao|Duração do efeito (em segundos)|INT|-|NOT NULL, CHECK (duracao > 0)|

---

### **11. Pergaminho**

**Descrição:** Representa pergaminhos mágicos com feitiços.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idPergaminho|Identificador único do pergaminho|INT|-|PRIMARY KEY, IDENTITY|
|idItemConsumivel|Relacionamento com item consumível|INT|-|FOREIGN KEY REFERENCES `item_nao_consumivel`|
|cor|Cor do pergaminho|VARCHAR|50|NOT NULL|
|descricao|Descrição do pergaminho|TEXT|-|-|

---

### **12. Feitiço**

**Descrição:** Representa feitiços disponíveis no jogo, vinculados a pergaminhos.

| Nome                    | Descrição                      | Tipo de Dado | Tamanho | Restrição de Domínio                          |
| ----------------------- | ------------------------------ | ------------ | ------- | --------------------------------------------- |
| idFeitico               | Identificador único do feitiço | INT          | -       | PRIMARY KEY, IDENTITY                         |
| idPergaminho            | Relacionamento com pergaminho  | INT          | -       | FOREIGN KEY REFERENCES `Pergaminho`           |
| elemento                | Elemento do feitiço            | VARCHAR      | 50      | CHECK (elemento IN ('Fogo', 'Água', etc.))    |
| energiaArcanaNecessaria | Energia arcana necessária      | INT          | -       | NOT NULL, CHECK (energiaArcanaNecessaria > 0) |

---

### **13. Instância de Item**

**Descrição:** Representa uma instância de item, que pode ser vinculada a um inventário.

| Nome            | Descrição                          | Tipo de Dado | Tamanho | Restrição de Domínio          |
| --------------- | ---------------------------------- | ------------ | ------- | ----------------------------- |
| idInstanciaItem | Identificador único da instância   | INT          | -       | PRIMARY KEY, IDENTITY         |
| idItem          | Relacionamento com a tabela `Item` | INT          | -       | FOREIGN KEY REFERENCES `Item` |

---

### **14. Item Não-Consumível**

**Descrição:** Representa itens que possuem atributos específicos, como bônus e penalidades, mas não podem ser consumidos.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idItemNaoConsumivel|Identificador único do item|INT|-|PRIMARY KEY, IDENTITY|
|idItem|Relacionamento com a tabela `Item`|INT|-|FOREIGN KEY REFERENCES `Item`|
|buff|Valor de bônus do item|INT|-|DEFAULT 0, CHECK (buff >= 0)|
|debuff|Valor de penalidade do item|INT|-|DEFAULT 0, CHECK (debuff >= 0)|

---
### **15. Inimigo**

**Descrição:** Representa um NPC hostil no jogo derivada de `Criatura`.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idInimigo|Identificador único do inimigo|INT|-|PRIMARY KEY, IDENTITY|
|idNPC|Relacionamento com a tabela `NPC`|INT|-|FOREIGN KEY REFERENCES `NPC`|
|idInstanciaCriatura|Relacionamento com `Instancia_Criatura`|INT|-|FOREIGN KEY REFERENCES `Instancia_Criatura`|
|elemento|Elemento principal do inimigo|VARCHAR|50|CHECK (elemento IN ('Fogo', 'Água', etc.))|
|pontosDeVidaTotal|Pontos de vida totais do inimigo|INT|-|NOT NULL, CHECK (pontosDeVidaTotal >= 0)|
|inteligencia|Inteligência do inimigo|INT|-|DEFAULT 0, CHECK (inteligencia >= 0)|

---
### **16. Mercador**

**Descrição:** Representa um NPC que atua como comerciante no jogo.

|Nome|Descrição|Tipo de Dado|Tamanho|Restrição de Domínio|
|---|---|---|---|---|
|idMercador|Identificador único do mercador|INT|-|PRIMARY KEY, IDENTITY|
|idNPC|Relacionamento com a tabela `NPC`|INT|-|FOREIGN KEY REFERENCES `NPC`|
|elemento|Elemento principal do mercador|VARCHAR|50|CHECK (elemento IN ('Fogo', 'Água', etc.))|
| Vendas | Quantidade de Itens disponíveis | INT | - | -

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 25/11/2024 | Criação   | Grupo |
