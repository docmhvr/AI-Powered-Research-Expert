import streamlit as st
import os
from model import clean_query, get_relevant_research, summarize_papers, make_paper_recommendation

# Set the title and description of the app
st.title("📄 AI Powered Research Expert")
st.write(
    "Enter your research goal, topic, or abstract below, and this app will provide research recommendations and relevant papers!"
)

# Ask for OpenAI API key
if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""

def save_api_key():
    st.session_state["openai_api_key"] = st.session_state["api_key_input"]

st.text_input(
    "Enter your OpenAI API key:",
    type="password",
    key="api_key_input",
    on_change=save_api_key
)

# Ensure the API key is set
if not st.session_state["openai_api_key"]:
    st.warning("Please enter your OpenAI API key to proceed.")
    st.stop()

# Ask the user for a question
query = st.text_area(
    "Enter your Research goal, topic or abstract!",
    placeholder="Can you give me a short summary or abstract?"
)

if query and st.button("Let's go!"):
    openai_api_key = st.session_state["openai_api_key"]

    # Clean the query
    cleaned_query = clean_query(query)

    # Get relevant research papers
    relevant_papers, urls = get_relevant_research(cleaned_query)

    # Summarize the papers
    summaries = summarize_papers(relevant_papers, openai_api_key)

    # Make paper recommendation
    recommendation = make_paper_recommendation(summaries, query, openai_api_key)

    # Save session state
    st.session_state['relevant_papers'] = relevant_papers
    st.session_state['urls'] = urls
    st.session_state['summaries'] = summaries
    st.session_state['recommendation'] = recommendation

# Display the research results
if 'relevant_papers' in st.session_state:
    relevant_papers = st.session_state['relevant_papers']
    urls = st.session_state['urls']
    summaries = st.session_state['summaries']
    recommendation = st.session_state['recommendation']

    # Create summaries and save to session state
    tab1, tab2 = st.tabs(['Relevant Papers', 'Assistant Recommendation'])

    with tab1:
        for paper, summary, url in zip(relevant_papers, summaries, urls):
            st.markdown(f'#### [{paper.title}]({url})')
            with st.expander(f'Summary of {paper.title}'):
                st.markdown(f'*{summary}*')

    with tab2:
        st.markdown(f'**{recommendation}**')
