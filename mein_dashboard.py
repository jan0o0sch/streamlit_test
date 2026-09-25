import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import time
from io import StringIO


st.set_page_config(page_title="meine erste streamlit app", layout="wide")

# run: streamlit run mein_dashboard.py

st.write("Wir bauen unsere erste Streamlit App.")

st.title("This is the app title")        # groesste Ueberschrift (Seitentitel)
st.header("This is the header")          # Abschnitts-Ueberschrift

st.subheader("This is the subheader")    # kleinere Unter-Ueberschrift
st.caption("This is the caption")        # kleiner, grauer Hinweistext
st.code("x = 2021")                      # Code-Block mit Syntax-Hervorhebung
st.latex(r''' a+a r^1+a r^2+a r^3 ''')   # mathematische Formel (LaTeX)


st.divider(width="stretch")
st.markdown("This is the markdown")      # Text mit Markdown-Formatierung (**fett**, *kursiv*, ...)
st.markdown("**fett**, *kursiv*, ~~durchgestrichen~~ und `inline code`")

st.divider(width="stretch")
st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)
st.divider(width="stretch")

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
 
st.divider(width="stretch")

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

st.divider(width="stretch")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

st.divider(width="stretch")

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

st.divider(width="stretch")

uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)

st.divider(width="stretch")


with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

st.divider(width="stretch")

with st.spinner("Wait for it...", show_time=True):
    time.sleep(1)
st.success("Done!")
st.button("Rerun")


st.divider(width="stretch")

st.success("You did it!")                          # gruen: Erfolg
st.error("Error occurred")                         # rot: Fehler
st.warning("This is a warning")                    # gelb: Warnung
st.info("It's easy to build a Streamlit app")      # blau: Info-Hinweis
st.exception(RuntimeError("RuntimeError exception"))  # zeigt eine Exception formatiert an

st.divider(width="stretch")

rand = np.random.normal(1,2,size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins= 15)
st.pyplot(fig)

st.divider(width="stretch")

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)   # Liniendiagramm
 
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)    # Balkendiagramm
 
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)   # Flaechendiagramm
 
# --- Altair-Diagramm (interaktiv, anpassbar) ----------------
# Altair ist deklarativ: man beschreibt, welche Spalte auf welche
# "Encoding" (x, y, Groesse, Farbe, Tooltip) abgebildet wird.
df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
chart = alt.Chart(df).mark_circle().encode(
    x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(chart, use_container_width=True)  # nutzt die volle Breite

st.divider(width="stretch")


df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)


st.divider(width="stretch")

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
 