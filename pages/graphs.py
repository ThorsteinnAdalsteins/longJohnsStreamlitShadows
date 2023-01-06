
import streamlit as st 
import pandas as pd
import numpy as np

'''
## Playing with graphs

Combining some widgets and a graph
'''

x = st.slider('Choose how many lines', min_value=2, max_value=20)


left_column, right_column = st.columns([1,3])

chart_data = pd.DataFrame(
     np.random.randn(x, 3),
     columns=['First set', 'Second set', 'Third set'])

# find list columns and allow me to check if they are shown
boxes = []
with left_column:    
    for i in chart_data.columns:
            checked = st.checkbox(i, key=i)
            if checked:
                    boxes.append(i)
    
    st.markdown('---')
    
    show_frame = st.checkbox('Show dataframe')


right_column.line_chart(chart_data[boxes])


with right_column:
    if show_frame:
        st.dataframe(chart_data.style.highlight_max(axis=0)) 


'''
The data is always randomized
'''