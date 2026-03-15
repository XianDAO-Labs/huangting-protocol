from setuptools import setup, find_packages

with open("../../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="huangting-soul",
    version="0.1.0",
    author="Meng Yuanjing",
    author_email="contact@huangting-protocol.org",
    description="The official Python SDK for the Huangting Protocol - an open-source framework for human life architecture optimization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/huangting-protocol/huangting-protocol",
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
    },
    keywords=[
        "huangting",
        "protocol",
        "cultivation",
        "daoist",
        "xingyiquan",
        "life-architecture",
        "self-optimization",
        "consciousness",
        "ai-agent",
    ],
)
