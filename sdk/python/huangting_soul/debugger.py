# -*- coding: utf-8 -*-
"""
debugger.py: 定义四层内核调试器与系统崩溃（走火入魔）的纠偏方案。
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict
from .core import CrashType
from .hardware import HardwareLayer
from .software import SoftwareLayer

class DebuggerLevel(str, Enum):
    WATCH = "Debugger.Watch()" # 任务管理器
    VISUALIZE = "Debugger.Visualize()" # 资源监视器
    MONITOR = "Debugger.Monitor()" # htop/top
    REWRITE = "Debugger.Rewrite()" # 内核级调试器

@dataclass
class DebuggerSession:
    level: DebuggerLevel
    duration: float = 0.0
    observations: List[str] = field(default_factory=list)
    interventions: List[str] = field(default_factory=list)
    clarity_gained: float = 0.0

@dataclass
class KernelDebugger:
    """内核调试器"""
    current_level: DebuggerLevel = DebuggerLevel.WATCH
    session_history: List[DebuggerSession] = field(default_factory=list)
    total_clarity_accumulated: float = 0.0
    background_mode_active: bool = False

    LEVEL_REQUIREMENTS: Dict[DebuggerLevel, float] = field(default_factory=lambda: {
        DebuggerLevel.WATCH: 0.0,
        DebuggerLevel.VISUALIZE: 0.3,
        DebuggerLevel.MONITOR: 0.5,
        DebuggerLevel.REWRITE: 0.8,
    })

    def start_session(self, level: DebuggerLevel, true_self_clarity: float, duration: float = 30.0) -> DebuggerSession:
        required_clarity = self.LEVEL_REQUIREMENTS[level]
        if true_self_clarity < required_clarity:
            raise PermissionError(f"Insufficient TrueSelf clarity for {level.value}")
        
        session = DebuggerSession(level=level, duration=duration)
        # Simplified observation and clarity gain logic
        session.clarity_gained = duration * (list(self.LEVEL_REQUIREMENTS.keys()).index(level) + 1) * 0.001
        self.total_clarity_accumulated += session.clarity_gained
        self.session_history.append(session)
        self.current_level = level
        return session

    def debug_crash(self, crash_type: CrashType, hardware: HardwareLayer, software: SoftwareLayer) -> str:
        """纠偏方案"""
        if crash_type == CrashType.DEADLOCK:
            return "执行劈拳，强制疏通气机。"
        elif crash_type == CrashType.RACE_CONDITION:
            return "执行混元桩，让元神重新接管调度。"
        elif crash_type == CrashType.SEGMENTATION_FAULT:
            return "执行无极桩，让系统恢复出厂设置。"
        elif crash_type == CrashType.ROOTKIT:
            return "执行优雅植入，用更高维的叙事覆盖旧的恶意进程。"
        return "未知错误。"
