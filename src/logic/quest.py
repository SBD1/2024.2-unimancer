from colorama import Fore, Style
import time

from database.dql.query import get_quest, get_civilian_info

# This file contains the logic for creating and manage a quest
class Quest:
    # Add a quest to the database
    def add_quest(self, quester_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT create_quest_instance(%s, %s)", (quester_id, 1))
                self.conn.commit()
                print(f"Quest {self.nome} adicionada com sucesso!")
                return self
        except Exception as e:
            self.conn.rollback()
            print(f"Erro ao adicionar quest: {e}")
    
    def show_quest(self, conn, npc_name, npc_id):
        quest = get_quest(conn, npc_id)
        print(Fore.CYAN + f"\n Missão: {quest['title']}" + Style.RESET_ALL)
        print(Fore.CYAN + f"{quest['description']}" + Style.RESET_ALL)
        print('..')
        time.sleep(1)
        for line in quest['dialog'].split('\n'):
            print(f"{npc_name} diz: {line}")
            #Quest.add_quest(conn, npc_id, )
            input("Pressione Enter para continuar...")