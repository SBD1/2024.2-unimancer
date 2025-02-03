from colorama import Fore, Style
import time

from numpy import add

from database.dql.query import get_quest, get_civilian_info

class Quest:
    def __init__(self, conn):
        self.conn = conn  # Store the database connection
        self.quest_region_map = {  # Mapeamento de quests para regiões
            'Peste de Ratos': 'Floresta Eterna',
            'Ruínas do Abismo Aterrorizada': 'Ruínas do Abismo',
            # ... add mais quests e regiões conforme necessário, lembrar de atualizar instancia de inimigo na regiao
        }

    def show_quest(self, npc_name, npc_id, character_id):
        quest = get_quest(self.conn, npc_id)
        print(Fore.CYAN + f"\n Missão: {quest['title']}" + Style.RESET_ALL)
        print(Fore.CYAN + f"{quest['description']}" + Style.RESET_ALL)
        print('..')
        time.sleep(1)
        for line in quest['dialog'].split('\n'):
            print(f"{npc_name} diz: {line}")
            input("Pressione Enter para continuar...")
        self.add_quest(quest['quest_id'], character_id, quest['title'])

    def add_quest(self, quest_id, character_id, quest_title):
        try:
            with self.conn.cursor() as cur:
                region = self.quest_region_map.get(quest_title)
                cur.execute("SELECT create_new_instance_quest(%s::INT, %s::INT, %s::VARCHAR)", (quest_id, character_id, region))
                self.conn.commit()
                return self
        except Exception as e:
            self.conn.rollback()
            print(f"Erro ao adicionar quest: {e}")
