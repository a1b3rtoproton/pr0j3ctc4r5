import streamlit as st

def payment_form(col) -> tuple[str]:
    card_number = col.text_input("Card Number")
    exp_month = col.text_input("Exp Month")
    exp_year = col.text_input("Exp Year")
    cvc = col.text_input("CVC")
    ammount = col.number_input("Ammount", step=1)
    pay_button = col.button("Pay")
    return card_number, exp_month, exp_year, cvc, ammount, pay_button