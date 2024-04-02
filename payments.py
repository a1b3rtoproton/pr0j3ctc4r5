import streamlit as st
from pipeline import pay_with_card
import forms

def payments(mode:str):
    '''
    mode SANDBOX | LIVE
    '''
    st.title(f'Credit Card Payments - {mode}')
    col1, col2 = st.columns(2)
    # Coluna 1 para inserir os dados do cartão
    col1.subheader('Payments')
    # Coluna 2 renpose das requests de dados
    col2.subheader('Reponse')
    card_number, exp_month, exp_year, cvc, ammount, pay_button = forms.payment_form(col1)
    if pay_button:
        charge_response = pay_with_card(
            card_number=card_number,
            exp_month=exp_month,
            exp_year=exp_year,
            cvc=cvc,
            ammount=ammount*100,
            mode=mode
            )
        col2.json(charge_response, expanded=True)
        try:
            col1.write(charge_response.status)
        except AttributeError:
            col1.write(charge_response['status'])