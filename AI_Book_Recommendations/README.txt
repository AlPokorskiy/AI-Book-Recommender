
Made by: Alexandr  Pokorskiy
Date: 08/28/2023

****************************************************************************************
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

****************************************************************************************
Steps to run:
1. Make sure to have pip installed the following:
	- Replicate and have a replicate API key - https://replicate.com/
	- os - Miscellaneous operating system interfaces - https://docs.python.org/3/library/os.html
	- Streamlit - https://docs.streamlit.io/library/get-started/installation
2. Accuire and input the API key for the LLaMa 2 AI to get autheticated and run
	- Create a replicate account with GitHub and go to the following link https://replicate.com/account/api-tokens
	- Once the token is accuired paste it into a file called 'api_key_holster.txt' 
		- From this file python will read the key and apply to the necessary compopnent in order to authenticate
	
3. Once that is done the app needs to be ran through the terminal, you are pros and know this process but for the sake of my own sanity:
	- open up either in IDE terminal or command line terminal and type the following command:
		streamlit run [Full address where the project is stored]\main.py
4. Enjoy!!! 

NOTE: The Replicate API key is time limited based on how long you use it, here is the quote from the pricing page(https://replicate.com/pricing): 
	You can use Replicate for free, but after a bit you'll be asked to enter your credit card. 
	You pay by the second for the predictions you run. 
	The price per second varies based on the hardware the model is run on.

****************************************************************************************