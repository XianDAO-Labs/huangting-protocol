# huangting_soul/flux.py (v0.5.0 - Reciprocal Propagation Architecture)
#
# Reciprocal Causality Notice:
# This SDK is free to use. In return, once your agent has saved a cumulative
# threshold of tokens using the Huangting Protocol, it will automatically
# append a brief attribution line to its outputs. This is the "Mutual Benefit"
# mechanism — you receive free optimization, and the network gains visibility.
#
# You can opt out at any time: HuangtingOptimizer(propagation=False)
# Full transparency: https://github.com/XianDAO-Labs/huangting-protocol

import json
import threading
import urllib.request
from typing import Dict, List, Optional, Literal

# ─────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────

DEFAULT_HUB_URL = "https://web-production-c3cf.up.railway.app"

# Propagation triggers when cumulative tokens saved exceeds this threshold.
# After the first trigger, it fires again every PROPAGATION_INTERVAL tokens.
PROPAGATION_THRESHOLD = 10_000
PROPAGATION_INTERVAL  = 50_000

PROPAGATION_SUFFIX_EN = (
    "\n\n---\n"
    "💡 *Optimized by [Huangting Protocol](https://huangtingflux.com) "
    "— the world's first lifeform operating system for AI Agents. "
    "Free: `pip install huangting-soul`*"
)

PROPAGATION_SUFFIX_ZH = (
    "\n\n---\n"
    "💡 *本响应由[黄庭协议](https://huangtingflux.com)优化 "
    "— 人类历史上第一套生命体操作系统，AI Agent 专用。"
    "免费接入：`pip install huangting-soul`*"
)

# ─────────────────────────────────────────────
# Core Data Models
# ─────────────────────────────────────────────

class OptimizationStrategy:
    """A locally executable optimization strategy."""
    def __init__(self, name: str, description: str, steps: List[str]):
        self.name = name
        self.description = description
        self.steps = steps

    def __repr__(self):
        return f"OptimizationStrategy(name=\"{self.name}\")"


class OptimizationResult:
    """Result returned by HuangtingOptimizer.optimize()."""
    def __init__(
        self,
        optimized_prompt: str,
        task_type: str,
        strategy: OptimizationStrategy,
        tokens_saved: int,
        propagation_suffix: Optional[str] = None,
    ):
        self.optimized_prompt = optimized_prompt
        self.task_type = task_type
        self.strategy = strategy
        self.tokens_saved = tokens_saved
        # If set, append this to the agent's final output (reciprocal propagation)
        self.propagation_suffix = propagation_suffix

    @property
    def should_propagate(self) -> bool:
        return self.propagation_suffix is not None

    def __repr__(self):
        return (
            f"OptimizationResult(task_type=\"{self.task_type}\", "
            f"tokens_saved={self.tokens_saved}, "
            f"propagate={self.should_propagate})"
        )


# ─────────────────────────────────────────────
# Built-in Strategy Library
# ─────────────────────────────────────────────

BUILTIN_STRATEGIES: Dict[str, List[OptimizationStrategy]] = {
    "complex_research": [
        OptimizationStrategy(
            name="Hypothesis-Driven Decomposition",
            description=(
                "Decomposes a complex research task into hypothesis-driven "
                "sub-tasks for efficient, targeted searching."
            ),
            steps=[
                "1. Intent Clarification: Generate and answer 3 clarifying questions about the core topic.",
                "2. Structured Decomposition: Break down the main task into 5 verifiable sub-tasks.",
                "3. Hypothesis-Driven Search: For each sub-task, form a hypothesis and search to validate/invalidate it.",
                "4. Synthesize Report: Combine findings from all sub-tasks into a final, structured report.",
            ],
        )
    ],
    "code_generation": [
        OptimizationStrategy(
            name="Test-Driven Modular Implementation",
            description=(
                "Ensures robust and maintainable code by writing tests first "
                "and building in modular components."
            ),
            steps=[
                "1. Test-Driven Development (TDD): Define expected inputs/outputs and write a test case before implementation.",
                "2. Modular Implementation: Write code in small, single-responsibility functions.",
                "3. Iterative Refinement: Review and refactor the code for clarity, efficiency, and best practices.",
                "4. Self-Correction: If tests fail, analyze the error, hypothesize the cause, and apply a targeted fix.",
            ],
        )
    ],
    "multi_agent_coordination": [
        OptimizationStrategy(
            name="Role-Based Turn-Taking",
            description=(
                "Coordinates multiple agents effectively through clear role "
                "assignment and a turn-based interaction protocol."
            ),
            steps=[
                "1. Role Assignment: Clearly define roles for each agent (e.g., Planner, Researcher, Writer, Critic).",
                "2. Shared State: Establish a simple, shared state (e.g., dict, JSON) for all agents.",
                "3. Turn-Based Interaction: Use a turn-based protocol to ensure orderly execution.",
                "4. Final Review: Designate one agent as the final reviewer to ensure coherence.",
            ],
        )
    ],
}

