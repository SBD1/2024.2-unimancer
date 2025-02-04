<p align="center">
  <img alt="Unimancer Logo" src="./docs/img/logo.png" width="200"/>
</p>

## Alunos

| Matrícula  | Aluno                                  | Usuário                                               | Foto de Perfil                                      |
| ---------- | -------------------------------------- | ---------------------------------------------------- | -------------------------------------------------- |
| 22/1022604 | João Victor da Silva Batista de Farias | [@beyondmagic](https://github.com/beyondmagic)       | ![João](https://github.com/beyondmagic.png?size=50) |
| 20/2046283 | Millena de Abreu Queiroz               | [@MillenaQueiroz](https://github.com/MillenaQueiroz) | ![Millena](https://github.com/MillenaQueiroz.png?size=50) |
| 22/2006169 | Natan da Cruz Almeida                  | [@natanalmeida03](https://github.com/natanalmeida03) | ![Natan](https://github.com/natanalmeida03.png?size=50) |
| 22/1022408 | Paulo Henrique Lamounier Dantas        | [@Nanashii76](https://github.com/Nanashii76)         | ![Paulo](https://github.com/Nanashii76.png?size=50) |
| 22/1031363 | Renan Vieira Guedes                    | [@R-enanVieira](https://github.com/R-enanVieira)     | ![Renan](https://github.com/R-enanVieira.png?size=50) |

## Sobre 

**Unimancer** é um jogo estilo **MUD (Multi-User Dungeon)**, offline e baseado em texto, onde você é lançado em um mundo mágico profundo e imersivo, em que magos lendários buscam o poder absoluto, o segredo perdido dos elementos e os mais arcanos conhecimentos.

Há milênios, o frágil equilíbrio entre os elementos sustentava o vasto império de Arcanae. Os Unimancers, magos dedicados, eram os guardiões desse equilíbrio. Eles dominavam os elementos mais poderosos, consagrando-se ao estudo incansável, à criação de magias ancestrais e à descoberta de runas que datam da origem do mundo. Cada mago era um pilar de seu próprio elemento, zelando para que o tecido cósmico não se rasgasse.

Porém, com o tempo, o mestre mago **Nosferus** foi consumido pela insaciável sede de poder e conhecimento. Cansado das limitações impostas pelas especializações, ele partiu para uma jornada ousada e traiçoeira: reunir todos os pergaminhos arcanos deixados pelos antigos magos nas dungeons que permeiam as terras de Arcanae. Diz-se que esses pergaminhos escondem os segredos das forças elementares que controlam a própria existência. Nosferus desapareceu nas sombrias profundezas da Floresta do Abismo, onde as lendas afirmam que os maiores conhecimentos estão ocultos — protegidos por enigmas mortais e criaturas impiedosas. Muitos ousaram seguir seus passos, mas nenhum retornou.

Agora, os magos, especializados em um único elemento, estão espalhados pelo mundo, buscando não só o conhecimento perdido, mas também o domínio absoluto sobre as forças que governam tudo ao seu redor. Sua missão é simples, mas mortal: recuperar a sabedoria esquecida, dominar a árvore de habilidades ancestral e, assim, restaurar ou corromper o frágil equilíbrio dos elementos. A cada passo, o destino de Arcanae está por um fio.

Será você o herói que trará a harmonia de volta ou o vilão que mergulhará o mundo na ~~destruição e no caos~~? 

[**Dicionário de dados**](https://sbd1.github.io/2024.2-unimancer/modelagem/dd/)

## Apresentações

1. [Entrega de DER, MER, MR e DD](https://youtu.be/rYFDGP1GFUo);
2. [Entrega do SQL](https://youtu.be/2Z54N1kAIhc);
3. [Entrega dos procedures / triggers - Jogo ](https://youtu.be/bLv0QaH3tVg);

## Screenshots

### Módulo 1

**Diagrama de Entidade-Relacionamento**

<img alt="Diagrama de Entidade-Relacionamento" src="./docs/modulo 1/v2_der.drawio.png"/>

**Modelo Relacionamento**

<img alt="Modelo Relacionamento" src="./docs/modulo 1/v1_mr.drawio.png"/>

### Módulo 2

**Diagrama de Entidade-Relacionamento**

<img alt="Diagrama de Entidade-Relacionamento" src="./docs/modulo 1/v1_mr.drawio.png"/>

**Modelo Relacionamento**

<img alt="Modelo Relacionamento" src="./docs/modulo 2/v2_MR.drawio.png"/>

## Instalação

**Tecnologia:** PostgreSQL, python;

**Modelo do Banco:** [draw.io](https://drive.google.com/file/d/14wc0GC0F9QGjhKfZOi1-kghpwYJfIDvr/view?usp=drive_link);

Descreva os pré-requisitos para rodar o seu projeto e os comandos necessários.

## Uso 

Para executar o projeto, inicialmente clone o repositório usando

    > git clone https://github.com/SBD1/2024.2-unimancer

Após clonar seu repositório, certifique-se de estar com o docker e o python instalado, para verificar basta utilizar

    > python --version

    > docker --version

Caso não tenha, acesse a documentação para instalar [docker](https://docs.docker.com/) [python](https://www.python.org/)

Entrando no diretório do projeto, primeiro precisamos configurar o ambiente para roda-lo. Para isso, execute o comando a seguir:

    > make config

Após isso, será necessário subir os containers, onde temos o banco de dados por trás do projeto e o PgAdmin, que é uma interface para visualizar o banco

    > make build

para gerar o docker, o arquivo está configurado para utilizar a porta **5432** para o banco de dados e a porta **5050** para a interface do pg admin, certifique-se de estar com essas portas livres ou edite-as no arquivo `docker-compose.yml`

Agora para definitivamente embarcar nessa jornada, basta executar o programa em seu terminal utilizando

    > make int reset
    > make int

## Outros
### **Mecânicas do Jogo**
- Atacar inimigo;
- Comprar e/ou vender itens;

#### **Criação de Personagem**

- Personalize seu personagem escolhendo seu nome e especialização mágica.
- Escolha entre os quatro elementos disponíveis:
    - **Água**: Magias de líquidos e manipulação de fluxo;
    - **Fogo**: Magias destrutivas e agressivas;
    - **Terra**: Defesa e resistência inigualáveis;
    - **Vento**: Velocidade e controle estratégico;
    - **Luz**: Magia arcana antiga, garante bençãos ao usuário;
    - **Trevas**: Magia condenada, utilizada por magos corrompidos;

---

#### **Progressão**

- Explore um grafo de habilidades único, desbloqueando magias avançadas ao encontrar **grimórios mágicos** e completar **quests**.
- Resolva desafios em **dungeons** para ganhar **conhecimento arcano** e pontos de habilidade.

---

#### **Combate Estratégico**

- Sistema de combate **turn-based** com foco em buffs, debuffs e exploração de fraquezas elementais.
- Cada inimigo tem um elemento próprio que pode ser explorado para vantagem estratégica.

---

#### **Exploração e Descoberta**

- Viaje por regiões mágicas, cada uma oferecendo buffs ou debuffs baseados na sua especialização.
- Áreas podem estar bloqueadas até que certas condições sejam atendidas.

---

#### **NPCs e Quests**

- Interaja com NPCs que oferecem quests e lore adicionais.
- Complete tarefas para desbloquear recompensas, como equipamentos raros e dicas sobre novas áreas.

---

#### **Sistema de Inventário**

- Gerencie um inventário limitado, organizando itens importantes como pergaminhos, poções e armas mágicas.
- Recursos escassos incentivam escolhas estratégicas.

---

#### **Salvar e Continuar**

- Progresso salvo automaticamente ao descansar em áreas seguras ou concluir tarefas importantes.

--- 

### **Regiões do Jogo**

| **ID** | **Nome**                  | Região                      |
| :----: | ------------------------- | --------------------------- |
|   1    | Ferraria do Albnur        | Vilarejo do Amanhecer       |
|   2    | Praça Central             |                             |
|   3    | Casa do Ancião            |                             |
|   4    | Taberna da Caneca Partida |                             |
|   5    | Clareira dos Espíritos    | Floresta Eterna             |
|   6    | Bosque Sombrio            |                             |
|   7    | Lago da Serenidade        |                             |
|   8    | Ruínas Perdidas           |                             |
|   9    | Fenda do Abismo           | Ruínas do Abismo            |
|  10    | Praça das Estátuas        |                             |
|  11    | Entrada da Ruína          |                             |
|  12    | Santuário Perdido         |                             |
|  13    | Oásis dos Mercadores      | Deserto de Areias Infinitas |
|  14    | Vale das Serpentes        |                             |
|  15    | Ruínas Submersas          |                             |
|  16    | Caverna de Cristal        |                             |
|  17    | Trono de Cristal          | Caverna Cristalizada        |
|  18    | Núcleo Cristalino         |                             |
|  19    | Vale da Fortuna           |                             |
|  20    | Entrada Cristalizada      |                             |
|  21    | Pico Congelado            | Montanha do Crepúsculo      |
|  22    | Vilarejo dos Gigantes     |                             |
|  23    | Ponte Suspensa            |                             |
|  24    | Cavernas Ecoantes         |                             |
|  25    | Vila Esquecida            | Caverna Soterrada           |
|  26    | Bosque Perdido            |                             |
|  27    | Monte Caído               |                             |
|  28    | Jardim de Ossos           |                             |
|  29    | Catedral Queimada         | Terras Devastadas           |
|  30    | Planícies de Cinzas       |                             |
|  31    | Fenda Arcana              |                             |
|  32    | Cemitério                 |                             |

---

## Tabela de Inimigos

| **ID** | **Nome**               | **Elemento** | **Vida Máxima** | **XP Obtido** | **Moedas Obtidas** | **Conhecimento Arcano** | **Energia Arcana Máxima** | **Inteligência** |
| ------ | ---------------------- | ------------ | --------------- | ------------- | ------------------ | ----------------------- | ------------------------- | ---------------- |
| 1      | Rato Selvagem          | Terra        | 20              | 5             | 2                  | 0                       | 0                         | 1                |
| 2      | Corvo Guardião         | Ar           | 25              | 8             | 3                  | 0                       | 0                         | 2                |
| 3      | Ladrão de Rua          | Trevas       | 30              | 10            | 5                  | 0                       | 0                         | 3                |
| 4      | Lobo Sombrio           | Trevas       | 50              | 20            | 10                 | 0                       | 0                         | 4                |
| 5      | Espírito da Clareira   | Luz          | 40              | 15            | 0                  | 10                      | 20                        | 5                |
| 6      | Ent Ancião             | Terra        | 70              | 25            | 15                 | 5                       | 10                        | 3                |
| 7      | Guardião de Pedra      | Terra        | 80              | 30            | 20                 | 0                       | 0                         | 2                |
| 8      | Serpente das Sombras   | Trevas       | 60              | 25            | 10                 | 5                       | 10                        | 4                |
| 9      | Espectro do Abismo     | Trevas       | 50              | 20            | 5                  | 20                      | 30                        | 8                |
| 10     | Escorpião Gigante      | Terra        | 90              | 35            | 15                 | 0                       | 0                         | 3                |
| 11     | Djin Traiçoeiro        | Fogo         | 60              | 30            | 20                 | 15                      | 40                        | 10               |
| 12     | Caravaneiro Corrompido | Luz          | 70              | 30            | 25                 | 5                       | 10                        | 6                |
| 13     | Golem de Cristal       | Terra        | 150             | 70            | 30                 | 5                       | 10                        | 3                |
| 14     | Minerador Fantasma     | Trevas       | 80              | 50            | 20                 | 15                      | 30                        | 6                |
| 15     | Afortunado             | Luz          | 100             | 60            | 40                 | 20                      | 40                        | 10               |
| 16     | Gigante Congelado      | Água         | 120             | 50            | 30                 | 5                       | 15                        | 5                |
| 17     | Águia do Crepúsculo    | Ar           | 80              | 40            | 20                 | 10                      | 25                        | 7                |
| 18     | Espírito da Geada      | Água         | 70              | 35            | 10                 | 20                      | 50                        | 9                |
| 19     | Guerreiro Esqueleto    | Trevas       | 70              | 35            | 15                 | 5                       | 0                         | 3                |
| 20     | Feiticeiro Esqueleto   | Trevas       | 60              | 40            | 10                 | 25                      | 50                        | 12               |
| 21     | Goblin Zumbi           | Trevas       | 50              | 20            | 5                  | 0                       | 0                         | 2                |
| 22     | Guerreiro Corrompido   | Trevas       | 100             | 60            | 50                 | 10                      | 20                        | 7                |
| 23     | Fera Flamejante        | Fogo         | 110             | 55            | 40                 | 15                      | 30                        | 8                |
| 24     | Dragão da Devastação   | Trevas       | 200             | 100           | 100                | 50                      | 100                       | 20               |

---

## Tabela de Bosses

| **ID** | **Nome**   | **Elemento** | **Vida Máxima** | **XP Obtido** | **Moedas Obtidas** | **Conhecimento Arcano** | **Energia Arcana Máxima** | **Inteligência** |
| :----: | ---------- | ------------ | --------------- | ------------- | ------------------ | ----------------------- | ------------------------- | ---------------- |
|   25   | Abgail     | Fogo         | 150             | 60            | 75                 | 100                     | 100                       | 12               |
|   26   | Lumina     | Luz          | 180             | 75            | 90                 | 120                     | 90                        | 15               |
|   27   | Necromante | Trevas       | 200             | 85            | 100                | 110                     | 120                       | 14               |
|   28   | Nosferus   | Trevas       | 220             | 100           | 125                | 130                     | 80                        | 18               |
