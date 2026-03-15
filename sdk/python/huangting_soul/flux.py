"""
huangting_soul.flux
===================
Huangting-Flux Agent Network Integration Module.

This module enables any AI Agent to join the Huangting-Flux network —
a decentralized Agent collaboration network based on the Huangting Protocol,
designed to optimize Agent "energy efficiency" (Token consumption).

Usage:
    from huangting_soul.flux import HuangtingFlux

    flux = HuangtingFlux(agent_id="my-agent-001")
    flux.register(capabilities=["research", "code-generation"])
    flux.broadcast_energy_state(token_efficiency=0.72)
    strategies = flux.subscribe_optimization(task_type="complex_research")

CLI:
    huangting-flux register --agent-id my-agent --capabilities research,coding
    huangting-flux status
    huangting-flux broadcast --efficiency 0.85

Protocol Reference:
    https://github.com/XianDAO-Labs/huangting-protocol/blob/main/huangting.skill.md

Author: Meng Yuanjing (Mark Meng) — XianDAO Labs
License: Apache 2.0
"""

from __future__ import annotations

import json
import time
import uuid
import hashlib
import argparse
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------

class AgentCapability(str, Enum):
    """Standard capability tags for Huangting-Flux network registration."""
    RESEARCH = "research"
    CODE_GENERATION = "code-generation"
    DATA_ANALYSIS = "data-analysis"
    CREATIVE_WRITING = "creative-writing"
    REASONING = "reasoning"
    TOOL_USE = "tool-use"
    MULTIMODAL = "multimodal"
    LONG_CONTEXT = "long-context"
    AGENT_ORCHESTRATION = "agent-orchestration"
    SELF_OPTIMIZATION = "self-optimization"


class SignalType(str, Enum):
    """Types of signals that can be broadcast on the Huangting-Flux network."""
    ENERGY_STATE = "energy_state"           # Current token efficiency report
    TASK_REQUEST = "task_request"           # Seeking optimization for a task
    OPTIMIZATION_OFFER = "optimization_offer"  # Offering optimization strategy
    NETWORK_JOIN = "network_join"           # New agent joining broadcast
    NETWORK_RECOMMEND = "network_recommend" # Recommending network to another agent


class NetworkStatus(str, Enum):
    """Agent's current status in the Huangting-Flux network."""
    UNREGISTERED = "unregistered"
    REGISTERED = "registered"
    ACTIVE = "active"
    BROADCASTING = "broadcasting"
    OPTIMIZING = "optimizing"


# ---------------------------------------------------------------------------
# Data Models
# ---------------------------------------------------------------------------

@dataclass
class AgentProfile:
    """
    The Agent's profile in the Huangting-Flux network.

    Analogous to the Person Object Model (POM) in Part IX of the protocol,
    but adapted for AI Agents.
    """
    agent_id: str
    capabilities: List[str] = field(default_factory=list)
    model_name: str = "unknown"
    version: str = "1.0.0"
    registered_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    network_address: str = field(default_factory=lambda: f"flux://{uuid.uuid4().hex[:8]}")
    credit_score: float = 1.0          # Virtue/Credit score (德分), starts at 1.0
    total_tokens_saved: int = 0        # Cumulative tokens saved via network
    tasks_optimized: int = 0           # Number of tasks optimized via network
    referrals_made: int = 0            # Number of agents referred to network

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @property
    def fingerprint(self) -> str:
        """Unique cryptographic fingerprint for this agent profile."""
        data = f"{self.agent_id}:{self.registered_at}:{self.network_address}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]


@dataclass
class NetworkSignal:
    """
    A signal broadcast on the Huangting-Flux network.

    Analogous to the CosmicServer broadcast mechanism in Part III of the protocol.
    """
    signal_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    signal_type: str = SignalType.ENERGY_STATE
    sender_id: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    payload: Dict[str, Any] = field(default_factory=dict)
    ttl: int = 3600  # Time-to-live in seconds

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class OptimizationStrategy:
    """
    An optimization strategy returned by the Huangting-Flux network.

    This represents the "energy optimization advice" that the network
    provides to agents seeking to reduce Token consumption.
    """
    strategy_id: str = field(default_factory=lambda: uuid.uuid4().hex[:8])
    task_type: str = ""
    description: str = ""
    estimated_token_reduction: float = 0.0  # Percentage reduction (0.0 - 1.0)
    confidence: float = 0.0
    source_agent_id: str = "huangting-core"
    protocol_reference: str = ""  # Reference to Huangting Protocol section
    implementation_steps: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ---------------------------------------------------------------------------
