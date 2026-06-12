import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

## conexão com a LLM
id_model = "llama-3.3-70b-versatile"
llm = ChatGroq(
    model=id_model,
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

## função de geração
def llm_generate(llm, prompt):
  template = ChatPromptTemplate.from_messages([
      ("system", "Você é um especialista em marketing digital com foco em SEO e escrita persuasiva."),
      ("human", "{prompt}"),
  ])

  chain = template | llm | StrOutputParser()

  res = chain.invoke({"prompt": prompt})
  return res

st.set_page_config(page_title = "Gerador de conteúdo 🤖", page_icon="🤖")
st.title("Gerador de conteúdo")

# Campos do formulário
topic = st.text_input("Tema:", placeholder="Ex: saúde mental, alimentação saudável, prevenção, etc.")
platform = st.selectbox("Plataforma:", ['Instagram', 'Facebook', 'LinkedIn', 'Blog', 'E-mail'])
tone = st.selectbox("Tom:", ['Normal', 'Informativo', 'Inspirador', 'Urgente', 'Informal'])
length = st.selectbox("Tamanho:", ['Curto', 'Médio', 'Longo'])
audience = st.selectbox("Público-alvo:", ['Geral', 'Jovens adultos', 'Famílias', 'Idosos', 'Adolescentes'])
cta = st.checkbox("Incluir CTA")
hashtags = st.checkbox("Retornar Hashtags")
keywords = st.text_area("Palavras-chave (SEO):", placeholder="Ex: bem-estar, medicina preventiva...")
