

import streamlit as st

import numpy as np
import pandas as pd

import ktrain
from ktrain import text

reloaded_predictor = ktrain.load_predictor('TeamB_predictor/')



st.title('Team B - NLP Project')

data = st.text_input('Please enter the question:', '')

predict = reloaded_predictor.predict(data)

dic = {
  "target": "insincere",
  "not_target": "normal"
}

st.write('The question is ', dic[predict])