# Import necessary libraries
import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the Groq client with the API key
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Streamlit UI
st.title("Personalized Study Assistant")
st.write("Generate a custom study plan to meet your goals.")

# Inputs
study_topic = st.text_input("Enter the study topic or exam subject:")
days = st.number_input("Number of days available for preparation:", min_value=1, step=1)
hours_per_day = st.number_input("Hours per day you can invest:", min_value=1, step=1)

if st.button("Generate Study Plan"):
    if study_topic and days > 0 and hours_per_day > 0:
        # Prompt for the model
        prompt = f"""
        Create a detailed, customized study plan to help prepare for {study_topic} over {days} days. I can dedicate {hours_per_day} hours per day to studying. Please divide the topics effectively, prioritizing key areas for maximum retention, and include daily goals, tips for revision, and any recommended resources. The study plan should be well-structured and adaptable, with checkpoints to assess progress and adjust if needed.
        """

        # Generate study plan
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )

        # Display result
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please fill in all fields.")

