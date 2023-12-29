import streamlit as st
import webbrowser
from PIL import Image


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


#opening the image

image = Image.open('QNA.jpeg')



#displaying the image on streamlit app

st.image(image, caption='ND' , width=200 )


st.header("This is QNA Consultant page")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

path = "..."
image = Image.open('QNA.jpeg')

st.write("Management is efficiency in climbing the ladder of success; leadership determines whether the ladder is leaning against the right wall.")
#st.image(image, width = 150)
st.write("If you have more money than brains, you should focus on outbound marketing. If you have more brains than money, you should focus on inbound marketing")
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



