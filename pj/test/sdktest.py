import asyncio

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
# from semantic_kernel.connectors.ai.prompt_execution_settings import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions.kernel_arguments import KernelArguments

from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)

from semantic_kernel.prompt_template import PromptTemplateConfig

from user_functions import FinanceSimulationSkill




# Initialize the kernel
kernel = Kernel()

# Add Azure OpenAI chat completion
kernel.add_service(AzureChatCompletion(
    deployment_name="test_model_fin",
    api_key="YOUR_AZURE_API_KEY",
    base_url="https://fin-test.openai.azure.com/",
))

# kernel.get_service(
#     skill_directory="./test",   # YAML 파일이 들어 있는 디렉토리 경로
#     skill_name="prompt_flow"      # YAML 파일 이름 (예: prompt-flow.yaml)
# )

prompt_config = PromptTemplateConfig.from_yaml_file("./promptflow.yaml")

# 커널 함수 생성
chat_function = kernel.create_function_from_prompt(
    function_name="promptflow",
    plugin_name="prompt_flow",
    prompt_template_config=prompt_config
)

math_plugin = kernel.import_plugin(
    FinanceSimulationSkill(), 
    plugin_name="MathPlugin"
)

# 실행 함수
async def run_flow():
    result = await kernel.run_async(
        chat_function,
        input_vars={"question": "오늘 서울 날씨에 맞는 옷차림을 추천해줘."}
    )
    print(result)

asyncio.run(run_flow())