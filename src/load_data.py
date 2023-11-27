import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def load():
    #load de dataframe

    df=pd.read_csv("data/pulp_fiction_dialogue.csv")

    # Reset the index with the column "Line number"
    df = df.set_index("Line number")

    # Drop the columns "Character (in script)", "Off screen", and "Voice-over". UNNECESARY AND REPEATED
    columns_to_drop = ["Character (in script)", "Off screen", "Voice-over"]
    df = df.drop(columns=columns_to_drop)

    # Change the column name "Character (actual)" to "Character"
    df = df.rename(columns={"Character (actual)": "Character"})
    
    #Add a column named "Sentiment" with the Sentiment Analysis:
    analyzer = SentimentIntensityAnalyzer()
    df["Sentiment"] = df["Line"].apply(lambda x: analyzer.polarity_scores(x)["compound"])

    return df