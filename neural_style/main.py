import streamlit as st
import os
from PIL import Image
import style

st.title("Pytorch Style Transfer")


img = st.sidebar.file_uploader("Choose an image...", type="jpeg")
if img is not None:
    ii = (Image.open(img).save(
        "images/content-images" + "content.jpeg"))
    input_image = "images/content-images" + "content.jpeg"

# TODO: delete content image after done

style_name = st.sidebar.selectbox(
    'Choose a style...', ('candy', 'mosaic', 'rain_princess', 'udnie'))


model = "saved_models/" + style_name + ".pth"
output_image = "images/output-images"+style_name+".jpeg"

if img is not None:
    st.write("### Source Image:")

    image = Image.open(img)

    st.image(image, caption='Uploaded Image.', width=300)

clicked = st.button("Stylize")
if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write("### Output Image:")

    image = Image.open(output_image)

    st.image(image, caption='Output Image.', width=300)
