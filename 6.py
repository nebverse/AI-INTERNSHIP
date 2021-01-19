import streamlit as st
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

def game(ans):
    a = random.randint(0,2)
    opt = ["Rock", "Paper", "Scissor"]
    c_ans = opt[a]
    st.write("You chose:{}".format(ans))
    st.write("Computer chose:{}".format(c_ans))

    if (c_ans == ans):
        st.write("Game tied!!!")

    elif ((c_ans == "Rock") and (ans == "Paper")):
        st.write("You Win!!!")

    elif ((c_ans == "Rock") and (ans == "Scissor")):
        st.write("Computer Wins!!!")

    elif ((c_ans == "Paper") and (ans == "Rock")):
        st.write("Computer Wins!!!")

    elif ((c_ans == "Paper") and (ans == "Scissor")):
        st.write("You Win!!!")

    elif ((c_ans == "Scissor") and (ans == "Rock")):
        st.write("You Win!!!")

    elif ((c_ans == "Scissor") and (ans == "Paper")):
        st.write("Computer Wins!!!")


st.title("ROCK PAPER SCISSOR GAME")
L = ["Rock", "Paper", "Scissor"]
ans = st.selectbox('(SELECT ONE option)',L)
game(ans)