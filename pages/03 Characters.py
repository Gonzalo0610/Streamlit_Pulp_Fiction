import streamlit as st
import src.group as gb
import src.load_data as ld

st.set_page_config(page_title="Character Analysis", page_icon=":gun:", layout="wide")

st.title("Character Analysis")

st.header("Main Characters:")

#still loading the same dataframe here
df=ld.load()
#Tabs, columns and sidebars are different ways to approach the organization of your page. If you find you have too many information for a column and the user must scroll down (boring) you can use either of the other 2 options. i used them both in this page. 
tab1, tab2, tab3, tab4 = st.tabs(["Vincent Vega", "Jules", "Mia", "Butch"])

tab1.image("images/pfgif.gif")
tab1.write(f"**Actor**: *John Travolta*")
#Here i used my other function: A groupped function to have all the sentiment, word count and lines of each character!
lista=gb.group(df, "Vincent")
name=lista[0]
words=lista[1]
senti=lista[2]
tab1.write(f"{name} said {words} words in the whole movie, and the sentiment analyzer of his text was {senti}")

tab2.image("images/samuel.gif")
tab2.write(f"**Actor**: *Samuel L. Jackson*")
lista=gb.group(df, "Jules")
name=lista[0]
words=lista[1]
senti=lista[2]
tab2.write(f"{name} said {words} words in the whole movie, and the sentiment analyzer of his text was {senti}")

tab3.image("images/uma.jpg")
tab3.write(f"**Actress**: *Uma Thurman*")
lista=gb.group(df, "Mia")
name=lista[0]
words=lista[1]
senti=lista[2]
tab3.write(f"{name} said {words} words in the whole movie, and the sentiment analyzer of his text was {senti}")

tab4.image("images/bruce.jpg")
tab4.write(f"**Actor**: *Bruce Willis*")
lista=gb.group(df, "Butch")
name=lista[0]
words=lista[1]
senti=lista[2]
tab4.write(f"{name} said {words} words in the whole movie, and the sentiment analyzer of his text was {senti}")
# and the last one! a groupby function, in the same .py as the last one mentioned. Remember that a .py can be used as a "library" and you can store different functions with different outputs. 
results=gb.groupby(df)

st.header("Character +-")
# Sidebars are messy yet sometimes useful. First you need to include a selection, and then with if conditions you can show every possible outcome.  
with st.sidebar:
    selection = st.radio('The character that has:', ["More Words", "Less Words", "More Dialogues", "Less Dialogues", "More Positiveness", "More Negativeness"])

if selection == "More Words":
    st.write(f"{results[0]} is the character with more words, with a total of {results[1]}")
elif selection=="Less Words":
    st.write(f"{results[2]} is the character with less words, with a total of {results[3]}")
elif selection=="More Dialogues":
    st.write(f"{results[4]} is the character with more dialogues, with a total of {results[5]}")
elif selection=="Less Dialogues":
    st.write(f"{results[6]} is the character with less dialogues, with a total of {results[7]}")
elif selection=="More Positiveness":
    st.write(f"{results[8]} is the most positive character, with a compound of {results[9]}")
else:
    st.write(f"{results[10]} is the most negative character, with a compound of {results[11]}")