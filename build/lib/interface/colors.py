from colorama import Fore, Style, init

class Colors:
    def __init__(self):
        init()
        
        # Colours.
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.yellow = Fore.YELLOW
        
        # Style.
        self.bold = Style.BRIGHT