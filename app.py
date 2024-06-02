import streamlit as st
from src.main import crew,crew2
from PIL import Image
import torch
from diffusers import StableDiffusionXLPipeline, DPMSolverSinglestepScheduler
import os

os.makedirs("output",exist_ok=True)
# image = Image.open("")

# # Load model.
pipe = StableDiffusionXLPipeline.from_pretrained("sd-community/sdxl-flash", torch_dtype=torch.float16).to("cpu")
pipe.scheduler = DPMSolverSinglestepScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")


st.title("Social Media Blog and Post")

if "message" not in st.session_state:
    st.session_state.messages = []
 
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])   
        
    
if prompt := st.chat_input("Write Your Topic"):
    with st.chat_message(name="assistant"):
        st.markdown(prompt)
        
    st.session_state.messages.append({"role": "assistant", "content":prompt})
    text = {"topic": prompt}
    result = crew.kickoff(inputs=text) 
    result2 = crew2.kickoff(inputs=text)
    
    responce = f"Echo: {result}"
    split_prompts = [prompt.strip() for prompt in result2.split("\n") if result2.strip()]
    for i in split_prompts:
        pipe(i, num_inference_steps=7, guidance_scale=3).images[0].save("output/output"+f"{i[0:1]}"+".png")
    with st.chat_message(name="assistant"):
        st.markdown(responce)
        
    st.session_state.messages.append({"role": "assistant", "content":responce})
    image = Image.open("output/output.png")
    image1 = Image.open("output/output2.png")
    image2 = Image.open("output/output3.png")
    image3 = Image.open("output/output4.png")
    image4 = Image.open("output/output5.png")
    st.image(image,width=200)
    st.image(image1,width=200)
    st.image(image2,width=200)
    st.image(image=image3, width=200)
    st.image(image=image4, width=200)
# with st.chat_message(name="assistant"):
#     st.write("Hello")output