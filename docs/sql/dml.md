# Data Manipulation Language - DML

## Introdução

DML é um conjunto de instruções SQL que permitem consultar, adicionar, editar e excluir dados de tabelas ou visualizações de banco de dados


### DML

#### Região

```sql
INSERT INTO regiao (nome, descricao, elemento) VALUES 
    ("Bosques dos Serafins", "Bosque com o alto índice de serafins.", "Fogo"),
    ("Deserto de Obsidiana", "Deserto com areias negras e calor extremo.", "Fogo"),
    ("Lago dos Espelhos", "Lago tranquilo com águas cristalinas.", "Água"),
    ("Planície dos Ventos", "Vasta planície com ventos constantes.", "Ar");
```

#### Sub-Região

```sql
-- Sub-regiões de "Bosques dos Serafins"
INSERT INTO sub_regiao (id_regiao, id_armazenamento, id_norte, id_leste, id_oeste, id_sul, nome, descricao) VALUES 
    (1, None, None, None, None, None, "Clareira Central", "Uma clareira iluminada no coração do bosque."),
    (1, None, 2, None, None, None, "Trilha Norte", "Uma trilha que leva ao norte do bosque.");

-- Sub-regiões de "Deserto de Obsidiana"
INSERT INTO sub_regiao (id_regiao, id_armazenamento, id_norte, id_leste, id_oeste, id_sul, nome, descricao) VALUES 
    (2, None, None, None, None, None, "Oásis Escondido", "Um pequeno oásis no meio do deserto."),
    (2, None, 6, None, None, None, "Dunas do Norte", "Dunas escaldantes ao norte do deserto.");

-- Sub-regiões de "Lago dos Espelhos"
INSERT INTO sub_regiao (id_regiao, id_armazenamento, id_norte, id_leste, id_oeste, id_sul, nome, descricao) VALUES 
    (3, None, None, None, None, None, "Ilha Central", "Uma ilha no centro do lago."),
    (3, None, 10, None, None, None, "Margem Norte", "A margem norte do lago.");

-- Sub-regiões de "Planície dos Ventos"
INSERT INTO sub_regiao (id_regiao, id_armazenamento, id_norte, id_leste, id_oeste, id_sul, nome, descricao) VALUES 
    (4, None, None, None, None, None, "Campo Aberto", "Um vasto campo aberto."),
    (4, None, 14, None, None, None, "Vale do Norte", "Um vale ao norte da planície.");
```


## Histórico de Versão

| Versão |     Data   | Descrição | Autor |
| :----: | :--------: | :-------: | :---: |
| `1.0`  | 13/01/2024 | Criação   | Grupo |