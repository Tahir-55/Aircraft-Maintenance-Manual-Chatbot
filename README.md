Aircraft Maintenance Manual Chatbot The objective of this project is to build an interactive chatbot that can use a PDF of an aircraft maintenance manual to reply to inquiries. The chatbot answers user questions and locates relevant content in the handbook by utilizing Natural Language Processing (NLP) techniques including question-answering models and embedding-based search.

Qualities Automated text extraction from an uploaded PDF aircraft maintenance manual is known as PDF parsing. Embedding-Based Search: This method saves text passages in an FAISS vector index for efficient similarity searches after encoding them with a SentenceTransformer model. Question-Answering: By using the "question-answering" pipeline created by Hugging Face, it is possible to reply to user questions by using relevant context found inside the document. Using an interactive chatbot's easy-to-use interface, ask questions and receive answers based on the airline handbook.

Steps to Execute:
--------------------------
Install Required Packages
Open a terminal in VS Code and create a Python virtual environment:

python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
---------------------
Then install the required dependencies:

pip install pydantic==1.10.7 langchain==0.0.150 pypdf pandas matplotlib tiktoken transformers openai faiss-cpu
pip install sentence-transformers PyPDF2
-----------------
Save Dependencies
Save the installed dependencies in requirements.txt:

pip freeze > requirements.txt
------------------
Run the Application:

python main.py
--------------------------

 Install Docker

 For Windows:

https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-amd64&_gl=1*cq7vxu*_gcl_au*MTg1ODgxMDEwMS4xNzMyNDE1MjM1*_ga*Nzc5MjQwODUuMTczMjQxNTIzNg..*_ga_XJWPQMJYHQ*MTczMjQxNTIzNS4xLjEuMTczMjQxNTI4MS4xNC4wLjA.

--------------------------
Build and Run Docker Container
 1. Build the Docker image:


docker build -t pdf-chatbot .

 2. Run the Docker container:

docker run -it --rm -v $(pwd)/data:/app/data pdf-chatbot
-----------------------
-----------------------
-----------------------


Run the Full Setup

Steps:
Install Dependencies Locally:

Save dependencies to requirements.txt.

pip freeze > requirements.txt

Build and Run Docker Container:

docker build -t pdf-chatbot .
docker run -it --rm -v $(pwd)/data:/app/data pdf-chatbot

Run the App:

The tkinter app launches, allowing you to upload a PDF, interact with the chatbot, and get responses.