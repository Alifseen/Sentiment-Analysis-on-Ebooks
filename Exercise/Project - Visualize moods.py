import streamlit as st
from plotly.express import line
from backend import sent

d, p, n = sent()

st.title("Dairy Tone")
st.subheader("Positivity Chart")
figp = line(x=d, y=p, labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(figp)

st.subheader("Negativity Chart")
fign = line(x=d,y=n, labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(fign)