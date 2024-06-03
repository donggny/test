import streamlit as st

# 국어 주관식 문제와 정답을 딕셔너리로 저장
questions = [
    {
        "question": "1. 훈민정음의(자음, 모음) 총개수는 몇 개인가요?",
        "answer": "28개"
    },
    {
        "question": "2. '청출어람'이라는 사자성어의 뜻은 무엇인가요?",
        "answer": "제자가 스승보다 낫다."
    },
    {
        "question": "3. '공든 탑이 무너지랴'라는 속담의 의미는 무엇인가요?",
        "answer": "힘을 다하고 정성을 다하여 한 일은 헛되지 않아 반드시 좋은 결과를 얻는다."
    }
]

# 세션 상태 초기화
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = [""] * len(questions)
if 'score' not in st.session_state:
    st.session_state.score = 0

def submit_answer(user_answer):
    """사용자가 입력한 답을 저장하고 다음 질문으로 이동"""
    question_idx = st.session_state.current_question
    st.session_state.answers[question_idx] = user_answer

    if user_answer.strip() == questions[question_idx]['answer']:
        st.session_state.score += 1

    if question_idx + 1 < len(questions):
        st.session_state.current_question += 1
    else:
        st.session_state.current_question = None  # 퀴즈 완료

def restart_quiz():
    """퀴즈를 재시작하기 위해 세션 상태 초기화"""
    st.session_state.current_question = 0
    st.session_state.answers = [""] * len(questions)
    st.session_state.score = 0

def show_question(question_idx):
    """현재 질문을 표시"""
    question = questions[question_idx]
    st.subheader(question["question"])

    user_answer = st.text_input("정답을 입력하세요:", value=st.session_state.answers[question_idx])

    if st.button("제출"):
        submit_answer(user_answer)

# 페이지 제목
st.title("국어 주관식 문제")

# 현재 질문을 표시하거나 결과를 표시
if st.session_state.current_question is not None:
    show_question(st.session_state.current_question)
else:
    st.subheader("퀴즈 완료!")
    st.write(f"총 점수: {st.session_state.score} / {len(questions)}")
    if st.button("다시 시작"):
        restart_quiz()
session.write('good')