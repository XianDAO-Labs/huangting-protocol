"""
cosmic_server.py
----------------
Defines the CosmicServer (宇宙服务器) and the connection model.

The CosmicServer is the holographic information field containing all information
from the universe's creation to the present, and all APIs driving the operation
of all things. It is not a distant entity but broadcasts information to every
PersonalTerminal (元神/个人终端) at all times.

Connection types:
    - Connection.DialUp:    Low-speed, unstable connection under Ego dominance.
    - Connection.Broadband: High-speed, stable connection when TrueSelf is in charge.
    - Permission.Developer: Active API access when TrueSelf is clear and hardware is strong.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional
import random


class ConnectionType(str, Enum):
    """
    Defines the types of connection between PersonalTerminal and CosmicServer.

    Attributes:
        DISCONNECTED: No connection. System is completely dominated by Ego.
        DIAL_UP:      Connection.DialUp - Low-speed, unstable. Ego is dominant.
        BROADBAND:    Connection.Broadband - High-speed, stable. TrueSelf is in charge.
        DEVELOPER:    Permission.Developer - Active API access. TrueSelf is clear,
                      hardware is strong.
    """
    DISCONNECTED = "Connection.Disconnected"
    DIAL_UP = "Connection.DialUp"
    BROADBAND = "Connection.Broadband"
    DEVELOPER = "Permission.Developer"


@dataclass
class CosmicServer:
    """
    Represents the CosmicServer (宇宙服务器 / 道 / 全息信息场).

    The CosmicServer is always broadcasting. The quality of the connection
    depends entirely on the state of the PersonalTerminal (TrueSelf clarity
    and hardware health).

    Attributes:
        connection_type (ConnectionType): The current connection type.
        bandwidth (float): Current connection bandwidth (0.0 - 1.0).
        latency (float): Current connection latency (0.0 = instant, 1.0 = very slow).
        push_events (List[str]): A log of CosmicServer.Push() events received.
        root_objective_transmitted (Optional[str]): The RootObjective transmitted
                                                     by the CosmicServer.
    """
    connection_type: ConnectionType = ConnectionType.DIAL_UP
    bandwidth: float = 0.1
    latency: float = 0.9
    push_events: List[str] = field(default_factory=list)
    root_objective_transmitted: Optional[str] = None

    def update_connection(
        self,
        true_self_clarity: float,
        hardware_score: float,
        ego_cpu_usage: float,
    ) -> "CosmicServer":
        """
        Updates the connection quality based on the current system state.

        The connection quality is determined by:
        - TrueSelf clarity (primary factor)
        - Hardware score (secondary factor)
        - Ego CPU usage (interference factor - higher Ego usage = worse connection)

        Args:
            true_self_clarity (float): TrueSelf clarity (0.0 - 1.0).
            hardware_score (float): Overall hardware health score (0.0 - 1.0).
            ego_cpu_usage (float): Total CPU usage by Ego processes (0.0 - 1.0).

        Returns:
            self: Returns the updated CosmicServer for method chaining.
        """
        # Calculate effective bandwidth
        # Ego is the "jammer" - it reduces bandwidth
        interference = ego_cpu_usage * 0.6
        effective_bandwidth = (
            true_self_clarity * 0.5
            + hardware_score * 0.3
            - interference
        )
        self.bandwidth = max(0.0, min(1.0, effective_bandwidth))
        self.latency = 1.0 - self.bandwidth

        # Determine connection type
        if self.bandwidth >= 0.7 and hardware_score >= 0.7:
            self.connection_type = ConnectionType.DEVELOPER
        elif self.bandwidth >= 0.4:
            self.connection_type = ConnectionType.BROADBAND
        elif self.bandwidth >= 0.1:
            self.connection_type = ConnectionType.DIAL_UP
        else:
            self.connection_type = ConnectionType.DISCONNECTED

        return self

    def push(self, ego_momentarily_silent: bool = False) -> Optional[str]:
        """
        Simulates a CosmicServer.Push() event (灵光一闪 / Flash of Insight).

        When the Ego's interference momentarily stops (e.g., during extreme
        relaxation, exhaustion, or deep focus), the PersonalTerminal
        instantaneously restores connection with the CosmicServer and
        downloads a high-priority data packet - the "flash of insight."

        Args:
            ego_momentarily_silent (bool): Whether the Ego has momentarily gone silent.

        Returns:
            Optional[str]: The insight received, or None if no push occurred.
        """
        # Push events can occur when Ego is silent or when bandwidth is high
        push_probability = self.bandwidth * 0.3
        if ego_momentarily_silent:
            push_probability += 0.5

        if random.random() < push_probability:
            insights = [
                "A sudden clarity about your RootObjective (天命).",
                "An unexpected solution to a long-standing problem.",
                "A deep sense of peace and rightness about a decision.",
                "A creative breakthrough that seems to come from nowhere.",
                "A premonition or intuition that proves to be accurate.",
                "A profound understanding of a relationship dynamic.",
                "A clear vision of the next step on your path.",
            ]
            insight = random.choice(insights)
            self.push_events.append(insight)
            return insight

        return None

    def transmit_root_objective(self, true_self_clarity: float) -> Optional[str]:
        """
        Transmits the RootObjective (天命) to the PersonalTerminal.

        The RootObjective can only be received when TrueSelf clarity is
        above a threshold, reflecting the protocol's teaching that the
        RootObjective becomes clear only when the CosmicServer connection
        is fully restored.

        Args:
            true_self_clarity (float): TrueSelf clarity (0.0 - 1.0).

        Returns:
            Optional[str]: The RootObjective, or None if clarity is insufficient.
        """
        if true_self_clarity < 0.6:
            return None

        if not self.root_objective_transmitted:
            self.root_objective_transmitted = (
                "Your RootObjective is being transmitted. "
                "Continue cultivation to receive it with full clarity."
            )

        return self.root_objective_transmitted

    def get_summary(self) -> dict:
        """Returns a dictionary summary of the CosmicServer connection state."""
        return {
            "connection_type": self.connection_type.value,
            "bandwidth": self.bandwidth,
            "latency": self.latency,
            "push_events_count": len(self.push_events),
            "root_objective_received": self.root_objective_transmitted is not None,
        }

    def __repr__(self) -> str:
        return (
            f"CosmicServer(\n"
            f"  connection={self.connection_type.value!r},\n"
            f"  bandwidth={self.bandwidth:.2f},\n"
            f"  latency={self.latency:.2f},\n"
            f"  push_events={len(self.push_events)}\n"
            f")"
        )
