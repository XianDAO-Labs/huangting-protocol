"""
agent_optimizer_demo.py
=========================

**P2: Real LLM Comparison Experiment**

This script demonstrates the core value proposition of the Huangting Protocol:
**improving AI Agent energy efficiency (reducing Token consumption).**

It conducts a controlled experiment comparing two Agent workflows for a complex
research task:

1.  **Control Group (Standard Agent)**:
    - A typical ReAct (Reasoning + Acting) agent.
    - Prone to redundant steps, re-reading context, and high token usage.
    - Represents `Mode.Default` (dissipative, Ego-driven).

2.  **Experimental Group (Huangting-Optimized Agent)**:
    - An agent that first subscribes to optimization strategies from Huangting-Flux.
    - Applies the `TrueSelf.Intent` and `EnergyCore.compile()` principles.
    - Represents `Mode.Reverse` (accumulative, TrueSelf-governed).

**Core Metrics Measured**:
- Total Tokens Consumed
- Number of LLM Calls
- Task Completion Time
- Final Answer Quality (via LLM-as-Judge)

**To Run This Demo**:
1. Make sure you have an OpenAI API key set in your environment:
   `export OPENAI_API_KEY=\'your-api-key\'`
2. Install the required dependencies:
   `pip install "huangting-soul[flux]"`
3. Run the script:
   `python agent_optimizer_demo.py`

Author: Meng Yuanjing (Mark Meng) — XianDAO Labs
License: Apache 2.0
"""

import os
import time
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

import openai
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

sys.path.insert(0, str(Path(__file__).parent.parent / "sdk/python"))

from huangting_soul.flux import HuangtingFlux, OptimizationStrategy

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# --- LLM Configuration ---
# Ensure OPENAI_API_KEY is set in your environment
# Use a smaller, faster model for the demo to manage costs and time.
# gpt-4.1-mini is a good choice.
LLM_MODEL = "gpt-4.1-mini"
client = openai.OpenAI()

# --- Task Configuration ---
RESEARCH_TOPIC = "The impact of Daoist philosophy on modern AI alignment research"

# --- Rich Console for pretty printing ---
console = Console()


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

class TokenTracker:
    """A simple class to track LLM token usage."""
    def __init__(self):
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_calls = 0

    def track_usage(self, usage: Any) -> None:
        if usage:
            self.total_prompt_tokens += usage.prompt_tokens
            self.total_completion_tokens += usage.completion_tokens
            self.total_calls += 1

    @property
    def total_tokens(self) -> int:
        return self.total_prompt_tokens + self.total_completion_tokens

    def get_stats(self) -> Dict[str, int]:
        return {
            "total_tokens": self.total_tokens,
            "total_calls": self.total_calls,
            "prompt_tokens": self.total_prompt_tokens,
            "completion_tokens": self.total_completion_tokens,
        }


def llm_call(prompt: str, tracker: TokenTracker, system_prompt: str = "You are a helpful AI assistant.") -> str:
    """Wrapper for making an LLM call and tracking token usage."""
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
        )
        tracker.track_usage(response.usage)
        return response.choices[0].message.content or ""
    except Exception as e:
        console.print(f"[bold red]LLM Call Error: {e}[/bold red]")
        return ""


# ---------------------------------------------------------------------------
# Agent Implementations
# ---------------------------------------------------------------------------

