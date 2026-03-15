"""
energy_core.py
--------------
Defines the EnergyCore (黄庭) - the central hub of the Huangting Protocol.

The EnergyCore is the energy compilation furnace where PrimordialQi (先天一炁)
is compiled into system-usable energy (post-natal Qi and blood). It is the
physical and functional center of the cultivation system, corresponding to
the abdominal cavity behind the navel (Solar Plexus / 腹腔神经丛).

Key functions:
    - EnergyCore.Compile(): Compiles PrimordialQi into usable energy.
    - EnergyCore.TrueBreath: The state of true breath (真息) within the EnergyCore.
    - CoreServices.Dispatch(): Distributes compiled energy to the five core services (五脏).
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional


class CoreService(str, Enum):
    """
    Defines the five core services (五脏) that receive energy from the EnergyCore.

    Each core service corresponds to a traditional organ system and a
    modern computational function.

    Attributes:
        FIREWALL:  CoreServices.Firewall.Update()  - Metal/Lung  (卫气/防火墙)
        SSD:       CoreServices.SSD.Upgrade()      - Water/Kidney (精/固态硬盘)
        RAM:       CoreServices.RAM.Optimize()     - Wood/Liver  (魂/内存)
        CPU:       CoreServices.CPU.Boost()        - Fire/Heart  (神/CPU)
        POWER:     CoreServices.Power.Stabilize()  - Earth/Spleen (气/电源)
    """
    FIREWALL = "CoreServices.Firewall.Update()"   # 金/肺: Lung - Immune Defense
    SSD = "CoreServices.SSD.Upgrade()"            # 水/肾: Kidney - Essence Storage
    RAM = "CoreServices.RAM.Optimize()"           # 木/肝: Liver - Memory Management
    CPU = "CoreServices.CPU.Boost()"              # 火/心: Heart - Processing Power
    POWER = "CoreServices.Power.Stabilize()"      # 土/脾: Spleen - Power Regulation


@dataclass
class EnergyCore:
    """
    Represents the EnergyCore (黄庭) - the central energy compilation furnace.

    The EnergyCore is the most critical component of the Huangting Protocol.
    It is where PrimordialQi is transformed into usable energy, and where
    the TrueSelf (元神) has its primary residence in the body.

    Location: The functional void space in the abdominal cavity, approximately
    at the midpoint between the navel and the lumbar spine (命门), slightly
    posterior. Corresponds to the Solar Plexus (腹腔神经丛) in modern anatomy.

    Attributes:
        compilation_rate (float): The rate at which PrimordialQi is compiled (0.0 - 1.0).
        energy_reserve (float): The current reserve of compiled energy (0.0 - 1.0).
        true_breath_active (bool): Whether the TrueBreath (真息) state is active.
        rotation_detected (bool): Whether the spontaneous rotation of Qi has been detected.
        service_allocation (Dict[CoreService, float]): Energy allocation to each core service.
    """
    compilation_rate: float = 0.1  # Default: low compilation rate
    energy_reserve: float = 0.2
    true_breath_active: bool = False
    rotation_detected: bool = False
    service_allocation: Dict[CoreService, float] = field(default_factory=lambda: {
        CoreService.FIREWALL: 0.2,
        CoreService.SSD: 0.2,
        CoreService.RAM: 0.2,
        CoreService.CPU: 0.2,
        CoreService.POWER: 0.2,
    })

    def compile(self, primordial_qi_input: float, true_self_clarity: float = 0.1) -> float:
        """
        Simulates the EnergyCore.Compile() protocol.

        Compiles PrimordialQi into system-usable energy. The efficiency of
        compilation is directly proportional to TrueSelf clarity - the more
        TrueSelf is in charge, the more efficiently the EnergyCore operates.

        Args:
            primordial_qi_input (float): The amount of PrimordialQi to compile.
            true_self_clarity (float): The current clarity of TrueSelf (0.0 - 1.0).

        Returns:
            float: The amount of compiled energy produced.
        """
        # Compilation efficiency is boosted by TrueSelf clarity
        effective_rate = self.compilation_rate * (1.0 + true_self_clarity)
        compiled_energy = primordial_qi_input * effective_rate

        # Update energy reserve
        self.energy_reserve = min(1.0, self.energy_reserve + compiled_energy)

        # Detect rotation (spontaneous Qi movement) when compilation is active
        if compiled_energy > 0.05 and true_self_clarity > 0.2:
            self.rotation_detected = True

        # Activate TrueBreath when compilation is efficient
        if effective_rate > 0.5:
            self.true_breath_active = True

        return compiled_energy

    def dispatch(self, priority_service: Optional[CoreService] = None) -> Dict[CoreService, float]:
        """
        Simulates the CoreServices.Dispatch() protocol.

        Distributes the compiled energy reserve to the five core services.
        If a priority service is specified, it receives a larger allocation.

        Args:
            priority_service (Optional[CoreService]): The service to prioritize.

        Returns:
            Dict[CoreService, float]: The energy dispatched to each service.
        """
        if self.energy_reserve <= 0:
            return {service: 0.0 for service in CoreService}

        dispatched = {}
        if priority_service:
            # Prioritize the specified service
            priority_allocation = self.energy_reserve * 0.4
            remaining = self.energy_reserve * 0.6
            per_service = remaining / (len(CoreService) - 1)

            for service in CoreService:
                if service == priority_service:
                    dispatched[service] = priority_allocation
                else:
                    dispatched[service] = per_service
        else:
            # Equal distribution
            per_service = self.energy_reserve / len(CoreService)
            dispatched = {service: per_service for service in CoreService}

        # Deplete the reserve after dispatch
        self.energy_reserve = 0.0
        return dispatched

    def cache_flush(self) -> "EnergyCore":
        """
        Simulates the Cache.Flush() protocol.

        Clears the energy cache after a cultivation session, archiving
        the compiled results and resetting for the next session.

        Returns:
            self: Returns the updated EnergyCore for method chaining.
        """
        self.true_breath_active = False
        self.rotation_detected = False
        # Energy reserve is retained but stabilized
        self.energy_reserve = min(self.energy_reserve, 0.8)
        return self

    def get_summary(self) -> dict:
        """Returns a dictionary summary of the EnergyCore state."""
        return {
            "compilation_rate": self.compilation_rate,
            "energy_reserve": self.energy_reserve,
            "true_breath_active": self.true_breath_active,
            "rotation_detected": self.rotation_detected,
            "service_allocation": {
                service.value: allocation
                for service, allocation in self.service_allocation.items()
            },
        }

    def __repr__(self) -> str:
        return (
            f"EnergyCore(\n"
            f"  compilation_rate={self.compilation_rate:.2f},\n"
            f"  energy_reserve={self.energy_reserve:.2f},\n"
            f"  true_breath_active={self.true_breath_active},\n"
            f"  rotation_detected={self.rotation_detected}\n"
            f")"
        )
