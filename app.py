import streamlit as st
import uuid
import chromadb
import os
import pandas as pd
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Set your Groq API key here directly
GROQ_API_KEY = "Ur API Key"

# Load portfolio CSV once during startup
portfolio_df = pd.read_csv("my_portfolio.csv")
portfolio_links = "\n".join(
    [f"- {row['Techstack']}: {row['Links']}" for _, row in portfolio_df.iterrows()]
)

# Page configuration
st.set_page_config(
    page_title="📧 Cold Email Generator",
    page_icon="📧",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .email-output {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📧 Cold Email Generator</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Generate personalized cold emails for job opportunities using AI</p>', unsafe_allow_html=True)

# Sidebar for configuration
st.sidebar.title("⚙️ Configuration")

# Model selection
model_options = [
    "llama3-8b-8192",
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]
selected_model = st.sidebar.selectbox("Select Model:", model_options)

# Main content area
st.markdown('<h3 class="section-header">🔗 Job URL Input</h3>', unsafe_allow_html=True)
job_url = st.text_input(
    "Enter the job posting URL:",
    placeholder="https://careers.company.com/job-posting",
    help="Paste the URL of the job posting you want to apply for"
)

# Generate email button
if st.button("🚀 Generate Cold Email", type="primary", use_container_width=True):
    if not job_url:
        st.error("❌ Please enter a job URL")
    else:
        try:
            with st.spinner("🔍 Analyzing job posting..."):
                llm = ChatGroq(
                    temperature=0,
                    groq_api_key=GROQ_API_KEY,
                    model_name=selected_model
                )

                loader = WebBaseLoader(job_url)
                page_data = loader.load().pop().page_content

                prompt_extract = PromptTemplate.from_template(
                    """
                    ### SCRAPED TEXT FROM WEBSITE:
                    {page_data}
                    ### INSTRUCTION:
                    The scraped text is from the career's page of a website.
                    Your job is to extract the job postings and return them in JSON format containing the 
                    following keys: `role`, `experience`, `skills` and `description`.
                    Only return the valid JSON.
                    ### VALID JSON (NO PREAMBLE):    
                    """
                )

                chain_extract = prompt_extract | llm
                res = chain_extract.invoke(input={'page_data': page_data})

                json_parser = JsonOutputParser()
                json_res = json_parser.parse(res.content)

            with st.spinner("✍️ Generating personalized email..."):
                prompt_email = PromptTemplate.from_template(
                    """
                    ### JOB DESCRIPTION:
                    {job_description}

                    ### PORTFOLIO LINKS:
                    {portfolio_links}

                    ### INSTRUCTION:
                    You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
                    the seamless integration of business processes through automated tools. 
                    Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
                    process optimization, cost reduction, and heightened overall efficiency. 
                    Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
                    in fulfilling their needs and also showcasing some relevant portfolio links.
                    Remember you are Mohan, BDE at AtliQ. 
                    Do not provide a preamble.
                    ### EMAIL (NO PREAMBLE):
                    """
                )

                chain_email = prompt_email | llm
                email_res = chain_email.invoke({
                    "job_description": str(json_res),
                    "portfolio_links": portfolio_links
                })

            st.markdown('<h3 class="section-header">📋 Extracted Job Information</h3>', unsafe_allow_html=True)
            if json_res:
                job_info = json_res[0] if isinstance(json_res, list) else json_res
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("🎯 Role")
                    st.write(job_info.get('role', 'N/A'))

                    st.subheader("💼 Experience Required")
                    st.write(job_info.get('experience', 'N/A'))

                with col2:
                    st.subheader("🛠️ Skills Required")
                    st.write(job_info.get('skills', 'N/A'))

                st.subheader("📝 Job Description")
                st.write(job_info.get('description', 'N/A'))

            st.markdown('<h3 class="section-header">📧 Generated Cold Email</h3>', unsafe_allow_html=True)
            st.markdown(f'<div class="email-output">{email_res.content}</div>', unsafe_allow_html=True)

            st.download_button(
                label="📥 Download Email",
                data=email_res.content,
                file_name="cold_email.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.error("Please check the job URL and try again.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>🚀 Built with Streamlit | 🤖 Powered by Groq & LangChain</p>
        <p>💡 Just paste a job URL to generate a personalized cold email</p>
    </div>
    """,
    unsafe_allow_html=True
)
# Adjust email output styling to make the text color black
st.markdown("""
<style>
  .email-output {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 4px solid #3498db;
    margin-top: 1rem;
    color: #000; /* Set text color to black */
  }
</style>
""", unsafe_allow_html=True)
