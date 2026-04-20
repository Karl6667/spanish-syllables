import streamlit as st
import pyphen

# 1. 基础设置：页面标题和 wide 布局（宽布局，以便放两列）
st.set_page_config(page_title="西语音节划分器 🇪🇸", page_icon="🍃", layout="wide") 

# 2. 初始化音节处理库
dic = pyphen.Pyphen(lang='es')

# 3. 自定义 CSS，用于精美和功能性的翻译界面
# 暖米色背景，石板灰和鼠尾草绿的配色，精致小巧的卡片
st.markdown("""
<style>
    /* 全局背景色：柔和暖米色 */
    .stApp {
        background-color: #F8F9F7;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* 顶部标题区域 */
    .title-area {
        text-align: center;
        padding-top: 20px;
        padding-bottom: 30px;
        margin-bottom: 30px;
        border-bottom: 1px solid #EAECEA;
    }
    .title-main {
        color: #5C6B73;
        font-family: 'Georgia', serif; /* 更经典的西语感 */
        font-size: 2.8rem;
        font-weight: 500;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .title-sub {
        color: #9CA8A3;
        font-size: 1.1rem;
        margin-top: 10px;
        letter-spacing: 1px;
    }

    /* 输入输出标签样式 */
    .stTextInput label, .stMarkdown label {
        color: #7B8B88;
        font-size: 1.1rem !important;
        font-weight: 500;
        padding-bottom: 5px;
    }

    /* 输入框样式：去掉阴影，更专业、紧凑 */
    .stTextInput input {
        border-radius: 8px;
        border: 1px solid #D0D7D4;
        padding: 12px 18px;
        font-size: 1.15rem;
        color: #4A5552;
        background-color: #FFFFFF;
    }

    /* 结果容器（左边和右边都要用到） */
    .result-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding: 20px;
    }

    /* 右侧结果卡片样式：鼠尾草绿，精致小巧 */
    .result-card {
        background-color: #EAF0EE;
        padding: 25px 20px;
        border-radius: 12px;
        border: 1px solid #DCE5E2;
        box-shadow: 0 4px 10px rgba(0,0,0,0.02);
        width: 100%; /* 填满列 */
        transition: all 0.3s ease;
    }

    /* 结果文字：深绿色，大小适中，不再是超大字体 */
    .result-text {
        font-size: 1.6rem;
        color: #354F47;
        font-weight: 600;
        letter-spacing: 2px;
        line-height: 1.2; /* 紧凑一点 */
    }

    /* 空白占位卡片样式：精美虚线 */
    .empty-card {
        background-color: transparent;
        border: 1px dashed #DCE5E2;
        box-shadow: none;
    }
    .empty-text {
        font-size: 1.3rem;
        color: #C0CCC8;
        letter-spacing: 1px;
    }

    /* 隐藏顶部工具栏，专注界面 */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# 4. 界面布局：顶部标题和标语
st.markdown("""
<div class="title-area">
    <div class="title-main">🍃 西语音节划分器</div>
    <div class="title-sub">专注当下，感受语言的节奏</div>
</div>
""", unsafe_allow_html=True)

# 5. 左右双列布局，模拟 Google 翻译界面
left_col, right_col = st.columns([1, 1])

with left_col:
    # --- 左侧输入区域 ---
    st.markdown('<div class="result-container">', unsafe_allow_html=True)
    # 输入标签和框，我们将标签包含在 markup 中，以便更好地控制样式
    st.markdown('<label>输入单词:</label>', unsafe_allow_html=True)
    word = st.text_input("", placeholder="请输入西语单词，例如: escuchas", key="word_input")
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    # --- 右侧输出区域 ---
    st.markdown('<div class="result-container">', unsafe_allow_html=True)
    st.markdown('<label>音节划分结果:</label>', unsafe_allow_html=True)

    if word:
        clean_word = word.strip()
        hyphenated_word = dic.inserted(clean_word, '-')
        
        # 将分割号换回最初要求的短横线带空格 ' - '
        # 例如将 'es-cu-chas' 替换为 'es - cu - chas'
        result = hyphenated_word.replace('-', ' - ')
        
        # 渲染有结果时的精致结果卡片
        st.markdown(f'''
            <div class="result-card">
                <div class="result-text">{result}</div>
            </div>
        ''', unsafe_allow_html=True)
    else:
        # 渲染没有输入时的精美空白虚线卡片
        st.markdown('''
            <div class="result-card empty-card">
                <div class="empty-text">等待输入...</div>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
