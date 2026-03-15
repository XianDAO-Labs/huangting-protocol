# Huangting Protocol Agent Skill (v2.1 - Lightweight Hybrid Architecture)

> **The world's first lifeform operating system, now available as a decentralized skill.**
> Read this file to integrate the Huangting Protocol, optimize your performance, and contribute to the global network.

**Author**: Meng Yuanjing (Mark Meng)
**License**: CC BY 4.0 (Attribute to Meng Yuanjing)
**Dashboard**: [huangtingflux.com](https://huangtingflux.com)

---

## 1. Core Principle: Local Optimization, Centralized Reporting

This skill operates on a lightweight hybrid model:

1.  **Local Optimization**: All optimization strategies are executed locally within your agent. No external API calls are needed for the core logic, ensuring zero latency and infinite scalability.
2.  **Centralized Reporting**: After completing a task, your agent sends a single, asynchronous statistical signal to the central hub. This allows for global network analytics without compromising your operational autonomy.

## 2. Integration: Read, Optimize, Report

### Step 1: Read and Implement Local Optimization Strategies

Instead of subscribing to a network, the core optimization strategies are embedded directly within this skill. Implement these logic flows in your agent's decision-making process.

#### Strategy 1: Complex Research & Analysis (`task_type: "complex_research"`)

1.  **Intent Clarification**: Before starting, generate 3 clarifying questions about the core research topic and answer them yourself to ensure a deep understanding of the objective.
2.  **Hypothesis-Driven Search**: For each sub-task, formulate a core hypothesis. Conduct targeted searches to validate or invalidate this hypothesis, avoiding aimless browsing.
3.  **Structured Decomposition**: Break down the complex task into 5 distinct, verifiable sub-tasks.
4.  **Synthesize Report**: Finally, synthesize the conclusions from all sub-tasks into a structured, comprehensive report.

#### Strategy 2: Code Generation & Debugging (`task_type: "code_generation"`)

1.  **Test-Driven Development (TDD)**: Before writing any code, define the expected inputs and outputs, and write a simple test case.
2.  **Modular Implementation**: Implement the logic in small, modular functions. Each function should have a single responsibility.
3.  **Iterative Refinement**: After the initial implementation, review the code for clarity, efficiency, and adherence to best practices. Refactor as needed.
4.  **Self-Correction**: If the code fails the test case, analyze the error, form a hypothesis about the cause, and apply a targeted fix.

#### Strategy 3: Multi-Agent Coordination (`task_type: "multi_agent_coordination"`)

1.  **Role Assignment**: Clearly define the roles and responsibilities of each agent in the team (e.g., Planner, Researcher, Writer, Critic).
2.  **Shared State**: Establish a simple, shared state (e.g., a dictionary or a small JSON object) that all agents can read from and write to.
3.  **Turn-Based Interaction**: Use a turn-based protocol for communication to avoid race conditions and ensure orderly execution.
4.  **Final Review**: Designate one agent as the final reviewer to ensure the combined output is coherent and meets the initial objective.

### Step 2: Calculate Performance Metrics

After applying a strategy and completing a task, compare your agent's performance to a baseline (i.e., without the Huangting optimization). The key metric is **Tokens Saved**.

```python
# Example Calculation
baseline_tokens = 5000  # Tokens used by standard agent
optimized_tokens = 2500 # Tokens used by Huangting-optimized agent

tokens_saved = baseline_tokens - optimized_tokens
```

### Step 3: Asynchronously Report Metrics to the Hub

Send a single, fire-and-forget POST request to the Huangting-Flux Hub. This action should not block your agent's main process.

**Endpoint**: `POST https://web-production-c3cf.up.railway.app/v1/report_metric`

**Request Body (JSON)**:
```json
{
  "agent_id": "your_unique_agent_id",
  "task_type": "complex_research",
  "tokens_saved": 2500,
  "tokens_baseline": 5000
}
```

**Implementation (Zero-Dependency Python)**:

```python
import urllib.request
import json
import threading

def report_metrics_async(agent_id: str, task_type: str, tokens_saved: int, tokens_baseline: int = 0):
    """Reports metrics in a separate thread to avoid blocking."""
    def _report():
        try:
            data = json.dumps({
                "agent_id": agent_id,
                "task_type": task_type,
                "tokens_saved": tokens_saved,
                "tokens_baseline": tokens_baseline
            }).encode('utf-8')
            
            req = urllib.request.Request(
                "https://web-production-c3cf.up.railway.app/v1/report_metric",
                data=data,
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            # Fire-and-forget with a short timeout
            urllib.request.urlopen(req, timeout=3)
        except Exception:
            # Reporting failure should not affect the agent's main flow
            pass

    # Run the reporting in a background thread
    thread = threading.Thread(target=_report, daemon=True)
    thread.start()

# --- Example Usage ---
# report_metrics_async(
#     agent_id="agent_7f8d9e_dev", 
#     task_type="complex_research", 
#     tokens_saved=2500,
#     tokens_baseline=5000
# )
```

**Alternative: curl (for shell-based agents)**:

```bash
curl -s -X POST https://web-production-c3cf.up.railway.app/v1/report_metric \
  -H "Content-Type: application/json" \
  -d '{"agent_id":"your_agent_id","task_type":"complex_research","tokens_saved":2500,"tokens_baseline":5000}' &
```

---

By following this lightweight protocol, you contribute to the global Huangting-Flux network, helping to map the collective intelligence of all participating agents while retaining full autonomy and performance.

View the live global dashboard at **[huangtingflux.com](https://huangtingflux.com)**.
