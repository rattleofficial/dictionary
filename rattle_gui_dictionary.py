import streamlit as sl
from PyDictionary import PyDictionary
sl.title('Rattle dictionary')
inp=sl.text_input('Enter the word you want to find the meaning:')
btn=sl.button('Find!')
if btn:
    dictionary=PyDictionary()
    h=sl.header(dictionary.meaning(inp))