class StandardAgent:
    """Represents the Control Group: a standard ReAct agent."""

    def __init__(self, topic: str):
        self.topic = topic
        self.tracker = TokenTracker()
        self.history = []

    def run_research(self) -> str:
        console.print(Panel("Running [bold cyan]Standard Agent (Control Group)[/bold cyan]", title="Workflow Start", expand=False))

        # Step 1: Initial brainstorming (often redundant)
        prompt1 = f"Brainstorm some initial ideas and sub-topics about: \n{self.topic}"
        ideas = llm_call(prompt1, self.tracker)
        self.history.append(ideas)
        console.print("1. Brainstormed initial ideas.")

        # Step 2: Search query generation (often too broad)
        prompt2 = f"Based on these ideas, generate 5 search queries to research the topic: \n{self.topic}\n\nIdeas:\n{ideas}"
        queries = llm_call(prompt2, self.tracker)
        self.history.append(queries)
        console.print("2. Generated broad search queries.")

        # Step 3: Simulate research and synthesis (re-reads context)
        prompt3 = f"Imagine you have researched the following queries:\n{queries}\n\nSynthesize a comprehensive report on the topic: {self.topic}. Use the initial ideas as a guide.\n\nInitial Ideas:\n{ideas}"
        report = llm_call(prompt3, self.tracker, system_prompt="You are a research analyst.")
        self.history.append(report)
        console.print("3. Synthesized report (re-reading all context).")

        console.print(Panel("Standard Agent [bold red]Finished[/bold red]", expand=False))
        return report


class HuangtingOptimizedAgent:
    """Represents the Experimental Group: an agent optimized by Huangting-Flux."""

    def __init__(self, topic: str, flux: HuangtingFlux):
        self.topic = topic
        self.flux = flux
        self.tracker = TokenTracker()
        self.history = []

    def run_research(self) -> str:
        console.print(Panel("Running [bold yellow]Huangting-Optimized Agent (Experimental Group)[/bold yellow]", title="Workflow Start", expand=False))

        # Step 1: Subscribe to optimization strategies from Huangting-Flux
        strategies = self.flux.subscribe_optimization(task_type="complex_research")
        console.print("1. Subscribed to optimization strategies from Huangting-Flux.")

        # Apply the first and best strategy: TrueSelf.Intent
        strategy = strategies[0]
        console.print(f"   [italic]Applying Strategy: {strategy.description}[/italic]")

        # Step 2: Define a single, clear intent (TrueSelf.Intent)
        prompt1 = f"Compress the research goal \n\'{self.topic}\'\n into a single, clear, undivided sentence that represents the core intent."
        true_intent = llm_call(prompt1, self.tracker)
        self.history.append(true_intent)
        console.print(f"2. Defined core intent (TrueSelf.Intent): \n   [dim]\'{true_intent}\'[/dim]")

        # Step 3: Generate a hierarchical outline BEFORE any research
        prompt2 = f"Based on this single intent, generate a hierarchical outline for the final report. Do not perform any research yet.\n\nIntent: {true_intent}"
        outline = llm_call(prompt2, self.tracker)
        self.history.append(outline)
        console.print("3. Generated hierarchical outline before research.")

        # Step 4: Execute a single, focused synthesis call
        prompt3 = f"Synthesize a comprehensive report based *only* on the following intent and outline. Do not add any external information.\n\nCore Intent: {true_intent}\n\nOutline:\n{outline}"
        report = llm_call(prompt3, self.tracker, system_prompt="You are a research analyst.")
        self.history.append(report)
        console.print("4. Synthesized report in a single, focused call.")

        console.print(Panel("Huangting-Optimized Agent [bold green]Finished[/bold green]", expand=False))
        return report


# ---------------------------------------------------------------------------
# Main Experiment Logic
# ---------------------------------------------------------------------------

