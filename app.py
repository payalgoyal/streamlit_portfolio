import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
from projects.retail_analytics.project_detail import retail_project_details, top_selling_products_by_price, monthly_revenue, top_avg_order
from projects.bank_marketing.project_detail import bank_project_details, job_vs_deposit, age_group_perf, edu_loan_stats
from projects.accounting_dashboard.project_detail import accounting_project_details, top_customers,net_position, monthly_trend
from projects.pyspark_learning.project_detail import pyspark_project_details
from sidebar_section.sidebar import sidebar_content

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

sns.set_theme(style="whitegrid")

def portfolio():
    st.title("Payal Goyal")
    st.write("Backend Developer | Data Engineering Enthusiast | Actively Seeking Returnship / Reentry Roles ")
    st.markdown("""
        📧  **Email**: payalgoyal90@gmail.com  
        📍  **Location**: India  
        📞  **Phone**: +91 95739 45583
        """)

    sidebar_content()

    st.markdown("----")

    st.header("Professional Summary")
    st.markdown("""
        Software Engineer with 2+ years of experience at Tata Consultancy Services and 2+ years of self-initiated project development during career break. Strong expertise in Python, Flask, PySpark, SQL, and production-grade ETL pipelines. Delivered both batch and streaming data pipelines using Apache Airflow and AWS Kinesis (Glue, Athena, Lambda). Actively seeking backend or data engineering roles leveraging my strong ETL orchestration, cloud skills, and hands-on coding experience.
                """)

    st.header("Skills")
    st.markdown("""
         🔹  **Languages**: Python, JavaScript, SQL  
         🔹  **Backend & Web**: Flask, Node.js, REST APIs, Axios  
         🔹 **Frontend**: React.js, HTML5, CSS3, Bootstrap, Tailwind CSS, Streamlit  
         🔹 **Data Engineering**: PySpark, Apache Airflow, MySQL, Batch & Streaming ETL, RDBMS  
         🔹 **Cloud & Tools**: AWS (Kinesis, Glue, Athena, Lambda, S3, QuickSight), Git, GitHub, VS Code, Jupyter  
                """)
    
    st.header("Project")
    #Project 1
    st.subheader("Retail Analytics ETL Pipeline (Airflow Orchestration + MySQL + Streamlit)")
    st.write("Retail Analytics ETL Pipeline – Architecture Diagram")
    st.image("Retail_analytics_workflow.png", caption="Airflow Orchestration for Retail Analytics ETL Pipeline")

    with open("Retail_analytics_workflow.png", "rb") as img_file:
        st.download_button(
            label="📥 Download Diagram",
            data=img_file,
            file_name="retail_analytics_workflow.png",
            mime="image/png"
        )
        
    with st.expander("Project Details"):
        st.write("GitHub: https://github.com/payalgoyal/retail-analytics-pipeline")
        st.write("Tech Stack: Python, Pandas, MySQL, Airflow, Seaborn, SQLAlchemy, Streamlit, Faker")
        
        retail_project_details()
        option = st.selectbox("📊 Choose Insights",["Select","Top 10 selling products by Price","Monthly Revenue","Top 10 average order by country"])
        if option == "Top 10 selling products by Price":
            top_selling_products_by_price()

        if option == "Monthly Revenue":
            monthly_revenue()

        if option == "Top 10 average order by country":
            top_avg_order()

    #Project 2
    st.subheader("Bank Marketing Real-Time Data Pipeline on AWS")
    st.write("AWS ETL Pipeline – Architecture Diagram")
    st.image("architecture-diagram.png", caption="Medallion Architecture for Bank Marketing ETL Pipeline")
    # Download button for the architecture diagram
    with open("architecture-diagram.png", "rb") as img_file:
        st.download_button(
            label="📥 Download Diagram",
            data=img_file,
            file_name="bank_etl_architecture.png",
            mime="image/png"
        )

    with st.expander("See Workflow Details"):
        st.markdown("""
        - **Kinesis** receives streaming data from producers.
        - **Lambda** consumes the stream and stores raw data in S3 (Bronze Layer).
        - **AWS Glue** cleans and transforms data into the Silver Layer.
        - Another Glue job aggregates for analytics into the Gold Layer.
        - **Athena** runs SQL queries on Gold Layer data.
        - **QuickSight** builds dashboards on Athena queries.
        """)
    with st.expander("Project Details"):
        st.write("GitHub: https://github.com/payalgoyal/Bank-Marketing-ETL-AWS")
        st.write("Tech Stack: AWS Kinesis, Lambda, S3, Glue (PySpark), Athena, QuickSight, Medallion Architecture")
        bank_project_details()

        options = st.selectbox("📊 Choose Insights",["Select","Job vs Deposit","Age Group Performance","Education Loan Statistics"])
        if options == "Job vs Deposit":
            job_vs_deposit()

        if options == "Age Group Performance":
            age_group_perf()

        if options == "Education Loan Statistics":
            edu_loan_stats()

    #Project 3
    st.subheader("Accounting Dashboard Project")
    with st.expander("Project Details"):
        st.write("GitHub: https://github.com/payalgoyal/Accounting_Dashboard.git")
        st.write("Tech Stack: Python, PySpark, MySQL, Matplotlib")
        accounting_project_details()

        options = st.selectbox("📊 Choose Insights ",["Select","Top 5 customers","Net Position","Monthly Trend"])
        if options == "Top 5 customers":
            top_customers()

        if options == "Net Position":
            net_position()

        if options == "Monthly Trend":
            monthly_trend()

    #Project 4
    st.subheader("PySpark Learning App")
    with st.expander("Project Details"):
        st.write("GitHub: https://github.com/payalgoyal/pyspark-learning-app.git")
        st.write("Tech Stack: Flask, PySpark, Python, CSV, JSON")
        pyspark_project_details()

    st.header("Returnship Readiness & Upskilling")
    with st.expander("Highlights"):
        st.markdown("""
            - Delivered business-ready insights such as product revenue trends, customer segmentation, and operational dashboards.
            - Practicing daily Git, SQL, Python ETL, Jupyter analysis, and Airflow orchestration.
            - Migrated all project pipelines into GitHub with modular code architecture, reusable ETL functions, and automated data loaders.
                    """)

    with st.expander("Career Break"):
        st.write("2017 – 2025")
        st.markdown("""
            - Focused on health recovery and technical upskilling during career break.
            - Built fully functional data engineering portfolio with real-world project simulations using production-grade technologies.
                    """)

    st.header("Professional Experience")
    with st.expander("Freelance Web Development"):
        st.write("Dec 2015 - Jul 2017")
        st.markdown("""
            - Built responsive websites using HTML, CSS, and JS for local businesses.
                    """)

    with st.expander("Tata Consultancy Services (TCS) - Software Engineer"):
        st.write("Jul 2013 – Nov 2015")
        st.markdown("""
            - Developed custom CRM modules using Microsoft Dynamics and SSRS.
            - Created automation scripts in Python for error tracking and reporting.
            - Awarded 'Shining Star' for top performance and client appreciation.

                    """)

    with st.expander("ISRO - MATLAB Developer (Intern)"):
        st.write("Jan 2013 – May 2013")
        st.markdown("""
            - Developed tools for satellite image processing.
            - Co-authored research publications with the R&D team.
                    """)

    st.markdown("---")
    st.header("Education")
    st.markdown("""
                B.Tech - Computer Science & Engineering\n
                Sikkim Manipal Institute of Technology | 2009-2013\n
                CGPA: 8.6 / 10\n
                Recipient of Merit Scholarship (All Semesters)
    """
)

    st.header("Awards & Recognition")
    st.markdown("""
      🔹 Shining Star, TCS (2015)  
      🔹 SMIT Merit Scholar, All Semesters  
    """)

if __name__ == "__main__":
    portfolio()