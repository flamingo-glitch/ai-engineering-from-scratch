# anatomy.md — Every Command of Lessons 01–06, Dissected

> The twin of `glossary.md` (that file = the WORDS; this file = the COMMANDS).
> Golden law: **A is for running. B is for becoming an engineer.**
> Goal: you can rebuild every command from memory AND explain every piece — asleep. 😴

---

## 0. HOW TO STUDY THIS FILE (the method that makes it stick)

1. Read a lesson's section: see A) the command, B) its anatomy.
2. **Cover B with your hand.** Say out loud what each piece does.
3. Get one wrong? Not shame — that's tomorrow's flashcard. Repeat just that one.
4. **The sleep test:** you can TYPE the command from memory AND explain
   each piece in one breath. Only then does a section get your ✅.
5. Do the self-exam at the bottom (§9) — write answers on paper FIRST,
   then check. Paper answers don't lie; glancing eyes do. 👀❌
6. Pace: ONE lesson section per sitting (10–20 min). Six days = whole book.

**The 6 glyphs that unlock half of every command** (see `glossary.md` §8½ for the full zoo):

| Glyph | Core meaning |
|---|---|
| (space) | separates the pieces of a command — one space, one boundary |
| `.` | hidden file prefix · current folder · (in Python) "reach inside" |
| `/` | folder separator — walking a path corridor by corridor |
| `" "` | everything inside = ONE text chunk |
| `>` / `>>` | write into a file (OVERWRITE) / append at the END |
| `&&` | "and then — ONLY IF the previous succeeded" |

---

## 1. LESSON 01 — the machine, Python, the sandbox

### 1.1 Ubuntu & the ground floor (🗣️ these were browser/install choices)

**`wsl --install -d Ubuntu-24.04`** *(typed in a Windows window, not Linux)*

| Piece | Meaning |
|---|---|
| `wsl` | Windows Subsystem for Linux — Windows' built-in "run Linux inside" feature |
| `--install` | double-dash flag: "perform the INSTALL action" (two dashes = long option name) |
| `-d` | short flag: "the next word = which distribution (flavour) of Linux" |
| `Ubuntu-24.04` | the flavour: Ubuntu, year 2024 release, LTS (Long-Term Support = maintained 5 years) |

**`sudo apt update`**

| Piece | Meaning |
|---|---|
| `sudo` | "superuser do" — run as administrator (asks password, shows NOTHING while typing — Linux is shy with passwords) |
| `apt` | Ubuntu's package manager — the phone-book of installable programs |
| `update` | refresh the phone-book (download the newest LIST of available programs — installs nothing yet) |

### 1.2 Build uv (the turbo tool) 💻

### A) 🟢 paste-as-is
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `curl` | command-line web client: fetch a URL (a librarian that fetches pages) |
| `-L` | follow redirects (if the address moved, keep following) |
| `-s` | silent (no progress noise) |
| `-S` | BUT still show errors if any happen (s-with-capital = the quiet worker that shouts when hurt) |
| `-f` | fail on a bad HTTP answer instead of "successfully" downloading an error page |
| `\|` | pipe: hand everything `curl` fetched to the next command |
| `sh` | the shell — it runs the fetched text (the official installer script) |

**Trust protocol we honor: we only pipe-to-sh scripts from addresses we trust, after checking the source. Same habit as env_setup.sh later.**

### 1.3 The Python of the sandbox 💻

### A) 🟢 paste-as-is
```bash
uv python install 3.12
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `uv` | our turbo tool (also installs/whole Pythons, not just packages) |
| `python` | subcommand: manage interpreters |
| `install` | verb |
| `3.12` | WHICH version (a stable, universally-compatible release; 3 digits = major.minor patch-ish lineage) |

### 1.4 Build the sandbox 💻

### A) 🟢 paste-as-is
```bash
uv venv
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `uv` | the tool |
| `venv` | subcommand: "virtual environment" — build a private sandbox folder `.venv` here (leading dot = hidden) |

### 1.5 Wear the badge (the morning spell) 💻