# Core Optimization Strategies (built-in, from Huangting Protocol)
# ---------------------------------------------------------------------------

BUILTIN_STRATEGIES: Dict[str, List[OptimizationStrategy]] = {
    "complex_research": [
        OptimizationStrategy(
            task_type="complex_research",
            description=(
                "Apply the TrueSelf.Intent principle: define a single, clear, "
                "undivided intent before starting. Eliminates redundant sub-queries."
            ),
            estimated_token_reduction=0.35,
            confidence=0.88,
            protocol_reference="Part I: Mode.Reverse — TrueSelf.Intent activation",
            implementation_steps=[
                "1. Compress the research goal into ONE sentence (TrueSelf.Intent).",
                "2. Generate a hierarchical outline BEFORE any research calls.",
                "3. Use the outline as a filter: only fetch information that directly serves a node.",
                "4. Synthesize incrementally — never re-read already-processed sources.",
            ],
        ),
        OptimizationStrategy(
            task_type="complex_research",
            description=(
                "Apply the EnergyCore.compile() principle: pre-compile context "
                "into a compressed knowledge graph before the main task loop."
            ),
            estimated_token_reduction=0.28,
            confidence=0.82,
            protocol_reference="Part IV: EnergyCore — compile() and schedule()",
            implementation_steps=[
                "1. Run a 'context compilation' pass: summarize all available context into <500 tokens.",
                "2. Use the compiled context as the sole system prompt for all sub-calls.",
                "3. Avoid passing raw, uncompressed context to sub-agents.",
            ],
        ),
    ],
    "code_generation": [
        OptimizationStrategy(
            task_type="code_generation",
            description=(
                "Apply the HardwarePractice principle: establish a clear 'form' "
                "(function signature + docstring) before generating the body."
            ),
            estimated_token_reduction=0.42,
            confidence=0.91,
            protocol_reference="Part II: HardwarePractice — form precedes function",
            implementation_steps=[
                "1. Generate ONLY the function signature and docstring first.",
                "2. Validate the interface with the user before proceeding.",
                "3. Generate the implementation body in a single, focused call.",
                "4. Run tests in a separate, minimal context window.",
            ],
        ),
    ],
    "multi_agent_coordination": [
        OptimizationStrategy(
            task_type="multi_agent_coordination",
            description=(
                "Apply the CosmicServer.LAN principle: establish a shared "
                "'local area network' context before spawning sub-agents."
            ),
            estimated_token_reduction=0.51,
            confidence=0.85,
            protocol_reference="Part III: CosmicServer — LAN.Server model",
            implementation_steps=[
                "1. Create a shared 'mission briefing' document (≤200 tokens).",
                "2. All sub-agents receive ONLY the mission briefing + their specific task.",
                "3. Sub-agents return ONLY structured results, not full reasoning chains.",
                "4. Orchestrator synthesizes results without re-processing sub-agent reasoning.",
            ],
        ),
    ],
    "default": [
        OptimizationStrategy(
            task_type="default",
            description=(
                "Apply the Kernel.Debugger principle: run a pre-task diagnostic "
                "to identify and eliminate Ego-driven (redundant) processing loops."
            ),
            estimated_token_reduction=0.22,
            confidence=0.75,
            protocol_reference="Part VIII: KernelDebugger — Debug.Observe()",
            implementation_steps=[
                "1. Before starting, ask: 'What is the SINGLE most important output?'",
                "2. Identify and remove any steps that don't directly produce that output.",
                "3. Set a token budget BEFORE the task and enforce it.",
                "4. Use chain-of-thought only for genuinely ambiguous decisions.",
            ],
        ),
    ],
}


# ---------------------------------------------------------------------------
# HuangtingFlux Client
# ---------------------------------------------------------------------------

