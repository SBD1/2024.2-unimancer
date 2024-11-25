# Dicionário de Dados

## Entidades e Atributos

### 1. Personagem
**Descrição:** Representa os personagens do jogo, contendo atributos básicos e progressos.

| Nome                | Descrição                          | Tipo de Dado | Tamanho  | Restrição de Domínio                          |
|---------------------|------------------------------------|--------------|----------|----------------------------------------------|
| idPersonagem        | Identificador único do personagem | INT          | -        | PRIMARY KEY, IDENTITY                        |
| idInstanciaCriatura | Relacionamento com uma criatura   | INT          | -        | FOREIGN KEY REFERENCES `Instancia_Criatura`  |
| idProgresso | Relacionamento com progresso  | INT          | -        | FOREIGN KEY REFERENCES `Progresso_personagem`  |
| nome                | Nome do personagem                | VARCHAR      | 100      | NOT NULL                                     |
| elemento            | Elemento associado ao personagem  | VARCHAR      | 50       | CHECK (elemento IN ('Fogo', 'Água', etc.))   |
| nivel               | Nível atual do personagem         | INT          | -        | NOT NULL, CHECK (nivel >= 1)                 |
| pontosDeVidaAtual   | Pontos de vida restantes          | INT          | -        | DEFAULT 0, CHECK (pontosDeVidaAtual >= 0)    |
| energiaArcanaAtual  | Energia mágica disponível         | INT          | -        | DEFAULT 0, CHECK (energiaArcanaAtual >= 0)   |
| conhecimentoArcano  | Conhecimento arcano disponível         | INT          | -        | DEFAULT 0, CHECK (conhecimentoArcano >= 0)   |
| inteligencia        | Inteligência do personagem        | INT          | -        | DEFAULT 0, CHECK (inteligencia >= 0)         |
| moedas              | Quantidade de moedas disponíveis  | INT          | -        | DEFAULT 0, CHECK (moedas >= 0)               |

---

### 2. Instancia_Criatura
**Descrição:** Relaciona uma criatura a um personagem com base em atributos e estatísticas.

| Nome                | Descrição                          | Tipo de Dado | Tamanho  | Restrição de Domínio                          |
|---------------------|------------------------------------|--------------|----------|----------------------------------------------|
| idInstanciaCriatura | Identificador único da instância  | INT          | -        | PRIMARY KEY, IDENTITY                        |
| idCriatura          | Identificador da criatura         | INT          | -        | FOREIGN KEY REFERENCES `Criatura`            |

---

### 3. Criatura
**Descrição:** Define as criaturas do jogo, incluindo seus atributos principais.

| Nome                | Descrição                          | Tipo de Dado | Tamanho  | Restrição de Domínio                          |
|---------------------|------------------------------------|--------------|----------|----------------------------------------------|
| idCriatura          | Identificador único da criatura   | INT          | -        | PRIMARY KEY, IDENTITY                        |
| pontosDeVidaMaximos | Pontos de vida máximos da criatura | INT          | -        | NOT NULL, CHECK (pontosDeVidaMaximos >= 0)   |
| nivel               | Nível da criatura                 | INT          | -        | NOT NULL, CHECK (nivel >= 0)                 |
| energiaArcanaMaxima | Energia mágica máxima da criatura | INT          | -        | DEFAULT 0, CHECK (energiaArcanaMaxima >= 0)  |
| XP | XP da criatura | INT          | -        | DEFAULT 0, CHECK (XP >= 0)  |
| pontosDeVida | Energia pontos de vida da criatura | INT          | -        | DEFAULT 0, CHECK (pontosDeVida >= 0)  |
| moedas              | Quantidade de moedas disponíveis  | INT          | -        | DEFAULT 0, CHECK (moedas >= 0)               |

---

### 4. Inventário
**Descrição:** Representa o inventário de itens associados a um personagem.

| Nome                | Descrição                          | Tipo de Dado | Tamanho  | Restrição de Domínio                          |
|---------------------|------------------------------------|--------------|----------|----------------------------------------------|
| idInventario        | Identificador único do inventário | INT          | -        | PRIMARY KEY, IDENTITY                        |
| idPersonagem        | Identificador do personagem       | INT          | -        | FOREIGN KEY REFERENCES `Personagem`          |

