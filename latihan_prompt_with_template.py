import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain_openai import ChatOpenAI

openai_api_key = "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"
os.environ["OPENAI_API_KEY"] = openai_api_key

# Mendefinisikan model AI
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key= openai_api_key
)

# Mendefinisikan PromptTemplate sebagai format prompt untuk input dari user
def chatbot(user_input):
    # defining a template
    template = """Pertanyaan: {pertanyaan}
    Tolong berikan jawaban yang step by step:
    """
    prompt = PromptTemplate(template=template, input_variables=["pertanyaan"])
    formated_prompt =prompt.format(pertanyaan=str(user_input))
    return llm.invoke(formated_prompt).content
   
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)
