import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

def retail_project_details():
    st.markdown("""
            - Built end-to-end batch ETL pipeline for Retail Analytics using Airflow orchestration with full task-level modularization.
            - Designed multi-stage DAG with task dependencies: Extraction → Cleaning → Transformation → Loading → Analysis.
            - Added scheduling, retries, SLA monitoring, and backfill readiness for production-grade pipeline stability.
            - Implemented separate ETL functions and Python modules for scalable and reusable code structure.
            - Cleaned and enriched UCI Retail + synthetic customer data, calculated RFM segments, KPIs, top customers & revenue trends.
            - Loaded Gold-layer data into MySQL using SQLAlchemy; built multiple KPI visualizations in Streamlit and Seaborn.
                    """)
    
def top_selling_products_by_price():
    df = pd.read_csv("data/retail_analytics/sales_enriched_gold.csv")
    if not os.path.exists(os.path.join(project_root, 'Portfolio/reports/plots')):
        os.makedirs(os.path.join(project_root, 'Portfolio/reports/plots'))

    top_products = df.groupby("Description")["TotalPrice"].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        x=top_products.values,
        y=top_products.index,
        hue=top_products.index,
        palette="viridis",
        legend=False,
        ax=ax
    )
    ax.set_title("Top 10 Products by Total Sales")
    ax.set_xlabel("Total Sales (£)")
    ax.set_ylabel("Product Description")
    plt.tight_layout()

    # Save and show
    plots_dir = os.path.join(project_root,"Portfolio/reports/plots")
    plot_path = os.path.join(plots_dir, "top_products_sales.png")
    plt.savefig(plot_path)
    st.pyplot(fig)  # This renders the figure inside Streamlit

    # Optional: Also show saved image
    #st.image(plot_path, caption="Top 10 Products by Total Sales")

def monthly_revenue():
    df = pd.read_csv("data/retail_analytics/sales_enriched_gold.csv")
    if not os.path.exists(os.path.join(project_root, 'Portfolio/reports/plots')):
        os.makedirs(os.path.join(project_root, 'Portfolio/reports/plots'))

    monthly_revenue = df.groupby(['InvoiceYear', 'InvoiceMonth'])['TotalPrice'].sum().reset_index()
    monthly_revenue['Month'] = monthly_revenue['InvoiceYear'].astype(str) + '-' + monthly_revenue['InvoiceMonth'].astype(str)

    # Step 2: Sort by Month
    monthly_revenue = monthly_revenue.sort_values('Month')

    # Step 3: Select last 6 months
    last_6_months = monthly_revenue.tail(6).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=last_6_months, x='Month', y='TotalPrice', marker='o', ax=ax)
    ax.set_title('Monthly Revenue Trend (Last 6 Months)')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Revenue (£)')
    plt.tight_layout()

    plots_dir = os.path.join(project_root,"Portfolio/reports/plots")
    # Step 5: Save and display
    plot_path = os.path.join(plots_dir, "monthly_revenue_trend.png")
    fig.savefig(plot_path)
    st.pyplot(fig)
    #st.image(plot_path, caption="Monthly Revenue for Last 6 Months")

def top_avg_order():
    df = pd.read_csv("data/retail_analytics/sales_enriched_gold.csv")
    if not os.path.exists(os.path.join(project_root, 'Portfolio/reports/plots')):
        os.makedirs(os.path.join(project_root, 'Portfolio/reports/plots'))

    top_countries = df.groupby("Country")["TotalPrice"].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        x=top_countries.index,
        y=top_countries.values,
        hue=top_countries.index,
        palette="viridis",
        legend=False,
        ax=ax
    )
    ax.set_title("Top 10 Countries by Average Order Value")
    ax.set_xlabel("Country")
    ax.set_ylabel("Average Order Value (£)")
    plt.tight_layout()

    # Save and show
    plots_dir = os.path.join(project_root,"Portfolio/reports/plots")
    plot_path = os.path.join(plots_dir, "top_countries_average_order_value.png")
    plt.savefig(plot_path)
    st.pyplot(fig)  # This renders the figure inside Streamlit

    # Optional: Also show saved image
    #st.image(plot_path, caption="Top 10 Countries by Average Order Value")
