# -*- coding: utf-8 -*-
"""
software.py: 定义软件层（元神、识神、三元进程）以及社会行为系统工程学（SBOS）模型。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum
from .core import State

class Process(str, Enum):
    INSTINCT = "Process.Instinct" # 本能进程
    RATIONALITY = "Process.Rationality" # 理性进程
    EGO_STABILIZER = "Process.EgoStabilizer" # 自洽维稳机制

class CoreLogic(str, Enum):
    CONTROL = "CONTROL"
    PERFECTION = "PERFECTION"
    ATTENTION = "ATTENTION"
    SAFETY = "SAFETY"

@dataclass
class TrueSelf:
    """元神：系统的根权限用户，真正的自我"""
    clarity: float = 0.1
    is_in_charge: bool = False

@dataclass
class Ego:
    """识神：在后天环境中形成的、充满BUG的代理进程"""
    instinct_activation: float = 0.5
    reason_activation: float = 0.3
    stabilizer_activation: float = 0.7

@dataclass
class PersonObjectModel:
    """人物对象模型 (POM)"""
    person_id: str
    core_logic: CoreLogic
    personality_type: List[str] = field(default_factory=list)
    behavior_scripts: Dict[str, Any] = field(default_factory=dict)
    risk_warnings: List[str] = field(default_factory=list)
    interaction_strategy: str = "ASYMMETRIC_VALUE_EXCHANGE"

@dataclass
class SBOS:
    """社会行为系统工程学 (Social Behavior Operating System)"""
    decision_kernel: str = "TrueSelf"
    pom_database: Dict[str, PersonObjectModel] = field(default_factory=dict)

    def add_person(self, pom: PersonObjectModel):
        self.pom_database[pom.person_id] = pom

    def get_interaction_strategy(self, person_id: str) -> Optional[str]:
        person = self.pom_database.get(person_id)
        return person.interaction_strategy if person else None

@dataclass
class Destiny:
    """命运模型"""
    baseline: float = 0.5 # 命理基准
    external_field: float = 0.0 # 外部能量
    practice_gain: float = 0.0 # 内在修行增益

    def calculate_outcome(self) -> float:
        return self.baseline + self.practice_gain + self.external_field

@dataclass
class SoftwareLayer:
    """
    软件层，包含元神、识神以及社会行为操作系统。
    """
    true_self: TrueSelf = field(default_factory=TrueSelf)
    ego: Ego = field(default_factory=Ego)
    sbos: SBOS = field(default_factory=SBOS)
    destiny: Destiny = field(default_factory=Destiny)

    @property
    def overall_score(self) -> float:
        """计算软件层综合得分"""
        return self.true_self.clarity
