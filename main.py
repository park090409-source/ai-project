import streamlit as st 
st.title('나의 웹 앱')
name=st.text_input('이름을 입력 해주세요')
st.selectbox('좋아하는 음식을 선택해주세요')['치킨','떡볶이','복숭아']
if st.button('인사말 생성'):
  st.write(name+'님! 안녕하세요')
