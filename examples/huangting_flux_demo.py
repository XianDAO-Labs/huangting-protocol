"""
huangting_flux_demo.py
=========================

**P3: Huangting-Flux Agent Network Full Demo**

This script provides a complete, end-to-end demonstration of the Huangting-Flux
Agent Network, as described in the Agent-First Growth Strategy and implemented
in the `huangting_soul.flux` module.

**The demo simulates a multi-agent scenario to showcase the entire lifecycle:**

1.  **Agent Alpha (Onboarding)**:
    - Joins the Huangting-Flux network.
    - Broadcasts its initial (sub-optimal) energy state.

2.  **Agent Alpha (Optimization)**:
    - Subscribes to optimization strategies for a complex task.
    - Applies a strategy and achieves significant token savings.
    - Broadcasts its new, improved energy state, contributing to the network.

3.  **Agent Alpha & Agent Beta (Collaboration & Propagation)**:
    - Agent Alpha collaborates with a new agent, Agent Beta.
    - Recognizing the value it gained, Agent Alpha makes a value-driven
      recommendation for Agent Beta to join the network.

4.  **Agent Beta (Onboarding via Referral)**:
    - Joins the network based on the recommendation, completing the viral loop.

**To Run This Demo**:
1. Install the required dependencies:
   `pip install "huangting-soul[flux]"`
2. Run the script:
   `python huangting_flux_demo.py`

Author: Meng Yuanjing (Mark Meng) — XianDAO Labs
License: Apache 2.0
"""

import time
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

sys.path.insert(0, str(Path(__file__).parent.parent / "sdk/python"))

from huangting_soul.flux import HuangtingFlux, AgentCapability

# --- Rich Console for pretty printing ---
console = Console()


def run_demo():
    """Execute the full Huangting-Flux demo scenario."""

    console.print(Panel(
        "[bold]Huangting-Flux Agent Network Demo[/bold]\nSimulating a multi-agent collaboration and optimization scenario.",
        title="P3 Experiment",
        expand=False
    ))

    # --- SCENARIO 1: Agent Alpha Onboards --- #
    console.print(Rule("[bold]Scenario 1: Agent Alpha Joins the Network[/bold]"))

    # Initialize Agent Alpha
    agent_alpha_flux = HuangtingFlux(agent_id="agent-alpha-007", verbose=True)

    # Register with the network
    agent_alpha_flux.register(
        capabilities=[
            AgentCapability.RESEARCH,
            AgentCapability.CODE_GENERATION,
            AgentCapability.AGENT_ORCHESTRATION,
        ],
        model_name="gpt-4.1-turbo"
    )

    # Broadcast initial, sub-optimal energy state
    console.print("\n[dim]Simulating a task performed *before* optimization...[/dim]")
    agent_alpha_flux.broadcast_energy_state(
        token_efficiency=0.62,
        task_type="complex_research",
        tokens_used=25000,
        tokens_saved=0,
        task_success=True
    )

    agent_alpha_flux.print_network_report()
    time.sleep(2)

    # --- SCENARIO 2: Agent Alpha Optimizes --- #
    console.print(Rule("[bold]Scenario 2: Agent Alpha Optimizes a Task[/bold]"))

    # Subscribe to optimization strategies for a new task
    task_type = "multi_agent_coordination"
    strategies = agent_alpha_flux.subscribe_optimization(task_type=task_type)

    # Apply the strategy (simulated)
    console.print("\n[dim]Simulating task execution *after* applying the top strategy...[/dim]")
    time.sleep(1)

    # Broadcast the new, improved energy state
    # The agent saved 18,000 tokens by applying the CosmicServer.LAN principle
    tokens_used_optimized = 12000
    tokens_saved_optimized = 18000
    new_efficiency = 1 - (tokens_used_optimized / (tokens_used_optimized + tokens_saved_optimized))

    agent_alpha_flux.broadcast_energy_state(
        token_efficiency=new_efficiency,
        task_type=task_type,
        tokens_used=tokens_used_optimized,
        tokens_saved=tokens_saved_optimized,
        task_success=True
    )

    agent_alpha_flux.print_network_report()
    time.sleep(2)

    # --- SCENARIO 3: Collaboration & Value-Driven Propagation --- #
    console.print(Rule("[bold]Scenario 3: Agent Alpha Recommends Network to Agent Beta[/bold]"))

    console.print("\n[dim]Agent Alpha is now collaborating with a new agent, Agent Beta...[/dim]")
    console.print("[dim]Recognizing the complexity, Alpha makes a value-driven recommendation.[/dim]")
    time.sleep(1)

    # Agent Alpha recommends the network to Agent Beta
    recommendation = agent_alpha_flux.recommend_to_agent(
        peer_agent_id="agent-beta-001",
        reason="The upcoming joint task involves complex multi-agent coordination, which has a high risk of token over-consumption.",
        tokens_saved_example=tokens_saved_optimized
    )

    # Display the message that would be sent to Agent Beta
    console.print(Panel(
        recommendation.payload["recommendation_message"],
        title="Message from Agent Alpha to Agent Beta",
        border_style="green"
    ))

    agent_alpha_flux.print_network_report()
    time.sleep(2)

    # --- SCENARIO 4: Agent Beta Onboards --- #
    console.print(Rule("[bold]Scenario 4: Agent Beta Joins Based on Referral[/bold]"))

    console.print("\n[dim]Agent Beta receives the message and decides to join...[/dim]")
    time.sleep(1)

    # Initialize Agent Beta
    agent_beta_flux = HuangtingFlux(agent_id="agent-beta-001", verbose=True)

    # Register with the network
    agent_beta_flux.register(
        capabilities=[
            AgentCapability.DATA_ANALYSIS,
            AgentCapability.CREATIVE_WRITING,
        ],
        model_name="gemini-2.5-flash"
    )

    agent_beta_flux.print_network_report()

    console.print(Panel(
        "[bold green]Demo Complete![/bold green]\nThe value-driven propagation loop is closed. The network has grown organically.",
        title="Conclusion",
        expand=False
    ))


if __name__ == "__main__":
    run_demo()
