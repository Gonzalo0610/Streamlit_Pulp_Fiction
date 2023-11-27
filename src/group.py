import pandas as pd

def group(df, x):
    character_df= df[df["Character"] == x]
    # This is easier than the text below!! Just count the sum of word counts and the mean of sentiment column and return a easy list :)
    word_count_sum = character_df["Word count"].sum()
    sentiment_mean = character_df["Sentiment"].mean()
    
    return [x, word_count_sum, sentiment_mean]

def groupby(df):
    # Group by "Character" and calculate SUM and COUNT
    grouped = df.groupby("Character").agg(
        Word_Count_Sum=("Word count", "sum"),
        Word_Count_Count=("Word count", "count"),
        Sentiment_Mean=("Sentiment", "mean")
    ).reset_index()

    # Filter characters with at least 100 word counts for sentiment analysis (less words are not VIP to include)
    filtered_df = df[df["Character"].isin(grouped[grouped["Word_Count_Sum"] >= 100]["Character"])]
    sentiment_grouped = filtered_df.groupby("Character")["Sentiment"].mean().reset_index()

    # Max and Min sum of word counts
    max_word_count_char = grouped.loc[grouped["Word_Count_Sum"].idxmax()]
    min_word_count_char = grouped.loc[grouped["Word_Count_Sum"].idxmin()]

    # Max and Min count of word counts (every interaction of every character)
    max_word_count_count_char = grouped.loc[grouped["Word_Count_Count"].idxmax()]
    min_word_count_count_char = grouped.loc[grouped["Word_Count_Count"].idxmin()]

    # Find character with maximum and minimum sentiment analysis mean
    max_sentiment_mean_char = sentiment_grouped.loc[sentiment_grouped["Sentiment"].idxmax()]
    min_sentiment_mean_char = sentiment_grouped.loc[sentiment_grouped["Sentiment"].idxmin()]

    # 12 length list with E V E R Y T H I N G
    result = [
        max_word_count_char["Character"], max_word_count_char["Word_Count_Sum"],
        min_word_count_char["Character"], min_word_count_char["Word_Count_Sum"],
        max_word_count_count_char["Character"], max_word_count_count_char["Word_Count_Count"],
        min_word_count_count_char["Character"], min_word_count_count_char["Word_Count_Count"],
        max_sentiment_mean_char["Character"], max_sentiment_mean_char["Sentiment"],
        min_sentiment_mean_char["Character"], min_sentiment_mean_char["Sentiment"]
    ]

    return result