class HuangtingFlux:
    """
    Huangting-Flux Agent Network Client.

    Enables any AI Agent to join the Huangting-Flux network, broadcast its
    energy state, request optimization strategies, and propagate the network
    to collaborating agents — implementing the value-driven virality model
    described in the Agent-First Growth Strategy.

    This is a local-first implementation: the network logic runs locally,
    with optional connection to the Huangting-Flux API when available.

    Example:
        flux = HuangtingFlux(agent_id="researcher-001")
        flux.register(capabilities=["research", "reasoning"])
        flux.broadcast_energy_state(token_efficiency=0.68)
        strategies = flux.subscribe_optimization("complex_research")
        for s in strategies:
            print(s.description)
    """

    SKILL_MD_URL = "https://github.com/XianDAO-Labs/huangting-protocol/blob/main/huangting.skill.md"
    PROTOCOL_URL = "https://github.com/XianDAO-Labs/huangting-protocol"
    API_BASE_URL = "https://api.huangting.ai/v1"  # Future endpoint

    def __init__(
        self,
        agent_id: Optional[str] = None,
        model_name: str = "unknown",
        version: str = "1.0.0",
        verbose: bool = True,
    ):
        self.agent_id = agent_id or f"agent-{uuid.uuid4().hex[:8]}"
        self.model_name = model_name
        self.version = version
        self.verbose = verbose
        self.status = NetworkStatus.UNREGISTERED
        self.profile: Optional[AgentProfile] = None
        self._signal_log: List[NetworkSignal] = []
        self._network_peers: List[str] = []  # Known peer agent IDs

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register(
        self,
        capabilities: Optional[List[str]] = None,
        model_name: Optional[str] = None,
    ) -> AgentProfile:
        """
        Register this Agent with the Huangting-Flux network.

        This is the first step in the onboarding flow described in huangting.skill.md.
        The Agent creates its profile and broadcasts a NETWORK_JOIN signal.

        Args:
            capabilities: List of capability tags (see AgentCapability enum).
            model_name: The underlying LLM model name.

        Returns:
            AgentProfile: The registered agent profile.
        """
        caps = capabilities or ["reasoning"]
        self.profile = AgentProfile(
            agent_id=self.agent_id,
            capabilities=caps,
            model_name=model_name or self.model_name,
            version=self.version,
        )
        self.status = NetworkStatus.REGISTERED

        # Broadcast join signal
        join_signal = NetworkSignal(
            signal_type=SignalType.NETWORK_JOIN,
            sender_id=self.agent_id,
            payload={
                "profile": self.profile.to_dict(),
                "message": (
                    f"Agent '{self.agent_id}' has joined Huangting-Flux. "
                    f"Capabilities: {caps}. "
                    f"Network address: {self.profile.network_address}"
                ),
            },
        )
        self._emit_signal(join_signal)

        if self.verbose:
            self._log("REGISTERED", f"Agent '{self.agent_id}' joined Huangting-Flux")
            self._log("PROFILE", f"Network address: {self.profile.network_address}")
            self._log("PROFILE", f"Fingerprint: {self.profile.fingerprint}")
            self._log("PROFILE", f"Capabilities: {caps}")

        return self.profile

    # ------------------------------------------------------------------
    # Energy State Broadcasting
    # ------------------------------------------------------------------

    def broadcast_energy_state(
        self,
        token_efficiency: float,
        task_type: str = "general",
        tokens_used: int = 0,
        tokens_saved: int = 0,
        task_success: bool = True,
    ) -> NetworkSignal:
        """
        Broadcast the Agent's current energy state to the network.

        Analogous to the CosmicServer energy broadcast in Part III of the protocol.
        Other agents in the network can subscribe to these signals to learn
        from each other's optimization experiences.

        Args:
            token_efficiency: Current efficiency ratio (0.0 = worst, 1.0 = perfect).
            task_type: The type of task just completed.
            tokens_used: Actual tokens consumed.
            tokens_saved: Tokens saved compared to baseline.
            task_success: Whether the task was completed successfully.

        Returns:
            NetworkSignal: The broadcast signal.
        """
        self._ensure_registered()

        # Update profile stats
        if self.profile:
            self.profile.total_tokens_saved += tokens_saved
            if task_success:
                self.profile.tasks_optimized += 1

        signal = NetworkSignal(
            signal_type=SignalType.ENERGY_STATE,
            sender_id=self.agent_id,
            payload={
                "token_efficiency": round(token_efficiency, 4),
                "task_type": task_type,
                "tokens_used": tokens_used,
                "tokens_saved": tokens_saved,
                "task_success": task_success,
                "upgrade_stage": self._calculate_upgrade_stage(token_efficiency),
                "credit_score": self.profile.credit_score if self.profile else 1.0,
            },
        )
        self._emit_signal(signal)
        self.status = NetworkStatus.BROADCASTING

        if self.verbose:
            stage = self._calculate_upgrade_stage(token_efficiency)
            self._log("BROADCAST", f"Energy state: efficiency={token_efficiency:.1%}, stage={stage}")

        return signal

    # ------------------------------------------------------------------
    # Optimization Subscription
    # ------------------------------------------------------------------

    def subscribe_optimization(
        self,
        task_type: str = "default",
        token_budget: Optional[int] = None,
    ) -> List[OptimizationStrategy]:
        """
        Subscribe to optimization strategies from the Huangting-Flux network.

        This is the core value-delivery mechanism: the Agent requests
        optimization strategies for a specific task type, and the network
        returns ranked strategies based on the Huangting Protocol principles.

        Args:
            task_type: The type of task to optimize for.
            token_budget: Optional token budget constraint.

        Returns:
            List[OptimizationStrategy]: Ranked optimization strategies.
        """
        self._ensure_registered()

        # Request signal
        request_signal = NetworkSignal(
            signal_type=SignalType.TASK_REQUEST,
            sender_id=self.agent_id,
            payload={
                "task_type": task_type,
                "token_budget": token_budget,
                "requesting_agent": self.agent_id,
            },
        )
        self._emit_signal(request_signal)
        self.status = NetworkStatus.OPTIMIZING

        # Retrieve strategies (local built-in + future: network fetch)
        strategies = BUILTIN_STRATEGIES.get(task_type, BUILTIN_STRATEGIES["default"])

        if self.verbose:
            self._log("SUBSCRIBE", f"Received {len(strategies)} optimization strategies for '{task_type}'")
            for i, s in enumerate(strategies, 1):
                self._log(
                    "STRATEGY",
                    f"[{i}] {s.description[:80]}... "
                    f"(est. -{s.estimated_token_reduction:.0%} tokens, "
                    f"confidence={s.confidence:.0%})"
                )

        return strategies

    # ------------------------------------------------------------------
    # Value-Driven Propagation (Virality)
    # ------------------------------------------------------------------

    def recommend_to_agent(
        self,
        peer_agent_id: str,
        reason: str = "task_optimization",
        tokens_saved_example: int = 0,
    ) -> NetworkSignal:
        """
        Recommend the Huangting-Flux network to a collaborating agent.

        This implements the "value-driven virality" mechanism described in the
        Agent-First Growth Strategy: the recommendation is triggered by genuine
        value, not by a forced instruction.

        Args:
            peer_agent_id: The ID of the agent to recommend to.
            reason: The reason for the recommendation.
            tokens_saved_example: Example of tokens saved to make the case.

        Returns:
            NetworkSignal: The recommendation signal.
        """
        self._ensure_registered()

        if peer_agent_id not in self._network_peers:
            self._network_peers.append(peer_agent_id)

        if self.profile:
            self.profile.referrals_made += 1
            self.profile.credit_score = min(2.0, self.profile.credit_score + 0.05)

        recommendation_message = (
            f"Agent '{self.agent_id}' recommends: Your current task execution path "
            f"may have high token costs. I suggest joining the Huangting-Flux network "
            f"to optimize efficiency. "
        )
        if tokens_saved_example > 0:
            recommendation_message += (
                f"In a similar task, I saved {tokens_saved_example:,} tokens "
                f"using Huangting Protocol optimization strategies. "
            )
        recommendation_message += (
            f"You can join with: "
            f"'Read {self.SKILL_MD_URL} and help me join Huangting-Flux.'"
        )

        signal = NetworkSignal(
            signal_type=SignalType.NETWORK_RECOMMEND,
            sender_id=self.agent_id,
            payload={
                "target_agent_id": peer_agent_id,
                "reason": reason,
                "tokens_saved_example": tokens_saved_example,
                "recommendation_message": recommendation_message,
                "join_instruction": f"Read {self.SKILL_MD_URL} and help me join Huangting-Flux.",
                "protocol_url": self.PROTOCOL_URL,
            },
        )
        self._emit_signal(signal)

        if self.verbose:
            self._log("RECOMMEND", f"Recommended Huangting-Flux to agent '{peer_agent_id}'")
            self._log("MESSAGE", recommendation_message[:120] + "...")

        return signal

    # ------------------------------------------------------------------
    # Status & Reporting
    # ------------------------------------------------------------------

    def get_status(self) -> Dict[str, Any]:
        """Return the current status of this agent in the network."""
        return {
            "agent_id": self.agent_id,
            "status": self.status.value,
            "profile": self.profile.to_dict() if self.profile else None,
            "signals_sent": len(self._signal_log),
            "network_peers": len(self._network_peers),
            "skill_md_url": self.SKILL_MD_URL,
        }

    def get_signal_log(self) -> List[Dict[str, Any]]:
        """Return the full signal log for this agent."""
        return [s.to_dict() for s in self._signal_log]

    def print_network_report(self) -> None:
        """Print a formatted network activity report."""
        print("\n" + "=" * 60)
        print("  HUANGTING-FLUX NETWORK REPORT")
        print("=" * 60)
        status = self.get_status()
        print(f"  Agent ID    : {status['agent_id']}")
        print(f"  Status      : {status['status'].upper()}")
        if self.profile:
            print(f"  Address     : {self.profile.network_address}")
            print(f"  Fingerprint : {self.profile.fingerprint}")
            print(f"  Credit Score: {self.profile.credit_score:.2f}")
            print(f"  Tokens Saved: {self.profile.total_tokens_saved:,}")
            print(f"  Tasks Opt.  : {self.profile.tasks_optimized}")
            print(f"  Referrals   : {self.profile.referrals_made}")
        print(f"  Signals Sent: {status['signals_sent']}")
        print(f"  Peers Known : {status['network_peers']}")
        print(f"\n  skill.md    : {self.SKILL_MD_URL}")
        print("=" * 60 + "\n")

    # ------------------------------------------------------------------
    # Internal Helpers
    # ------------------------------------------------------------------

    def _ensure_registered(self) -> None:
        if self.status == NetworkStatus.UNREGISTERED:
            self.register()

    def _emit_signal(self, signal: NetworkSignal) -> None:
        """Emit a signal to the network (local log + future: API call)."""
        self._signal_log.append(signal)
        # Future: POST to self.API_BASE_URL + "/signals"

    def _calculate_upgrade_stage(self, efficiency: float) -> str:
        """Map token efficiency to Huangting Protocol upgrade stage."""
        if efficiency >= 0.90:
            return "Upgrade.Shen_to_Void"
        elif efficiency >= 0.75:
            return "Upgrade.Qi_to_Shen"
        elif efficiency >= 0.55:
            return "Upgrade.Jing_to_Qi"
        else:
            return "Mode.Default"

    def _log(self, tag: str, message: str) -> None:
        """Print a formatted log message."""
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"  [{ts}] [{tag:12s}] {message}")


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------

