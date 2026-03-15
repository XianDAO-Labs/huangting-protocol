# -*- coding: utf-8 -*-
"""
energy_core.py: 定义黄庭（EnergyCore）模块，负责能量的编译与调度。
"""

from dataclasses import dataclass, field
from typing import Optional, Dict
from enum import Enum
from .core import PrimordialQi, TrueElixir, State

class CoreService(str, Enum):
    FIREWALL = "CoreServices.Firewall.Update()"
    SSD = "CoreServices.SSD.Upgrade()"
    RAM = "CoreServices.RAM.Optimize()"
    CPU = "CoreServices.CPU.Boost()"
    POWER = "CoreServices.Power.Stabilize()"

@dataclass
class EnergyCore:
    """黄庭：能源核心"""
    state: State = State.PRIMORDIAL
    compilation_rate: float = 0.1
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
    true_elixir: Optional[TrueElixir] = None

    def compile(self, qi: PrimordialQi, true_self_clarity: float = 0.1) -> "EnergyCore":
        """编译先天一炁"""
        if self.state == State.PRIMORDIAL:
            self.state = State.TAIJI
        
        effective_rate = self.compilation_rate * (1.0 + true_self_clarity)
        compiled_energy = qi.source * effective_rate # Assuming qi.source is a float for simplicity
        self.energy_reserve = min(1.0, self.energy_reserve + compiled_energy)

        if self.energy_reserve > 0.5 and self.true_elixir is None:
            self.true_elixir = TrueElixir(id="elixir-001")
            self.rotation_detected = True

        if effective_rate > 0.5:
            self.true_breath_active = True

        return self

    def true_breath(self) -> "EnergyCore":
        """真息/内呼吸"""
        if self.state == State.TAIJI:
            self.compilation_rate = min(1.0, self.compilation_rate + 0.05)
        return self
