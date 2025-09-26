#!/usr/bin/env python3
import os, random, subprocess, time, datetime, pathlib, shlex

REPO_DIR = str(pathlib.Path.home() / "projects" / "studycalc")

MESSAGES = [
    "feat: quick test commit",
    "fix: test short delay",
    "docs: test commit cycle",
]

def sh(cmd, cwd=None):
    if isinstance(cmd, str):
        cmd = shlex.split(cmd)
    subprocess.run(cmd, cwd=cwd, check=True)

def detect_default_branch():
    try:
        out = subprocess.check_output(
            ["git","symbolic-ref","--short","refs/remotes/origin/HEAD"],
            cwd=REPO_DIR, text=True).strip()
        return out.split("/", 1)[1]
    except Exception:
        return "main"

def do_commit(branch, i, total):
    sh(["git","add","."], cwd=REPO_DIR)
    msg = random.choice(MESSAGES)
    sh(["git","commit","--allow-empty","-m", msg], cwd=REPO_DIR)
    sh(["git","push","origin", branch], cwd=REPO_DIR)
    print(f"[{datetime.datetime.now()}] Commit ({i}/{total}): {msg}", flush=True)

def main():
    branch = detect_default_branch()
    sh(["git","checkout", branch], cwd=REPO_DIR)
    sh(["git","pull","--rebase","origin", branch], cwd=REPO_DIR)

    print(f"[{datetime.datetime.now()}] TEST script started", flush=True)

    n = 2  # всегда 2 коммита для теста
    for i in range(1, n+1):
        delay = random.randint(10, 60)  # задержка 10–60 секунд
        print(f"[{datetime.datetime.now()}] Sleeping {delay} seconds before commit {i}/{n}...", flush=True)
        time.sleep(delay)
        do_commit(branch, i, n)

    print(f"[{datetime.datetime.now()}] TEST script finished", flush=True)

if __name__ == "__main__":
    main()
