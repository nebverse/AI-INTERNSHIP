# Run it on streamlit

import streamlit as st
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import PIL

def game(ans):

    a = random.randint(0, 2)
    opt = ["Rock", "Paper", "Scissor"]
    c_ans = opt[a]

    col1, col2 = st.beta_columns(2)

    col1.header("You chose:{}".format(ans))
    if ans == "Rock":
        col1.image("rock.txt", width=None)
    elif ans == "Paper":
        col1.image("paper.gif", width=None)
    elif ans == "Scissor":
        col1.image("scissor.gif", width=None)


    col2.header("Computer chose:{}".format(c_ans))
    if c_ans == "Rock":
        col2.image("rock.txt", width=None)
    elif c_ans == "Paper":
        col2.image("paper.gif", width=None)
    elif c_ans == "Scissor":
        col2.image("scissor.gif", width=None)

    if (c_ans == ans):
        st.subheader("Game tied!!!")
        st.image("draw.gif", width=None)

    elif ((c_ans == "Rock") and (ans == "Paper")):
        st.subheader("You Win!!!")
        st.image("win.gif", width=None)

    elif ((c_ans == "Rock") and (ans == "Scissor")):
        st.subheader("Computer Wins!!!")
        st.image("lose.gif", width=None)

    elif ((c_ans == "Paper") and (ans == "Rock")):
        st.subheader("Computer Wins!!!")
        st.image("lose.gif", width=None)

    elif ((c_ans == "Paper") and (ans == "Scissor")):
        st.subheader("You Win!!!")
        st.image("win.gif", width=None)

    elif ((c_ans == "Scissor") and (ans == "Rock")):
        st.subheader("You Win!!!")
        st.image("win.gif", width=None)

    elif ((c_ans == "Scissor") and (ans == "Paper")):
        st.subheader("Computer Wins!!!")
        st.image("lose.gif", width=None)


st.title("ROCK PAPER SCISSOR GAME")
L = ["Rock", "Paper", "Scissor"]
ans = st.selectbox('(SELECT ONE OPTION)', L)
game(ans)

sharingMode = "on"

# Tried to create a loop for asking if you want to play another game
# con = True
# while con:
#     user_input = st.text_input("Want to play another game!!(Y/N)")
#     if user_input == "Y":
#         ans1 = st.selectbox('(SELECT ONE option)', L)
#         game(ans1)
#
#     elif user_input == "N":
#         st.write("Bye Bye!!")
#         con = False