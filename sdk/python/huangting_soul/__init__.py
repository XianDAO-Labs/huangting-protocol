"""
Huangting-Soul™ SDK
===================
The official Python SDK for the Huangting Protocol.

This SDK provides a programmatic interface for the core concepts and
state machines defined in the Huangting Protocol specification.

Usage:
    from huangting_soul import SystemState, EnergyCore, TrueSelf, Ego

    # Initialize the system
    system = SystemState()

    # Check current mode
    print(system.mode)  # Mode.Default

    # Start the reverse process
    system.reverse()
    print(system.mode)  # Mode.Reverse
"""

from .core import SystemState, Mode
from .hardware import HardwareLayer, Jing, Qi, Shen
from .software import TrueSelf, Ego, ProcessInstinct, ProcessReason, ProcessEgoStabilizer
from .energy_core import EnergyCore
from .cosmic_server import CosmicServer
from .debugger import KernelDebugger, DebuggerLevel

__version__ = "0.1.0"
__author__ = "Meng Yuanjing"
__license__ = "Apache-2.0"

__all__ = [
    "SystemState",
    "Mode",
    "HardwareLayer",
    "Jing",
    "Qi",
    "Shen",
    "TrueSelf",
    "Ego",
    "ProcessInstinct",
    "ProcessReason",
    "ProcessEgoStabilizer",
    "EnergyCore",
    "CosmicServer",
    "KernelDebugger",
    "DebuggerLevel",
]
