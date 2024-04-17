import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Basic Shapes",
    page_icon="👋",
)
# TODO Devin, think about whether there's a better way to re-use the code so we don't have to paste this on every page
top1,top2 = st.columns(2)
# TODO update the project title
top1.write("# Your Title of the project")
top1.write("## Basic Shapes")
c1, c2, c3,c4 = top2.columns(4)

c1.markdown('<a href="/start" target="_self"><button>Home</button></a>', unsafe_allow_html=True)
c2.markdown('<a href="/advanced_shapes" target="_self"><button>Advanced Shapes</button></a>', unsafe_allow_html=True)
c3.markdown('<a href="/custom_shapes" target="_self"><button>Custom Shapes</button></a>', unsafe_allow_html=True)
c4.markdown('<a href="/additional_resources" target="_self"><button>Additional Resources</button></a>', unsafe_allow_html=True)

st.write("""
Welcome to our basic shapes page! Here we provide simple animations to demonstrate building up volumes in various coordinate systems. Utilize the widgets below to learn more. 
""")


option = st.selectbox(
    'select a shape for integration',
    ('Cone','Box','Sphere'))

st.write('You selected:', option)
if option == "Cone":
    st.video("Cone.mp4")
elif option == "Box":
    st.video("CartesianExample.mp4")
elif option == "Sphere":
    st.video("SphereExample(1).mp4")
