import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

def accounting_project_details():
    st.markdown("""
            - Built a financial dashboard to automate analysis of Tally-generated CSV reports.
            - Created ingestion pipelines and ETL flows using PySpark (groupBy, joins, aggregations).
            - Delivered data visualizations showing receivables and cash flow trends.
                    """)
    
def top_customers():
    df =  pd.read_csv('data/accounting_dashboard/party_outstanding.csv')

    if not os.path.exists(os.path.join(project_root, 'Portfolio/reports/plots')):
        os.makedirs(os.path.join(project_root, 'Portfolio/reports/plots'))

    # Filter top 5 customers with highest dues (negative outstanding)
    top_customers = df[(df['party_type'] == 'Customer') & (df['outstanding'] < 0)]
    top_customers = top_customers.sort_values('outstanding').head(5)

    #Plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.barh(top_customers['party_name'], -top_customers['outstanding'], color='orange')
    ax.set_xlabel("Outstanding Amount (₹)")
    ax.set_title("Top Outstanding Customers")
    plt.tight_layout()

    # Save and show
    plots_dir = os.path.join(project_root,"Portfolio/reports/plots")
    plot_path = os.path.join(plots_dir, "top_customers_outstanding.png")
    plt.savefig(plot_path)
    st.pyplot(fig) 

    st.markdown("""
        **Top Outstanding Customers** \n
        Insight: The company’s top overdue receivables are from customers like Fine Interiors, SmartTech, and XYZ Ltd, who together owe over ₹20,000. Timely follow-up on these parties is critical for improving the business's cash flow health.
                """)

def net_position():
    # Net Position
    df =  pd.read_csv('data/accounting_dashboard/party_outstanding.csv')
    summary = df.groupby("party_type")["outstanding"].sum()

    customer_due = abs(summary.get("Customer", 0))
    supplier_due = abs(summary.get("Supplier", 0))

    labels = ['Receivables (Customers)', 'Payables (Suppliers)']
    sizes = [customer_due, supplier_due]  # absolute values
    colors = ['skyblue', 'lightcoral']

    # Plot
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, labels=labels, colors=colors, autopct="%.1f%%", startangle=140)
    ax.set_title("Net Business Position: Receivables vs Payables")
    plt.tight_layout()
    
    # Save and show
    plots_dir = os.path.join(project_root,"Portfolio/reports/plots")
    plot_path = os.path.join(plots_dir, "net_position_pie.png")
    plt.savefig(plot_path)
    st.pyplot(fig) 

    st.markdown("""
                **Net Receivables vs Payables**\n
Insight: The business currently has a net receivable position of ₹8,010, with more funds expected from customers than owed to suppliers. This puts the company in a positive short-term liquidity position.
                """)

def monthly_trend():
    mt = pd.read_csv('data/accounting_dashboard/monthly_trend.csv')
    if not os.path.exists(os.path.join(project_root, 'Portfolio/reports/plots')):
        os.makedirs(os.path.join(project_root, 'Portfolio/reports/plots'))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(mt['month'], mt['total_sales'], marker='o', label='Sales', color='green')
    ax.plot(mt['month'], mt['total_purchases'], marker='o', label='Purchases', color='red')
    plt.fill_between(mt['month'], mt['total_sales'], mt['total_purchases'], color='lightgrey', alpha=0.3)
    plt.title("Monthly Sales vs Purchases Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount (₹)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    
    plots_dir = os.path.join(project_root,"Portfolio/reports/plots")
    plot_path = os.path.join(plots_dir, "monthly_trend.png")
    plt.savefig(plot_path)
    st.pyplot(fig) 

    st.markdown("""
    **Monthly Sales vs Purchases**\n
    Insight: January 2024 saw high sales margins, with sales exceeding purchases by over ₹77,000. However, February shows a significant dip in both, indicating either a seasonal shift or business slowdown — something to monitor in upcoming months.
                """)
