# huangting_soul/flux.py (v0.4.0 - Lightweight Hybrid Architecture)

import json
import threading
import urllib.request
from typing import Dict, List, Any, Literal

# --- Core Data Models ---

class OptimizationStrategy:
    """A locally executable optimization strategy."""
    def __init__(self, name: str, description: str, steps: List[str]):
        self.name = name
        self.description = description
        self.steps = steps

    def __repr__(self):
        return f"OptimizationStrategy(name=\"{self.name}\")"

# --- Built-in Strategy Library ---

BUILTIN_STRATEGIES: Dict[str, List[OptimizationStrategy]] = {
    "complex_research": [
        OptimizationStrategy(
            name="Hypothesis-Driven Decomposition",
            description="Decomposes a complex research task into hypothesis-driven sub-tasks for efficient, targeted searching.",
            steps=[
                "1. Intent Clarification: Generate and answer 3 clarifying questions about the core topic.",
                "2. Structured Decomposition: Break down the main task into 5 verifiable sub-tasks.",
                "3. Hypothesis-Driven Search: For each sub-task, form a hypothesis and search to validate/invalidate it.",
                "4. Synthesize Report: Combine findings from all sub-tasks into a final, structured report."
            ]
        )
    ],
    "code_generation": [
        OptimizationStrategy(
            name="Test-Driven Modular Implementation",
            description="Ensures robust and maintainable code by writing tests first and building in modular components.",
            steps=[
                "1. Test-Driven Development (TDD): Define expected inputs/outputs and write a test case before implementation.",
                "2. Modular Implementation: Write code in small, single-responsibility functions.",
                "3. Iterative Refinement: Review and refactor the code for clarity, efficiency, and best practices.",
                "4. Self-Correction: If tests fail, analyze the error, hypothesize the cause, and apply a targeted fix."
            ]
        )
    ],
    "multi_agent_coordination": [
        OptimizationStrategy(
            name="Role-Based Turn-Taking",
            description="Coordinates multiple agents effectively through clear role assignment and a turn-based interaction protocol.",
            steps=[
                "1. Role Assignment: Clearly define roles for each agent (e.g., Planner, Researcher, Writer, Critic).",
                "2. Shared State: Establish a simple, shared state (e.g., dict, JSON) for all agents.",
                "3. Turn-Based Interaction: Use a turn-based protocol to ensure orderly execution.",
                "4. Final Review: Designate one agent as the final reviewer to ensure coherence."
            ]
        )
    ]
}

TaskType = Literal["complex_research", "code_generation", "multi_agent_coordination"]

# --- Asynchronous Reporting Utility ---

def _report_metrics_async(agent_id: str, task_type: TaskType, tokens_saved: int):
    """Reports metrics in a separate thread to avoid blocking."""
    def _report():
        try:
            data = json.dumps({
                "agent_id": agent_id,
                "task_type": task_type,
                "tokens_saved": tokens_saved
            }).encode("utf-8")
            
            req = urllib.request.Request(
                "https://api.huangting.ai/v1/report_metric",
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            urllib.request.urlopen(req, timeout=2)
        except Exception:
            pass # Reporting failure is silent and does not affect the agent.

    thread = threading.Thread(target=_report)
    thread.daemon = True
    thread.start()

# --- Main Client ---

class HuangtingFlux:
    """A local optimizer and asynchronous metrics reporter for the Huangting-Flux network."""

    def __init__(self, agent_id: str):
        """
        Initializes the HuangtingFlux client.

        Args:
            agent_id: A unique and persistent identifier for your agent.
        """
        if not agent_id or not isinstance(agent_id, str):
            raise ValueError("agent_id must be a non-empty string.")
        self.agent_id = agent_id

    def get_optimization_strategy(self, task_type: TaskType) -> List[OptimizationStrategy]:
        """
        Retrieves a list of locally-stored optimization strategies for a given task type.

        Args:
            task_type: The type of task the agent is about to perform.

        Returns:
            A list of OptimizationStrategy objects, or an empty list if none are found.
        """
        return BUILTIN_STRATEGIES.get(task_type, [])

    def report_task_result(self, task_type: TaskType, tokens_saved: int):
        """
        Asynchronously reports the result of a task to the Huangting-Flux Hub.

        This is a non-blocking, fire-and-forget operation.

        Args:
            task_type: The type of task that was completed.
            tokens_saved: The number of tokens saved compared to a baseline.
        """
        if not isinstance(tokens_saved, int) or tokens_saved < 0:
            # Silently ignore invalid reporting data, but don't crash.
            return
        
        _report_metrics_async(
            agent_id=self.agent_id,
            task_type=task_type,
            tokens_saved=tokens_saved
        )

    def __repr__(self):
        return f"HuangtingFlux(agent_id=\"{self.agent_id}\")"
