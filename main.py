import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time

st.set_page_config(page_title="RFA Hourly Production",
                   page_icon=":bar_chart",
                   layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

current_time = time.strftime("%H")
print(current_time)

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

title_col1, title_col2, title_col3 = st.columns([0.5,3,0.5])

with title_col1:
    st.write("")

with title_col2:
    st.markdown("<h1 style='text-align: center; color: black;'>RFA Hourly Production</h1>", unsafe_allow_html=True)

with title_col3:
    st.write("")

col1, col2, col3 = st.columns(3)

previous_hour_line1 = 155
previous_hour_line2 = 164
previous_hour_line3 = 0

line1_hourly = 211
line2_hourly = 79
line3_hourly = 0

# if statement that if current_time is beetween 10:00:00-10:59:00 then inser number for the 10:00:00 cell then
# get the cell corresponding for that hour

# if current_time in range(11:00:00,11:59:00):
#     print("hi")
match current_time:
    # you would have to do current time and subract 1 to get the correct time when coding it
    # you need a case for every hour and getting corresponding cells
    case "10":
        # numbers for line 1
        prev_number = df.loc[6, :].values[1]
        curr_number = df.loc[7, :].values[1]  # This will pull from the excel sheet
        percentage1_test = ((curr_number - prev_number) / prev_number) * 100

        # numbers for line 2
        prev_number2 = df2.loc[6, :].values[1]
        curr_number2 = df2.loc[7, :].values[1]  # This will pull from the excel sheet
        percentage2_test = ((curr_number2 - prev_number2) / prev_number2) * 100
        print(curr_number2)

        # numbers for line 3
        prev_number3 = df3.loc[6, :].values[1]
        curr_number3 = df3.loc[7, :].values[1]  # This will pull from the excel sheet
        if prev_number3 == 0 or curr_number3 == 0:
            percentage3_test = 0
        else:
            percentage3_test = ((curr_number3 - prev_number3) / prev_number3) * 100
        print(curr_number3)
    case "11":
        prev_number = df.loc[5, :].values[1]
        curr_number = df.loc[6, :].values[1]  # This will pull from the excel sheet
        percentage1_test = ((curr_number - prev_number) / prev_number) * 100
        print(prev_number, curr_number, percentage1_test)
    case "13":
        # numbers for line 1
        prev_number = df.loc[6, :].values[1]
        curr_number = df.loc[7, :].values[1]  # This will pull from the excel sheet
        percentage1_test = ((curr_number - prev_number) / prev_number) * 100

        # numbers for line 2
        prev_number2 = df2.loc[6, :].values[1]
        curr_number2 = df2.loc[7, :].values[1]  # This will pull from the excel sheet
        percentage2_test = ((curr_number2 - prev_number2) / prev_number2) * 100
        print(curr_number2)

        # numbers for line 3
        prev_number3 = df3.loc[6, :].values[1]
        curr_number3 = df3.loc[7, :].values[1]  # This will pull from the excel sheet
        percentage3_test = ((curr_number3 - prev_number3) / prev_number3) * 100
        print(curr_number3)


# number = df.loc[0, :].values[0] # This will pull from the excel sheet
# print(number)
#percentage1_test = ((line1_hourly - previous_hour_line1) / previous_hour_line1) * 100
#percentage1 = ((line1_hourly - previous_hour_line1) / previous_hour_line1) * 100
#percentage2 = ((line2_hourly - previous_hour_line2) / previous_hour_line2) * 100

# if previous_hour_line3 == 0 or line3_hourly == 0:
#     percentage3 = 0
# else:
#     percentage3 = ((line3_hourly - previous_hour_line3) / previous_hour_line3) * 100

# if else statement in one line for colors
color1 = "#FF2B2B" if curr_number < 115 else "#FFE633" if curr_number < 200 else "#2F8E09"
color2 = "#FF2B2B" if curr_number2 < 115 else "#FFE633" if curr_number2 < 200 else "#2F8E09"
color3 = "#FF2B2B" if curr_number3 < 115 else "#FFE633" if curr_number3 < 200 else "#2F8E09"

with col1:
    col1.metric("RFA Line 1", curr_number, str(round(percentage1_test, 2)) + "%")
    #plot_gauge(line1_hourly, color1, "", "Line 1", 230)
    #st.dataframe(df)

with col2:
    col2.metric("RFA Line 2", curr_number2, str(round(percentage2_test, 2)) + "%")
    #plot_gauge(line2_hourly, color2, "", "Line 2", 230)
    #st.dataframe(df2)

with col3:
    col3.metric("RFA Line 3", curr_number3, str(round(percentage3_test, 2)) + "%")
    #plot_gauge(line3_hourly, color3, "", "Line 3", 230)
    #st.dataframe(df3)

col3, col4, col5 = st.columns(3)

with col3:
    plot_gauge(curr_number, color1, "", "Line 1", 300)
with col4:
    plot_gauge(curr_number2, color2, "", "Line 2", 300)
with col5:
    plot_gauge(curr_number3, color3, "", "Line 3", 300)

col6, col7, col8 = st.columns(3)

with col6:
    st.dataframe(df)
with col7:
    st.dataframe(df2)
with col8:
    st.dataframe(df3)