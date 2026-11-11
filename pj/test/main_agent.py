import asyncio
import os
import json
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.functions.kernel_arguments import KernelArguments
from user_functions import FinanceSimulationSkill

async def main():
    # .env 로드
    load_dotenv()

    # Kernel 초기화
    kernel = Kernel()

    # Azure OpenAI 연결
    kernel.add_service(
        AzureChatCompletion(
            deployment_name="test_model_fin",   # 모델 이름
            base_url=os.getenv("BASE_URL"),
            api_key=os.getenv("OPENAI_API_KEY")
        )
    )

    # Plugin 등록 (FinanceSimulationSkill 클래스)
    kernel.add_plugin(FinanceSimulationSkill(), plugin_name="FinanceSimulationSkill")

    # JSON 워크플로우 로드
    skill_path = os.path.join(os.getenv("BASE_DIR"), "skills", "investment-simulation.json")
    with open(skill_path, "r", encoding="utf-8") as f:
        workflow = json.load(f)

    # 사용자 입력
    user_input = input(">>user   : ")

    # 1단계: input_to_json 프롬프트 실행
    input_stage = next(s for s in workflow["stages"] if s["id"] == "input_to_json")
    prompt = input_stage["prompt"].replace("{{user_input}}", user_input)

    result = await kernel.invoke_prompt(
        prompt=prompt,
        function_name="input_to_json",
        plugin_name="investment_simulation"
    )

    new_variables = result.value
    print(">> JSON 추출:", new_variables)

    # 2단계: Monte Carlo Simulation 실행
    sim_result = await kernel.invoke(
        function_name="monte_carlo_simulation",
        plugin_name="FinanceSimulationSkill",
        arguments=KernelArguments(**new_variables)
    )
    print(">> Simulation:", sim_result.value)

    # 3단계: 결과 설명
    explain_stage = next(s for s in workflow["stages"] if s["id"] == "explain_result")
    explain_prompt = explain_stage["prompt"] \
        .replace("{{simulation_result.average_net_profit}}", str(sim_result.value["average_net_profit"])) \
        .replace("{{simulation_result.loss_probability}}", str(sim_result.value["loss_probability"]))

    explanation = await kernel.invoke_prompt(
        prompt=explain_prompt,
        function_name="explain_result",
        plugin_name="investment_simulation"
    )

    print("\n>>agent  : ")
    print(explanation.value)

if __name__ == "__main__":
    asyncio.run(main())
