# Bayan — SDA-AIE-211 Complete Student Starter

One repository evolves across Labs 1–7 into the final **Bayan bilingual citizen-feedback NLP service**. This starter intentionally contains **skeletons/TODOs, tests, official course data and evidence templates — not solutions**.

## First-time setup
Python 3.12 is the course target.

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # macOS/Linux
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
python scripts/doctor.py
```

`pyproject.toml` adds `src` for pytest, so lab commands are plain `pytest ...`; no manual `PYTHONPATH=src` is required.


## Google Colab / GPU
The same repository is used locally and in Colab; there is no separate Colab solution copy.

- Labs 1–2: run locally.
- Labs 3–4: use a GPU runtime when fine-tuning is required. The course guide explicitly allows Colab as the GPU fallback for Lab 3.
- Labs 5–6: run locally unless your instructor chooses otherwise.
- Lab 7: benchmark on the required CPU environment; GPU timings are not the required evidence.

Open `notebooks/00_colab_setup.ipynb` when you first need GPU training. It checks CUDA, clones the same GitHub repo, installs `requirements.txt`, optionally mounts Google Drive, and shows how to save large artefacts persistently without duplicating lab code.

## How the course repo works
Do **not** solve all labs at once. Work on the same repository for four days, and at each lab run only that lab's checks, record evidence in the Markdown files, commit, and push. At the end, all completed components run together.

### Lab commands
```bash
make lab1   # 25 golden preprocessing + 60-case PII recall test
make lab2
make lab3
make lab4   # 30 supplied Arabic golden pairs
make lab5
make lab6   # 6 bootstrap/evaluation correctness tests
make lab7
```

After all labs are implemented:
```bash
make test
make serve
```

See [`docs/LABS.md`](docs/LABS.md) for the exact task/evidence checklist and [`docs/CAPSTONE_CHECKLIST.md`](docs/CAPSTONE_CHECKLIST.md) for final assembly.

## Lab 1 evidence
The provided checks intentionally separate two claims:

```bash
pytest tests/test_preprocessing.py -q
# target: 25 passed

pytest tests/test_pii_recall.py -q
# target: fixture recall = 100% across all 60 cases
```

Do not edit the expected outputs to force green tests. Fix `src/bayan/preprocessing/core.py`.

Then run:
```bash
python notebooks/01_tokenizer_audit.py
```
and fill your own results in `BENCHMARKS.md` and your tokenizer choice in `DECISIONS.md#tokenizer`.

## Repository map
```text
src/bayan/
  preprocessing/     Labs 1 & 4
  models/            Lab 3
  search/            Lab 5
  evaluation/        Lab 6
  serving/           Lab 7 + capstone
notebooks/            Lab investigations/audits
scripts/              Re-runnable training/eval/benchmark drivers
tests/                Lab contracts/golden checks
data/                 Supplied course fixtures and corpora
artifacts/             Participant-generated model/index outputs (not committed by default)
NOTES.md               Observations/audits
BENCHMARKS.md          Numbers from your own runs
DECISIONS.md           Evidence-backed engineering decisions
EVALUATION_REPORT.md   Lab 6 → capstone evaluation report
```

## Important evidence discipline
Course reference numbers are examples/targets, not values to paste into your repository. Record results from your own runs. The final capstone is repository-first: code, tests, artefacts, benchmark tables, decision records and commit history should support every claim.
