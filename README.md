# AI Agent - Social Media Content Generator 🤖

## Overview

This project is an AI-powered content generation agent designed to create optimized text content for social media platforms and digital channels.

The application uses a Large Language Model (LLM) to generate personalized content based on user-defined parameters such as:

* Topic
* Publishing platform
* Writing tone
* Target audience
* Content length
* SEO keywords
* Call-to-action (CTA)
* Hashtags

The goal of this project is to demonstrate the implementation of an AI Agent capable of interacting with an LLM, processing user instructions, and generating marketing-oriented content automatically.

---

# Project Structure

```
AIAGENT_POST_GENERATE/
│
├── .env
├── app.py
└── requirements.txt
```

## Files Description

| File               | Description                                                            |
| ------------------ | ---------------------------------------------------------------------- |
| `.env`             | Stores environment variables, including the Groq API Key               |
| `app.py`           | Main application containing the Streamlit interface and AI agent logic |
| `requirements.txt` | List of Python dependencies required to run the project                |

---

# Technologies Used

## Python

The main programming language used to build the AI agent.

---

## Streamlit

Streamlit is used to create the web interface for interacting with the AI agent.

The application provides input fields where users can define:

* Content topic
* Social media platform
* Writing style
* Audience
* SEO keywords
* Additional generation options

---

## LangChain

LangChain is used as the framework responsible for connecting the application with the Large Language Model.

It provides:

* Prompt management
* LLM orchestration
* Processing pipeline creation

The project uses:

* `ChatPromptTemplate` to define AI instructions
* `StrOutputParser` to process generated responses

---

## Groq API

The project uses Groq as the Large Language Model provider.

The configured model is:

```
llama-3.3-70b-versatile
```

Groq provides fast inference capabilities for Large Language Models, allowing the application to generate content efficiently.

---

## python-dotenv

Used to load environment variables from the `.env` file.

The application requires the following environment variable:

```
GROQ_API_KEY
```

This key is used to authenticate requests to the Groq API.

---

# How the AI Agent Works

The application follows this workflow:

1. The user provides content requirements through the Streamlit interface.
2. The application builds a customized prompt containing:

   * Topic
   * Platform
   * Tone
   * Audience
   * Content length
   * SEO requirements
   * CTA and hashtag preferences
3. The prompt is sent to the Groq LLM through LangChain.
4. The model generates optimized content.
5. The generated text is displayed in the application.

---

# Installation and Setup

## 1. Clone the repository

Clone this repository:

```bash
git clone <repository-url>
```

Navigate into the project folder:

```bash
cd AIAGENT_POST_GENERATE
```

---

# 2. Create and activate a virtual environment

Creating a virtual environment is recommended to isolate project dependencies.

Create the environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

# 3. Install project dependencies

All project dependencies are listed in the `requirements.txt` file.

Install them using:

```bash
pip install -r requirements.txt
```

This command installs all required packages, including:

* Streamlit
* LangChain
* LangChain Groq integration
* Groq SDK
* python-dotenv
* Supporting AI and data processing libraries

---

# 4. Configure Groq API Key

This project requires a Groq API Key to communicate with the Large Language Model.

## Creating a Groq Account

1. Access the Groq platform:

https://console.groq.com/

2. Create an account or sign in.

3. After authentication, open the API Keys section:

```
Dashboard → API Keys
```

4. Click:

```
Create API Key
```

5. Enter a name for your API Key.

6. Generate and copy the API Key.

⚠️ Keep your API Key secure. Never commit it to GitHub or share it publicly.

---

## Configure the `.env` file

Create or update the `.env` file in the project root directory:

```
AIAGENT_POST_GENERATE/
│
├── .env
├── app.py
└── requirements.txt
```

Add your Groq API Key:

```env
GROQ_API_KEY=your_api_key_here
```

Replace:

```
your_api_key_here
```

with the API Key generated in Groq.

---

# 5. Run the Application

Inside the project root directory, execute:

```bash
python -m streamlit run app.py
```

After starting, Streamlit will provide a local URL similar to:

```
http://localhost:8501
```

Open this URL in your browser.

---

# Example Usage

The user can generate content by defining:

## Topic

Example:

```
Healthy lifestyle
```

## Platform

Available options:

* Instagram
* Facebook
* LinkedIn
* Blog
* Email

## Tone

Available options:

* Normal
* Informative
* Inspirational
* Urgent
* Informal

## Target Audience

Available options:

* General audience
* Young adults
* Families
* Seniors
* Teenagers

## Additional Features

The user can also request:

✅ SEO optimized content
✅ Call-to-action generation
✅ Relevant hashtags

---  

# License

This project is intended for educational and demonstration purposes related to AI Agents, Large Language Models, and Generative AI applications.
