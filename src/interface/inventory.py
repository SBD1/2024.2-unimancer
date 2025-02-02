from colorama import Back, Style, Fore
import database.dql.query as query

def display(character, conn):
    print(Fore.GREEN + " "*30 +f"Inventário de === {character.nome} ===" + Style.RESET_ALL)
    print("\n")
    print(Fore.YELLOW + "-" * 80 + Style.RESET_ALL)

    items = query.list_item_inventory(conn, character.id)

    if not items:
       print("O inventário está vazio.")
    else:
       print(Fore.YELLOW + f"{'Tipo':<15} {'Nome':<20} {'Descrição':<30} {'Quantidade':<10}" + Style.RESET_ALL)
       print(Fore.YELLOW + "-" * 80 + Style.RESET_ALL)
       for item in items:
           tipo, nome, descricao, qtd = item
           print(f"{tipo:<15} {nome:<20} {descricao:<30} {qtd:<10}")
    
    print("-" * 80)

# Display player spells
def list_spells(conn, spells):
    print(Style.BRIGHT + Fore.CYAN + f"\n--- Feitiços Disponíveis ---\n" + Style.RESET_ALL)
    print(Fore.CYAN + "-" * 110 + Style.RESET_ALL)
    
    if not spells:
        print(Fore.RED + "Nenhum feitiço aprendido." + Style.RESET_ALL)
    else:
        for nome, tipo, descricao, custo, dano, *_ in spells:
            print(Fore.MAGENTA + f"{nome:<30} {tipo}" + Style.RESET_ALL)
            print(f"{descricao}")
            print(Fore.YELLOW + f"{'Custo de energia:':<30} {custo}" + Style.RESET_ALL)
            print(Fore.RED + f"{'Dano:':<30} {dano}" + Style.RESET_ALL)
            print(Fore.CYAN + "-" * 110 + Style.RESET_ALL)

    input("\nPressione Enter para continuar...")

