from colorama import Style, Fore
import database.dql.query as query
from character import Character

def display(character, conn):
    print(f"Inventário de === {character.nome} ===")
    print("-" * 40)

    items = query.list_item_inventory(conn, character.id)

    if not items:
       print("O inventário está vazio.")
    else:
       for item in items:
           nome, descricao, qtd = item
           print(f"- {nome} ({descricao}) - {qtd}")
    
    print("-" * 40)

# Display player header information.
def header(character: Character):
    print(f"=== {character.nome} === vida: {character.vida}/{character.vida_maxima} "
          f"energia arcana: {character.energia_arcana}/{character.energia_arcana_maxima} "
          f"moedas: {character.moedas} xp: {character.xp}/{character.xp_total} ===")

# Display player spells
def list_spells(conn, spells):
    print(Style.BRIGHT + Fore.CYAN + f"\n--- Feitiços Disponíveis ---\n" + Style.RESET_ALL)
    
    if not spells:
        print(Fore.RED + "Nenhum feitiço aprendido." + Style.RESET_ALL)
    else:
        for descricao, custo in spells:
            print(Fore.CYAN + f"  Custo de energia: {custo}" + Style.RESET_ALL)
            print(f"  {descricao}")
            print("-" * 40)
    
    input("\nPressione Enter para continuar...")

