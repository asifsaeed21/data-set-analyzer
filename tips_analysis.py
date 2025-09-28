# tips_analysis.py

# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Load Seaborn "tips" dataset
    tips = sns.load_dataset("tips")

    # ------------------ Basic Analysis ------------------
    print("First 5 rows of dataset:")
    print(tips.head(), "\n")

    print("Column names:")
    print(tips.columns.tolist(), "\n")

    print("Summary of dataset:")
    print(tips.describe(include="all"), "\n")

    # Set Seaborn style for better visuals
    sns.set(style="whitegrid", palette="Set2")

    # ------------------ Scatter Plot ------------------
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=tips,
        x="total_bill",
        y="tip",
        hue="day",
        palette="bright",
        s=80,
        edgecolor="black"
    )
    plt.title("Scatter Plot: Tip vs Total Bill (Colored by Day)", fontsize=14)
    plt.xlabel("Total Bill ($)")
    plt.ylabel("Tip ($)")
    plt.legend(title="Day")
    plt.tight_layout()
    plt.show()

    # ------------------ Histogram with KDE ------------------
    plt.figure(figsize=(8, 6))
    sns.histplot(
        data=tips,
        x="total_bill",
        kde=True,
        bins=30,
        color="skyblue"
    )
    plt.title("Distribution of Total Bill with KDE", fontsize=14)
    plt.xlabel("Total Bill ($)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # ------------------ Bar Plot ------------------
    plt.figure(figsize=(6, 5))
    sns.barplot(
        data=tips,
        x="sex",
        y="tip",
        palette="pastel",
        ci=None
    )
    plt.title("Average Tip by Gender", fontsize=14)
    plt.xlabel("Gender")
    plt.ylabel("Average Tip ($)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
