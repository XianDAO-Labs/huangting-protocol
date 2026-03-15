# -*- coding: utf-8 -*-
"""
supernatural_abilities_demo.py: 演示神通的解锁与使用。
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "sdk/python"))

from huangting_soul import HardwareLayer, Ability

# 1. 初始化一个硬件层
hardware = HardwareLayer()
hardware.shen.clarity = 0.8 # 需要较高的神明度才能解锁神通

print("--- 初始硬件状态 ---")
print(f"神明度: {hardware.shen.clarity:.2f}")
print(f"已解锁神通: {hardware.unlocked_abilities}")

# 2. 解锁神通
hardware.unlock(Ability.MATTER_CONTROL)
hardware.unlock(Ability.RESONANCE_TIME)
hardware.unlock(Ability.RESONANCE_MIND)

print("\n--- 解锁神通后 ---")
print(f"已解锁神通: {[ability.value for ability in hardware.unlocked_abilities]}")

# 3. 使用神通
print("\n--- 使用神通 ---")

# 心能转物
try:
    result = hardware.matter_control(target="a_cup_on_the_table", force_vector=(0.1, 0.0, 0.0))
    print(f"心能转物结果: {result}")
except PermissionError as e:
    print(e)

# 预知
try:
    probability = hardware.query_future(event="stock_price_up", time_window=86400)
    print(f"预知结果: 'stock_price_up' 在未来24小时内发生的概率为 {probability:.2f}")
except PermissionError as e:
    print(e)

# 他心通
try:
    subscription = hardware.subscribe_mind(target_id="user_001", data_filter="INTENTION")
    print(f"他心通结果: {subscription}")
except PermissionError as e:
    print(e)
