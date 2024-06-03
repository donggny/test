import streamlit as st

# 국어 문제와 선택지를 딕셔너리로 저장
questions = [
    {
        "question": "1. 다음 중 올바른 맞춤법을 고르시오.",
        "options": ["갔다오다", "갔다 오다", "갔다 오았다", "갔다 오았다"],
        "answer": "갔다 오다"
    },
    {
        "question": "2. '사과하다'의 반대말은?",
        "options": ["사과를 먹다", "사과하지 않다", "칭찬하다", "비난하다"],
        "answer": "비난하다"
    },
    {
        "question": "3. 다음 중 속담의 의미가 '작은 것을 아끼려다 큰 손해를 본다'와 가장 가까운 것은?",
        "options": ["배보다 배꼽이 크다", "소 잃고 외양간 고친다", "낫 놓고 기역 자도 모른다", "등잔 밑이 어둡다"],
        "answer": "배보다 배꼽이 크다"
    },
    {
        "question": "4. 다음 중 '희망'의 의미와 가장 가까운 단어는?",
        "options": ["기대", "절망", "공포", "슬픔"],
        "answer": "기대"
    },
    {
        "question": "5. '고진감래'라는 사자성어의 뜻은?",
        "options": ["즐거움 뒤에 슬픔이 온다", "힘든 일이 끝나면 즐거움이 온다", "빠른 행동이 좋다", "느린 행동이 좋다"],
        "answer": "힘든 일이 끝나면 즐거움이 온다"
    }
]

# 세션 상태 초기화
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = [None] * len(questions)
if 'score' not in st.session_state:
    st.session_state.score = 0

def submit_answer(selected_option):
    """사용자가 선택한 답을 저장하고 다음 질문으로 이동"""
    question_idx = st.session_state.current_question
    st.session_state.answers[question_idx] = selected_option

    if selected_option == questions[question_idx]['answer']:
        st.session_state.score += 1

    if question_idx + 1 < len(questions):
        st.session_state.current_question += 1
    else:
        st.session_state.current_question = None  # 퀴즈 완료

def restart_quiz():
    """퀴즈를 재시작하기 위해 세션 상태 초기화"""
    st.session_state.current_question = 0
    st.session_state.answers = [None] * len(questions)
    st.session_state.score = 0

def show_question(question_idx):
    """현재 질문과 선택지를 표시"""
    question = questions[question_idx]
    st.subheader(question["question"])
    options = question["options"]

    selected_option = st.radio(
        "정답을 선택하세요:",
        options,
        index=options.index(st.session_state.answers[question_idx]) if st.session_state.answers[question_idx] else 0
    )

    if st.button("제출"):
        submit_answer(selected_option)

# 페이지 제목
st.title("국어 객관식 문제")

# 현재 질문을 표시하거나 결과를 표시
if st.session_state.current_question is not None:
    show_question(st.session_state.current_question)
else:
    st.subheader("퀴즈 완료!")
    st.write(f"총 점수: {st.session_state.score} / {len(questions)}")
    if st.button("다시 시작"):
        restart_quiz()
