"""Lab 3A starter: TF-IDF + LinearSVC baseline."""

from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score, classification_report
from sklearn.svm import LinearSVC


DATA_PATH = Path("data/raw/bayan_feedback.csv")
BENCHMARKS_PATH = Path("BENCHMARKS.md")


def main():
    # 1) Load the supplied dataset
    df = pd.read_csv(DATA_PATH)

    # 2) Use the supplied frozen split
    train_df = df[df["split"] == "train"].copy()
    test_df = df[df["split"] == "test"].copy()

    # 3) Convert text to TF-IDF features
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=2,
        max_features=50000,
        sublinear_tf=True,
    )

    X_train = vectorizer.fit_transform(train_df["text"].fillna(""))
    X_test = vectorizer.transform(test_df["text"].fillna(""))

    y_train = train_df["topic"]
    y_test = test_df["topic"]

    # 4) Train Linear SVM classifier
    model = LinearSVC()
    model.fit(X_train, y_train)

    # 5) Evaluate on the frozen test split
    predictions = model.predict(X_test)

    macro_f1 = f1_score(
        y_test,
        predictions,
        average="macro",
    )


#test
    print(f"Train rows: {len(train_df)}")
    print(f"Test rows: {len(test_df)}")
    print(f"Baseline macro-F1: {macro_f1:.4f}")
    print()
    print(classification_report(y_test, predictions))

    # 6) Record YOUR measured result
    with BENCHMARKS_PATH.open("a", encoding="utf-8") as f:
        f.write("\n## Lab 3A — TF-IDF + LinearSVC baseline\n")
        f.write(f"- Macro-F1: {macro_f1:.4f}\n")

    print(f"\nRecorded result in {BENCHMARKS_PATH}")


if __name__ == "__main__":
    main()