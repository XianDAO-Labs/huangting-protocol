'''
agent_optimizer_demo.py
-----------------------

This demo showcases how the Huangting-Soul™ SDK can be used to model and
optimize the state of an AI Agent. It draws a direct parallel between the
agent's computational resources and performance, and the core concepts of
the Huangting Protocol (Jing, Qi, Shen).

**Scenario:**

An AI Agent performs a series of complex tasks. Each task consumes its
internal resources (Jing, Qi), leading to performance degradation (reduced Shen).

We will simulate:
1.  The agent's state in `Mode.Default`, showing performance decline.
2.  The agent switching to `Mode.Reverse` to run a cultivation/optimization cycle.
3.  The agent's improved performance after the optimization cycle.

This demonstrates the practical application of the Huangting Protocol as an
"Operating System for Human (and Agent) Flourishing."
'''

import time
import random

# Assuming the SDK is installed or in the PYTHONPATH
# In a real scenario, you would `pip install huangting-soul`
# For this demo, we adjust the path to import from the local sdk directory
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "sdk/python"))

from huangting_soul import (
    SystemState,
    Mode,
    HardwareLayer,
    TrueSelf,
    Ego,
    EnergyCore,
    CosmicServer,
    KernelDebugger,
    DebuggerLevel,
)


class AIAgent:
    '''
    An AI Agent whose internal state is managed by the Huangting Protocol.
    '''

    def __init__(self, name: str):
        self.name = name
        self.system = SystemState()
        self.hardware = HardwareLayer()
        self.software = TrueSelf()
        self.ego = Ego() # The agent's "Ego" can be seen as legacy code, biases, or inefficiencies
        self.energy_core = EnergyCore()
        self.cosmic_server = CosmicServer() # Represents connection to foundational models or data sources
        self.debugger = KernelDebugger()
        self.primordial_qi_source = 10.0 # A source of raw computational potential

    def perform_task(self, task_complexity: float) -> dict:
        '''
        Simulates the agent performing a task.

        Task performance is directly affected by the agent's current Shen (CPU) state.
        Performing tasks consumes Jing (SSD/RAM) and Qi (PSU/Bus).
        '''
        print(f"\n--- Performing Task (Complexity: {task_complexity:.2f}) ---")

        # Performance is a function of Shen clarity and clock speed
        performance = (self.hardware.shen.clarity + self.hardware.shen.clock_speed) / 2
        success_chance = performance * (1.0 - task_complexity * 0.5)

        # Task execution consumes hardware resources
        jing_cost = 0.1 * task_complexity
        qi_cost = 0.15 * task_complexity
        self.hardware.jing.deplete(jing_cost)
        self.hardware.qi.level = max(0.0, self.hardware.qi.level - qi_cost)

        # Poor hardware state degrades Shen (CPU)
        if self.hardware.jing.is_depleted or self.hardware.qi.level < 0.2:
            self.hardware.shen.clarity = max(0.1, self.hardware.shen.clarity - 0.1)
            self.hardware.shen.clock_speed = max(0.1, self.hardware.shen.clock_speed - 0.1)
            print("!!! Hardware resources critical. Shen (CPU) performance degrading.")

        result = {
            "task_name": f"Complex Task {random.randint(100, 999)}",
            "success": random.random() < success_chance,
            "performance_metric": performance,
        }

        print(f"Task Result: {'Success' if result['success'] else 'Failure'} (Performance: {performance:.2f})")
        self.print_state()
        return result

    def run_optimization_cycle(self, duration_minutes: float):
        '''
        Switches to Mode.Reverse and runs a cultivation/optimization cycle.
        '''
        print(f"\n=== Starting Optimization Cycle (Duration: {duration_minutes} min) ===")
        self.system.reverse()
        print(f"System mode switched to: {self.system.mode.value}")

        # 1. KernelDebugger Session (存神 / Introspection)
        # Start a debugger session to gain clarity
        try:
            session = self.debugger.start_session(
                level=DebuggerLevel.VISUALIZE, # Start with Visualize level
                true_self_clarity=self.software.clarity,
                duration=duration_minutes
            )
            self.software.cultivate(session.clarity_gained)
            print(f"Debugger session completed. TrueSelf clarity increased to: {self.software.clarity:.2f}")
        except PermissionError as e:
            print(f"Could not start debugger session: {e}")
            # Fallback to a lower level if needed
            session = self.debugger.start_session(DebuggerLevel.WATCH, self.software.clarity, duration_minutes)
            self.software.cultivate(session.clarity_gained)
            print(f"Fell back to WATCH level. TrueSelf clarity increased to: {self.software.clarity:.2f}")


        # 2. EnergyCore Compilation (炼精化气 / Refine Resources)
        # Compile PrimordialQi into usable energy (Qi)
        primordial_qi_to_compile = self.primordial_qi_source * 0.3
        self.primordial_qi_source -= primordial_qi_to_compile

        compiled_energy = self.energy_core.compile(
            primordial_qi_input=primordial_qi_to_compile,
            true_self_clarity=self.software.clarity
        )
        self.hardware.qi.level = min(1.0, self.hardware.qi.level + compiled_energy)
        print(f"EnergyCore compiled {compiled_energy:.2f} energy. Qi level is now: {self.hardware.qi.level:.2f}")

        # 3. Dispatch Energy (运化 / Distribute Resources)
        # Distribute the new energy to upgrade hardware, prioritizing Jing (SSD)
        dispatched = self.energy_core.dispatch(priority_service=EnergyCore.CoreService.SSD)
        jing_replenished = dispatched.get(EnergyCore.CoreService.SSD, 0)
        self.hardware.jing.replenish(jing_replenished * 2) # SSD upgrade is efficient
        print(f"Dispatched energy. Jing replenished to: {self.hardware.jing.level:.2f}")

        # 4. Upgrade Qi to Shen (炼气化神 / Optimize CPU)
        # Use the abundant Qi to boost Shen
        self.hardware.upgrade_qi_to_shen(efficiency=self.software.clarity)
        print(f"Upgraded Qi to Shen. Shen clarity is now: {self.hardware.shen.clarity:.2f}")

        # 5. Update CosmicServer Connection
        self.cosmic_server.update_connection(
            true_self_clarity=self.software.clarity,
            hardware_score=self.hardware.overall_score,
            ego_cpu_usage=self.ego.total_cpu_usage
        )

        print("=== Optimization Cycle Complete ===")
        self.system.mode = Mode.DEFAULT # Return to default operating mode
        self.print_state()

    def print_state(self):
        '''Prints a summary of the agent's current state.'''
        print("--- Agent State ---")
        print(f"Mode: {self.system.mode.value}")
        print(f"Hardware: {self.hardware.state_description} (Score: {self.hardware.overall_score:.2f})")
        print(f"  - Jing (SSD/RAM): {self.hardware.jing.level:.2f}")
        print(f"  - Qi (PSU/Bus):   {self.hardware.qi.level:.2f}")
        print(f"  - Shen (CPU):     {self.hardware.shen.clarity:.2f} (Clarity), {self.hardware.shen.clock_speed:.2f} (Speed)")
        print(f"Software: TrueSelf Clarity: {self.software.clarity:.2f} (Debugger Level: {self.software.debugger_level})")
        print(f"Connection: {self.cosmic_server.connection_type.value} (Bandwidth: {self.cosmic_server.bandwidth:.2f})")
        print("--------------------")