---

### 5. Item
**Descrição:** Representa itens que podem ser armazenados no inventário.

| Nome                | Descrição                          | Tipo de Dado | Tamanho  | Restrição de Domínio                          |
|---------------------|------------------------------------|--------------|----------|----------------------------------------------|
| idItem              | Identificador único do item       | INT          | -        | PRIMARY KEY, IDENTITY                        |
| idInventario        | Identificador do inventário       | INT          | -        | FOREIGN KEY REFERENCES `Inventário`          |
| nome                | Nome do item                      | VARCHAR      | 100      | NOT NULL                                     |
| peso                | Peso do item                      | FLOAT        | -        | DEFAULT 0, CHECK (peso >= 0)                 |
| preco               | Preço do item                     | FLOAT        | -        | DEFAULT 0, CHECK (preco >= 0)                |
| chanceDrop               | chance de drop do item                    | INT        | -        | DEFAULT 0, CHECK (chanceDrop >= 0)                |

---

### 6. Mochila
**Descrição:** Representa mochilas que armazenam itens e possuem limite de peso.

| Nome                | Descrição                          | Tipo de Dado | Tamanho  | Restrição de Domínio                          |
|---------------------|------------------------------------|--------------|----------|----------------------------------------------|
| idMochila           | Identificador único da mochila    | INT          | -        | PRIMARY KEY, IDENTITY                        |
| idInventario        | Relacionamento com inventário     | INT          | -        | FOREIGN KEY REFERENCES `Inventário`          |
| pesoMaximo          | Peso máximo suportado pela mochila | FLOAT       | -        | NOT NULL, CHECK (pesoMaximo >= 0)            |
| pesoAtual        | Peso atual da mochila | FLOAT       | -        | NOT NULL, CHECK (pesoAtual >= 0)            |

---

### 7. Região
**Descrição:** Representa regiões do mapa onde locais podem ser encontrados.

| Nome                | Descrição                          | Tipo de Dado | Tamanho  | Restrição de Domínio                          |
|---------------------|------------------------------------|--------------|----------|----------------------------------------------|
| idRegiao            | Identificador único da região     | INT          | -        | PRIMARY KEY, IDENTITY                        |
| nome                | Nome da região                    | VARCHAR      | 100      | NOT NULL                                     |
| descricao           | Descrição da região               | TEXT         | -        | -                                            |
| elementoRegiao           | Elemento da região               | TEXT         | -        | CHECK (elemento IN ('Fogo', 'Água', etc.))                                         |


---

### 8. Local
**Descrição:** Representa locais onde os jogadores podem interagir.

| Nome                | Descrição                          | Tipo de Dado | Tamanho  | Restrição de Domínio                          |
|---------------------|------------------------------------|--------------|----------|----------------------------------------------|
| idLocal             | Identificador único do local      | INT          | -        | PRIMARY KEY, IDENTITY                        |
| idRegiao            | Identificador da região           | INT          | -        | FOREIGN KEY REFERENCES `Regiao`              |
| idInstanciaItem           | Identificador da instancia de item           | INT          | -        | FOREIGN KEY REFERENCES `Instancia_item`              |
| nome                | Nome do local                     | VARCHAR      | 100      | NOT NULL                                     |
| descricao           | Descrição do local                | TEXT         | -        | -                                            |

---

### 9. NPC
**Descrição:** Representa personagens não jogáveis.

| Nome                | Descrição                          | Tipo de Dado | Tamanho  | Restrição de Domínio                          |
|---------------------|------------------------------------|--------------|----------|----------------------------------------------|
| idNPC               | Identificador único do NPC        | INT          | -        | PRIMARY KEY, IDENTITY                        |
| idLocal             | Relacionamento com local          | INT          | -        | FOREIGN KEY REFERENCES `Local`               |
| nome                | Nome do NPC                       | VARCHAR      | 100      | NOT NULL                                     |
| dialogo             | Texto de diálogo do NPC           | TEXT         | -        | -                                            |

## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 24/11/2024 | Criação   | Millena |
