import streamlit as st
import pyphen

# 1. 布局改回 "centered"（居中），这样整个界面会集中在屏幕中央，框就不会被无限拉长而显得“太大”
st.set_page_config(page_title="西语音节划分器", page_icon="🇪🇸", layout="centered")

dic = pyphen.Pyphen(lang='es')

# 2. 核心 CSS：强制让输出框和输入框长得一模一样，尺寸完全统一
st.markdown("""
<style>
    /* 全局背景色：柔和的暖米色 */
    .stApp {
        background-color: #F8F9F7;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* 隐藏杂乱的自带工具栏 */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* 顶部标题区，精简克制 */
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

    /* 统一的顶部文字标签样式 */
    .custom-label {
        color: #7B8B88;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 8px;
        display: block;
    }

    /* 左侧：Streamlit 自带输入框的深度美化 */
    .stTextInput input {
        border-radius: 6px;
        border: 1.5px solid #DCE5E2;
        padding: 12px 16px;
        font-size: 1.15rem;
        color: #4A5552;
        background-color: #FFFFFF;
        box-shadow: none; /* 去掉多余阴影 */
    }
    .stTextInput input:focus {
        border-color: #88A096; /* 聚焦时变成淡淡的鼠尾草绿 */
        box-shadow: 0 0 0 1px #88A096;
    }

    /* 右侧：自定义输出框（严格对齐输入框的尺寸和边距） */
    .output-box {
        border-radius: 6px;
        border: 1.5px solid #DCE5E2;
        padding: 12px 16px;
        font-size: 1.15rem;
        color: #354F47;
        background-color: #EAF0EE; /* 淡淡的绿底，以示区分 */
        min-height: 52px; /* 强制高度，与左侧输入框完美对齐 */
        display: flex;
        align-items: center;
        font-weight: 500;
        letter-spacing: 1px;
    }

    /* 右侧：没有输入单词时的虚线空状态 */
    .output-box.empty {
        background-color: transparent;
        border: 1.5px dashed #DCE5E2;
        color: #C0CCC8;
        font-weight: normal;
    }
</style>
""", unsafe_allow_html=True)

# 3. 渲染标题区
st.markdown("""
<div class="title-box">
    <h1>🍃 西语音节划分器</h1>
    <p>输入西语单词，感受语言的节奏</p>
</div>
""", unsafe_allow_html=True)

# 4. 严格的 1:1 双列布局
col1, col2 = st.columns(2)

with col1:
    # 左侧输入区域
    st.markdown('<span class="custom-label">输入单词:</span>', unsafe_allow_html=True)
    # label_visibility="collapsed" 会隐藏自带的标签，使用我们上面写的 custom-label，保证左右绝对对齐
    word = st.text_input("hidden", label_visibility="collapsed", placeholder="例如: escuchas")

with col2:
    # 右侧输出区域
    st.markdown('<span class="custom-label">音节划分结果:</span>', unsafe_allow_html=True)
    
    if word:
        clean_word = word.strip()
        hyphenated_word = dic.inserted(clean_word, '-')
        result = hyphenated_word.replace('-', ' - ')
        
        # 显示有结果时的标准框
        st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
    else:
        # 显示无结果时的占位框
        st.markdown('<div class="output-box empty">等待输入...</div>', unsafe_allow_html=True)
