_version_info = "0.0.1" 
__autor__ = "Marcus Vinicius"
__license__ = "Unlicense"


import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, world"

if current_language == 'pt_BR':
    msg = "Olá mundo"
elif current_language == 'it_IT':
    msg = "Ciao, Mondo"
elif current_language == 'fr_FR':
    msg = "Bonjuor Monde"

print(msg)