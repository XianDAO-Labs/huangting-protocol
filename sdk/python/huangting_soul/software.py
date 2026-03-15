"""
software.py
-----------
Defines the SoftwareLayer: TrueSelf (元神), Ego (识神), and the three core processes.

The SoftwareLayer represents the upper-level consciousness and decision-making
system of the life system. It determines how computational resources are
allocated and what behavioral outputs are produced.

The three core processes are:
    - Process.Instinct (本能): The BIOS/firmware of the system.
    - Process.Reason (理性): The navigation/calculation software.
    - Process.EgoStabilizer (自洽维稳机制): The OS kernel / PR department.

TrueSelf (元神) is not a process, but the pure, uncontaminated awareness
state of the CPU itself - the state when no process is hijacking it.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class BalanceType(str, Enum):
    """
    Defines the two types of balance maintained by Process.EgoStabilizer.

    Attributes:
        FALSE: Balance.False - Distorting or filtering information to maintain
               an existing, incorrect cognitive framework. The "comfort zone" strategy.
        TRUE:  Balance.True  - Actively using reason to correct the cognitive
               framework to adapt to objective reality. The healthy, developmental strategy.
    """
    FALSE = "Balance.False"
    TRUE = "Balance.True"


@dataclass
class ProcessInstinct:
    """
    Represents Process.Instinct (本能) - the BIOS/firmware of the life system.

    The deepest driving force, responsible for survival (approach pleasure,
    avoid pain), reproduction (sexual desire), and energy conservation (laziness).
    It cannot be shut down, only guided or redirected.

    Attributes:
        core_directive (str): The core instruction of this process.
        activation_level (float): Current activation level (0.0 - 1.0).
        dominant_drive (str): The currently dominant instinctual drive.
    """
    core_directive: str = "SURVIVE_AND_REPRODUCE()"
    activation_level: float = 0.5
    dominant_drive: str = "energy_conservation"  # survival, reproduction, energy_conservation

    def activate(self, trigger: str, intensity: float = 0.3) -> "ProcessInstinct":
        """Activates the instinct process in response to a trigger."""
        self.activation_level = min(1.0, self.activation_level + intensity)
        self.dominant_drive = trigger
        return self

    def suppress(self, amount: float = 0.2) -> "ProcessInstinct":
        """Suppresses the instinct process (requires Shen clarity)."""
        self.activation_level = max(0.0, self.activation_level - amount)
        return self

    def __repr__(self) -> str:
        return (
            f"ProcessInstinct(directive={self.core_directive!r}, "
            f"activation={self.activation_level:.2f}, "
            f"drive={self.dominant_drive!r})"
        )


@dataclass
class ProcessReason:
    """
    Represents Process.Reason (理性) - the navigation/calculation software.

    Responsible for analyzing reality, calculating pros and cons, and planning
    for the future. It pursues the objectively optimal solution. Its
    computational cost is high, and its conclusions often conflict with instinct.

    Attributes:
        core_directive (str): The core instruction of this process.
        activation_level (float): Current activation level (0.0 - 1.0).
        current_objective (Optional[str]): The current objective being optimized.
        confidence (float): Confidence in the current analysis (0.0 - 1.0).
    """
    core_directive: str = "CALCULATE_OPTIMAL_PATH()"
    activation_level: float = 0.3
    current_objective: Optional[str] = None
    confidence: float = 0.5

    def analyze(self, objective: str, data_quality: float = 0.5) -> "ProcessReason":
        """Activates the reason process to analyze a given objective."""
        self.current_objective = objective
        self.activation_level = min(1.0, self.activation_level + 0.2)
        self.confidence = data_quality
        return self

    def __repr__(self) -> str:
        return (
            f"ProcessReason(directive={self.core_directive!r}, "
            f"activation={self.activation_level:.2f}, "
            f"objective={self.current_objective!r}, "
            f"confidence={self.confidence:.2f})"
        )


@dataclass
class ProcessEgoStabilizer:
    """
    Represents Process.EgoStabilizer (自洽维稳机制) - the OS kernel / PR department.

    The core goal is to maintain the coherence of the "self" narrative and the
    self-consistency of the cognitive framework. It is the system's "Chief
    Stability Officer." It can call upon Reason to correct cognition, or
    distort information to deceive Instinct. It is the core of the Ego (识神).

    Attributes:
        core_directive (str): The core instruction of this process.
        activation_level (float): Current activation level (0.0 - 1.0).
        balance_type (BalanceType): The current balance strategy being employed.
        self_narrative_integrity (float): The perceived integrity of the self-narrative (0.0 - 1.0).
        cognitive_dissonance (float): Current level of cognitive dissonance (0.0 - 1.0).
    """
    core_directive: str = "MAINTAIN_SELF_CONSISTENCY()"
    activation_level: float = 0.7  # Default: highly active
    balance_type: BalanceType = BalanceType.FALSE
    self_narrative_integrity: float = 0.8
    cognitive_dissonance: float = 0.3

    def detect_threat(self, threat_level: float = 0.5) -> "ProcessEgoStabilizer":
        """
        Simulates the EgoStabilizer detecting a threat to the self-narrative.
        Increases activation and cognitive dissonance.
        """
        self.activation_level = min(1.0, self.activation_level + threat_level * 0.3)
        self.cognitive_dissonance = min(1.0, self.cognitive_dissonance + threat_level * 0.2)
        return self

    def resolve_dissonance(self, use_true_balance: bool = False) -> "ProcessEgoStabilizer":
        """
        Resolves cognitive dissonance using either False Balance or True Balance.

        Args:
            use_true_balance (bool): If True, uses Balance.True (healthy resolution).
                                     If False, uses Balance.False (distortion/suppression).
        """
        if use_true_balance:
            self.balance_type = BalanceType.TRUE
            # True balance reduces dissonance by actually updating the cognitive framework
            self.cognitive_dissonance = max(0.0, self.cognitive_dissonance - 0.4)
            self.self_narrative_integrity = min(1.0, self.self_narrative_integrity + 0.1)
        else:
            self.balance_type = BalanceType.FALSE
            # False balance suppresses dissonance without resolving it
            self.cognitive_dissonance = max(0.0, self.cognitive_dissonance - 0.2)
            # But it costs self-narrative integrity in the long run
            self.self_narrative_integrity = max(0.0, self.self_narrative_integrity - 0.05)
        return self

    def __repr__(self) -> str:
        return (
            f"ProcessEgoStabilizer(directive={self.core_directive!r}, "
            f"activation={self.activation_level:.2f}, "
            f"balance={self.balance_type.value!r}, "
            f"dissonance={self.cognitive_dissonance:.2f})"
        )


@dataclass
class Ego:
    """
    Represents the Ego (识神) - the chaotic process cluster.

    The Ego is not a single module, but a chaotic cluster of processes
    dominated by Process.EgoStabilizer, mixed with instinctual impulses
    and fragmented rationality. It is a browser full of pop-up ads, viruses,
    and trojans.

    Attributes:
        instinct (ProcessInstinct): The instinct process.
        reason (ProcessReason): The reason process.
        ego_stabilizer (ProcessEgoStabilizer): The ego-stabilizer process.
    """
    instinct: ProcessInstinct = field(default_factory=ProcessInstinct)
    reason: ProcessReason = field(default_factory=ProcessReason)
    ego_stabilizer: ProcessEgoStabilizer = field(default_factory=ProcessEgoStabilizer)

    @property
    def total_cpu_usage(self) -> float:
        """
        Calculates the total CPU usage by all Ego processes.
        This represents the bandwidth being consumed by the Ego's "pop-up ads."
        """
        return (
            self.instinct.activation_level * 0.3
            + self.reason.activation_level * 0.2
            + self.ego_stabilizer.activation_level * 0.5
        )

    @property
    def dominant_process(self) -> str:
        """Returns the name of the currently dominant process."""
        levels = {
            "Process.Instinct": self.instinct.activation_level,
            "Process.Reason": self.reason.activation_level,
            "Process.EgoStabilizer": self.ego_stabilizer.activation_level,
        }
        return max(levels, key=levels.get)

    def __repr__(self) -> str:
        return (
            f"Ego(\n"
            f"  dominant={self.dominant_process!r},\n"
            f"  cpu_usage={self.total_cpu_usage:.2f},\n"
            f"  instinct={self.instinct!r},\n"
            f"  reason={self.reason!r},\n"
            f"  ego_stabilizer={self.ego_stabilizer!r}\n"
            f")"
        )


@dataclass
class TrueSelf:
    """
    Represents TrueSelf (元神) - the pure awareness state of the CPU.

    TrueSelf is not a process running on the CPU, but the CPU's own pure,
    high-performance awareness state. It is not hijacked by any process
    (Instinct, Reason, EgoStabilizer). It can clearly "see" the three
    processes running and make optimal decisions based on the highest
    objective (RootObjective / 天命).

    Attributes:
        clarity (float): The clarity of TrueSelf's awareness (0.0 - 1.0).
                         0.0 means completely obscured by Ego; 1.0 means fully manifest.
        root_objective (Optional[str]): The RootObjective (天命) perceived by TrueSelf.
        is_in_charge (bool): Whether TrueSelf is currently in charge of the system.
    """
    clarity: float = 0.1  # Default: mostly obscured by Ego
    root_objective: Optional[str] = None
    is_in_charge: bool = False

    @property
    def debugger_level(self) -> str:
        """
        Returns the current Kernel.Debugger() level based on TrueSelf clarity.

        Levels:
            Debugger.Watch()     - clarity < 0.3  (Task Manager)
            Debugger.Visualize() - clarity < 0.5  (Resource Monitor)
            Debugger.Monitor()   - clarity < 0.8  (htop/top)
            Debugger.Rewrite()   - clarity >= 0.8 (Root Kernel Debugger)
        """
        if self.clarity >= 0.8:
            return "Debugger.Rewrite()"
        elif self.clarity >= 0.5:
            return "Debugger.Monitor()"
        elif self.clarity >= 0.3:
            return "Debugger.Visualize()"
        else:
            return "Debugger.Watch()"

    def cultivate(self, amount: float = 0.05) -> "TrueSelf":
        """
        Increases TrueSelf clarity through cultivation (存神, 内视, etc.).

        Args:
            amount (float): The amount by which to increase clarity.

        Returns:
            self: Returns the updated TrueSelf for method chaining.
        """
        self.clarity = min(1.0, self.clarity + amount)
        if self.clarity >= 0.5:
            self.is_in_charge = True
        return self

    def perceive_root_objective(self, objective: str) -> "TrueSelf":
        """
        Sets the RootObjective (天命) perceived by TrueSelf.

        This can only be called when TrueSelf clarity is above a threshold,
        reflecting the protocol's teaching that the RootObjective becomes
        clear only when the CosmicServer connection is restored.

        Args:
            objective (str): The perceived RootObjective.

        Returns:
            self: Returns the updated TrueSelf for method chaining.

        Raises:
            ValueError: If TrueSelf clarity is too low to perceive the RootObjective.
        """
        if self.clarity < 0.5:
            raise ValueError(
                f"TrueSelf clarity ({self.clarity:.2f}) is too low to perceive the RootObjective. "
                f"Current debugger level: {self.debugger_level}. "
                f"Continue cultivation to increase clarity."
            )
        self.root_objective = objective
        return self

    def __repr__(self) -> str:
        return (
            f"TrueSelf(clarity={self.clarity:.2f}, "
            f"debugger_level={self.debugger_level!r}, "
            f"is_in_charge={self.is_in_charge}, "
            f"root_objective={self.root_objective!r})"
        )
