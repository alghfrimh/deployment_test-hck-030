# Import libraries
import streamlit as st
import eda, predict

# bagian dalam sidebar
with st.sidebar:
    st.write('# Page Navigation')

    # Toggle choose menu
    page = st.selectbox('Choose Page', ('EDA', 'Predict Rating'))

    # Test
    st.write('Halaman yang dituju', page)

    st.write(' ## About')
    
    st.markdown("""
<div style="text-align: justify;">
                
Hello football enthusiasm,
Page ini adalah analisis FIFA 2024.<br>
                
Are u ready to see ur potential player? Let's see!!
</div>
""", unsafe_allow_html=True)

# bagian luar sidebar
if page == 'EDA':
    eda.run()
else:
    predict.run()