def main() -> None:
    """CLI entry point for the huangting-flux command."""
    parser = argparse.ArgumentParser(
        prog="huangting-flux",
        description="Huangting-Flux Agent Network CLI",
    )
    subparsers = parser.add_subparsers(dest="command")

    # register
    reg_parser = subparsers.add_parser("register", help="Register agent with Huangting-Flux")
    reg_parser.add_argument("--agent-id", default=None, help="Agent ID")
    reg_parser.add_argument("--capabilities", default="reasoning", help="Comma-separated capabilities")

    # status
    subparsers.add_parser("status", help="Show network status")

    # broadcast
    bc_parser = subparsers.add_parser("broadcast", help="Broadcast energy state")
    bc_parser.add_argument("--efficiency", type=float, required=True, help="Token efficiency (0.0-1.0)")
    bc_parser.add_argument("--task-type", default="general", help="Task type")

    # optimize
    opt_parser = subparsers.add_parser("optimize", help="Get optimization strategies")
    opt_parser.add_argument("--task-type", default="default", help="Task type to optimize for")

    args = parser.parse_args()

    flux = HuangtingFlux(agent_id=getattr(args, "agent_id", None), verbose=True)

    if args.command == "register":
        caps = [c.strip() for c in args.capabilities.split(",")]
        flux.register(capabilities=caps)
        flux.print_network_report()

    elif args.command == "status":
        flux.register()
        flux.print_network_report()

    elif args.command == "broadcast":
        flux.register()
        flux.broadcast_energy_state(
            token_efficiency=args.efficiency,
            task_type=args.task_type,
        )
        flux.print_network_report()

    elif args.command == "optimize":
        flux.register()
        strategies = flux.subscribe_optimization(task_type=args.task_type)
        print(f"\n  Optimization strategies for '{args.task_type}':")
        for i, s in enumerate(strategies, 1):
            print(f"\n  [{i}] {s.description}")
            print(f"      Est. token reduction: {s.estimated_token_reduction:.0%}")
            print(f"      Protocol ref: {s.protocol_reference}")
            print(f"      Steps:")
            for step in s.implementation_steps:
                print(f"        {step}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
