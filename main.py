import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="RFA Hourly Production",
                   page_icon=":bar_chart",
                   layout="wide")

filename = "hourly_production_lines.xlsx"

# dataframe
excel_file = pd.ExcelFile(filename)
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A,B,C,D')

df2 = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='F,G,H,I')

df3 = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='K,L,M,N')
def plot_gauge(
        indicator_number, indicator_color, indicator_suffix, indicator_title, max_bound
):
    fig = go.Figure(
        go.Indicator(
            value=indicator_number,
            mode="gauge+number",
            domain={"x": [0, 1], "y": [0, 1]},
            number={
                "suffix": indicator_suffix,
                "font.size": 26,
            },
            gauge={
                "axis": {"range": [0, max_bound], "tickwidth": 1},
                "bar": {"color": indicator_color},
            },
            title={
                "text": indicator_title,
                "font": {"size": 28},
            },
        )
    )
    fig.update_layout(
        # paper_bgcolor="lightgrey",
        height=200,
        margin=dict(l=10, r=10, t=50, b=10, pad=8),
    )
    st.plotly_chart(fig, use_container_width=True)

st.title("RFA Hourly Production")
col1, col2, col3 = st.columns(3)

with col1:
    col1.metric("RFA Line 1", "10", "%")
    plot_gauge(10, "#FF2B2B", "", "Line 1", 230)
    st.dataframe(df)

with col2:
    col2.metric("RFA Line 2", "115", "-12%")
    plot_gauge(115, "#FFE633", "", "Line 2", 230)
    st.dataframe(df2)

with col3:
    col3.metric("RFA Line 3", "215", "10%")
    plot_gauge(215, "#2F8E09", "", "Line 3", 230)
    st.dataframe(df3)

# col3, col4, col5 = st.columns(3)
#
# with col3:
#     st.dataframe(df)
#
# with col4:
#     st.dataframe(df2)
#
# with col5:
#     st.dataframe(df3)