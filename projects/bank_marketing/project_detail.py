import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

def bank_project_details():
    st.markdown("""
            - Designed and deployed an end-to-end real-time ETL pipeline using AWS services following Medallion Architecture (Bronze → Silver → Gold)
- Streamed marketing data via Kinesis, processed events with Lambda, and stored raw data in S3 Bronze layer.
- Cleaned and normalized streaming data using Glue PySpark jobs; wrote structured output to Silver layer in JSON
- Aggregated business insights like deposit rates by job, age, and education; stored results in Gold layer
- Enabled ad-hoc SQL analysis using Athena, and built interactive dashboards in QuickSight
- Demonstrated data lake design, real-time ingestion, ETL transformation, and cloud-native insight delivery
                    """)
    
def job_vs_deposit():
    df = pd.read_json("data/bank_marketing/job_vs_deposit.json", lines=True)
    if not os.path.exists('reports/plots'):
        os.makedirs('reports/plots')

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        data = df,
        x="job_title",
        y="deposits",
        palette="viridis",
        ax=ax
    )
    ax.set_title("Deposits by Job Title")
    ax.set_xlabel("Job Title")
    ax.set_ylabel("Deposit Amount (£)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save and show
    plots_dir = "reports/plots"
    plot_path = os.path.join(plots_dir, "job_vs_deposit.png")
    plt.savefig(plot_path)
    st.pyplot(fig)  

def age_group_perf():
    df = pd.read_json("data/bank_marketing/age_group_perf.json",lines=True)
    if not os.path.exists('reports/plots'):
        os.makedirs('reports/plots')

    labels = df["age_group"]
    sizes = df["deposits"]
    fig, ax = plt.subplots(figsize=(4, 4))
    colors = ['#66c2a5', '#fc8d62', '#8da0cb']
    ax.pie(
        x = sizes,
        labels= labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        wedgeprops={'edgecolor': 'white'}
    )

    ax.set_title("Deposit Distribution by Age Group")

    plt.tight_layout()
    plots_dir = "reports/plots"
    plot_path = os.path.join(plots_dir, "job_vs_deposit.png")
    plt.savefig(plot_path)
    st.pyplot(fig)  

def edu_loan_stats():
    df = pd.read_json("data/bank_marketing/edu_loan_stats.json",lines=True)
    if not os.path.exists('reports/plots'):
        os.makedirs('reports/plots')

    fig, ax = plt.subplots(figsize=(12,6))
    sns.barplot(
        data=df,
        x="loan_percentage",
        y="education_level",
        palette="crest",
        ax=ax
    )
    ax.set_title("📊 Loan Percentage by Education Level", fontsize=14)
    ax.set_xlabel("Loan Percentage (%)")
    ax.set_ylabel("Education Level")

    for i, v in enumerate(df["loan_percentage"]):
        ax.text(v + 0.5, i, f"{v:.1f}%", va='center', fontsize=10)

    plt.tight_layout()

    st.pyplot(fig)
