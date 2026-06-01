import streamlit as st

st.title("⚡ 가장 쉬운 옴의 법칙 계산기")

# 1. 입력받기
v = st.number_input("전압(V) 입력", value=10.0)
r = st.number_input("저항(R) 입력", value=5.0)

# 2. 조건문 (저항이 0인 경우 방지)
if r == 0:
    st.error("저항은 0보다 커야 합니다!")
else:
    # 옴의 법칙 계산 (I = V / R)
    i = v / r
    st.success(f"현재 전류는 {i} A 입니다.")

    # [리스트]와 [조건문]으로 현재 상태 진단하기
    warn_list = []
    if i > 5.0:
        warn_list.append("⚠️ 전류가 너무 높아요! 과열 주의!")
    else:
        warn_list.append("✅ 안전한 전류 범위입니다.")
        
    # [반복문]으로 리스트 내용 출력하기
    for message in warn_list:
        st.write(message)

    st.divider()

    # 3. [반복문]과 [리스트]로 저항이 커질 때 전류 변화 미리보기
    st.write("🔄 저항이 2배, 3배, 4배가 되면 전류는 어떻게 될까?")
    
    r_list = [r*2, r*3, r*4] # 저항 리스트 생성
    
    for test_r in r_list:   # 반복문으로 하나씩 계산
        test_i = v / test_r
        st.write(f"저항이 {test_r} Ω이 되면 ➡️ 전류는 {test_i:.2f} A")