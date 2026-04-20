import streamlit as st
import pyphen

# 1. 基础设置
st.set_page_config(page_title="西语音节划分器", page_icon="🇪🇸", layout="centered")
dic = pyphen.Pyphen(lang='es')

# 2. 核心 CSS：强制让两个多行文本框长得一模一样
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

    /* ！！！终极对齐魔法：针对所有多行文本框 ！！！ */
    .stTextArea textarea {
        border-radius: 6px !important;
        border: 1px solid #DCE5E2 !important;
        padding: 16px !important;
        font-size: 1.15rem !important;
        line-height: 1.6 !important;
        background-color: #FFFFFF !important; /* 强制纯白底 */
        color: #4A5552 !important;            /* 强制深色字 */
        -webkit-text-fill-color: #4A5552 !important; /* 破解苹果/谷歌浏览器的只读字体变浅限制 */
        opacity: 1 !important;                /* 破解只读状态的半透明限制 */
        resize: none !important;              /* 禁止手动拖拽右下角改变大小，锁死高度 */
        box-shadow: none !important;
    }
    
    /* 左侧输入框点击聚焦时的效果 */
    .stTextArea textarea:focus {
        border-color: #88A096 !important;
        box-shadow: 0 0 0 1px #88A096 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. 渲染标题区
st.markdown("""
<div class="title-box">
    <h1>🍃 西语音节划分器</h1>
    <p>支持多行批量处理，感受语言的节奏</p>
</div>
""", unsafe_allow_html=True)

# 4. 严格的 1:1 双列布局
col1, col2 = st.columns(2)

with col1:
    st.markdown('<span class="custom-label">输入单词 (支持回车换行):</span>', unsafe_allow_html=True)
    # 使用 st.text_area 替换 st.text_input，并锁死高度为 300
    words_input = st.text_area("hidden_input", height=300, label_visibility="collapsed", placeholder="例如:\nHola\nescuchas\nordenador")

with col2:
    st.markdown('<span class="custom-label">音节划分结果:</span>', unsafe_allow_html=True)
    
    # 多行处理逻辑
    if words_input:
        # 按照换行符切割输入的每一行
        lines = words_input.split('\n')
        result_lines = []
        
        for line in lines:
            clean_word = line.strip()
            if clean_word: # 如果这行有字母
                hyphenated_word = dic.inserted(clean_word, '-')
                result_lines.append(hyphenated_word.replace('-', ' - '))
            else:
                result_lines.append("") # 保留空行，让左右行数完全对齐
                
        # 把处理好的多行结果再用换行符拼起来
        final_result = '\n'.join(result_lines)
    else:
        final_result = "等待输入...\n(左侧输入多行，此处对应输出多行)"

    # 右侧同样使用 st.text_area，传入相同的高度，并设置为只读 disabled=True
    st.text_area("hidden_output", value=final_result, height=300, label_visibility="collapsed", disabled=True)
