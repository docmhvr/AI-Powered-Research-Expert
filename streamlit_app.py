import streamlit as st
import utils

# Show title and description.
st.title("📄 AI Powered Research Expert")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management

# Ask the user for a question via `st.text_area`.
query = st.text_area(
    "Enter your Research goal, topic or abstract!",
    placeholder="Can you give me a short summary or abstract?"
)

if query and st.button("Lets go!"):

    # Process the question to extract essential query.
    cleaned_query = utils.clean_query(query)

    # relevant research papers, 
     
    # references
    
    # research recommendation, 
    
    document = ""
    messages = [
        {
            "role": "user",
            "content": f"Here's a document: {document} \n\n---\n\n {query}",
        }
    ]

    # Generate an answer using Groq API.
    stream = ""

    # Stream the response to the app using `st.write_stream`.
    st.write_stream(stream)
