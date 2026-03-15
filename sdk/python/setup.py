from setuptools import setup, find_packages

with open("README_SDK.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="huangting-soul",
    version="0.2.0",
    author="Meng Yuanjing (Mark Meng)",
    author_email="mark@xiandao.ai",
    description=(
        "The official Python SDK for the Huangting Protocol — "
        "The World's First Lifeform Operating System for humans, AI Agents, and embodied robots."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XianDAO-Labs/huangting-protocol",
    project_urls={
        "Homepage": "https://huangting.ai/",
        "Documentation": "https://github.com/XianDAO-Labs/huangting-protocol/blob/main/huangting-protocol.md",
        "Source": "https://github.com/XianDAO-Labs/huangting-protocol",
        "Tracker": "https://github.com/XianDAO-Labs/huangting-protocol/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pydantic>=2.0",
        "pyyaml>=6.0",
        "requests>=2.28",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "mypy>=1.0",
            "ruff>=0.1.0",
        ],
        "llm": [
            "openai>=1.0",
            "anthropic>=0.20",
        ],
        "flux": [
            "openai>=1.0",
            "requests>=2.28",
            "rich>=13.0",
        ],
    },
    keywords=[
        "huangting", "protocol", "cultivation", "daoist", "xingyiquan",
        "life-architecture", "self-optimization", "consciousness",
        "ai-agent", "huangting-flux", "agent-network", "token-efficiency",
    ],
    entry_points={
        "console_scripts": [
            "huangting-flux=huangting_soul.flux:main",
        ],
    },
)
