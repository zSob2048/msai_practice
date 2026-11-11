# from semantic_kernel.functions import kernel_function

# # class TaskManagementPlugin(KernelPlugin):
# #     @kernel_function(name="complete_task", description="Marks a task as completed by its ID.")
# #     def complete_task(self, id: int) -> dict | None:
# #         # ...complete the task logic...
# #         pass

# class MonteCarloSimulationPlugin:

#     @kernel_function(name="monte-carlo_simulation", description="Runs Monte Carlo simulations with monthly revenue and cost variables to estimate financial outcomes and assess risk.")
#     def complete_task(self, revenue: int, cost: int) -> dict | None:
#         import random


#         return
    
import random
# from semantic_kernel import Kernel
# from semantic_kernel.functions import kernel_function

# class FinanceSimulationSkill:
    
#     @kernel_function(
#         name="monte-carlo_simulation",
#         description="Runs Monte Carlo simulations with monthly revenue and cost variables to estimate financial outcomes and assess risk."
#     )
#     # def monte_carlo_simulation(self, revenue: float, cost: float, iterations: int = 1000) -> dict:
#     def monte_carlo_simulation(self, revenue: float, cost: float) -> dict:
#     """
#     월 매출과 원가를 기반으로 몬테카를로 시뮬레이션 수행.

#     Args:
#         revenue: 예상 월 매출
#         cost: 예상 원가

#     Returns:
#         dict: 평균 이익과 손실 발생 확률
#     """
#         results = []
#         for _ in range(10000):
#             simulated_revenue = revenue * (1 + random.uniform(-0.1, 0.1))
#             simulated_cost = cost * (1 + random.uniform(-0.1, 0.1))
#             profit = simulated_revenue - simulated_cost
#             results.append(profit)
        
#         avg_profit = sum(results) / 10000
#         loss_probability = sum(1 for r in results if r < 0) / 10000
        
#         return {
#             "average_profit": avg_profit,
#             "loss_probability": loss_probability
#         }

# # 커널에 플러그인 등록
# kernel = Kernel()
# kernel.import_skill(FinanceSimulationSkill(), skill_name="FinanceSimulation")




def monte_carlo_simulation(revenue: float, cost: float, goal: float = 0) -> dict:

    results = []
    for _ in range(10000):
        # 분포 수정 필요. 현재 코드는 정규분포를 사용중
        simulated_revenue =  (random.normalvariate(revenue, revenue*0.1))
        simulated_cost =  (random.normalvariate(cost, cost*0.1))

        # import numpy as np
        # import matplotlib.pyplot as plt

        # nums = [1, 2, 3, 4, 5, 6]
        # prob = [0.5, 0.1, 0.1, 0.1, 0.1, 0.1] # 지정확률
        # # prob = np.ones(6) * (1/6) # 동일확률
        # ## # >> 데이터에 따라 전체 동일확률??
        # ## # 데이터 불러와서>전체를 list에 > 동일확률로 len(nums) 사용 : 이건 루프 밖에 빼둔다... 동일확률이면 굳이 prob를 안해도??

        profit = simulated_revenue - simulated_cost
        results.append(profit)
    
    avg_profit = sum(results) / 10000
    loss_probability = sum(1 for r in results if r < 0) / 100
    goal_probability = sum(1 for r in results if r > goal) / 100
    
        # simulated_revenue = revenue * (1 + random.uniform(-0.1, 0.1)) # 균등분포 이건쓰지말어라

    return {
        "average_profit": avg_profit,
        "loss_probability(%)": loss_probability,
        "goal_probability(%)": goal_probability
    }


print(monte_carlo_simulation(700,650,100))

def calculate_salary(salary: float, hours: float = None) -> float:
    """
    급여를 고정급 또는 시급으로 입력받아 월 비용으로 변환.
    - hours가 None이면 고정급으로 처리
    - hours가 주어지면 시급 × 근무시간으로 계산
    """
    if hours is None:
        return salary
    else:
        return salary * hours

def investment_recovery(initial_investment: float, avg_profit: float) -> dict:
    """
    초기 투자비용 회수 가능성 평가.
    - 평균 순이익을 기반으로 몇 개월 내 회수 가능한지 추정
    """
    if avg_profit <= 0:
        return {"recoverable": False, "months": None}
    
    months = initial_investment / avg_profit
    return {"recoverable": True, "months": math.ceil(months)}

import random
import math
from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function

