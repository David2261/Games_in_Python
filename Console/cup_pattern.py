from rich import print
from rich.style import Style
from rich.console import Console
from rich.theme import Theme
# from prettytable import PrettyTable
# from loguru import logger


# For rich: python -m pip install rich 
# For beautyful pattern

# For prettytable: python -m pip install -U prettytable
# For: ASCII symbols
 
# For Loguru: pip install loguru
# For: logging in py

custom_theme = Theme({
	"info": "italic cyan",
	"warning": "bold magenta",
	"danger": "bold red"
})

console = Console(theme = custom_theme)
print("[italic red]Hello[/italic red] World!")

danger = Style(color = "red", blink = True, bold = True)
console.print("Danger, Will Robinson!", style = danger)

print("\n")

console.print("This is information", style = "info")
console.print("[warning]The pod bay happend![/warning]")
console.print("Something terrible happend!", style = danger)