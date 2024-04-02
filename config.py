import json
import streamlit as st

def config() -> None:
    with open('data/keys.json', 'r') as file:
        keys = json.load(file)
    st.title('Stripe Keys')
    col1, col2 = st.columns(2)
    col1.title('SANDBOX')
    public_sandbox = col1.text_input(label="S PUBLIC KEY", value=keys['SANDBOX']['PUBLIC'])
    secret_sandbox = col1.text_input(label="S SECRET KEY", value=keys['SANDBOX']['SECRET'])
    col2.title('LIVE')
    public_live = col2.text_input(label="L PUBLIC KEY", value=keys['LIVE']['PUBLIC'])
    secret_live = col2.text_input(label="L SECRET KEY", value=keys['LIVE']['SECRET'])
    if st.button('Save'):
        keys['SANDBOX']['PUBLIC'] = public_sandbox
        keys['SANDBOX']['SECRET'] = secret_sandbox
        keys['LIVE']['PUBLIC'] = public_live
        keys['LIVE']['SECRET'] = secret_live
        with open('data/keys.json', 'w') as file:
            json.dump(keys, file)