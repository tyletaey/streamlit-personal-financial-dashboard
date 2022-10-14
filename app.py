import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image

# Page setting
st.set_page_config(
    # layout = 'wide',
    page_title = 'Personal Finalcial Dashboard',
    page_icon = '✅'
)

# Data
df = pd.read_csv('https://raw.githubusercontent.com/tyletaey/data/main/my_finance.csv')

# Dashboard title
# st.title("Personal Finalcial Dashboard")

# st.sidebar
sidebar_main = st.sidebar.selectbox('Navigation', ['Home','Dashboard', 'Explore'])
st.sidebar.success("Select a menu above.")

################# Home

if sidebar_main == 'Home' : 
    st.write('# Personal Financial Dashboard💰')
    st.markdown("""
        ### 
        **👈 Select a navigation from the sidebar** to see the dashboard !
        """)
    # image = Image.open('kelly-sikkema-unsplash.jpg')
    # st.image(image)
    st.markdown('''
    ---
    Created by tyletaey [Github](https://github.com/tyletaey/).
    ''')

#################### Dashboard

elif sidebar_main == 'Dashboard':
    st.title('Summary Dashboard💸')
    
    # Row a
    a1, a2 = st.columns(2)
    with a1:
        st.markdown('##### Total expense by month')
        month_amount = df.groupby("month").Amount.sum()
        st.line_chart(month_amount)

    with a2:
        st.markdown('##### Total expense by year')
        total_year = df.groupby("year").Amount.sum()
        st.bar_chart(total_year)

    # Row b
    b1, b2 = st.columns((6,4))
    with b1:
        st.markdown('##### Total expense by category')
        fig = px.pie(df, 
        names='Category')
        st.plotly_chart(fig)


    with b2:
        st.markdown('##### Top 10 expense by category')
        top10_cate = df[["Category", "Amount"]].groupby("Category", as_index=False)\
            .sum().sort_values(by = "Amount", ascending = False).head(10)
        st.bar_chart(data=top10_cate, x='Category', y='Amount')


elif sidebar_main == 'Explore' : 
    st.title('Explore data📊')
    sidebar_sub = st.sidebar.selectbox('Navigation', ['Expense', 'Category'])

## Side bar sub

    if sidebar_sub == 'Expense' : 
        st.markdown(
            """
            ##### Check the expenses by year
            """
        )
        
        year_col = df['year'].unique()
        select_year = st.selectbox('Select year',
                        year_col) # Will change to multiselect next time

        st.subheader('You select {}'.format(select_year))
        # st.line_chart(df.year, x = total_year, y = select_year)

        if select_year == 2018:
            sum_2018 = df[df['year'] == 2018].groupby('month').Amount.sum()
            st.line_chart(sum_2018)
            st.write(sum_2018)
        
        if select_year == 2019:
            sum_2019 = df[df['year'] == 2019].groupby('month').Amount.sum()
            st.line_chart(sum_2019)
            st.write(sum_2019)
            
        if select_year == 2020:
            sum_2020 = df[df['year'] == 2020].groupby('month').Amount.sum()
            st.line_chart(sum_2020)
            st.write(sum_2020)

        if select_year == 2021:
            sum_2021 = df[df['year'] == 2021].groupby('month').Amount.sum()
            st.line_chart(sum_2021)
            st.write(sum_2021)

        if select_year == 2022:
            st.error("Please select 2018 - 2021")

    if sidebar_sub == 'Category' : 
        st.markdown(
            """
            ##### Check the expenses by category🥧
            """
        )

        year_col = df['year'].unique()
        select_year = st.selectbox('Select year',
                        year_col)
        
        if select_year == 2018:
            cate_2018 = df[df['year'] == 2018].groupby('Category').Amount.sum()
            st.bar_chart(cate_2018)
            st.write(cate_2018)
        
        if select_year == 2019:
            cate_2019 = df[df['year'] == 2019].groupby('Category').Amount.sum()
            st.bar_chart(cate_2019)
            st.write(cate_2019)
        
        if select_year == 2020:
            cate_2020 = df[df['year'] == 2020].groupby('Category').Amount.sum()
            st.bar_chart(cate_2020)
            st.write(cate_2020)
        
        if select_year == 2021:
            cate_2021 = df[df['year'] == 2021].groupby('Category').Amount.sum()
            st.bar_chart(cate_2021)
            st.write(cate_2021)
        
        if select_year == 2022:
            st.error("Please select 2018 - 2021")


