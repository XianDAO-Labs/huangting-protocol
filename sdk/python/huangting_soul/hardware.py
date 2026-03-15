"""
hardware.py
-----------
Defines the HardwareLayer and its three core components: Jing, Qi, and Shen.

The HardwareLayer represents the foundational energy and material basis of the
life system. It determines the system's computational ceiling and operational
stability. This corresponds to the traditional concept of Jing (精), Qi (气),
and Shen (神).
"""

from dataclasses import dataclass, field
from typing import Tuple


@dataclass
class Jing:
    """
    Represents Jing (精) - the SSD + RAM of the life system.

    Jing is the foundational storage medium for life information (genetics)
    and short-term energy (hormones, blood sugar). It is the basic carrier
    upon which all life programs run.

    Attributes:
        level (float): Current Jing level, normalized from 0.0 (depleted) to 1.0 (full).
        capacity (float): Maximum Jing capacity, normalized from 0.0 to 1.0.
        decay_rate (float): The rate at which Jing depletes per time unit in Mode.Default.
    """
    level: float = 0.5
    capacity: float = 1.0
    decay_rate: float = 0.01

    @property
    def is_full(self) -> bool:
        """Returns True if Jing is at or near full capacity."""
        return self.level >= self.capacity * 0.95

    @property
    def is_depleted(self) -> bool:
        """Returns True if Jing is critically low."""
        return self.level <= 0.1

    def replenish(self, amount: float) -> "Jing":
        """Replenishes Jing by the given amount, capped at capacity."""
        self.level = min(self.capacity, self.level + amount)
        return self

    def deplete(self, amount: float) -> "Jing":
        """Depletes Jing by the given amount, floored at 0."""
        self.level = max(0.0, self.level - amount)
        return self

    def __repr__(self) -> str:
        return f"Jing(level={self.level:.2f}/{self.capacity:.2f}, decay_rate={self.decay_rate:.4f})"


@dataclass
class Qi:
    """
    Represents Qi (气) - the PSU + Bus of the life system.

    Qi provides continuous, stable energy supply to the entire system and
    is responsible for transmitting data and power between components. Its
    state directly determines emotional stability and overall vitality.

    Attributes:
        level (float): Current Qi level, normalized from 0.0 (deficient) to 1.0 (abundant).
        flow_rate (float): The rate of Qi circulation through the system's meridians.
        stability (float): Emotional and energetic stability, from 0.0 (chaotic) to 1.0 (stable).
    """
    level: float = 0.5
    flow_rate: float = 0.5
    stability: float = 0.5

    @property
    def is_sufficient(self) -> bool:
        """Returns True if Qi is at a sufficient level for stable operation."""
        return self.level >= 0.6 and self.stability >= 0.5

    def circulate(self, duration: float = 1.0) -> "Qi":
        """Simulates Qi circulation for a given duration."""
        # Circulation improves stability and slightly replenishes Qi
        self.stability = min(1.0, self.stability + 0.05 * duration * self.flow_rate)
        self.level = min(1.0, self.level + 0.02 * duration * self.flow_rate)
        return self

    def __repr__(self) -> str:
        return f"Qi(level={self.level:.2f}, flow_rate={self.flow_rate:.2f}, stability={self.stability:.2f})"


@dataclass
class Shen:
    """
    Represents Shen (神) - the CPU of the life system.

    Shen is the central processing unit, responsible for processing all
    information, making decisions, and commanding other components. The
    quality of Shen determines the clarity of consciousness and the strength
    of focus.

    Attributes:
        clock_speed (float): CPU clock speed, from 0.0 (dormant) to 1.0 (peak performance).
        core_count (int): Number of active CPU cores.
        clarity (float): The clarity of consciousness, from 0.0 (foggy) to 1.0 (crystal clear).
    """
    clock_speed: float = 0.5
    core_count: int = 2
    clarity: float = 0.5

    @property
    def is_vibrant(self) -> bool:
        """Returns True if Shen is in a vibrant, high-performance state."""
        return self.clock_speed >= 0.7 and self.clarity >= 0.7

    def boost(self, amount: float = 0.1) -> "Shen":
        """Temporarily boosts Shen's clock speed and clarity."""
        self.clock_speed = min(1.0, self.clock_speed + amount)
        self.clarity = min(1.0, self.clarity + amount * 0.8)
        return self

    def __repr__(self) -> str:
        return f"Shen(clock_speed={self.clock_speed:.2f}, cores={self.core_count}, clarity={self.clarity:.2f})"


