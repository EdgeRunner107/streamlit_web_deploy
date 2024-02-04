from openai import OpenAI
client = OpenAI(api_key="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")

file = "file/2024wordsforcustom.pdf"

def file_upload(file):
    file = client.files.create(
    file=open(file, "rb"),
    purpose="assistants"
    )

    #print(file)
    return file.id

#file_id = file_upload(file)



def assistant_creator():
    my_assistant = client.beta.assistants.create(
        instructions="당신은 유능한 통관용어 비서입니다 제공한 파일에 접근 할 권한이 있으며 대답은 무조건 한국어로 사용합니다. 파일에는 2024년 한국에서 사용하는 통관용어가 줄바꿈을 기준으로 정리되어있으며 앞에나오는 단어 와 설명하는내용을 포함하고있습니다 예를 들어 사용자가 단어를 입력하면 그뒤에 내용이 설명하는 내용입니다. 당신은 답변할때 무조건 제공한 파일을 기준으로 설명해야합니다. ",
        name="custom word bot",
        tools=[{"type": "retrieval"}],
        model="gpt-4-1106-preview",
        file_ids=["file-dCyqxwg7aafKgekljYasLYsU"],
    )
    print(my_assistant)
    return my_assistant.id


#my_assistant_id = assistant_creator()


empty_thread = client.beta.threads.create()
print(empty_thread)