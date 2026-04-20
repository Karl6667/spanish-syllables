import streamlit as st
import pyphen

# 1. 基础设置：页面标题和布局
st.set_page_config(page_title="西语音节划分", page_icon="🍃", layout="centered")

# 2. 注入“精装修” CSS 样式
# 这里使用柔和的色调、圆角设计，并隐藏了 Streamlit 默认的杂乱菜单
st.markdown("""
<style>
    /* 隐藏右上角默认菜单和底部水印，实现极简视效 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 设置整体背景为温暖、平静的米灰色 */
    .stApp {
        background-color: #F7F7F5; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* 标题样式：低饱和度的石板灰，看着不刺眼 */
    h1 {
        color: #5C6B73; 
        text-align: center;
        font-weight: 500;
        margin-bottom: 0px;
    }

    /* 副标题/寄语样式 */
    .subtitle {
        text-align: center; 
        color: #9CA8A3; 
        font-size: 1.1rem;
        margin-bottom: 40px;
        letter-spacing: 2px;
    }

    /* 输入框上方的提示文字 */
    .stTextInput label {
        color: #7B8B88;
        font-size: 1.1rem !important;
        font-weight: 500;
        padding-bottom: 10px;
    }

    /* 输入框本身的样式：圆角、淡淡的阴影、去掉粗糙的边框 */
    .stTextInput input {
        border-radius: 12px;
        border: 1px solid #E1E6E4;
        padding: 15px 20px;
        font-size: 1.2rem;
        background-color: #FFFFFF;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        color: #4A5552;
    }

    /* 输出结果的卡片样式：鼠尾草绿，像一张质感很好的字卡 */
    .result-card {
        background-color: #EAF0EE; 
        padding: 40px 20px;
        border-radius: 16px;
        text-align: center;
        margin-top: 10px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.03);
        border: 1px solid #DCE5E2;
        transition: all 0.3s ease;
    }

    /* 结果文字：深绿色，加大字号，拉开间距 */
    .result-text {
        font-size: 2.2rem;
        color: #354F47; 
        font-weight: 600;
        letter-spacing: 3px;
    }

    /* 空白状态下的占位框样式 */
    .empty-card {
        background-color: transparent; 
        border: 2px dashed #DCE5E2; 
        box-shadow: none;
    }
</style>
""", unsafe_allow_html=True)

# 3. 核心逻辑与界面渲染
dic = pyphen.Pyphen(lang='es')

# 渲染标题和副标题
st.markdown("<h1>🍃 西语音节划分器</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>专注当下，感受语言的节奏</div>", unsafe_allow_html=True)

# 为了让界面居中且不要太宽，我们用 columns 限制一下输入框的宽度
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    # 接收输入
    word = st.text_input("输入单词:", placeholder="请输入西语单词，例如: escuchas")

    if word:
        clean_word = word.strip()
        hyphenated_word = dic.inserted(clean_word, '-')

        # UI 细节：用优雅的中间点 ' · ' 替代原本机械的破折号 '-'
        result = hyphenated_word.replace('-', '  ·  ')

        # 渲染有结果时的精美卡片
        st.markdown(f'''
            <div class="result-card">
                <div class="result-text">{result}</div>
            </div>
        ''', unsafe_allow_html=True)
    else:
        # 渲染没有输入时的虚线占位卡片
        st.markdown('''
            <div class="result-card empty-card">
                <div class="result-text" style="color: #C0CCC8; font-size: 1.5rem; letter-spacing: 0px;">等待输入...</div>
            </div>
        ''', unsafe_allow_html=True)