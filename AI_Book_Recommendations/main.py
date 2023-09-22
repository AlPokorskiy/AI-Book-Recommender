"""
========================================================================================================================
Made by: Alexandr  Pokorskiy

Project description:
    Link: https://mym-official.notion.site/LLM-Internship-Assessment-33484cafa9d748058729cbccfbcb614b
    Task:
        Deploy a Streamlit application that allows a user to enter in text and have a back and forth conversation powered
        by an LLM model (preferably Llama or another open-source hugging face framework.)
    Example: https://platform-eleena.vercel.app/eleena

Project made using the Streamlit and LLaMa AI
    Streamlit
        - https://streamlit.io/ Front end of the software, used for the creating a vibrant user interface that will be
            connecting directly to the AI Language model (LLAMA 2)
    LLaMa 2
        - AI language model used for text communication with the user and recommending the right book sets based on the
        user's preferences and communication with the AI - https://ai.meta.com/llama/#resources
        - Using pip install replicate and os and a use of a replicate API key found here: https://replicate.com/
    DATASET
        - By using a dataset found in Kaggle as such: https://www.kaggle.com/datasets/arpansri/books-summary?resource=download
        - This dataset is mainly used for the AI to go through the books and their summaries to better adjust for the user's preference

========================================================================================================================

AI DATASET TRAINING PROCESS
1.Collect and Prepare Data: You need to gather a dataset that is relevant to the task you want the AI to learn.
This could be text, images, audio, or any other type of data depending on the application. The data should be cleaned,
preprocessed, and organized before being fed to the AI model.

2.Choose an AI Model: Depending on the nature of your data and the task you want the AI to perform, you'll need to choose
an appropriate AI model. For example, if you're working with text data, you might choose a model like GPT-3 for language-related tasks,
or if you're dealing with images, you might choose a convolutional neural network (CNN).

3.Training Process: During the training process, you provide the AI model with the dataset you've collected. The model
learns by adjusting its internal parameters based on the patterns and relationships present in the data. The goal is for
the model to generalize from the training data and be able to make accurate predictions or classifications on new, unseen data.

4.Validation and Testing: It's important to have separate datasets for validation and testing. These datasets help you
evaluate how well the model is performing during training and how well it generalizes to new data. You use the validation
data to fine-tune the model's hyperparameters and architecture to prevent overfitting (when the model memorizes the training
data rather than learning useful patterns) and underfitting (when the model doesn't capture the complexity of the data).

5.Fine-Tuning and Iteration: Based on the performance on the validation set, you might need to fine-tune the model's
parameters, adjust its architecture, or modify other aspects of the training process. This might involve several iterations
of training, validation, and adjustment.

6.Evaluation and Deployment: Once you're satisfied with the model's performance on the validation and testing data,
you can deploy it for real-world applications. Keep in mind that the model's performance should be monitored in a production
environment, and updates might be necessary as new data becomes available.


"""
import streamlit as st
import os
import replicate

st.set_page_config(
    page_title="Book recommender AI",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'Report a bug': "https://www.google.com",
        'About': "### This is a custom made AI helper built using LLaMa 2 and Streamlit | Link: "}
)
st.title('Welcome Book Assistant AI!')
st.markdown('-----------------------------------------------------')

st.text("Made by Alex Pokorskiy")
st.text("Don't be afraid he doesn't bite! (or take over the world)")

# Pre-prompt so that the AI does not misunderstand that he is the machine and needs to be responding as an assistant
pre = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."

# Stores the response of the as a string
ai_response = ""

# Replicate API key, please insert your own key into the designated file
api_file = open("api_key_holster.txt", "r")
key = api_file.readline()
os.environ["REPLICATE_API_TOKEN"] = str(key)

# Introduction section for when the user is first loading in, this isn't the robot talking just a quick welcome message
with st.chat_message('assistant'):
    st.markdown('''
    :red[Hi there!] I am your helpful :blue[AI Assistant]! 
    
    I am ready to handle any challenge you throw at me big or small!
    
    -Please ask me any question you may have!
        
    -Don't worry I don't bite like that other guy with the terminators 🦾🦿 
    
    Lets get started!
    ''')

# Dataset feeder - Here I feed the AI a csv data for referencing the books in better detail
filepath = 'books_summary.csv'  # Filepath to the dataset that trains the AI
instr = "Go to this filepath and interpret the data " + filepath + " this is for recommending books"  # Prompt for the AI to use the dataset for deeper understanding/training on launch

replicate.run(
    'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
    # This is the mdel of LLaMa 2 13b that is used from replicate
    input={"prompt": f"{pre} {instr} assistant:",  # This is the input prompt that will initially run
           "temperature": 0.9, "top_p": 0.9, "max_length": 200, "repetition_penalty": 1})
# Temperature referes to how detailed/in-depth the AI's answer/reply is
# max_length is how many characters can the AI print out for its answer currently set to 200 characters to minimize load times more characters means more processing time

# Create the necessary role/content key/value pairs for both AI and user
if "msg" not in st.session_state:
    st.session_state.msg = []

for msg in st.session_state.msg:  # Save session state under the specific role and display it
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
# User input stored as string that will then be sent to the AI as a prompt
user_query = st.chat_input('Enter query')

if user_query:  # Must be true to start the process
    # User entry recorded
    with st.chat_message('user', avatar="human"):  # Name is user and avatar icon is human
        st.markdown(user_query)

    st.session_state.msg.append({"role": "user", "content": user_query})
    # Store the AI response value in the rbt container
    rbt = replicate.run(
        'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
        input={"prompt": f"{pre} {user_query} assistant:",  # User query added as part of the prompt
               "temperature": 0.8, "top_p": 0.9, "max_length": 400, "repetition_penalty": 1})

    with st.chat_message('assistant'):
        # Go through the items that the AI returns and stuff them into a string
        for item in rbt:
            ai_response += item
        st.markdown(ai_response)  # Set it into the Message box

    st.session_state.msg.append({"role": 'assistant', "content": ai_response})