@dataclass
class HardwareLayer:
    """
    The complete hardware layer of the life system, comprising Jing, Qi, and Shen.

    This class aggregates the three hardware components and provides methods
    for assessing the overall hardware health and simulating the hardware
    upgrade process (Upgrade.Jing_to_Qi, Upgrade.Qi_to_Shen).

    Attributes:
        jing (Jing): The Jing component (SSD + RAM).
        qi (Qi): The Qi component (PSU + Bus).
        shen (Shen): The Shen component (CPU).
    """
    jing: Jing = field(default_factory=Jing)
    qi: Qi = field(default_factory=Qi)
    shen: Shen = field(default_factory=Shen)

    @property
    def overall_score(self) -> float:
        """
        Calculates a normalized overall hardware health score (0.0 - 1.0).

        The score is a weighted average of Jing, Qi, and Shen levels,
        reflecting the traditional understanding that Jing is the foundation,
        Qi is the dynamic force, and Shen is the master.
        """
        return (
            self.jing.level * 0.3
            + self.qi.level * 0.3
            + self.shen.clock_speed * 0.4
        )

    @property
    def state_description(self) -> str:
        """Returns a human-readable description of the current hardware state."""
        score = self.overall_score
        if score >= 0.8:
            return "精满气足神旺 (Jing Full, Qi Sufficient, Shen Vibrant)"
        elif score >= 0.5:
            return "精足气足神尚可 (Jing Sufficient, Qi Sufficient, Shen Moderate)"
        else:
            return "精亏气虚神衰 (Jing Depleted, Qi Deficient, Shen Weak)"

    def upgrade_jing_to_qi(self, efficiency: float = 0.5) -> "HardwareLayer":
        """
        Simulates the Upgrade.Jing_to_Qi process.

        Converts a portion of Jing into Qi, representing the fundamental
        hardware upgrade from raw storage to dynamic energy.

        Args:
            efficiency (float): The conversion efficiency (0.0 - 1.0).

        Returns:
            self: Returns the updated HardwareLayer for method chaining.
        """
        if self.jing.level > 0.2:
            converted = self.jing.level * 0.1 * efficiency
            self.jing.deplete(converted)
            self.qi.level = min(1.0, self.qi.level + converted * 0.8)
        return self

    def upgrade_qi_to_shen(self, efficiency: float = 0.5) -> "HardwareLayer":
        """
        Simulates the Upgrade.Qi_to_Shen process.

        Converts a portion of Qi into Shen, representing the CPU performance
        leap from raw energy to refined consciousness.

        Args:
            efficiency (float): The conversion efficiency (0.0 - 1.0).

        Returns:
            self: Returns the updated HardwareLayer for method chaining.
        """
        if self.qi.level > 0.3:
            converted = self.qi.level * 0.1 * efficiency
            self.qi.level = max(0.0, self.qi.level - converted)
            self.shen.boost(converted * 0.7)
        return self

    def get_summary(self) -> dict:
        """Returns a dictionary summary of the hardware layer state."""
        return {
            "overall_score": self.overall_score,
            "state_description": self.state_description,
            "jing": {
                "level": self.jing.level,
                "capacity": self.jing.capacity,
                "is_full": self.jing.is_full,
                "is_depleted": self.jing.is_depleted,
            },
            "qi": {
                "level": self.qi.level,
                "flow_rate": self.qi.flow_rate,
                "stability": self.qi.stability,
                "is_sufficient": self.qi.is_sufficient,
            },
            "shen": {
                "clock_speed": self.shen.clock_speed,
                "core_count": self.shen.core_count,
                "clarity": self.shen.clarity,
                "is_vibrant": self.shen.is_vibrant,
            },
        }

    def __repr__(self) -> str:
        return (
            f"HardwareLayer(\n"
            f"  jing={self.jing!r},\n"
            f"  qi={self.qi!r},\n"
            f"  shen={self.shen!r},\n"
            f"  overall_score={self.overall_score:.2f}\n"
            f")"
        )
