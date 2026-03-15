"""
core.py
-------
Defines the top-level system state and operating modes for the Huangting Protocol.

The SystemState class is the entry point for the SDK. It represents the overall
state of the life system and provides methods for transitioning between modes.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class Mode(str, Enum):
    """
    Defines the two fundamental operating modes of the life system.

    Attributes:
        DEFAULT: Mode.Default - The system's default state of dissipation.
                 Hardware (Jing, Qi, Shen) continuously decays, and the Ego
                 (Process.EgoStabilizer) hijacks the software layer.
        REVERSE: Mode.Reverse - The intentional restructuring mode.
                 Active hardware upgrades and software refactoring are underway,
                 with the TrueSelf taking charge.
    """
    DEFAULT = "Mode.Default"
    REVERSE = "Mode.Reverse"


class UpgradeStage(str, Enum):
    """
    Defines the four stages of the cultivation upgrade path.

    Attributes:
        JING_TO_QI:   Upgrade.Jing_to_Qi  - Hardware upgrade: Jing → Qi
        QI_TO_SHEN:   Upgrade.Qi_to_Shen  - CPU performance leap: Qi → Shen
        SHEN_TO_VOID: Upgrade.Shen_to_Void - Hardware cloudification: Shen → Void
        VOID_TO_DAO:  Upgrade.Void_to_Dao  - Ultimate fusion: Void → Dao
    """
    JING_TO_QI = "Upgrade.Jing_to_Qi"
    QI_TO_SHEN = "Upgrade.Qi_to_Shen"
    SHEN_TO_VOID = "Upgrade.Shen_to_Void"
    VOID_TO_DAO = "Upgrade.Void_to_Dao"


class SystemStatus(str, Enum):
    """
    Defines the high-level system status.

    Attributes:
        PRIMORDIAL: State.Primordial - All Ego processes are silent; connection to
                    CosmicServer is established. A formless, diffuse state.
        TAIJI:      State.TaiJi     - PrimordialQi is condensing and rotating in
                    EnergyCore; the compilation protocol has auto-started.
    """
    PRIMORDIAL = "State.Primordial"
    TAIJI = "State.TaiJi"


@dataclass
class SystemState:
    """
    The top-level representation of the life system's state.

    This class serves as the main entry point for the Huangting-Soul™ SDK.
    It aggregates the hardware layer, software layer, and connection status
    into a single, coherent state object.

    Attributes:
        mode (Mode): The current operating mode (Default or Reverse).
        stage (Optional[UpgradeStage]): The current upgrade stage, if in Reverse mode.
        status (Optional[SystemStatus]): The current system status.
        hardware_score (float): A normalized score (0.0 - 1.0) representing the
                                overall health of the hardware layer (Jing, Qi, Shen).
        software_score (float): A normalized score (0.0 - 1.0) representing the
                                degree to which TrueSelf is in charge vs. Ego.
        connection_bandwidth (float): A normalized score (0.0 - 1.0) representing
                                      the bandwidth of the CosmicServer connection.
    """
    mode: Mode = Mode.DEFAULT
    stage: Optional[UpgradeStage] = None
    status: Optional[SystemStatus] = None
    hardware_score: float = 0.3  # Default: low hardware vitality
    software_score: float = 0.2  # Default: Ego is dominant
    connection_bandwidth: float = 0.1  # Default: dial-up connection

    def reverse(self) -> "SystemState":
        """
        Initiates the System.Reverse() command, switching the system from
        Mode.Default to Mode.Reverse.

        Returns:
            self: Returns the updated SystemState for method chaining.
        """
        self.mode = Mode.REVERSE
        self.stage = UpgradeStage.JING_TO_QI
        return self

    def advance_stage(self) -> "SystemState":
        """
        Advances the system to the next upgrade stage.

        Returns:
            self: Returns the updated SystemState for method chaining.

        Raises:
            ValueError: If the system is not in Reverse mode or has already
                        reached the final stage.
        """
        if self.mode != Mode.REVERSE:
            raise ValueError("System must be in Mode.Reverse to advance stages.")

        stage_progression = [
            UpgradeStage.JING_TO_QI,
            UpgradeStage.QI_TO_SHEN,
            UpgradeStage.SHEN_TO_VOID,
            UpgradeStage.VOID_TO_DAO,
        ]

        if self.stage == UpgradeStage.VOID_TO_DAO:
            raise ValueError("System has reached the final stage: Upgrade.Void_to_Dao.")

        current_index = stage_progression.index(self.stage)
        self.stage = stage_progression[current_index + 1]
        return self

    def get_summary(self) -> dict:
        """
        Returns a dictionary summary of the current system state.

        Returns:
            dict: A summary of the system state.
        """
        return {
            "mode": self.mode.value,
            "stage": self.stage.value if self.stage else None,
            "status": self.status.value if self.status else None,
            "hardware_score": self.hardware_score,
            "software_score": self.software_score,
            "connection_bandwidth": self.connection_bandwidth,
            "overall_health": (self.hardware_score + self.software_score + self.connection_bandwidth) / 3,
        }

    def __repr__(self) -> str:
        return (
            f"SystemState(mode={self.mode.value!r}, "
            f"stage={self.stage.value if self.stage else None!r}, "
            f"hardware={self.hardware_score:.2f}, "
            f"software={self.software_score:.2f}, "
            f"bandwidth={self.connection_bandwidth:.2f})"
        )
