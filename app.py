import numpy as np
import pandas as pd
import streamlit as st

st.markdown("""
<style>
.stApp {
    background: #f9f7ff;
}
    .stButton>button {
    background-color: #5032a8;
    color: white;
    border-radius: 10px;
}
</style>""",unsafe_allow_html=True)
dataset = pd.read_csv('res.csv')

st.markdown("""
            <h1 style = "text-shadow: 1px -2px 3px white;
                        ">CartLens</h1>
            """,unsafe_allow_html=True)
st.markdown("""
            <h3 style = "text-shadow: 1px -2px 3px white;
                ">Product Affinity Recommendation Engine</h3>
            """,unsafe_allow_html=True)
st.divider()

tab1, tab2 = st.tabs(['Recommendations','Business Insights'])
with tab1:
    selected_item = st.selectbox('Select a product',['fromage blanc','light cream', 'pasta', 'whole wheat pasta', 'tomato sauce', 
                                                  'mushroom cream sauce', 'herb & pepper'])

    if st.button('Recommend'):
        index = dataset[dataset['Left Hand Side'] == selected_item].index
        items = []
        for i in index:
            items.append(dataset.iloc[i,2])

        st.markdown('#### You will also love...')
        cols = st.columns(len(items))
        for i, item in enumerate(items):
            with cols[i]:
                st.markdown(f"""
            <div style="
                border: 1px solid #e8e8e8;
                border-radius: 12px;
                padding: 16px;
                background: #fafafa;
                box-shadow: 0 4px 8px rgba(0,0,0,0.05);
                text-align: center;
            ">
                <h4 style="margin: 0; font-size: 18px;">{item.title()}</h4>
                <p style="margin: 8px 0 0; color: #555; font-size: 13px;">Recommended for you</p>
            </div>
        """, unsafe_allow_html=True)
      
with tab2:
    st.subheader('Business Insights')
    for i in range(0,8):
        st.markdown(f"""
            <div style="
                border: 1px solid #e8e8e8;
                border-radius: 12px;
                padding: 16px;
                background: #fafafa;
                box-shadow: 0 4px 8px rgba(0,0,0,0.05);
                text-align: center;
            ">
                <p style="margin: 8px 0 0; color: #555; font-size: 18px;">Customers who buy <b>{dataset.iloc[i,1]}</b> are <b>{(dataset.iloc[i,4]*100).round(2)}</b> % more likely to buy <b>{dataset.iloc[i,2]}</b></p>
            </div>
        """, unsafe_allow_html=True)
        
        
        
