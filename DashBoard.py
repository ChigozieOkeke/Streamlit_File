import streamlit as st
import pandas as pd
import plotly.express as px

st.title("SAMPLE PIVOT")
table=pd.read_csv("File_sample_pivot.csv")
st.text("Sample Pivot Analysis")
st.write(table)

bar_plot_fig=px.bar(table, x="Region",y="Units",title="Bar Plot")
st.plotly_chart(bar_plot_fig,use_container_width=True)

pie_plot_fig=px.pie(table, values="Sales",names="Region",title="Pie Plot Of the Distribution of Sales Regions")
st.plotly_chart(pie_plot_fig,use_container_width=True)

st.title("Tip Dataset")
table2=px.data.tips()
st.text("Tips Dataset")
button_label=st.button("Click to See The Dataset")
hide=st.checkbox("Hide/Show Dataset")
if not hide:
   st.write(table2)
#Create Sunburst
sun_fig=px.sunburst(table2,path=["day","time","sex","smoker"], values="tip",title="SurnBurst For The Day")
st.plotly_chart(sun_fig,use_container_width=True)