
import streamlit as st

# Streamlit 앱의 제목 설정
st.title('한국어 설명 페이지')

# 한국어 소개 섹션
st.header('한국어 소개')
st.write("""
한국어는 대한민국과 조선민주주의인민공화국의 공용어이며, 중앙아시아의 고려인들과 중국의 조선족들, 일본의 재일 한국인들 등 한민족 디아스포라들이 사용합니다.
한국어는 한글로 표기되며, 한글은 1443년에 세종대왕이 창제한 문자입니다.
""")

# 한글 자음과 모음 설명
st.header('한글 자음과 모음')
st.write("""
한글은 14개의 자음과 10개의 모음으로 구성되어 있습니다. 자음과 모음이 결합되어 하나의 음절을 형성합니다.
""")

st.subheader('자음')
st.markdown("""
ㄱ (기역), ㄴ (니은), ㄷ (디귿), ㄹ (리을), ㅁ (미음), ㅂ (비읍), ㅅ (시옷), ㅇ (이응), ㅈ (지읒), ㅊ (치읓), ㅋ (키읔), ㅌ (티읕), ㅍ (피읖), ㅎ (히읗)
""")

st.subheader('모음')
st.markdown("""
ㅏ (아), ㅑ (야), ㅓ (어), ㅕ (여), ㅗ (오), ㅛ (요), ㅜ (우), ㅠ (유), ㅡ (으), ㅣ (이)
""")

# 한국어 문법 설명 섹션
st.header('한국어 문법')
st.write("""
한국어 문법은 주어-목적어-동사(SOV) 순서를 따릅니다. 또한, 조사와 어미를 사용하여 문법적 관계를 나타냅니다.
""")

st.subheader('조사')
st.write("""
조사는 명사나 대명사 뒤에 붙어서 그 단어가 문장에서 어떤 역할을 하는지를 나타냅니다. 예를 들어, '은/는', '이/가', '을/를', '에', '에서' 등이 있습니다.
""")

st.subheader('동사 및 형용사 어미')
st.write("""
동사와 형용사는 어미가 변하여 시제, 높임, 의도 등을 나타냅니다. 예를 들어, '하다'는 현재형 '합니다', 과거형 '했습니다', 미래형 '할 것입니다' 등으로 변화합니다.
""")

# 예제 문장 제공
st.header('예제 문장')
st.write("""
아래는 한국어의 예제 문장들입니다:
""")

st.markdown("""
1. 저는 학생입니다. (I am a student.)
2. 그는 책을 읽습니다. (He reads a book.)
3. 우리는 학교에 갑니다. (We go to school.)
4. 그녀는 노래를 잘합니다. (She sings well.)
""")

# 한국어 학습 자료 섹션
st.header('한국어 학습 자료')
st.write("""
한국어를 더 배우고 싶다면 아래 자료들을 참고하세요:
""")

st.markdown("""
- [세종학당](https://www.sejonghakdang.org): 한국어와 한국 문화를 배우기 위한 온라인 학습 사이트
- [Talk To Me In Korean](https://www.talktomeinkorean.com): 다양한 한국어 학습 자료를 제공하는 웹사이트
- [How to Study Korean](https://www.howtostudykorean.com): 초급부터 고급까지 단계별 한국어 학습 자료 제공
""")

session.write('hello')