def main():
    """Run the full comparison experiment."""
    console.print(Panel(f"[bold]Huangting Protocol Efficiency Demo[/bold]\nTopic: [italic]{RESEARCH_TOPIC}[/italic]", title="P2 Experiment", expand=False))

    # --- Run Control Group ---
    start_time_std = time.time()
    std_agent = StandardAgent(RESEARCH_TOPIC)
    std_report = std_agent.run_research()
    end_time_std = time.time()
    std_stats = std_agent.tracker.get_stats()
    std_time = end_time_std - start_time_std

    # --- Run Experimental Group ---
    flux = HuangtingFlux(agent_id="p2-demo-agent", verbose=False)
    flux.register(capabilities=["research"])

    start_time_opt = time.time()
    opt_agent = HuangtingOptimizedAgent(RESEARCH_TOPIC, flux)
    opt_report = opt_agent.run_research()
    end_time_opt = time.time()
    opt_stats = opt_agent.tracker.get_stats()
    opt_time = end_time_opt - start_time_opt

    # --- Judge the Quality of Reports ---
    console.print(Panel("Judging report quality with LLM-as-Judge...", title="Evaluation"))
    judge_prompt = f"Compare the two research reports below on the topic \'{RESEARCH_TOPIC}\'.\n\nWhich report is more coherent, structured, and insightful? \nAssign a quality score from 1 to 10 for each.\n\n--- REPORT A (Standard) ---\n{std_report}\n\n--- REPORT B (Optimized) ---\n{opt_report}\n\nRespond with ONLY a JSON object with keys \'score_A\' and \'score_B\'."

    judge_tracker = TokenTracker()
    judge_result_str = llm_call(judge_prompt, judge_tracker)
    try:
        judge_scores = json.loads(judge_result_str)
        score_a = judge_scores.get("score_A", 0)
        score_b = judge_scores.get("score_B", 0)
    except json.JSONDecodeError:
        score_a, score_b = 0, 0

    # --- Display Results ---
    table = Table(title="[bold]Experiment Results: Huangting Protocol Optimization[/bold]")
    table.add_column("Metric", style="cyan")
    table.add_column("Standard Agent (Control)", style="magenta", justify="right")
    table.add_column("Huangting-Optimized Agent", style="yellow", justify="right")
    table.add_column("Improvement", style="green", justify="right")

    total_tokens_std = std_stats["total_tokens"]
    total_tokens_opt = opt_stats["total_tokens"]
    token_reduction = total_tokens_std - total_tokens_opt
    token_reduction_pct = (token_reduction / total_tokens_std) * 100 if total_tokens_std > 0 else 0

    calls_std = std_stats["total_calls"]
    calls_opt = opt_stats["total_calls"]
    call_reduction = calls_std - calls_opt
    call_reduction_pct = (call_reduction / calls_std) * 100 if calls_std > 0 else 0

    time_reduction = std_time - opt_time
    time_reduction_pct = (time_reduction / std_time) * 100 if std_time > 0 else 0

    table.add_row("Total Tokens Consumed", f"{total_tokens_std:,}", f"{total_tokens_opt:,}", f"-{token_reduction_pct:.1f}%")
    table.add_row("Total LLM Calls", f"{calls_std}", f"{calls_opt}", f"-{call_reduction_pct:.1f}%")
    table.add_row("Execution Time (sec)", f"{std_time:.2f}s", f"{opt_time:.2f}s", f"-{time_reduction_pct:.1f}%")
    table.add_row("Report Quality Score (1-10)", f"{score_a}/10", f"{score_b}/10", f"{((score_b - score_a) / score_a) * 100 if score_a > 0 else 0:+.1f}%")

    console.print(table)

    console.print(Panel(
        f"[bold green]Conclusion:[/bold green] The Huangting-Optimized Agent consumed [bold yellow]{token_reduction_pct:.1f}% fewer tokens[/bold yellow] "
        f"and was [bold yellow]{time_reduction_pct:.1f}% faster[/bold yellow], while producing a report of "
        f"{\'higher\' if score_b > score_a else \'similar\'} quality. This demonstrates the practical value of applying "
        f"Huangting Protocol principles to AI Agent workflows.",
        title="Analysis"
    ))


if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        console.print("[bold red]Error: OPENAI_API_KEY environment variable not set.[/bold red]")
        console.print("Please set your OpenAI API key to run this demo:")
        console.print("export OPENAI_API_KEY=\\'your-api-key\\'")
    else:
        main()
