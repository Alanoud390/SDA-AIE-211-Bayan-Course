"""Lab 3 starter: dataset construction and split integrity."""


from pathlib import Path
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit


def build_topic_dataset():
    df = pd.read_csv("data/raw/bayan_feedback.csv")

    groups = df["citizen_group_id"]

    gss = GroupShuffleSplit(
        n_splits=1,
        test_size=0.2,
        random_state=42
    )

    train_idx, temp_idx = next(
        gss.split(df, groups=groups)
    )

    train_df = df.iloc[train_idx].reset_index(drop=True)
    temp_df = df.iloc[temp_idx].reset_index(drop=True)

    gss2 = GroupShuffleSplit(
        n_splits=1,
        test_size=0.5,
        random_state=42
    )

    valid_idx, test_idx = next(
        gss2.split(
            temp_df,
            groups=temp_df["citizen_group_id"]
        )
    )

    valid_df = temp_df.iloc[valid_idx].reset_index(drop=True)
    test_df = temp_df.iloc[test_idx].reset_index(drop=True)

    return {
        "train": train_df,
        "validation": valid_df,
        "test": test_df,
    }