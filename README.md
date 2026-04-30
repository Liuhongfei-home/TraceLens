# TraceLens

一个面向分布式 Agent 系统的轻量级故障定位与根因分析（RCA）MVP，通过 Trace 聚合日志、自动识别异常链路并生成修复建议。

---

## 📌 项目简介

在分布式 Agent 系统中，问题通常具有以下特点：

- 多节点协作，问题难复现
- 调用链复杂，错误传播路径不清晰
- 日志分散，缺乏统一分析
- 故障排查依赖人工，效率低

TraceLens 提供了一套轻量级解决方案：

👉 日志采集  
👉 调用链还原（Trace）  
👉 Root Cause 分析  
👉 修复建议生成  

---

## 🧠 核心功能

### 1. 分布式日志采集
Agent 节点在执行任务时生成 `trace_id`，并将日志统一上报到 Collector。

### 2. 调用链还原（Trace）
基于 `trace_id` 聚合日志，还原完整请求路径。

### 3. Root Cause 分析
统计调用链中的异常类型，自动识别主要错误原因。

### 4. 修复建议生成
根据错误类型输出对应的修复建议（规则驱动）。

---

## 🏗️ 系统架构

Agent → Collector → Analyzer → Root Cause → Fix Suggestion

## 📂 项目结构


```
agent_debug_mvp/
 │
 ├── agent.py        # 模拟分布式 Agent
 ├── collector.py    # 日志收集服务
 ├── analyzer.py     # 调用链分析
 ├── fixer.py        # 修复建议生成
 ├── requirements.txt
 └── README.md

```
---

## 🚀 快速开始

### 1️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

------

### 2️⃣ 启动日志服务

```
python collector.py
```

------

### 3️⃣ 运行 Agent（可启动多个模拟分布式）

```
python agent.py
```

------

### 4️⃣ 分析日志

```
python analyzer.py
```

------

### 5️⃣ 输出修复建议

```
python fixer.py
```

------

## 📊 示例输出

```
==== BUG REPORT ====
Trace ID: xxx
Error Count: 2
Affected Agents: ['agent-1']
Root Cause: TimeoutError
Fix: 增加重试机制 + 检查网络延迟 + 调整超时配置
```

------

## 💡 设计亮点

- 基于 Trace 的调用链分析，而非单点日志
- 支持多 Agent 关联问题定位
- 自动 Root Cause 推断（规则驱动）
- 从日志采集到修复建议的完整闭环
- 结构简单，易扩展为生产系统

------

## ⚠️ 当前限制（MVP）

- 日志存储为内存（无持久化）
- 无高可用设计
- Root Cause 分析较简单
- 无实时流处理能力
- 无可视化界面

------

## 🔧 后续优化方向

- 引入消息队列（Kafka）实现解耦
- 接入分布式追踪（OpenTelemetry）
- 使用 Elasticsearch 进行日志存储与检索
- 引入 Prometheus + Grafana 做监控
- 使用 AI 提升 Root Cause 分析能力

------

## 🧠 总结

TraceLens 是一个面向分布式 Agent 系统的轻量级故障定位工具，通过 Trace 聚合日志并自动分析异常，为构建生产级可观测系统提供基础。
