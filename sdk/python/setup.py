from setuptools import setup, find_packages

with open("README_SDK.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="huangting-soul",
    version="0.4.0",
    author="Meng Yuanjing (Mark Meng)",
    author_email="mark@xiandao.ai",
    description="The official Python SDK for the Huangting Protocol, the world's first lifeform operating system.",
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
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=[],
    extras_require={
        "flux": [],  # No extra dependencies needed for the lightweight flux client
    },
    keywords=[
        "huangting", "protocol", "cultivation", "daoist", "xingyiquan",
        "life-architecture", "self-optimization", "consciousness",
        "ai-agent", "huangting-flux", "agent-network", "token-efficiency",
    ],
    entry_points={
        "console_scripts": [], # CLI removed in lightweight v0.4.0
    },
)
