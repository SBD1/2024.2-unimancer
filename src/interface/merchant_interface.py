from colorama import Fore, Style
import database.dql.query as query
import interface.display as display
import interface.inventory as inventory
import logic.main as display
import interface.display
from database.dql.query import get_merchants_subregion, get_merchant_items, list_item_inventory

def trade_with_merchant(conn, character):
    merchants = get_merchants_subregion(conn, character.sub_regiao_id)
    if not merchants:
        print(Fore.RED + "Não há mercadores nesta área." + Style.RESET_ALL)
        return

    merchant_names = [m[1] for m in merchants]
    merchant_index = display.ask(merchant_names, lambda: [
        interface.display.clear_screen(),
        print(Fore.YELLOW + "Escolha um mercador para negociar:" + Style.RESET_ALL),
        interface.display.list_options(merchant_names)  
    ])

    if merchant_index == 0:
        return
    merchant_id, merchant_name = merchants[merchant_index - 1]

    while True:
        interface.display.clear_screen()
        print(Fore.YELLOW + f"Negociação com {merchant_name}" + Style.RESET_ALL)
        options = ["Comprar", "Vender", "Sair"]
        option_index = display.ask(options, lambda: [
        interface.display.clear_screen(),
        print(Fore.YELLOW + "Negociação com " + merchant_name + Style.RESET_ALL),
        interface.display.list_options(options)  
    ])
        if option_index == 0 or options[option_index - 1] == "Sair":
            break
        elif options[option_index - 1] == "Comprar":
            buy_items(conn, character, merchant_id)
        elif options[option_index - 1] == "Vender":
            sell_items(conn, character, merchant_id)

def buy_items(conn, character, merchant_id):
    items = get_merchant_items(conn, merchant_id)
    if not items:
        print(Fore.RED + "Este mercador não tem itens disponíveis." + Style.RESET_ALL)
        return

    while True:
        interface.display.clear_screen()
        print(Fore.GREEN + "Itens disponíveis para compra:" + Style.RESET_ALL)
        for idx, (item_id, nome, preco, quantidade) in enumerate(items, start=1):
            print(f"{idx}. {nome} - {preco} moedas (x{quantidade})")
        print("0. Sair")
        
        choice = display.ask("Escolha um item para comprar:")
        if choice == "0":
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(items):
                item_id, nome, preco, quantidade = items[choice - 1]
                if character.moedas >= preco:
                    query.buy_item(conn, character.id, item_id, preco)
                    character.moedas -= preco
                    print(Fore.GREEN + f"Você comprou {nome} por {preco} moedas." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Você não tem moedas suficientes!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Escolha inválida." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Digite um número válido!" + Style.RESET_ALL)
        interface.display.press_enter()

def sell_items(conn, character, merchant_id):
    items = list_item_inventory(conn, character.id)
    if not items:
        print(Fore.RED + "Seu inventário está vazio!" + Style.RESET_ALL)
        return
    
    while True:
        interface.display.clear_screen()
        print(Fore.BLUE + "Seus itens disponíveis para venda:" + Style.RESET_ALL)
        for idx, (item_id, tipo, nome, descricao, quantidade) in enumerate(items, start=1):
            print(f"{idx}. {nome} - x{quantidade}")
        print("0. Sair")
        
        choice = display.ask("Escolha um item para vender:")
        if choice == "0":
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(items):
                item_id, tipo, nome, _, quantidade = items[choice - 1]
                preco_venda = query.get_item_sell_price(conn, item_id)  # Agora usando item_id
                if preco_venda is None:
                    print(Fore.RED + "Erro ao obter preço do item." + Style.RESET_ALL)
                    continue
                success = query.sell_item(conn, character.id, item_id, preco_venda, merchant_id)
                if success:
                    character.moedas += preco_venda
                    print(Fore.GREEN + f"Você vendeu {nome} por {preco_venda} moedas." + Style.RESET_ALL)
                    items = list_item_inventory(conn, character.id)
                else:
                    print(Fore.RED + "Falha ao vender o item." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Escolha inválida." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Digite um número válido!" + Style.RESET_ALL)
        interface.display.press_enter()
