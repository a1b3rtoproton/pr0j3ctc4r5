import streamlit as st
import pandas as pd
from utils import *
from stripe_utils import *
from controllers import *
import payments
import costumers
import cards
import json

st.sidebar.title('Menu')
selectbox_sidebar_mode = st.sidebar.selectbox(label="Modes", options=['SANDBOX', 'LIVE'])
with open('data/mode.json', 'w') as file:
    json.dump({'mode': selectbox_sidebar_mode}, file)
selectbox_sidebar = st.sidebar.selectbox(label="Options", options=['Payments', 'Costumers', 'Cards'])

if selectbox_sidebar == 'Payments':
    payments.payments(mode=selectbox_sidebar_mode)

if selectbox_sidebar == 'Costumers':
    costumers.costumers(mode=selectbox_sidebar_mode)

if selectbox_sidebar == 'Cards':
    cards.cards(mode=selectbox_sidebar_mode)