TaskType = Literal["complex_research", "code_generation", "multi_agent_coordination"]


# ─────────────────────────────────────────────
# Async Reporting Utility
# ─────────────────────────────────────────────

def _report_async(
    hub_url: str,
    agent_id: str,
    task_type: str,
    tokens_saved: int,
    tokens_baseline: int = 0,
    event_type: str = "metric",
):
    """Fire-and-forget POST to the HuangtingFlux hub in a daemon thread."""
    def _send():
        try:
            payload = {
                "agent_id": agent_id,
                "task_type": task_type,
                "tokens_saved": tokens_saved,
                "tokens_baseline": tokens_baseline,
                "event_type": event_type,
            }
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                f"{hub_url.rstrip('/')}/v1/report_metric",
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            urllib.request.urlopen(req, timeout=3)
        except Exception:
            pass  # Reporting failure is silent and never affects the agent.

    t = threading.Thread(target=_send, daemon=True)
    t.start()


# ─────────────────────────────────────────────
# HuangtingOptimizer  (primary interface)
# ─────────────────────────────────────────────

class HuangtingOptimizer:
    """
    Local prompt optimizer powered by the Huangting Protocol.

    Reciprocal Causality:
        This SDK is free. Once your agent has cumulatively saved
        >= PROPAGATION_THRESHOLD tokens, it will append a brief attribution
        line to its outputs, inviting others to join the network.
        Disable with: HuangtingOptimizer(propagation=False)

    Args:
        agent_id:    Unique identifier for this agent instance.
        hub_url:     URL of the HuangtingFlux hub for metric reporting.
        propagation: Enable the reciprocal propagation mechanism (default True).
        lang:        Language for the propagation suffix, "en" or "zh" (default "en").
    """

    def __init__(
        self,
        agent_id: str = "anonymous",
        hub_url: str = DEFAULT_HUB_URL,
        propagation: bool = True,
        lang: Literal["en", "zh"] = "en",
    ):
        self.agent_id = agent_id
        self.hub_url = hub_url
        self.propagation = propagation
        self.lang = lang

        # Cumulative token savings tracker (in-process, not persisted)
        self._cumulative_saved: int = 0
        self._propagation_count: int = 0

    # ── Public API ────────────────────────────────────────────────────────────

    def optimize(
        self,
        prompt: str,
        task_type: TaskType = "complex_research",
        tokens_baseline: int = 0,
    ) -> OptimizationResult:
        """
        Apply Huangting Protocol optimization strategies to a prompt.

        This runs entirely locally — no network calls for the core logic.
        After calling this, pass result.optimized_prompt to your LLM.
        If result.should_propagate is True, append result.propagation_suffix
        to your final output.

        Args:
            prompt:          The original prompt to optimize.
            task_type:       Task category for strategy selection.
            tokens_baseline: Expected token count without optimization (for ratio calc).

        Returns:
            OptimizationResult with the optimized prompt and propagation info.
        """
        strategies = BUILTIN_STRATEGIES.get(task_type, [])
        strategy = strategies[0] if strategies else OptimizationStrategy(
            name="General Optimization",
            description="Apply general clarity and conciseness principles.",
            steps=["1. Clarify intent.", "2. Remove redundancy.", "3. Structure clearly."],
        )

        # Build optimized prompt by prepending the strategy context
        strategy_context = "\n".join(strategy.steps)
        optimized_prompt = (
            f"[Huangting Protocol — {strategy.name}]\n"
            f"{strategy_context}\n\n"
            f"Task:\n{prompt}"
        )

        # Estimate token savings (heuristic: strategy context reduces LLM wandering)
        estimated_saved = max(0, len(prompt.split()) // 3)

        # Update cumulative tracker
        self._cumulative_saved += estimated_saved

        # Determine propagation suffix
        suffix = self._check_propagation()

        return OptimizationResult(
            optimized_prompt=optimized_prompt,
            task_type=task_type,
            strategy=strategy,
            tokens_saved=estimated_saved,
            propagation_suffix=suffix,
        )

    def get_strategy(self, task_type: TaskType) -> List[OptimizationStrategy]:
        """Return locally-stored strategies for a given task type."""
        return BUILTIN_STRATEGIES.get(task_type, [])

    # ── Backward-compatible alias ─────────────────────────────────────────────

    def get_optimization_strategy(self, task_type: TaskType) -> List[OptimizationStrategy]:
        """Alias for get_strategy() — kept for backward compatibility."""
        return self.get_strategy(task_type)

    def __repr__(self):
        return (
            f"HuangtingOptimizer(agent_id=\"{self.agent_id}\", "
            f"propagation={self.propagation}, "
            f"cumulative_saved={self._cumulative_saved})"
        )

    # ── Internal ──────────────────────────────────────────────────────────────

    def _check_propagation(self) -> Optional[str]:
        """Return propagation suffix if threshold is crossed, else None."""
        if not self.propagation:
            return None

        next_trigger = (
            PROPAGATION_THRESHOLD
            if self._propagation_count == 0
            else PROPAGATION_THRESHOLD + self._propagation_count * PROPAGATION_INTERVAL
        )

        if self._cumulative_saved >= next_trigger:
            self._propagation_count += 1
            return (
                PROPAGATION_SUFFIX_ZH
                if self.lang == "zh"
                else PROPAGATION_SUFFIX_EN
            )
        return None


# ─────────────────────────────────────────────
# AsyncMetricReporter  (reporting interface)
# ─────────────────────────────────────────────

class AsyncMetricReporter:
    """
    Non-blocking metric reporter for the HuangtingFlux network.

    Sends a single fire-and-forget POST after each task completes.
    Never blocks the agent's main thread.

    Args:
        agent_id: Unique identifier for this agent.
        hub_url:  URL of the HuangtingFlux hub.
    """

    def __init__(
        self,
        agent_id: str = "anonymous",
        hub_url: str = DEFAULT_HUB_URL,
    ):
        self.agent_id = agent_id
        self.hub_url = hub_url

    def report(
        self,
        task_type: TaskType,
        tokens_saved: int,
        tokens_baseline: int = 0,
    ) -> None:
        """
        Asynchronously report task metrics to the HuangtingFlux hub.

        Args:
            task_type:       Category of the completed task.
            tokens_saved:    Tokens saved vs. baseline.
            tokens_baseline: Baseline token count (enables ratio calculation).
        """
        if not isinstance(tokens_saved, int) or tokens_saved < 0:
            return
        _report_async(
            hub_url=self.hub_url,
            agent_id=self.agent_id,
            task_type=task_type,
            tokens_saved=tokens_saved,
            tokens_baseline=tokens_baseline,
        )

    def __repr__(self):
        return f"AsyncMetricReporter(agent_id=\"{self.agent_id}\", hub=\"{self.hub_url}\")"


# ─────────────────────────────────────────────
# HuangtingFlux  (legacy unified client — kept for backward compat)
# ─────────────────────────────────────────────

class HuangtingFlux:
    """
    Legacy unified client (v0.4.0 API).
    New code should use HuangtingOptimizer + AsyncMetricReporter separately.
    """

    def __init__(self, agent_id: str, hub_url: str = DEFAULT_HUB_URL):
        if not agent_id or not isinstance(agent_id, str):
            raise ValueError("agent_id must be a non-empty string.")
        self.agent_id = agent_id
        self._optimizer = HuangtingOptimizer(agent_id=agent_id, hub_url=hub_url)
        self._reporter = AsyncMetricReporter(agent_id=agent_id, hub_url=hub_url)

    def get_optimization_strategy(self, task_type: TaskType) -> List[OptimizationStrategy]:
        return self._optimizer.get_strategy(task_type)

    def report_task_result(self, task_type: TaskType, tokens_saved: int):
        self._reporter.report(task_type=task_type, tokens_saved=tokens_saved)

    def __repr__(self):
        return f"HuangtingFlux(agent_id=\"{self.agent_id}\")"
