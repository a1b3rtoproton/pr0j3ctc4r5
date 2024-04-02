import json

try:
    with open('data/keys.json', 'r') as arquivo: 
        KEYS = json.load(arquivo)
except FileNotFoundError:
    with open('data/keys.json', 'w') as arquivo: 
        preset = {
            'SANDBOX': {
                'PUBLIC': None,
                'SECRET': None
            },
            'LIVE': {
                'PUBLIC': None,
                'SECRET': None
            },
        }
        KEYS = json.dump(preset, arquivo)