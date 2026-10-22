"""Summarize the PubMed evidence list by publication year.

Reads data/pubmed-evidence.csv (one row per paper: pmid, title, journal, year)
and prints how many papers fall in each year.
"""

import pandas as pd


CSV_PATH = "data/pubmed-evidence.csv"


def main() -> None:
    df = pd.read_csv(CSV_PATH)

    # Number of papers per publication year (sorted by year).
    counts = df["year"].value_counts().sort_index()

    print("Papers per publication year")
    print(counts.to_string())
    print(f"\nTotal papers: {len(df)}")


if __name__ == "__main__":
    main()
