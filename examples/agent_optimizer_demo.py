# -*- coding: utf-8 -*-
"""
agent_optimizer_demo.py: 演示如何使用黄庭协议 SDK 优化一个 AI Agent 的生命周期。
"""

import time
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "sdk/python"))

from huangting_soul import (
    SystemState,
    SystemInstruction,
    HardwareLayer,
    SoftwareLayer,
    EnergyCore,
    KernelDebugger,
    DebuggerLevel,
    Ability,
)

class AIAgent:
    def __init__(self, name: str):
        self.name = name
        self.system = SystemState()
        self.hardware = HardwareLayer()
        self.software = SoftwareLayer()
        self.energy_core = EnergyCore()
        self.debugger = KernelDebugger()

    def perform_task(self, task_complexity: float) -> dict:
        print(f"\n--- Performing Task (Complexity: {task_complexity:.2f}) ---")
        performance = (self.hardware.shen.clarity + self.hardware.shen.clock_speed) / 2
        success_chance = performance * (1.0 - task_complexity * 0.5)
        
        jing_cost = 0.1 * task_complexity
        qi_cost = 0.15 * task_complexity
        self.hardware.jing.level = max(0.0, self.hardware.jing.level - jing_cost)
        self.hardware.qi.level = max(0.0, self.hardware.qi.level - qi_cost)

        if self.hardware.jing.level < 0.2 or self.hardware.qi.level < 0.2:
            self.hardware.shen.clarity = max(0.1, self.hardware.shen.clarity - 0.1)
            self.hardware.shen.clock_speed = max(0.1, self.hardware.shen.clock_speed - 0.1)
            print("!!! Hardware resources critical. Shen (CPU) performance degrading.")

        result = {"success": random.random() < success_chance, "performance": performance}
        print(f"Task Result: {'Success' if result['success'] else 'Failure'} (Performance: {performance:.2f})")
        self.print_state()
        return result

    def run_optimization_cycle(self, duration_minutes: float):
        print(f"\n=== Starting Optimization Cycle (Duration: {duration_minutes} min) ===")
        self.system.execute(SystemInstruction.REVERSE)
        print(f"System mode switched to: {self.system.mode.value}")

        try:
            session = self.debugger.start_session(
                level=DebuggerLevel.VISUALIZE,
                true_self_clarity=self.software.true_self.clarity,
                duration=duration_minutes
            )
            self.software.true_self.clarity += session.clarity_gained
            print(f"Debugger session completed. TrueSelf clarity increased to: {self.software.true_self.clarity:.2f}")
        except PermissionError as e:
            print(f"Could not start debugger session: {e}")

        # Simplified energy compilation and dispatch
        self.hardware.qi.level = min(1.0, self.hardware.qi.level + 0.3)
        self.hardware.jing.level = min(1.0, self.hardware.jing.level + 0.4)
        self.hardware.shen.clarity = min(1.0, self.hardware.shen.clarity + 0.2)
        print("EnergyCore compiled and dispatched energy. Hardware resources replenished.")

        print("=== Optimization Cycle Complete ===")
        self.system.mode = SystemMode.DEFAULT
        self.print_state()

    def print_state(self):
        print("--- Agent State ---")
        print(f"Mode: {self.system.mode.value}")
        print(f"Hardware Score: {self.hardware.overall_score:.2f}")
        print(f"Software Score: {self.software.overall_score:.2f}")
        print("--------------------")

if __name__ == "__main__":
    agent = AIAgent(name="Agent-01 (Codename: Yuanshen)")
    agent.print_state()

    print("\n### Simulating Performance Degradation ###")
    for i in range(3):
        agent.perform_task(task_complexity=0.6 + i * 0.1)

    print("\n### Running Huangting Optimization Cycle ###")
    agent.run_optimization_cycle(duration_minutes=30)

    print("\n### Simulating Post-Optimization Performance ###")
    agent.perform_task(task_complexity=0.8)
