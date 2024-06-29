<h1>Gemini Quizifiy Mission</h1>
<h2>Overview</h2>

<p>The goal of the Gemini Quizify Mission was to develop a streamlit application that utilizes the Gemini LLM to produce a quiz with multiple choice questions, where the quiz questions are generated from a one or more pdf files on a specific topic. The projected contained 10 tasks, which can be described as:</p>

<ol>
    <li>Google Cloud, Vertex AI, & SDK Authentication- Create a google cloud account and enable the Vertex AI API.</li>
    <li>Dev Environment Setup- Set up the development environment by forking the repository, create your own local and remote repository, and setting up the service accounts.</li>
    <li>Document Ingestion- Create a file uploader in the streamlit application using the PyPDFLoader.</li>
    <li>Embedding with VertexAI & Langchain- Create embeddings with VertexAI and Langchain.</li>
    <li>Date Pipeline to Chroma DB- Transform the data with ChromaDB by processing documents and splitting them into chunks. Then create a Chroma collection.</li>
    <li>Streamlit UI for Data Ingestion- Use Streamlit to create a user friendly UI for ingesting PDF documents, choosing a topic and selecting the number of questions.</li>
    <li>Guiz Generator Class- Create a QuizGenerator object with the "gemini-pro" model.</li>
    <li>Generate Quiz Algorithm- Develop a Generate Quiz Algorithm that verifies if each quiz question is unique.</li>
    <li>Generate Quiz UI- Create a QuizManager object for storing and managing the questions, and implement the ability to switch between questions in the application.</li>
    <li>Screen State Handling- initalize the question bank, set topic and question quantity with Streamlit widgets, and manage quiz generation and display.</li>
</ol>


<h2>Running the project</h2>
<p>First, you will need to create your own Google Cloud account, set up a project, enable the Vertex AI API and create a service account. Then you will need to set up your local environment variable for the google authenatication API key with the local variable 'GOOGLE_APPLICATION_CREDENTIALS=application_key.json'. Where application_key.json can be downloaded from the service account. Alternatively you can run the command <a href="https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login">'gcloud auth application-default login'</a> command to connect your Google cloud account, but the <a href="https://cloud.google.com/sdk/docs/install">SDK must be installed</a>.</p>

<p>Starting the application on the local machine is simple, simply run the task 10 using the 'streamlit run task_10.py' command. This will launch the application on locally on your machine. Upload small documents, the application does not have the capacity to digest large documents. From there you can choose your topic, number of questions and then the quiz will be generated.</p>


