import streamlit as st
import smtplib
from email.message import EmailMessage

def sidebar_content():
    with open("Payal_Goyal_Resume_Data_engg.pdf", "rb") as file:
        st.sidebar.download_button(
            label="📄 Download My Resume",
            data=file,
            file_name="Payal_Goyal_Resume.pdf",
            mime="application/pdf"
        )

    st.sidebar.markdown("### 🔗 Connect with Me")
    st.sidebar.markdown("[GitHub](https://github.com/payalgoyal)")
    st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/yourprofile)")

    st.sidebar.title("📬 Contact Me")
    with st.sidebar.form(key='contact_form'):
        name = st.text_input("Your Name", key="name")
        sender_email = st.text_input("Your Email", key="sender_email")
        message = st.text_area("Your Message", key="message")
        submit_button = st.form_submit_button(label="Send Message")

    if submit_button:
        try:
            # Compose email
            msg = EmailMessage()
            msg['Subject'] = f"New message from {name}"
            msg['From'] = sender_email
            msg['To'] = "payalgoyal90@gmail.com"  
            msg.set_content(f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}")

            # Send email via Gmail SMTP
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("payalgoyal90@gmail.com", "ybci ughy youp qdgv")  
                smtp.send_message(msg)

            st.success("✅ Your message was sent successfully!")

        except Exception as e:
            st.error(f"❌ Failed to send message. Error: {e}")