class FinanceSimulationSkill:
    
    @kernel_function(
        name="monte-carlo_simulation",
        description="Monte Carlo simulation with revenue, cost, salaries, rent, admin, and fees using normal distribution."
    )
    def monte_carlo_simulation(
        self,
        revenue: list,
        cost: float,
        salary: float,
        hours: float = None,
        rent: float = 0,
        admin: float = 0,
        fee: float = 0,
        tax_rate: float = 0.2
    ) -> dict:
        """
        월 매출, 원가, 급여(고정급/시급), 임대료, 관리비, 수수료를 고려한 몬테카를로 시뮬레이션.
        """
        iterations = 10000
        results = []
        
        salary_cost = calculate_salary(salary, hours)
        
        for _ in range(iterations):
            simulated_revenue = random.choice(revenue)
            simulated_cost = random.gauss(cost, cost * 0.1)
            
            gross_profit = simulated_revenue - simulated_cost - salary_cost - rent - admin - fee
            net_profit = gross_profit * (1 - tax_rate)
            
            results.append(net_profit)
        
        avg_profit = sum(results) / iterations
        loss_probability = sum(1 for r in results if r < 0) / iterations
        
        return {
            "average_net_profit": avg_profit,
            "loss_probability": loss_probability
        }


from semantic_kernel import Kernel

# 커널 생성
kernel = Kernel()

# 플러그인(skill) 등록
kernel.import_skill(FinanceSimulationSkill(), skill_name="FinanceSimulation")

# 플러그인 함수 호출
result = kernel.skills["FinanceSimulation"].monte_carlo_simulation(
    revenue=100000,   # 예상 월매출
    cost=40000,       # 원가
    salary=3000,      # 직원 급여 (고정급)
    hours=None,       # 시급 입력 시 근무시간 지정, 고정급이면 None
    rent=2000,        # 임대료
    admin=1000,       # 관리비
    fee=500,          # 수수료
    tax_rate=0.2      # 세율
)

print("평균 순이익:", result["average_net_profit"])
print("손실 확률:", result["loss_probability"])


### 확률을 조정 << numpy사용
# import numpy as np
# import matplotlib.pyplot as plt

# nums = [1, 2, 3, 4, 5, 6]
# prob = [0.5, 0.1, 0.1, 0.1, 0.1, 0.1] # 지정확률
# # prob = np.ones(6) * (1/6) # 동일확률
# ## # >> 데이터에 따라 전체 동일확률??

# res = np.random.choice(nums, 10000, p=prob)
# plt.hist(res, bins=np.arange(0.5, 7.5, 1), align='mid', rwidth=0.8)
# plt.show()

### 결과 요약 표
# import numpy as np
# import pandas as pd
# import seaborn as sns

# s0, mu, sigma, T = 58000, 0.1, 0.25, 0.5
# M = 10000
# res = []

# for i in range(M):
#     epsilon = np.random.randn()
#     sT = s0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * epsilon * np.sqrt(T)).round(2)
#     r = (sT - s0) / s0
#     res.append(r)

# df = pd.DataFrame({'수익률': res})

# stats = df.describe()
# stats

import asyncio
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

# 1. 커널 생성
kernel = Kernel()

# 2. Foundry(Azure OpenAI) LLM 연결
# Foundry 환경에서는 Azure OpenAI 리소스를 통해 모델을 호출합니다.
kernel.add_text_completion_service(
    "foundry-gpt",
    AzureChatCompletion(
        deployment_name="gpt-4",   # Foundry에 배포된 모델 이름
        endpoint="https://YOUR-FOUNDY-ENDPOINT.openai.azure.com/",
        api_key="YOUR_AZURE_API_KEY"
    )
)

# 3. 플러그인(skill) 등록
kernel.import_skill(FinanceSimulationSkill(), skill_name="FinanceSimulation")

# 4. LLM과 함께 호출
async def run():
    # LLM에게 시뮬레이션 실행 요청
    result = await kernel.skills["FinanceSimulation"].monte_carlo_simulation(
        revenue=150000,   # 예상 월매출
        cost=60000,       # 원가
        salary=25,        # 시급 입력
        hours=160,        # 월 근무시간
        rent=4000,        # 임대료
        admin=2000,       # 관리비
        fee=1000,         # 수수료
        tax_rate=0.25     # 세율
    )
    
    print("평균 순이익:", result["average_net_profit"])
    print("손실 확률:", result["loss_probability"])

asyncio.run(run())


"""
사용자가 다음과 같은 질문을 했습니다:
"3천만 원으로 카페 창업이 가능할까?"

이 질문을 기반으로 아래 변수들을 추정해 JSON으로 출력하세요:
- revenue: 예상 월매출 (숫자)
- cost: 예상 월 원가 (숫자)
- salary: 직원 급여 (숫자, 고정급 또는 시급)
- hours: 월 근무시간 (시급일 경우만)
- rent: 임대료
- admin: 관리비
- fee: 수수료
- tax_rate: 세율 (기본값 0.2)
- initial_investment: 초기 투자비용

출력은 JSON 형식으로만 하세요.

//

다음은 재무 시뮬레이션 결과입니다:
- Average net profit: 4825000
- Loss probability: 0.18
- Investment recovery: 7 months

이 결과를 바탕으로 사업 가능성을 설명하세요.
- 숫자는 원화 단위로 표현하세요.
- 위험 요인과 기회 요인을 함께 언급하세요.
- 경영자가 이해하기 쉽게 자연어로 작성하세요.


"""