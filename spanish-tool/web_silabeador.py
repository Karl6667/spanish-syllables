import streamlit as st
import pyphen

# 1. 基础设置
st.set_page_config(page_title="西语音节划分器", page_icon="🇪🇸", layout="centered")

# === 性能优化核心 ===
# 使用 Streamlit 的缓存装饰器。
# 这样音节字典只会加载一次并常驻内存，敲击键盘时不再重复读取，告别卡顿！
@st.cache_resource
def load_dictionary():
    return pyphen.Pyphen(lang='es')

dic = load_dictionary()

# 2. 核心 CSS
st.markdown("""
<style>
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

    /* 统一的文本框基础样式 */
    .stTextArea textarea {
        border-radius: 6px !important;
        border: 1px solid #DCE5E2 !important;
        padding: 16px !important;
        font-size: 1.15rem !important;
        line-height: 1.6 !important;
        background-color: #FFFFFF !important; 
        resize: none !important;              
        box-shadow: none !important;
    }
    
    /* === 光标修复核心 === */
    /* 1. 针对左侧的正常输入框 */
    .stTextArea textarea:not(:disabled) {
        color: #4A5552 !important;
        caret-color: #354F47 !important; /* 强制显示光标，并调成优雅的深绿色 */
    }

    /* 左侧输入框点击聚焦时的边缘变色效果 */
    .stTextArea textarea:focus {
        border-color: #88A096 !important;
        box-shadow: 0 0 0 1px #88A096 !important;
    }

    /* 2. 针对右侧的只读输出框 */
    .stTextArea textarea:disabled {
        color: #4A5552 !important;
        -webkit-text-fill-color: #4A5552 !important; /* 只在禁用的框里使用这个强制变色魔法 */
        opacity: 1 !important; 
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
    <h1>🍃 西语音节划分器</h1>
    <p>支持多行批量处理，感受语言的节奏</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<span class="custom-label">输入单词 (支持回车换行):</span>', unsafe_allow_html=True)
    words_input = st.text_area("hidden_input", height=300, label_visibility="collapsed", placeholder="例如:\nHola\nescuchas\nordenador")

with col2:
    st.markdown('<span class="custom-label">音节划分结果:</span>', unsafe_allow_html=True)
    
    if words_input:
        lines = words_input.split('\n')
        result_lines = []
        for line in lines:
            clean_word = line.strip()
            if clean_word:
                hyphenated_word = dic.inserted(clean_word, '-')
                result_lines.append(hyphenated_word.replace('-', ' - '))
            else:
                result_lines.append("") 
        final_result = '\n'.join(result_lines)
    else:
        final_result = "等待输入...\n(左侧输入多行，此处对应输出多行)"

    st.text_area("hidden_output", value=final_result, height=300, label_visibility="collapsed", disabled=True)
