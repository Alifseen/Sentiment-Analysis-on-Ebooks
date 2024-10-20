from glob import glob
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer

files = glob("diary/*.txt")
analyzer = SentimentIntensityAnalyzer()


def sent():
    pos = []
    neg = []
    dates = []

    for file in files:
        with open(file, "r") as diary:
            content = diary.read()
        tone = analyzer.polarity_scores(content)
        neg.append(tone["neg"])
        pos.append(tone["pos"])
        path = Path(file).stem
        dates.append(path)
    return dates, pos, neg

if __name__ == "__main__":
    print(sent())