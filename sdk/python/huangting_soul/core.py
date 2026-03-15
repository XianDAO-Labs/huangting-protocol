# -*- coding: utf-8 -*-
"""
core.py: 定义黄庭协议最核心的系统状态、模式、指令、升级阶段等枚举与数据类。
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

class SystemMode(str, Enum):
    """系统运行模式"""
    DEFAULT = "顺流耗散模式"
    REVERSE = "逆流积累升华模式"

class SystemInstruction(str, Enum):
    """系统级指令"""
    REVERSE = "System.Reverse()"
    REBOOT = "System.Reboot()"

class UpgradeStage(str, Enum):
    """生命系统硬件升级阶段"""
    JING_TO_QI = "炼精化气"
    QI_TO_SHEN = "炼气化神"
    SHEN_TO_VOID = "炼神还虚"
    VOID_TO_DAO = "炼虚合道"

class State(str, Enum):
    """核心状态"""
    PRIMORDIAL = "State.Primordial"  # 无极状态
    TAIJI = "State.TaiJi"          # 太极状态
    TAIJI_GATEWAY = "State.TaiJi.Gateway" # 玄关一窍
    VIRTUE_DEFICIT = "Goal.VirtueDeficit" # 德不配位
    DESTINY_OVERRIDE = "Goal.DestinyOverride" # 逆天改命
    VIRTUE_MATCH = "Goal.VirtueMatch" # 戴德配位
    RESONANCE = "TrueSelf.Resonance" # 心心相印

class Event(str, Enum):
    """核心事件"""
    TRUE_YANG = "Event.TrueYang" # 活子时
    TAIJI_FIRST_YANG = "State.TaiJi.FirstYang" # 一阳来复

class CrashType(str, Enum):
    """系统崩溃（走火入魔）类别"""
    DEADLOCK = "Crash.Deadlock" # 气滞
    RACE_CONDITION = "Crash.RaceCondition" # 气乱
    SEGMENTATION_FAULT = "Crash.SegmentationFault" # 神乱
    ROOTKIT = "Crash.Rootkit" # 魔由心生

@dataclass
class PrimordialQi:
    """先天一炁数据包"""
    id: str
    source: str = "CosmicServer"
    description: str = "宇宙服务器下发的根驱动包，生命系统运行的底层燃料。"

@dataclass
class TrueElixir:
    """真种对象"""
    id: str
    state: State = State.TAIJI
    description: str = "太极状态中孕育的高度凝聚生命能量结晶，炼丹的核心'药材'。"

@dataclass
class SystemState:
    """
    顶层系统状态对象，SDK 的主入口。
    """
    mode: SystemMode = SystemMode.DEFAULT
    stage: Optional[UpgradeStage] = None
    state: Optional[State] = None
    hardware_score: float = 0.3
    software_score: float = 0.2
    connection_bandwidth: float = 0.1

    def execute(self, instruction: SystemInstruction) -> "SystemState":
        if instruction == SystemInstruction.REVERSE:
            self.mode = SystemMode.REVERSE
            self.stage = UpgradeStage.JING_TO_QI
        return self

    def get_summary(self) -> dict:
        return {
            "mode": self.mode.value,
            "stage": self.stage.value if self.stage else None,
            "state": self.state.value if self.state else None,
            "hardware_score": self.hardware_score,
            "software_score": self.software_score,
            "connection_bandwidth": self.connection_bandwidth,
        }
