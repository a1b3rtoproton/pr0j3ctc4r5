import streamlit as st
import pandas as pd
import controllers

def costumers(mode:str) -> None:
    '''
    mode SANDBOX | LIVE
    '''
    st.title(f'Costumers - {mode}')
    costumers = controllers.UserController().select_all()
    costumers = [[costumer.id, costumer.email, costumer.token] for costumer in costumers]
    costumers = pd.DataFrame(costumers, columns=['id', 'email', 'token'])
    st.table(costumers)