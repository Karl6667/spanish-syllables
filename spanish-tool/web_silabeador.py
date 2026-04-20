import streamlit as st
import pyphen

# 居中布局
st.set_page_config(page_title="西语音节划分器", page_icon="🇪🇸", layout="centered")

dic = pyphen.Pyphen(lang='es')

# CSS 核心修改：强制统一样式
st.markdown("""
<style>
    /* 全局背景色 */
    .stApp {
        background-color: #F8F9F7;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}

    .title-box {
        text-align: center;
        margin-bottom: 2rem;
        padding-top: 1rem;
    }
    .title-box h1 {
        color: #4A5552;
        font-size: 2rem;
        font-weight: 500;
        margin-bottom: 0.3rem;
    }
    .title-box p {
        color: #9CA8A3;
        font-size: 1rem;
        letter-spacing: 1px;
    }

    .custom-label {
        color: #7B8B88;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 8px;
        display: block;
    }

    /* ！！！核心修复：将输入框和输出框的标准完全统一 ！！！ */
    .stTextInput input, .output-box {
        border-radius: 6px;
        border: 1px solid #DCE5E2 !important; /* 统一实线边框 */
        padding: 12px 16px;
        font-size: 1.15rem;
        background-color: #FFFFFF !important; /* 统一纯白背景 */
        box-shadow: none !important;
        height: 52px; /* 强制统一高度，防止内容不同导致框体会忽高忽低 */
        box-sizing: border-box;
    }
    
    /* 左侧输入框专属属性 */
    .stTextInput input {
        color: #4A5552;
    }
    .stTextInput input:focus {
        border-color: #88A096 !important;
        box-shadow: 0 0 0 1px #88A096 !important;
    }

    /* 右侧输出框专属属性 */
    .output-box {
        color: #354F47;
        display: flex;
        align-items: center;
        font-weight: 500;
        letter-spacing: 1px;
    }

    /* 空状态时：框体还是那个白色的框，仅仅把字体颜色变浅，模拟等待输入的占位符感觉 */
    .output-box.empty {
        color: #C0CCC8;
        font-weight: normal;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
    <h1>🍃 西语音节划分器</h1>
    <p>输入西语单词，感受语言的节奏</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<span class="custom-label">输入单词:</span>', unsafe_allow_html=True)
    word = st.text_input("hidden", label_visibility="collapsed", placeholder="例如: escuchas")

with col2:
    st.markdown('<span class="custom-label">音节划分结果:</span>', unsafe_allow_html=True)
    
    if word:
        clean_word = word.strip()
        hyphenated_word = dic.inserted(clean_word, '-')
        result = hyphenated_word.replace('-', ' - ')
        
        st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
    else:
        # 移除了虚线和透明背景，现在它就是一个规规矩矩的白框
        st.markdown('<div class="output-box empty">等待输入...</div>', unsafe_allow_html=True)
