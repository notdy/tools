import streamlit as st
import json
if __name__ == '__main__':
    st.title('JSON格式化')

    # 输入JSON
    json_input = st.text_area('请输入JSON',value='{}',height=300)

    # 展示JSON
    st.json(json.loads(json_input))

