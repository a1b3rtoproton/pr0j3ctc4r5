from faker import Faker
import random
import uuid

def uuid_gen() -> str:
  return str(uuid.uuid4()).upper()

def time_on_page() -> int:
  return random.randint(5000, 50000)

def email() -> str:
  str_email = Faker('pt_BR').email().replace('example', 'gmail')
  number = random.randint(0, 5000)
  letters = 'abcdefghijklmnopqrstuvxwyx'
  str_email = str_email.replace('@', f'{random.choice(letters)}{random.choice(letters)}{number}@')
  terminals = ['.org', '.net']
  for terminal in terminals:
    str_email = str_email.replace(terminal, '.com')
  return str_email

def validate_card_number(numero:str) -> bool:
    if len(numero) == 16:
       return True
    else:
       return False

def validate_month_date(date:str) -> bool:
   if len(date) <= 2:
      return True
   return False

def validate_cvc(cvc:str) -> bool:
   if len(cvc) == 3:
      return True
   return False