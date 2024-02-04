from openai import OpenAI
import streamlit as st
import time
assistant_id = "asst_AQHCCarzrPldnAwojmkywt7u"


with st.sidebar:
    openai_api_key = st.secrets["api_key"]
    client = OpenAI(api_key=openai_api_key)
    thread_id = "thread_izO4OSbHw10ykea3YM6vAM0M"

    newbtn = st.button("(비행기)통관언어도우미")
    newbtn2 = st.button("교육 언어 도우미")
    newbtn3 = st.button("의료 언어")




st.title("💬 2024 통관언어 도우미")
# st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "통관언어를 입력해주세요 데이터를 기반으로 응답합니다. -BKS "}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
   
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    if not thread_id:
        st.info("생성된 대화 코드를 넣어주세요")
        st.stop()
   
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=prompt,
    )
    print(response)

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    print(run)
    run_id = run.id
    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        if run.status =="completed":
            break
        else:
            time.sleep(2)
        print(run)


    thread_messages = client.beta.threads.messages.list(thread_id)
    print(thread_messages.data)

    msg = thread_messages.data[0].content[0].text.value
    print(msg)
    
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

    # response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    # msg = response.choices[0].message.content
    # st.session_state.messages.append({"role": "assistant", "content": msg})
    # st.chat_message("assistant").write(msg)
