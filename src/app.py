import streamlit as st
import requests
import json

page = st.sidebar.selectbox('Choose your page', ['registration', 'list'])

if page == 'registration':
    st.title('User登録画面')
    with st.form(key='registration'):
        name_content: str = st.text_input('名前入力', max_chars=20)
        age_content: int = st.number_input('年齢入力',0,100,0)
        hometown_content: str = st.text_input('出身地入力', max_chars=10)

        print(name_content)
        # print(name_content.apparent_encoding)

        data = {
                "name": name_content,
                "age": age_content,
                "hometown": hometown_content
        }
        print(json.dumps(data,ensure_ascii=False))
    
        submit_button = st.form_submit_button(label='User登録')

        if submit_button:
            url = 'https://2ov1sz.deta.dev/users/'
            res = requests.post(
                url,
                data=json.dumps(data,ensure_ascii=False).encode('utf-8').decode('unicode-escape')
            )
            if res.status_code == 200:
                st.success('User登録完了')
            print(res.json())
            st.json(res.json())

elif page == 'list':
    st.title('User一覧画面')
    res = requests.get('https://2ov1sz.deta.dev/users/')
    records = res.json()
    print(records)
    for record in records:
        st.subheader(record)