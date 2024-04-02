from models import *
from engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

class UserController:

    def add(self, email:str, token:str) -> None:
        with Session(engine) as session:
            new_user = User(
                email=email,
                token=token
            )
            session.add_all([new_user])
            session.commit()
    
    def select(self, email:str) -> list:
        with Session(engine) as session:
            stmt = select(User).where(User.email.in_([email]))
            return [user for user in session.scalars(stmt)]
    
    def select_with_id(self, id:int) -> list:
        with Session(engine) as session:
            stmt = select(User).where(User.id.in_([id]))
            return [user for user in session.scalars(stmt)]
    
    def select_all(self) -> list:
        with Session(engine) as session:
            stmt = select(User)
            return [user for user in session.scalars(stmt)]
        
class CardController:

    def add(self, card_number:str, exp_month:str, exp_year:str, cvc:str, token:str, user_id:int) -> None:
        with Session(engine) as session:
            new_card = Card(
                card_number=card_number, 
                exp_month=exp_month, 
                exp_year=exp_year,
                cvc=cvc,
                token=token,
                user_id=user_id
            )
            session.add_all([new_card])
            session.commit()

    def select(self, card_number:str, cvc:str) -> list:
        with Session(engine) as session:
            stmt = select(Card).where(Card.card_number.in_([card_number])).where(Card.cvc.in_([cvc]))
            return [card for card in session.scalars(stmt)]

    def select_all(self) -> list:
        with Session(engine) as session:
            stmt = select(Card)
            return [card for card in session.scalars(stmt)]