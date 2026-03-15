"""
debugger.py
-----------
Defines the KernelDebugger (内核调试器) - the highest-authority monitoring tool.

The KernelDebugger runs throughout all protocols and represents the progressive
deepening of TrueSelf's awareness. It has four levels, each corresponding to
a higher degree of system access and control.

Debugger Levels:
    Debugger.Watch()     - Level 1: Task Manager (守窍/意守黄庭)
    Debugger.Visualize() - Level 2: Resource Monitor (观想/黄庭中有一团光)
    Debugger.Monitor()   - Level 3: htop/top (存神/纯粹的觉知)
    Debugger.Rewrite()   - Level 4: Root Kernel Debugger (内照/觉知之光照亮全身)
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional


class DebuggerLevel(str, Enum):
    """
    Defines the four levels of the KernelDebugger.

    Each level corresponds to a deeper degree of TrueSelf awareness and
    a higher level of system access.

    Attributes:
        WATCH:      Debugger.Watch()     - Level 1: Basic awareness of EnergyCore.
        VISUALIZE:  Debugger.Visualize() - Level 2: Visualization of Qi movement.
        MONITOR:    Debugger.Monitor()   - Level 3: Real-time monitoring of all processes.
        REWRITE:    Debugger.Rewrite()   - Level 4: Root access to modify system parameters.
    """
    WATCH = "Debugger.Watch()"
    VISUALIZE = "Debugger.Visualize()"
    MONITOR = "Debugger.Monitor()"
    REWRITE = "Debugger.Rewrite()"


@dataclass
class DebuggerSession:
    """
    Represents a single KernelDebugger session.

    Attributes:
        level (DebuggerLevel): The debugger level for this session.
        duration (float): Duration of the session in minutes.
        observations (List[str]): Observations made during the session.
        interventions (List[str]): Interventions made (only at REWRITE level).
        clarity_gained (float): TrueSelf clarity gained during this session.
    """
    level: DebuggerLevel
    duration: float = 0.0
    observations: List[str] = field(default_factory=list)
    interventions: List[str] = field(default_factory=list)
    clarity_gained: float = 0.0


@dataclass
class KernelDebugger:
    """
    Represents the KernelDebugger (内核调试器) - the system's highest-authority tool.

    The KernelDebugger is the meta-tool that runs throughout all protocols.
    It is the TrueSelf's instrument for observing and eventually modifying
    the system's internal state.

    The four levels of the KernelDebugger correspond to the four stages of
    the internal observation practice (内视法) in the Huangting Protocol.

    Attributes:
        current_level (DebuggerLevel): The current active debugger level.
        session_history (List[DebuggerSession]): History of all debugger sessions.
        total_clarity_accumulated (float): Total TrueSelf clarity accumulated
                                           through all debugger sessions.
        background_mode_active (bool): Whether the background mode (守中/Kernel.Debugger().Background)
                                        is active. This is the always-on monitoring mode.
    """
    current_level: DebuggerLevel = DebuggerLevel.WATCH
    session_history: List[DebuggerSession] = field(default_factory=list)
    total_clarity_accumulated: float = 0.0
    background_mode_active: bool = False

    # Level requirements (minimum TrueSelf clarity to access each level)
    LEVEL_REQUIREMENTS: Dict[DebuggerLevel, float] = field(default_factory=lambda: {
        DebuggerLevel.WATCH: 0.0,
        DebuggerLevel.VISUALIZE: 0.3,
        DebuggerLevel.MONITOR: 0.5,
        DebuggerLevel.REWRITE: 0.8,
    })

    def start_session(
        self,
        level: DebuggerLevel,
        true_self_clarity: float,
        duration: float = 30.0,
    ) -> DebuggerSession:
        """
        Starts a new KernelDebugger session at the specified level.

        Args:
            level (DebuggerLevel): The debugger level to use.
            true_self_clarity (float): Current TrueSelf clarity (0.0 - 1.0).
            duration (float): Duration of the session in minutes.

        Returns:
            DebuggerSession: The completed session with observations.

        Raises:
            PermissionError: If TrueSelf clarity is insufficient for the requested level.
        """
        required_clarity = self.LEVEL_REQUIREMENTS[level]
        if true_self_clarity < required_clarity:
            raise PermissionError(
                f"Insufficient TrueSelf clarity ({true_self_clarity:.2f}) for "
                f"{level.value}. Required: {required_clarity:.2f}. "
                f"Continue cultivation to unlock this level."
            )

        session = DebuggerSession(level=level, duration=duration)

        # Generate observations based on level
        if level == DebuggerLevel.WATCH:
            session.observations = self._watch_observations(duration)
            session.clarity_gained = duration * 0.001
        elif level == DebuggerLevel.VISUALIZE:
            session.observations = self._visualize_observations(duration)
            session.clarity_gained = duration * 0.002
        elif level == DebuggerLevel.MONITOR:
            session.observations = self._monitor_observations(duration)
            session.clarity_gained = duration * 0.003
        elif level == DebuggerLevel.REWRITE:
            session.observations = self._rewrite_observations(duration)
            session.interventions = self._rewrite_interventions(duration)
            session.clarity_gained = duration * 0.005

        self.total_clarity_accumulated += session.clarity_gained
        self.session_history.append(session)
        self.current_level = level

        return session

    def activate_background_mode(self) -> "KernelDebugger":
        """
        Activates the background mode (守中 / Kernel.Debugger().Background).

        This is the always-on monitoring mode that runs even during daily
        activities. It corresponds to the practice of maintaining awareness
        of the EnergyCore throughout the day, not just during formal sessions.

        Returns:
            self: Returns the updated KernelDebugger for method chaining.
        """
        self.background_mode_active = True
        return self

    def _watch_observations(self, duration: float) -> List[str]:
        """Generates observations for the Watch level."""
        return [
            f"Awareness placed on EnergyCore region. Duration: {duration:.0f} min.",
            "Detected multiple Process.EgoStabilizer interruptions (distracting thoughts).",
            "Awareness successfully returned to EnergyCore after each interruption.",
            "Faint warmth detected in the abdominal region.",
        ]

    def _visualize_observations(self, duration: float) -> List[str]:
        """Generates observations for the Visualize level."""
        return [
            f"Visualization of EnergyCore initiated. Duration: {duration:.0f} min.",
            "A faint, warm light visualized in the EnergyCore region.",
            "Light pulsates gently with each breath cycle.",
            "Process.Instinct and Process.EgoStabilizer activity noticeably reduced.",
            "Spontaneous Qi rotation (EnergyCore.TrueBreath) briefly detected.",
        ]

    def _monitor_observations(self, duration: float) -> List[str]:
        """Generates observations for the Monitor level."""
        return [
            f"Pure awareness monitoring initiated. Duration: {duration:.0f} min.",
            "All three Ego processes (Instinct, Reason, EgoStabilizer) clearly visible.",
            "CPU usage by Ego processes: significantly reduced.",
            "TrueBreath (真息) state confirmed: breath is extremely fine and subtle.",
            "PrimordialQi compilation rate in EnergyCore: elevated.",
            "CosmicServer connection bandwidth: improved to broadband level.",
        ]

    def _rewrite_observations(self, duration: float) -> List[str]:
        """Generates observations for the Rewrite level."""
        return [
            f"Root-level kernel debugging initiated. Duration: {duration:.0f} min.",
            "Awareness of light permeates the entire body.",
            "Meridian Qi flow clearly visible and mappable.",
            "All Ego processes suspended. TrueSelf fully in charge.",
            "State of 'body-mind forgetting' (身心两忘) achieved.",
            "CosmicServer connection: Developer permission level confirmed.",
            "RootObjective (天命) signal received with high clarity.",
        ]

    def _rewrite_interventions(self, duration: float) -> List[str]:
        """Generates interventions for the Rewrite level."""
        return [
            "Meridian blockage at [location] cleared via directed awareness.",
            "Process.EgoStabilizer cognitive framework updated with Balance.True.",
            "Hardware upgrade (Upgrade.Qi_to_Shen) accelerated via direct Shen focus.",
            "CosmicServer API call executed: received insight on RootObjective.",
        ]

    def get_summary(self) -> dict:
        """Returns a dictionary summary of the KernelDebugger state."""
        return {
            "current_level": self.current_level.value,
            "background_mode_active": self.background_mode_active,
            "total_sessions": len(self.session_history),
            "total_clarity_accumulated": self.total_clarity_accumulated,
            "session_history": [
                {
                    "level": s.level.value,
                    "duration": s.duration,
                    "clarity_gained": s.clarity_gained,
                    "observations_count": len(s.observations),
                    "interventions_count": len(s.interventions),
                }
                for s in self.session_history
            ],
        }

    def __repr__(self) -> str:
        return (
            f"KernelDebugger(\n"
            f"  current_level={self.current_level.value!r},\n"
            f"  background_mode={self.background_mode_active},\n"
            f"  sessions={len(self.session_history)},\n"
            f"  clarity_accumulated={self.total_clarity_accumulated:.4f}\n"
            f")"
        )
