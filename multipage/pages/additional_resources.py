import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Additional Resources",
    page_icon="👋",
)
# TODO Devin, think about whether there's a better way to re-use the code so we don't have to paste this on every page
top1,top2 = st.columns(2)
# TODO update the project title
top1.write("# Additional Resources")
c1, c2, c3,c4 = top2.columns(4)

c1.markdown('<a href="/start" target="_self"><button>Home</button></a>', unsafe_allow_html=True)
c2.markdown('<a href="/advanced_shapes" target="_self"><button>Basic Shapes</button></a>', unsafe_allow_html=True)
c3.markdown('<a href="/advanced_shapes" target="_self"><button>Advanced Shapes</button></a>', unsafe_allow_html=True)
c4.markdown('<a href="/custom_shapes" target="_self"><button>Custom Shapes</button></a>', unsafe_allow_html=True)