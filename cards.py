import streamlit as st
import pandas as pd
import controllers

def cards(mode:str) -> None:
    '''
    mode SANDBOX | LIVE
    '''
    st.title(f'Credit Cards - {mode}')
    cards = controllers.CardController().select_all()
    cards = [[card.id, card.user_id,  card.card_number, card.exp_month, card.exp_year, card.cvc, card.token] for card in cards]
    cards = pd.DataFrame(cards, columns=[
        'id', 'user_id', 'card_number', 'exp_month', 'exp_year', 'cvc', 'token'
        ])
    st.table(cards)