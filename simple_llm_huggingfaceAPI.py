import os
from langchain_community.llms import HuggingFaceEndpoint 
import gradio as gr

# Mengatur environment variable "OPENAI_API_KEY" dengan OpenAI API key milikmu. ini diperlukan untuk proses autentikasi ke OpenAI API.
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "API_KEY_MARCO"

# Mendefinisikan jenis model 
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")

def chatbot(prompt):
    return llm.invoke(prompt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)
