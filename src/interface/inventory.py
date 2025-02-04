from colorama import Back, Style, Fore
import database.dql.query as query
import interface.display as display

def list_items(character, conn):
    display.print_center(
        Fore.GREEN +
        f"Inventário de " +
        Style.BRIGHT +
        character.nome +
        Style.RESET_ALL
    )
    print()
    display.print_terminal_width("-")

    items = query.list_item_inventory(conn, character.id)

    if not items:
        print("O inventário está vazio.")
    else:
        print(
            Fore.YELLOW +
            f"{'Tipo':<15} {'Nome':<20} {'Descrição':<30} {'Quantidade':<10}" +
            Style.RESET_ALL
        )
        display.print_terminal_width("-")
        for item in items:
            _, tipo, nome, descricao, qtd = item
            print(f"{tipo:<15} {nome:<20} {descricao:<30} {qtd:<10}")
    
    display.print_terminal_width("-")

# Display player spells
def list_spells(spells):
    display.print_center(
        Style.BRIGHT +
        Fore.CYAN +
        f"--- Feitiços Disponíveis ---" +
        Style.RESET_ALL
    )

    display.print_terminal_width("-")
    
    if not spells:
        print(
            Fore.RED +
            "Nenhum feitiço aprendido." +
            Style.RESET_ALL
        )
    else:
        for idx, spell in enumerate(spells):
            nome, tipo, descricao, custo, dano, *_ = spell
            print(
                Fore.MAGENTA +
                f"{idx+1}. {nome} ({tipo})" +
                Style.RESET_ALL
            )
            print(f"{descricao}")
            print(
                f"{'Custo de energia: '}" +
                Fore.GREEN +
                f"{custo}" +
                Style.RESET_ALL
            )
            print(
                f"{'Dano: '}" +
                Fore.RED +
                f"{dano}" +
                Style.RESET_ALL
            )
            display.print_terminal_width(
                Fore.CYAN +
                "-"
            )

# Display player potions
def list_potions(potions):
    print(Style.BRIGHT + Fore.CYAN + f"\n--- Poções Disponíveis ---\n" + Style.RESET_ALL)
    print(Fore.CYAN + "-" * 110 + Style.RESET_ALL)

    if not potions:
        print(Fore.RED + "Nenhuma poção disponível." + Style.RESET_ALL)
    else:
        for idx, potion in enumerate(potions):
            ii_id, id, nome, descricao, usado = potion
            usado_color = Fore.GREEN if not usado else Fore.RED
            usado_label = "Disponível" if not usado else "Usado"
            print(Fore.MAGENTA + f"{idx+1}. {nome:<30}" + Style.RESET_ALL)
            print(f"{descricao}")
            #print(f"{'Turnos:':<30} {turnos}")
            print(f"{'Usado:':<30}" + usado_color + usado_label + Style.RESET_ALL)
            print(Fore.CYAN + "-" * 110 + Style.RESET_ALL)