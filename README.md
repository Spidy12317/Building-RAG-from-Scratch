# Building RAG from Scratch 

A comprehensive, hands-on guide to understanding Retrieval-Augmented Generation (RAG) systems from the ground up. This repository breaks down each component of the RAG pipeline with interactive notebooks and practical assignments focused on building intuition, not just copying code.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

---

## 📖 What is RAG?

**Retrieval-Augmented Generation (RAG)** is a technique that enhances Large Language Models (LLMs) by providing them with relevant, up-to-date information retrieved from external knowledge sources.

### The Problem RAG Solves

LLMs have inherent limitations:
- **Knowledge Cutoff**: They only know information up to their training date
- **Hallucinations**: They can generate plausible but incorrect information
- **No Access to Private Data**: They can't access your documents, databases, or company-specific information

### How RAG Works

```
┌─────────────────────────────────────────────────────────────┐
│                         RAG Pipeline                        │
└─────────────────────────────────────────────────────────────┘

User Query
    │
    ├─→ 1. Embed Query (convert to vector)
    │
    ├─→ 2. Search Vector Database (find similar documents)
    │
    ├─→ 3. Retrieve Top-K Documents (most relevant)
    │
    ├─→ 4. Construct Context (combine query + documents)
    │
    └─→ 5. Generate Response (LLM with context)
         │
         └─→ Final Answer
```

**Example:**

**Without RAG:**
```
User: "What is my favorite drink?"
LLM:  "I'm not sure. I don't have access to your personal preferences..."
```

**With RAG:**
```
User: "What is my favorite drink?"
RAG:  [Retrieves personal notes from your database]
LLM:  "Based on your notes, your favorite drink is: L.I.I.T (Long Island Iced Tea)."
```

---

## 🎯 What You'll Learn

This series focuses on **understanding, not just implementing**. By the end, you'll have:

✅ Deep intuition for how each RAG component works  
✅ Understanding of fundamental limitations and tradeoffs  
✅ Hands-on experience implementing core concepts from scratch  
✅ Knowledge of when RAG works (and when it doesn't)  

---

## 📚 Series Structure

This repository is organized into **6 progressive parts**. Each part includes:
- 📓 Interactive Jupyter notebook with detailed explanations
- 🎯 Hands-on assignments to build intuition
- 🐍 Python service implementations
- 🧪 Working examples and test cases

---

### Part 1: Understanding Embeddings ✅
**Status**: 🟢 Available Now

Start here to build intuition for embeddings and similarity in RAG. The notebook will guide you through:
- What embeddings are
- Why we use them in Retrieval-Augmented Generation
- Hands-on with vector similarity

Focus on experimenting and connecting the concepts as you work through the notebook. No prior knowledge of embeddings is needed!


```
services/1_embedding_services/
├── assignment.ipynb          # Interactive notebook (start here!)
├── embedding_services.py     # Service implementation template
└── __init__.py              # Module initialization

``` 
📓 **[Start Part 1](services/1_embedding_services/assignment.ipynb)**

---

## Getting Started

### Prerequisites

- Python 3.11
- Basic understanding of Python
- Familiarity with Jupyter notebooks

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Spidy12317/Building-RAG-from-Scratch.git
cd Building-RAG-from-Scratch
```

**2. Create a virtual environment**
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# OR using conda
conda create -n rag python=3.11
conda activate rag
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```
---

## 🏗️ Repository Structure

```
rag-from-scratch/
│
├── core/                           # Core utilities
│   ├── config/                     # Configuration management
│   ├── constant/                   # Project constants
│   └── error/                      # Custom error handlers
│
├── data/                           # Data and assets
│   └── photos/                     # Images and diagrams
│
├── services/                       # Main implementation
│   └── 1_embedding_services/       # Part 1: Embeddings
│       ├── assignment.ipynb
│       ├── embedding_services.py
│       └── __init__.py
│
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 🛠️ Technologies Used

**Core Libraries:**
- [sentence-transformers](https://www.sbert.net/) - State-of-the-art embeddings
- [NumPy](https://numpy.org/) - Numerical computing
- [Matplotlib](https://matplotlib.org/) - Visualization

---
## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use this code for learning
- ✅ Modify and adapt for your projects
- ✅ Use in commercial applications
- ✅ Share and distribute

Attribution appreciated but not required!

---
## 🗺️ Roadmap

**Current Status:**
- [x] Part 1: Understanding Embeddings

**Coming Soon:**
- [ ] Part 2: Building the Retriever
- [ ] Part 3: Generation Setup
- [ ] Part 4: Data Ingestion
- [ ] Part 5: Full RAG Pipeline
- [ ] Part 6: Testing the Limits

---

**Building RAG systems, one component at a time.*