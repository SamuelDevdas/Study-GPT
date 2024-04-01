# import required modules
import streamlit as st
import streamlit.components.v1 as components
from embedchain import App
from io import StringIO

# import query_mdx

# Set main page config
st.set_page_config(
    page_title="STUDY-GPT",
    page_icon=":robot_face:",
    initial_sidebar_state="auto",
    layout="centered",
)

# Set the title of the main window
st.markdown(
    """ 
    <h1 style='text-align: center; color: #FFFFFF; font-family: 'Bebas Neue'; font-size: 4em; text-shadow: 2px 2px #808080;'>STUDY-GPT</h1>    
    <h5 style='text-align: center; color: #d9d38f; font-family: 'Bebas Neue'; font-size: 1em;'>Transform Your Study Media into Notes, Chat Your Way to Success!</h5>

    """,
    unsafe_allow_html=True,
)

# Initialize session state counters

if "file_uploaded" not in st.session_state:
    st.session_state["file_uploaded"] = 0


st.write("#")

# Document upload for RAG
st.write("### 1. Upload your document below:")

# Add file uploader
file_uploaded = st.file_uploader("Choose a file", type=["mdx"])

# To make sure the submit button is clicked only once
if file_uploaded:
    st.session_state.file_uploaded = 1
else:
    st.session_state.file_uploaded = 0

# To convert to a string based IO:
if file_uploaded is not None:
    stringio = StringIO(file_uploaded.getvalue().decode("utf-8"))

# Display the uploaded document
if file_uploaded:
    st.write("##### Here is the document you uploaded:")
    st.write(stringio)

#####################################################################

st.write("#")

# Chat with the document

# Text input box for the user to input their prompt
st.write("### 2. Chat with the document:")
prompt_input = st.text_area(
    "",
    height=150,
    max_chars=500,
    label_visibility="collapsed",
    placeholder="""Try prompts like : \n‘What is this document about?’                                \nOR ‘Summarize the key points?’
                                    \nOR Write a joke about this document?’
                                    \nOR ‘create a json about the sentiments of the sections of the document’
                                    """,
)
#####################################################################



if file_uploaded is None:
    # st.write("### Please upload a document to chat with it.")
    # The line `st.write("""<span style="color:blue">some *blue* text</span>""",
    # unsafe_allow_html=True)` is attempting to write HTML code within a Streamlit application.
    st.write("""<h3 style="color: #d9d38f">Please upload a document to chat with it.</h3>""", unsafe_allow_html=True)

# Function to chat with the document
# @st.cache_data
def chat(prompt_input):
    app = App()

    # Clear old data
    app.reset()

    if file_uploaded:
        app.add(str(stringio.read()), data_type="text")

    answer = app.query(
        f"""{prompt_input}""",
    )
    # print(answer)
    return answer


# Call the chat function for
if prompt_input:
    answer = chat(prompt_input)

with st.spinner('Wait for it...'):
    # Display the response to the user
    submit_button = st.button("Send", type="primary")

    # Display the response to the user
    if submit_button and answer:
        st.write("##### Here is the response to your query:")
        st.write(answer)
        st.success('Done!')



#####################################################################

# Function to Generate notes from the document and download as a text file
notes_prompt = """ Rewrite and return as all the content covered in the doc as properly formatted, Comprehensive
            professional quality lecture notes, with a separate section containing real wikipedia url citations for only the Generative AI or other contextually related keywords present in the doc contents as a numbered section."""

@st.cache_data  
def generate_notes():
    # For gpt-4 load llm configuration from gpt4.yaml file
    # app = App.from_config(config_path="configs/gpt4.yaml")
    app = App()

    app.reset()

    app.add(str(stringio.read()), data_type="text") #data_type="text"

    answer = app.query(
        f"""{notes_prompt}""",
    )
    print(answer)
    return answer

st.write("#")

# Chat with the document

# Text input box for the user to input their prompt
st.write("### 2. Create notes from the document:")

with st.spinner('Wait for it...'):
    # Add submit button for generating notes
    submit_button = st.button(
        "Create Notes", on_click=generate_notes, type="primary"
    )

    # Download the generated notes as a Markdown file
    if submit_button:
        file = generate_notes()
        # Download the generated notes as a Markdown file
        st.download_button(
            label="Download the Notes",
            data= file,
            file_name="notes.md",
        )
        st.success('Done!')





