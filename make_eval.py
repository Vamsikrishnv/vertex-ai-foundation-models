import json
import random

TRAIN_FILE = "tune_data_stack_overflow_python_qa.jsonl"   # must exist
EVAL_FILE  = "tune_eval_stack_overflow_python_qa.jsonl"   # will be created

EVAL_RATIO = 0.10  # 10% eval

with open(TRAIN_FILE, "r", encoding="utf-8") as f:
    lines = [line for line in f if line.strip()]

random.seed(42)
random.shuffle(lines)

n_eval = max(1, int(len(lines) * EVAL_RATIO))
eval_lines = lines[:n_eval]
train_lines = lines[n_eval:]

with open(TRAIN_FILE, "w", encoding="utf-8") as f:
    f.writelines(train_lines)

with open(EVAL_FILE, "w", encoding="utf-8") as f:
    f.writelines(eval_lines)

print("Done.")
print("Train lines:", len(train_lines))
print("Eval lines :", len(eval_lines))
print("Eval file  :", EVAL_FILE)
