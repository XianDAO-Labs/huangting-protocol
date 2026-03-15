# -*- coding: utf-8 -*-
"""
social_engineering_demo.py: 演示社会行为系统工程学（SBOS）的应用。
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "sdk/python"))

from huangting_soul import SBOS, PersonObjectModel, CoreLogic

# 1. 初始化 SBOS
sbos = SBOS()

# 2. 创建一个人物对象模型 (POM)
pom_ceo = PersonObjectModel(
    person_id="ceo_of_competitor_company",
    core_logic=CoreLogic.CONTROL,
    personality_type=["TYPE_A", "DOMINANT"],
    behavior_scripts={
        "on_challenge": {"action": "assert_authority", "probability": 0.8},
        "on_flattery": {"action": "lower_guard", "probability": 0.6},
    },
    risk_warnings=["High ego", "Prone to anger when questioned"],
    interaction_strategy="Find a way to make him feel in control while achieving our goals."
)

# 3. 将 POM 添加到 SBOS 数据库
sbos.add_person(pom_ceo)
print("--- 已创建并添加人物对象模型 (POM) ---")
print(f"人物ID: {pom_ceo.person_id}")
print(f"核心需求: {pom_ceo.core_logic.value}")

# 4. 根据 POM 获取交互策略
strategy = sbos.get_interaction_strategy("ceo_of_competitor_company")
print("\n--- 获取交互策略 ---")
print(f"对 {pom_ceo.person_id} 的交互策略: {strategy}")
