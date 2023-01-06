import streamlit as st 
import pandas as pd

st.markdown('# This is where I start')

with open('markdowns/text_1.md', 'r') as file:
        md1 = file.read()
                 
st.markdown(md1)

st.subheader('Examples from the "Main concepts" page')

'''
#### Something within three quotation marks is a markdown

This text is also written in markdown form, 
but this time the text is within three single quotes.
It seems that this is also rendered properly on the page

---

#### Showing simple tables

The system also appears to understand simple tables
'''

x = st.sidebar.slider('x', min_value=7, max_value=17,)
st.write(x)

df = pd.DataFrame(
        {"first":['a','b','c'],
         "second":[1,2,3],
         "third":[x, x/2, x/3]}
)

st.write(df)

'''
This is a simple Pandas dataframe that is
generated from a simple dictionary (or json object). 

Here I write it using the `st.write()` function that is
the swiss army knife. I could also have written it without
any wrapper. the st.write() does returns `None` 
so you can't use it in other segments.
'''

dfr = st.dataframe(df)

dfr.add_rows([['e', 4, x/4]])

'''
Here I put the dataframe into a `st.dataframe()` function 
and captured the output. Then I added a row to the
output
'''

