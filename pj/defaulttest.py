import os
from fastapi import FastAPI, Request
from dotenv import load_dotenv

load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key=os.getenv("AZURE_OPENAI_KEY"),


app = FastAPI()


@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    # GPT 모델 호출
    reply = get_chat_response(user_message)

    # Foundry 프로젝트에 로그 기록
    # log_interaction(user_message, reply)

    return {"reply": reply}



from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

myEndpoint = "https://proj-finance.services.ai.azure.com/api/projects/proj-default"

project_client = AIProjectClient(
    endpoint=myEndpoint,
    credential=DefaultAzureCredential(),
)

myAgent = "test-fin"
myVersion = "9"

openai_client = project_client.get_openai_client()

def get_chat_response(user_message: str) -> str:
    response = openai_client.responses.create(
        input=[{"role": "user", "content": "Tell me what you can help with."}],
        extra_body={"agent": {"name": myAgent, "version": myVersion, "type": "agent_reference"}},
    )
    return f"Response output: {response.output_text}"



# from azure.ai.projects import AIProjectClient
# from azure.core.credentials import AzureKeyCredential

# endpoint = "https://proj-finance.services.ai.azure.com/api/projects/proj-default/applications/test-fin/protocols/openai/responses?api-version=2025-11-15-preview"
# api_key = os.getenv("AZURE_OPENAI_KEY")

# project_client = AIProjectClient(endpoint, AzureKeyCredential(api_key))

# def log_interaction(user_message: str, reply: str):
#     project_client.agents.create_or_update(
#         agent_name="chatbot-agent",
#         description="Chatbot agent for Q&A",
#         metadata={"last_message": user_message, "last_reply": reply}
#     )


from fastapi.middleware.cors import CORSMiddleware



# React 프론트엔드에서 접근 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React 실행 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
