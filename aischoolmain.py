import streamlit as st
import finance_naver
# import warnings

# 메인 화면
# st.subheader("플레타의 일상에 오신 것을 환영합니다.")
# 사이드바 화면
# warnings.filterwarnings('ignore')
st.sidebar.header("로그인")
st.sidebar.text_input("아이디 입력", value='streamlit', max_chars=15)
user_password = st.sidebar.text_input("패스워드 입력,", value="1234",type="password")

if user_password == '1234':
    st.sidebar.header("플레타의 포트폴리오")
    opt_data=['', '환율조회', '따릉이', '유성우']
    menu = st.sidebar.selectbox('메뉴 선택', opt_data, index=0)
    st.write('선택한 메뉴:', menu)

    if menu=='환율조회':
        st.subheader("환율조회>>>>>> ")
        finance_naver.exchange_main()

    elif menu=='따릉이':
        st.subheader("따릉이 데이터 분석 >>>>>>")
    elif menu=='유성우':
        st.subheader("유성우 데이터 분석 >>>>>>")
    else:
        st.subheader("환영합니다.")






