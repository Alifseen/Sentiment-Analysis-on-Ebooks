from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
from glob import glob
from pathlib import Path
from plotly.express import line


## Backend
files = glob("diary/*.txt")

days = []
dates= []
pos = []
neg = []

for file in files:
    with open(file, "r") as diary:
        days.append(diary.readlines())
    path = Path(file).stem
    dates.append(path)

analyzer = SentimentIntensityAnalyzer()
for day in days:
    daily_tone = analyzer.polarity_scores(day[0])
    neg.append(daily_tone["neg"])
    pos.append(daily_tone["pos"])

st.write(dates)
print(pos)
print(neg)

## Frontend

# st.title("Dairy Tone")
# st.subheader("Positivity Chart")
# print(dates)
# print(pos)
# print(neg)
# figp = line(x=dates, y=pos, labels={"x": "Dates", "y": "Positivity"})
# st.plotly_chart(figp)
#
# st.subheader("Negativity Chart")
# figp1 = line(x=dates,y=neg, labels={"x": "Dates", "y": "Negativity"})
# st.plotly_chart(figp1)