### A) 🟢 paste-as-is
```bash
source .venv/bin/activate
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `source` | run a script INSIDE the current shell (a copy would die with it — sourcing is what makes the badge LAST) |
| `.venv` | the sandbox folder (hidden) |
| `bin` | binaries — where its executable programs live |
| `activate` | the switcher: makes `python` and installed packages point at the sandbox |

**Reward:** the badge `(ai-engineering-from-scratch)` on the prompt = "you are inside the sandbox NOW." Wears off on every new window (session-scoped); files stay (disk-scoped).

### 1.6 Install the first libraries 💻

### A) 🟢 paste-as-is
```bash
uv pip install numpy matplotlib jupyter
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `uv` | tool |
| `pip` | Python's classic installer language (uv speaks it, way faster) |
| `install` | verb: fetch and set up |
| `numpy` | fast math on grids of numbers |
| `matplotlib` | graph/chart drawing |
| `jupyter` | the lab-notebook family |
| (many names OK) | installers accept a list — one command, many guests |

---

## 2. LESSON 02 — git & GitHub (the time machine)

### 2.1 Tell git who you are 💻

### A) 🟢 paste-as-is (shape — YOUR name/email)
```bash
git config --global user.name "flamingo-glitch"
git config --global user.email "eduardmozes2002@gmail.com"
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `git` | the time machine itself |
| `config` | settings workshop |
| `--global` | these settings apply to ALL your repos on this machine (one dash = short flags, two = words) |
| `user.name` | WHICH setting (dot = field inside category) |
| `"..."` | the value — quotes make spaces-and-symbols one chunk |
| (both lines) | git needs to know who signs each snapshot (commit captions borrow this) |

### 2.2 bring a repo to disk 💻

### A) 🟢 paste-as-is (shape)
```bash
git clone https://github.com/flamingo-glitch/ai-engineering-from-scratch.git
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `clone` | download the repo + its ENTIRE history to disk (a photo album with all pages) |
| (the URL) | whose repo, which name — the `.git` =
 "this URL speaks git protocol" |