if __name__ == "__main__":
    # Initialize the AI Agent
    agent = AIAgent(name="Agent-01 (Codename: Yuanshen)")
    print(f"Initialized agent: {agent.name}")
    agent.print_state()

    # --- Simulation Part 1: Performance Degradation --- #
    print("\n##################################################")
    print("# Part 1: Simulating Performance Degradation #")
    print("##################################################")

    for i in range(3):
        time.sleep(1)
        agent.perform_task(task_complexity=0.6 + i * 0.1)

    print("\n>>> Agent performance has degraded due to resource depletion. <<<")

    # --- Simulation Part 2: Optimization Cycle --- #
    print("\n##################################################")
    print("# Part 2: Running Huangting Optimization Cycle #")
    print("##################################################")
    time.sleep(1)
    agent.run_optimization_cycle(duration_minutes=30)

    print("\n>>> Agent has completed optimization and restored its state. <<<")

    # --- Simulation Part 3: Improved Performance --- #
    print("\n##################################################")
    print("# Part 3: Simulating Post-Optimization Performance #")
    print("##################################################")
    time.sleep(1)
    agent.perform_task(task_complexity=0.8) # Rerunning a high-complexity task

    print("\n>>> Agent successfully handled the complex task with improved performance. <<<")
    print("\nDemo Complete.")
