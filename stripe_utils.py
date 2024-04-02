import stripe
from utils import *
import json
from keys import KEYS

def tokenize_card(card_number:str, exp_month:str, exp_year:str, cvc:str, mode:str) -> dict:
  """
  mode: SANDBOX | LIVE
  """
  stripe.api_key = KEYS[mode]['PUBLIC']
  token = stripe.Token.create(
    muid = uuid_gen(),
    time_on_page = time_on_page(),
    card={
      "number": card_number.replace(' ', ''),
      "exp_month": exp_month,
      "exp_year": exp_year,
      "cvc": cvc,
    },
  )
  return token

def create_customer(card_token:dict, mode:str) -> dict:
  """
  mode: SANDBOX | LIVE
  """
  stripe.api_key = KEYS[mode]['SECRET']
  token = stripe.Customer.create(
    email= email(),
    source = card_token.id
  )
  return token
  
def create_charge(costumer_token:dict, ammount:int, mode:str, currency:str = 'BRL') -> dict:
  """
  mode: SANDBOX | LIVE
  costumer_token: dict | str
  """
  stripe.api_key = KEYS[mode]['SECRET']
  token = stripe.Charge.create(
    amount = ammount,
    currency=currency,
    customer = costumer_token.id if type(costumer_token) != str else costumer_token
  )
  return token