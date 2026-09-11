## Bayan | بيان
---

# SDA-AIE-211 Bayan Course

This repository contains my solutions and implementations for the SDAIA Academy Bayan Course labs. The project includes data preprocessing, dataset preparation, evaluation scripts, and experiments completed throughout the course.

The work focuses on applying practical AI and machine learning concepts while following software engineering best practices such as version control, documentation, and reproducible experimentation.

Course materials and resources are provided by SDAIA Academy:
https://github.com/SDAIAAcademy






# 🚀 What are we building?

**Bayan (بيان)** is a bilingual citizen-feedback intelligence service for Arabic and English text.

By the end of the course, this repository should be able to:

- 🧹 preprocess Arabic + English text consistently
- 🔐 mask PII before model use
- 🧠 classify feedback topics/sentiment
- 🏷️ extract entities with NER
- ❓ handle extractive QA with honest no-answer behaviour
- 🔎 retrieve similar historical cases using semantic search
- 📊 evaluate models with slices, confidence intervals, and behavioural tests
- ⚡ optimise inference with ONNX + INT8
- 🌐 serve the final pipeline through FastAPI

```text
Raw Citizen Feedback
        ↓
Versioned Preprocessing
        ↓
Topic Classification / NER / QA
        ↓
Arabic-aware Model Decisions
        ↓
Semantic Search → FAISS → Re-ranking
        ↓
Evaluation + Model Cards + Benchmarks
        ↓
ONNX / INT8 Optimisation
        ↓
FastAPI Bayan Service
```

---

# 🗺️ Project Roadmap

| Day | Lab | Main outcome |
|---|---|---|
|  Bilingual preprocessing + tokenizer decision |
|  Transformer attention from scratch + diagnostics |
| Topic classifier that beats TF-IDF baseline |
| NER + extractive QA |
| Arabic normalisation + dialect-aware model |
| Bilingual semantic search |
| Honest evaluation report + model cards |
| ONNX / INT8 optimisation + serving |
| Capstone | Integrate everything into one Bayan service |

> **Important:** Keep yesterday's work. Every lab builds evidence and components that later labs reuse.

---

# 📁 Repository Structure

```text
SDA-AIE-211-Bayan/
│
├── src/bayan/
│   ├── preprocessing/
│   │   ├── core.py             # Lab 1
│   │   ├── segmentation.py     # Lab 1
│   │   └── arabic.py           # Lab 4
│   ├── attention.py            # Lab 2
│   ├── models/
│   │   ├── data.py             # Lab 3A
│   │   ├── ner.py              # Lab 3B
│   │   └── qa.py               # Lab 3B
│   ├── search/
│   │   ├── index.py            # Lab 5
│   │   └── service.py          # Lab 5
│   ├── evaluation/
│   │   ├── bootstrap.py        # Lab 6
│   │   ├── slices.py           # Lab 6
│   │   └── behavioural.py      # Lab 6
│   └── serving/
│       ├── api.py              # Lab 7 + Capstone
│       └── canaries.py         # Lab 7 + Capstone
│
├── notebooks/
│   ├── 00_colab_setup.ipynb
│   ├── 01_tokenizer_audit.py   # Lab 1
│   ├── 02_transformer_anatomy.py # Lab 2
│   └── 05_retrieval_eval.py    # Lab 5
│
├── scripts/
│   ├── doctor.py
│   ├── parameter_audit.py      # Lab 2
│   ├── tfidf_baseline.py       # Lab 3A
│   ├── train_classifier.py     # Lab 3A
│   ├── train_ner.py            # Lab 3B
│   ├── qa_smoke.py             # Lab 3B
│   ├── dialect_audit.py        # Lab 4
│   ├── arabic_bakeoff.py       # Lab 4
│   ├── evaluation_report.py    # Lab 6
│   ├── benchmark_inference.py  # Lab 7
│   ├── export_onnx.py          # Lab 7
│   └── load_test.sh            # Lab 7
│
├── tests/
├── data/
├── artifacts/
├── templates/
│   └── model_card.md.j2
│
├── NOTES.md
├── BENCHMARKS.md
├── DECISIONS.md
├── EVALUATION_REPORT.md
├── requirements.txt
├── pyproject.toml
└── Makefile
```

---




Build it one checkpoint at a time. Measure everything that matters. Keep the evidence. 🚀
