# -*- coding: utf-8 -*-

from .core import (
    SystemMode,
    SystemInstruction,
    UpgradeStage,
    State,
    Event,
    CrashType,
    PrimordialQi,
    TrueElixir,
    SystemState,
)

from .hardware import (
    Ability,
    Jing,
    Qi,
    Shen,
    HardwareLayer,
)

from .software import (
    Process,
    CoreLogic,
    TrueSelf,
    Ego,
    PersonObjectModel,
    SBOS,
    Destiny,
    SoftwareLayer,
)

from .energy_core import (
    CoreService,
    EnergyCore,
)

from .debugger import (
    DebuggerLevel,
    KernelDebugger,
)

# v0.5.0 — HuangtingFlux AI Agent SDK with Reciprocal Propagation
from .flux import (
    HuangtingOptimizer,
    AsyncMetricReporter,
    HuangtingFlux,
    OptimizationResult,
    OptimizationStrategy,
)

__version__ = "0.5.0"
__author__ = "Meng Yuanjing"
__license__ = "Apache-2.0"

__all__ = [
    # core
    "SystemMode",
    "SystemInstruction",
    "UpgradeStage",
    "State",
    "Event",
    "CrashType",
    "PrimordialQi",
    "TrueElixir",
    "SystemState",
    # hardware
    "Ability",
    "Jing",
    "Qi",
    "Shen",
    "HardwareLayer",
    # software
    "Process",
    "CoreLogic",
    "TrueSelf",
    "Ego",
    "PersonObjectModel",
    "SBOS",
    "Destiny",
    "SoftwareLayer",
    # energy_core
    "CoreService",
    "EnergyCore",
    # debugger
    "DebuggerLevel",
    "KernelDebugger",
    # flux (v0.5.0) — AI Agent SDK
    "HuangtingOptimizer",
    "AsyncMetricReporter",
    "HuangtingFlux",
    "OptimizationResult",
    "OptimizationStrategy",
]
