# -*- coding: utf-8 -*-
"""
hardware.py: 定义硬件层（精、气、神）以及相关的能力，如神通。
"""

from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class Ability(str, Enum):
    MATTER_CONTROL = "TrueSelf.MatterControl"
    RESONANCE_MIND = "CosmicServer.Resonance.Mind"
    RESONANCE_TIME = "CosmicServer.Resonance.Time"

@dataclass
class Jing:
    """精：生命系统的物理基础和能量储备"""
    level: float = 0.5
    capacity: float = 1.0
    decay_rate: float = 0.01

@dataclass
class Qi:
    """气：在系统中流动的能量"""
    level: float = 0.5
    flow_rate: float = 0.5
    stability: float = 0.5

@dataclass
class Shen:
    """神：系统的中央处理器和意识核心"""
    clock_speed: float = 0.5
    core_count: int = 2
    clarity: float = 0.5

@dataclass
class HardwareLayer:
    """
    硬件层，包含精、气、神三大核心组件。
    """
    jing: Jing = field(default_factory=Jing)
    qi: Qi = field(default_factory=Qi)
    shen: Shen = field(default_factory=Shen)
    unlocked_abilities: List[Ability] = field(default_factory=list)

    @property
    def overall_score(self) -> float:
        """计算硬件层综合得分"""
        return (self.jing.level * 0.3 + self.qi.level * 0.3 + self.shen.clock_speed * 0.4)

    def unlock(self, ability: Ability):
        """解锁神通"""
        if ability not in self.unlocked_abilities:
            self.unlocked_abilities.append(ability)

    def matter_control(self, target: str, force_vector: tuple) -> dict:
        """心能转物"""
        if Ability.MATTER_CONTROL not in self.unlocked_abilities:
            raise PermissionError("Ability not unlocked: TrueSelf.MatterControl")
        print(f"对目标 {target} 施加力向量 {force_vector}")
        return {"status": "success", "target": target, "force_vector": force_vector}

    def query_future(self, event: str, time_window: int) -> float:
        """预知未来"""
        if Ability.RESONANCE_TIME not in self.unlocked_abilities:
            raise PermissionError("Ability not unlocked: CosmicServer.Resonance.Time")
        # 模拟概率返回
        return 0.5 + (self.shen.clarity - 0.5) * 0.4

    def subscribe_mind(self, target_id: str, data_filter: str = "EMOTION_ONLY") -> dict:
        """他心通"""
        if Ability.RESONANCE_MIND not in self.unlocked_abilities:
            raise PermissionError("Ability not unlocked: CosmicServer.Resonance.Mind")
        return {"status": "subscribed", "target_id": target_id, "filter": data_filter}