*(the FORK (GitHub copies rohitg00's repo into YOUR account) is browser-side — no terminal: 🗣️)*

### 2.3 remember the original 💻

### A) 🟢 paste-as-is (shape)
```bash
git remote add upstream https://github.com/rohitg00/ai-engineering-from-scratch.git
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `remote` | manage remote (far-away) copies of the repo |
| `add` | remember a new one |
| `upstream` | its nickname (upstream = upstream river: the ORIGINAL you forked FROM) |
| (yours stays `origin`) | origin = "where MY pushes go" = your fork = your house |

### 2.4 your own lane 💻

### A) 🟢 paste-as-is
```bash
git checkout -b my-progress
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `checkout` | move to (a branch/snapshot) |
| `-b` | "create a NEW branch first" |
| `my-progress` | its name — a parallel lane where your work lives safely |

### 2.5 THE CORE LOOP (bonus: glossary §8½ has its full table too)

### A) 🟢 paste-as-is (shape)
```bash
git status
git add FILE
git commit -m "CAPTION"
git push
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `status` | "what changed around here?" (red = seen/green = staged) |
| `add` | stage: put on the photography desk — the NEXT snapshot includes it |
| `commit` | glue snapshot into history with caption |
| `-m` | flag: message/caption follows |
| `push` | upload history to origin (your GitHub fork) |

### 2.6 the museum's index 💻

### A) 🟢 paste-as-is
```bash
git log --oneline -5
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `log` | show the timeline |
| `--oneline` | compact mode: one line per snapshot (short code + caption) |
| `-5` | only the 5 newest |

### 2.7 the key-hygiene drill 💻

### A) 🟢 paste-as-is
```bash
echo ".env" >> .gitignore
git check-ignore -v .env
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `echo` | print text |
| `".env"` | the rule text (quotes = chunk) |
| `>>` | APPEND to the no-photo list (a lone `>` would overwrite — danger!) |
| `.gitignore` | git's "never track me" list |
| `check-ignore` | ask: "is this name ignored?" |
| `-v` | verbose: show WHICH RULE protects it (print nothing = NOT protected — the hole-finder!) |

---

## 3. LESSON 03 — GPU & CUDA (the graphics card becomes a math device)

**`nvidia-smi`** 💻 🟢

| Piece | Meaning |
|---|---|
| `nvidia` | the GPU maker |
| `-smi` | System Management Interface — the dashboard: driver version, VRAM usage, temperature |
| (no args) | just show the panel |

**`python gpu_check.py`** 💻 🟢

| Piece | Meaning |
|---|---|
| `python` | run file with Python |
| `gpu_check.py` | the script (`.py` = Python file) — run top to bottom like a script SHOULD (no notebook scattering) |

**PyTorch + CUDA build** (`uv pip install torch`, our build speaks CUDA 12.4):

| Piece | Meaning |
|---|---|
| CUDA | NVIDIA's language that lets programs talk to the GPU |
| `cu124` | "this build speaks CUDA 12.4" — must match your driver's dialect (lesson's mismatch trap) |
| check ritual: | `python -c "import torch; print(torch.cuda.is_available())"` → `True` |

---

## 4. LESSON 04 — APIs & keys (talk to a server)

### 4.1 the lockbox loading ritual 💻

### A) 🟢 paste-as-is
```bash
set -a && source .env && set +a
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `set` | change shell options |
| `-a` | option `a` = "allexport": variables defined next become visible to child programs |
| `&&` | chain, only-if-worked |
| `source .env` | read the hidden key file INTO this session |
| `set +a` | `+` = turn OFF the option again (clean up) |

**Reward:** the key is a SESSION sticky-note (`echo`-less, no display). Dies with window; lives in `.env` on disk.

### 4.2 the phone-call script 💻

**`python first_api_call.py`** — inside it (concept anatomy):

| Piece | Meaning |
|---|---|
| `base_url = "https://openrouter.ai/api/v1"` | WHICH provider's restaurant window |
| `model = "...:free"` | WHICH brain on the menu (`:free` = the free-tier ticket) |
| `max_tokens` | answer-length budget |
| the result `.choices[0]...` | the reply's text inside the JSON envelope |

**The whole call in one breath:** login-sticky + JSON question → server thinks (tokens burn) → JSON answer + usage stats.

---

## 5. LESSON 05 — the Jupyter lab (browser + cells + kernel)

### 5.1 install & launch 💻

### A) 🟢 paste-as-is
```bash
uv pip install jupyterlab
jupyter lab
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| (first line) | install package `jupyterlab` (lowercase, no spaces — package names) |
| `jupyter lab` | boot the lab: terminal shows "Jupyter Server is running…"; browser opens at `localhost:8888` |
| `localhost` | "this very machine" (a website living on YOUR computer) |
| `:8888` | the port — numbered door Jupyter serves through |

### 5.2 the page mechanics 🖱️/⌨️ (no anatomy — but the reflexes)

| Action | Effect |
|---|---|
| **➕** | new empty box |
| **▷** | run the selected box (mouse version of the drumbeat) |
| **Shift + Enter** | run + select next (the drumbeat 🥁) |
| dropdown `Code`/`Markdown` | box type: DOES / EXPLAINS |
| 💾 | save to disk |
| `Kernel → Restart Kernel and Run All Cells` | the cure: wipe brain memory (RAM), replay page top-to-bottom |
| `In [n]` | the honest run-counter |

### 5.3 the cells' code dissected (Python species) 📓

### A) 🟢 paste into a notebook box
```python
import numpy as np

a = np.array([1, 2, 3])
np.dot(a, a)
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `import numpy as np` | bring the library in, and give it the NICKNAME `np` (as = rename) |
| `np.array([1, 2, 3])` | `.` = reach inside numpy → `array` = build a grid from the list |
| `np.dot(a, a)` | the dot product: multiply matching, add them (2+4+9=wait, 1+4+9=14 🙂) |
| (last line bare) | notebooks auto-display the last line — that's why `14` showed with no `print` |

### A) 🟢 (plot cell)
```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.show()
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `import matplotlib.pyplot as plt` | bring the DRAWING module specifically, nickname `plt` |
| `plt.plot(x, y)` | dots at each (x, y), straight segments between |
| `plt.show()` | paint it under the box |

### A) 🟢 (stopwatch cell)
```python
%timeit [n * n for n in range(1_000_000)]
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `%` | magic-command prefix (an order for the NOTEBOOK, not Python) |
| `timeit` | the honest stopwatch: many runs, averaged, ± wobble reported |
| `[n * n for n in range(1_000_000)]` | list comprehension: build a list by looping INSIDE the brackets |

### 5.4 the trap we caught (story-form anatomy)

```python
mystery = 5        # scene 1: brain memorizes 5
mystery * 2        # scene 2: asks brain → 10
mystery = 100      # scene 3: rewires memory
# re-run scene 2 AFTER scene 3 → 200 (click-order trap!)
```
| Conclusion | |
|---|---|
| page-order | behaves like a script ✅ |
| click-order | remix of history ❌ |
| cure | Restart + Run All Cells |

---

## 6. LESSON 06 — environments & lockfiles (walls, cards, receipts)

### 6.1 the verification robot 💻

### A) 🟢 paste-as-is
```bash
bash phases/00-setup-and-tooling/06-python-environments/code/env_setup.sh
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `bash` | run this text file as a bash program |
| (the long path) | corridor by corridor: phases → 00-setup → lesson 06 → code → the recipe |
| `env_setup.sh` | `.sh` = shell script; we READ its insides before running (robot = stop-on-first-error type, safe) |

### 6.2 the second sandbox (isolation proof) 💻

### A) 🟢 paste-as-is
```bash
cd ~
uv venv lab-two
source lab-two/bin/activate
uv pip install "numpy==1.26.4"
python -c "import numpy; print(numpy.__version__)"
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `cd ~` | walk home (OUTSIDE the repo — room B must never pollute the museum) |
| `uv venv lab-two` | build sandbox with a NAME (badge will read `(lab-two)`) |
| `source lab-two/bin/activate` | wear THIS room's badge (badge = the sandbox you're IN, regardless of folder) |
| `"numpy==1.26.4"` | the pin: `==` = EXACTLY this version |
| `python -c "..."` | one-line Python: `-c` = code; `__version__` = library's self-declared version (dunder = double-underscores) |
| then `deactivate` + home + re-ask | `1.26.4` vs `2.5.4` = walls are REAL 🏆 |

### 6.3 the ID card 💻

### A) 🟢 paste-as-is
```bash
cat > pyproject.toml << 'EOF'
[project]
name = "demo-project"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "numpy>=1.26",
    "requests>=2.32",
]
EOF
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `cat > pyproject.toml` | cat writes (overwrites) INTO this file — the > alone means overwrite |
| `<< 'EOF'` | heredoc: "everything UNTIL a lone EOF line = the file's text" — swallows multi-line pastes, immune to the `!` landmine meanwhile |
| `[project]` | TOML section header |
| `name` / `version` | identity fields |
| `requires-python = ">=3.12"` | demands 3.12+ (`>=` = at least) |
| `dependencies = [ ... ]` | the shopping list (`>=` = minimum-version floors) |
| `EOF` | the terminator — alone on a line, ends the swallow |

### 6.4 the receipt 💻

### A) 🟢 paste-as-is
```bash
uv lock
head -40 uv.lock
```
### B) 🧠 anatomy
| Piece | Meaning |
|---|---|
| `uv lock` | resolve the WHOLE family tree (guests + luggage), write `uv.lock` with exact barcodes |
| `head -40` | first 40 lines |
| (inside) | `wheels` = ready-to-run packages per machine species (`cp312` = CPython 3.12); `sdist` = build-it-yourself source; `sha256` hash = byte-fingerprint (tamper-proofing) |

**The pair's law:** pyproject.toml = shopping list (loose floors) · uv.lock = receipt with barcodes (exact pins) · commit the RECEIPT so anyone reproduces your room. **Reproducibility.**

---

## 7. THE DAILY RITUAL (anatomy compressed — the wake-up card)

### A) 🟢 paste-as-is
```bash
cd ~/ai-engineering-from-scratch
source .venv/bin/activate
set -a && source .env && set +a    # ONLY on API-lesson days
git status && pwd
```
### B) 🧠 one-breath version
walk home (disk-scoped) → wear the badge (session-scoped) → load key stickies (session-scoped, API days only) → 10-second insurance check (branch + clean tree + right place).

**Session-scoped vs disk-scoped = the whole mental model. Badge & stickies die with the window; files, history and rooms persist. The morning ritual re-arms only the session part. 🔑**

---

## 8. THE STORY IN ONE BREATH (glue for the memory)

Open Linux → walk home → wear the badge → (load keys) → robots verify →
you build (cells, scripts, cards, receipts) → stage → glue with caption →
push to the museum → sleep well. 😴
Everything above is ONE of those verbs with its anatomy.

---

## 9. SELF-EXAM (write answers on paper first — answers in §10)

**Lesson 01**
1. What's the difference between `apt update` and `apt install`?
2. Why must `source` (not just run) the activate script?
3. The badge disappeared. Why, and what two commands fix it?

**Lesson 02**
4. `>` vs `>>` — what's the fatal difference?
5. What does `&&` guarantee?
6. Why did we create `my-progress` instead of working on main?
7. How do you ask git WHICH rule ignores a file?

**Lesson 03**
8. What does `cu124` mean in a torch version?
9. CPU vs GPU — one sentence each (genius chefs vs …)?
10. What did `python -c` let us do without files?

**Lesson 04**
11. Decode `set -a && source .env && set +a` — why the `-a`?
12. Session-scoped vs disk-scoped: where does the API key "live" while loaded?
13. Status 401 vs 429 — the restaurant story difference?

**Lesson 05**
14. Why did plain Enter "do nothing" in a notebook cell?
15. What is the kernel, and what does the top-right circle tell you?
16. Same box said 10 then 200 — which ORDER was broken and which ORDER healed it?
17. What does `%` at a line's start signal?

**Lesson 06**
18. Why did pandas bring 7 packages when we invited 2?
19. `==` vs `>=` in a shopping list — pin vs floor. Explain by example.
20. What does a wheel's `cp312` stamp guarantee?
21. Which file do you commit for others to reproduce your EXACT setup?
22. Why build `lab-two` OUTSIDE the repo folder?
23. The badge said `(ai-engineering-from-scratch)` while inside demo-project — is that broken? Explain.
24. What harms what: truth table for `>` into an existing file?

---

## 10. ANSWERS (only after paper!)

1. update = refreshes the LIST of available programs; install = actually downloads/sets one up.
2. Running it plainly would activate a THROWAWAY copy and die; `source` executes INSIDE this shell so the badge persists.
3. Session-scoped badge died with the window — `cd ~/ai-engineering-from-scratch` then `source .venv/bin/activate`.
4. `>` overwrites (destroys existing content); `>>` appends at the end. `>` on the wrong file = data murder. 💀
5. The next command runs only if the previous SUCCEEDED.
6. Main is the author's clean lane; your lane (`my-progress`) holds experiments + history without touching upstream.
7. `git check-ignore -v FILE` (prints the matching rule; silence = NOT protected).
8. "This torch build speaks CUDA 12.4" — its GPU-dialect version; must be ≤ driver's CUDA.
9. CPU: few genius chefs, versatile, one-at-a-time. GPU: thousands of line-cooks, identical simple math, massively parallel.
10. `-c` = run one text line as Python and exit — quick checks with no file.
11. `-a` = allexport: variables from the file become visible to child programs; `+a` turns it back off.
12. Session-scoped: lives in this session's memory only; disk copy sits unread in `.env`.
13. 401 = your key was refused/bad (the bouncer doesn't accept the card); 429 = right key, but the queue is full (too many requests).
14. Plain Enter = new line INSIDE the box (write more code); run = Shift+Enter / ▷.
15. Kernel = the background Python brain that runs ALL boxes; circle: white = idle, orange = busy, X'd = dead.
16. Click-order (remix) was broken; page-order (Restart + Run All Cells) healed it — counters climbed In [1], In [2]... in order again.
17. A magic command — an order for the notebook itself, not the Python language.
18. Transitive dependencies: each guest brings its own required helpers (pandas→scipy etc.) — 2 invited, 7 arrived.
19. `==` = exactly this version, forever; `>=` = at least this version (grows). Pin survives audits; floors allow drift.
20. It's pre-built FOR CPython 3.12 — your machine species; install without compiling from source.
21. The lockfile (`uv.lock`) — exact barcodes for everything, reproducible on any machine.
22. So git never sees it: the repo only holds INTENTIONAL artifacts; spare rooms stay outside the museum.
23. Not broken: the badge follows ACTIVATION, not folder location. It changes which python/uv-pip targets; `uv lock` works folder-based regardless.
24. `>` truncates (erases all previous content) then writes; `>>` preserves and appends. On a journal: `>` = history butchered. 😱

---

*BUILT Oct 24 2026 — Lessons 01–06, every command owned.*
*Companion files: `glossary.md` (the WORDS) · `lesson-log.md` (the DATES).*
*Next sections nest here as lessons land: Lesson 07 (Docker) will append its own anatomy box.* 🦉
