import gradio as gr
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
import os

# Mengatur LLM
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")

def handle_complaint(complaint: str) -> str:
    #Buat instance LLM dengan nilai temprature 0,9 (nilai lebih tinggi membuat keluaran lebih acak).
    

    # Merancang template untuk merespon komplain
    prompt = PromptTemplate(input_variables=["complaint"], template="I am part of some group/company's customer service. I got some complaints like this: {complaint}. Here's my responses:")

    # Membuat model bahasa berantai dengan template yang telah dirancang
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(complaint)

# Membuat antarmuka Gradio untuk fungsi handle_complaint
iface = gr.Interface(fn=handle_complaint, inputs="text", outputs="text")
iface.launch(share=True)