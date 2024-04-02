import stripe_utils
import controllers
from utils import validate_card_number, validate_month_date, validate_cvc

def pay_with_card(card_number:str, exp_month:str, exp_year:str, cvc:str, ammount:int, mode:str,) -> dict:
    '''
    mode: SANDBOX | LIVE
    '''
    if validate_card_number(card_number) and validate_month_date(exp_month) and validate_month_date(exp_year) and validate_cvc(cvc):
        cards = controllers.CardController().select(card_number=card_number, cvc=cvc)
        if len(cards) == 0:
            card_token = stripe_utils.tokenize_card(
                card_number=card_number, 
                exp_month=exp_month,
                exp_year=exp_year,
                cvc=cvc,
                mode=mode
            )
            costumer_token = stripe_utils.create_customer(card_token, mode)
            charge_response = stripe_utils.create_charge(costumer_token, ammount, mode)
            selected_users = controllers.UserController().select(costumer_token.email)
            if len(selected_users) == 0:
                controllers.UserController().add(email=costumer_token.email, token=costumer_token.id)
                selected_users = controllers.UserController().select(costumer_token.email)
            controllers.CardController().add(
                card_number=card_number,
                exp_month=exp_month, exp_year=exp_year,
                cvc=cvc, token=card_token.id,
                user_id=selected_users[0].id
                )
            return charge_response
        else:
            user_id = cards[0].id
            user = controllers.UserController().select_with_id(id=user_id)
            user_token = user[0].token
            charge_response = stripe_utils.create_charge(
                costumer_token=user_token, 
                ammount=ammount, 
                mode=mode
            )
            return charge_response
    else:
        return {
            'error': 'card_does_not_exists',
            'status':'Failed'
            }