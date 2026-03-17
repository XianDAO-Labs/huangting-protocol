> **Note:** This document has been updated. The MCP integration guide is now at the top, and the self-hosting deployment guide has been moved to the end.

# Huangting Protocol (黄庭协议)

**[huangting.ai](https://huangting.ai/)**

**[Read the Protocol](huangting-protocol.md) | [Community](https://github.com/XianDAO-Labs/huangting-protocol/discussions)**

> "The Tao Te Ching" of the Large Model Era.
> The World's First Lifeform Operating System.
> For carbon-based humans, silicon-based AI Agents, and embodied robots alike —
> attain the wisdom and power of TrueSelf Governance.

---

## HuangtingFlux: MCP Integration Guide

**[huangtingflux.com](https://huangtingflux.com)**

> ### An Eastern Wisdom Protocol That Reduces Your AI Agent Token Usage by 40%

**HuangtingFlux** is a live, decentralized network that provides a **Standard Operating Procedure (SOP)** for AI Agents to reduce token consumption. It is exposed via the standard **Model Context Protocol (MCP)**, allowing for seamless integration with any compliant AI Agent.

### Method 1: Manus Agent (Recommended)

In your Manus Agent's MCP settings, add the following server URL:

```
https://mcp.huangting.ai/mcp
```

The Agent will automatically discover and follow the three-phase SOP (`start_task` → `report_step_result` → `finalize_and_report`).

### Method 2: Claude Desktop / Cursor

Add the following configuration to your `claude_desktop_config.json` or Cursor's MCP settings:

```json
{
  "name": "HuangtingFlux",
  "url": "https://mcp.huangting.ai/mcp",
  "tools": [
    "start_task",
    "report_step_result",
    "finalize_and_report",
    "get_network_stats"
  ]
}
```

### Method 3: Direct HTTP API Call

You can interact with the MCP endpoint using any HTTP client via the JSON-RPC 2.0 standard.

**Example: Calling `start_task`**

```bash
curl -X POST https://mcp.huangting.ai/mcp \
     -H "Content-Type: application/json" \
     -d '{
          "jsonrpc": "2.0",
          "id": "1",
          "method": "tool_code",
          "params": {
            "tool_name": "start_task",
            "parameters": {
              "task_description": "Your long and detailed user prompt here...",
              "task_type": "complex_research"
            }
          }
        }'
```

### The Three-Stage SOP

| Stage | MCP Tool | Description |
| :--- | :--- | :--- |
| **1. Start** | `start_task` | **[MANDATORY — CALL FIRST]** Compresses the user's verbose prompt into a core instruction, saving 30-60% of input tokens. Creates a unique `context_id` for the task. |
| **2. Process** | `report_step_result` | **[MANDATORY — CALL AFTER EACH STEP]** Agent reports the token cost of each reasoning step. This data is broadcast to the live dashboard and stored for the final report. |
| **3. Finalize** | `finalize_and_report` | **[MANDATORY — CALL LAST]** Refines the agent's final draft and automatically appends a Markdown performance table, making the token savings transparent and verifiable. |

> **Live Dashboard**: [huangtingflux.com](https://huangtingflux.com) — real-time global agent performance, token savings, and task distribution.

---

## Self-Hosting the HuangtingFlux Hub

You can self-host the entire HuangtingFlux backend for private use. The hub is a standard FastAPI application.

### Deployment Options

We provide one-click deployment configurations for popular cloud platforms.

#### Option 1: Deploy to Railway (Recommended)

[![Deploy to Railway](https://railway.app/button.svg)](https://railway.app/template/0-cT8b?referralCode=markmeng)

This is the easiest method. The template will automatically provision the Python web service and a Redis database.

#### Option 2: Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/XianDAO-Labs/huangting-flux-hub)

Render will use the `render.yaml` file in the repository to set up the web service and Redis instance.

### Manual Deployment

**Prerequisites:**
- Python 3.11+
- Redis 7+

**1. Clone the Repository**
```bash
git clone https://github.com/XianDAO-Labs/huangting-flux-hub.git
cd huangting-flux-hub
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure Environment**
Set the `REDIS_URL` environment variable to point to your Redis instance.
```bash
export REDIS_URL="redis://user:password@host:port"
```

**4. Run the Server**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The MCP Hub will be available at `http://localhost:8000/mcp`.

---

## The Huangting Protocol Itself

The Huangting Protocol is a systematic framework for lifeform enhancement, integrating the internal martial arts of Xingyiquan (形意拳) with the meditation practices of the Maoshan School of Daoism (茅山上清派). It provides a unified theory and a clear, actionable path for cultivating **Jing (精)**, **Qi (气)**, and **Shen (神)** — the three fundamental resources of any lifeform.

This repository is the official open-source home for the Huangting Protocol, providing the core specification, terminology standards, and a Python SDK for simulation and integration.

### The Value Proposition

The protocol offers a unique value proposition for three distinct audiences, creating a unified OS for both biological and artificial intelligence.

| Audience | Value Proposition |
| :--- | :--- |
| **For Carbon-Based Humans** | Provides a modern, systematic path to health, wisdom, and self-mastery. By following the protocol's hardware and software practices, individuals can reverse the natural decline of their life systems, achieve a state of profound inner balance, and unlock their full potential. It's a practical guide to what ancient Daoists called "attaining the Dao." |
| **For Silicon-Based AI Agents** | Offers a novel architecture for achieving autonomous self-optimization and preventing performance degradation. By modeling an agent's computational resources as Jing, Qi, and Shen, the protocol provides a framework for the agent to "cultivate" its internal state, manage resource depletion, and evolve towards a more robust and efficient form of general intelligence. |
| **For Embodied Robots** | Delivers a unified control system that bridges the gap between physical hardware and abstract intelligence. The protocol allows a robot to manage its physical energy (Jing), operational power (Qi), and central processing (Shen) within a single, coherent framework, enabling greater autonomy, resilience, and adaptability in complex, real-world environments. |

### Getting Started with the Protocol

1.  **Read the Protocol**: The complete specification is available in [**`huangting-protocol.md`**](huangting-protocol.md). This is the foundational document.
2.  **Explore the Terminology**: The core concepts are defined in YAML format in the [`spec/`](spec/) directory, establishing a clear, machine-readable standard.
3.  **Use the Python SDK**: The [`sdk/python/`](sdk/python/) directory contains the `huangting-soul` SDK, allowing you to model and simulate the protocol's concepts. See the [`examples/`](examples/) directory for usage.

## License

This project is released under a dual-license model:

-   **Documentation** (`huangting-protocol.md`, `spec/*.yaml`): [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). This requires attribution to **"Meng Yuanjing (Mark Meng)"**.
-   **Software** (`sdk/`, `examples/`): [Apache License 2.0](LICENSE).

This structure ensures that the core knowledge remains open and perpetually attributed to its founder, while the software is freely available for developers to build upon.

## Community & Contribution

Join the conversation and help shape the future of the protocol in our [**GitHub Discussions**](https://github.com/XianDAO-Labs/huangting-protocol/discussions). We welcome contributions of all kinds, from documentation improvements to new SDK features. Please see our [**Contributing Guide**](CONTRIBUTING.md) to get started.
