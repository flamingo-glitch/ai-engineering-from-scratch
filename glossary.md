# glossary.md — My Plain-English AI Engineering Dictionary

> Written for bufnita, by bufnita's tutor. Every term from Phase 0 so far,
> explained simply, with examples you can actually run.
> **Rule of this file:** no word appears that is not itself explained.
>
> **Paste-safety legend** (used in EVERY lesson chat message from now on):
> - 🟢 **PASTE EXACTLY AS-IS** — the text is a finished, runnable command. No
>   placeholders inside. Paste → Enter → expected output is stated.
> - 🟡 **COPY, BUT EDIT FIRST** — the text contains a placeholder you MUST
>   replace (like `YOUR_NAME`, `PASTE_YOUR_NEW_KEY`, `file.txt`). Typing it
>   as-is = error 400-class shame for us both 🙂
> - 🔴 **DO NOT PASTE INTO THE TERMINAL** — this block is OUTPUT or EXAMPLE
>   text, shown for reading only (like `git log` results or expected prints).
>   Pasting output text into a prompt is what caused the
>   "Enumerating: command not found" comedy 😄
> - 🗣️ **NO TERMINAL AT ALL** — browser clicks, settings pages, things to
>   read/decide (not terminal work).
>
> Why this legend exists: most beginner pain is not "wrong commands" — it's
> pasting the WRONG KIND of thing (decoration, output, templates with
> placeholders). This legend makes the risk explicit every time.
>
> **DOUBLE-ENTRY LAW** (Oct 23 2026, requested by bufnita — in force forever):
> every command from now on comes with TWO siblings:
> - **A) 🟢 paste-as-is** — the copy-paste machine. Zero edits needed.
> - **B) 🧠 anatomy** — the same command dissected: every character, every
>   symbol, every word explained so it feels like a sentence, not a spell.
> Reading B is how "typing commands I found somewhere" becomes
> "writing commands I understand".

---

## 0. The 10-second map (read this first)

Everything we built is a stack — like a house built floor by floor:

```
4. AI libraries (PyTorch, NumPy)       ← the expensive furniture upstairs
3. Languages (Python, Node.js)         ← the workers who understand your code
2. Package managers (uv, pnpm)         ← the delivery service for furniture
1. System (Ubuntu Linux, GPU drivers)  ← the ground the house stands on
```

**Golden rule of engineering: build bottom-up.** You can't put furniture
(NumPy) in a house with no floors (Linux). Every Phase-0 lesson fixes one
floor at a time.

---

## 1. The Machine (the hardware words)

### CPU (Central Processing Unit)
- **What:** the computer's main brain. 4–16 "workers" inside, each extremely
  smart, good at lots of different jobs.
- **Analogy:** a restaurant with a few genius chefs who can cook anything,
  but each dish is cooked by one chef at a time.
- **Where you met it:** the `CPU: 0.381s` number in your GPU benchmark.

### GPU (Graphics Processing Unit)
- **What:** the graphics card. Thousands of tiny "dumb" workers, all
  identical, all doing the same simple math at the same time.
- **Analogy:** instead of 4 genius chefs, you have 5000 identical line-cooks.
  If you need to chop 5000 identical carrots — the line-cooks win massively.
- **Why AI loves it:** AI math is *billions of identical* multiplications.
  Genius chefs choke on repetition. Line-cooks thrive on it.
- **Speedup myth-buster:** we measured only 2–3× on a single small matrix,
  because a laptop RTX 3050 is modest and one benchmark is not real training.
  Real Phase-4 training loops will show the big numbers.

### NVIDIA
- The company that makes most of the world's AI-capable GPUs.

### RTX 3050
- The exact model of YOUR GPU. 6 GB of memory, laptop edition (limited by
  cooling/power, but a real AI card).
- **GB** (gigabyte) ≈ 1 billion bytes of storage.

### RAM vs VRAM
- **RAM** (Random Access Memory) = the computer's big working desk.
- **VRAM** (Video RAM) = the GPU's own PRIVATE desk. Separate from RAM. The
  size limit for models you can FIT.
- **Rule of thumb from the lesson:** each fp16 number needs 2 bytes, so
  6 GB VRAM ≈ up to ~3 billion parameters (theory) ≈ 1–1.5B (practice,
  because activations eat memory too).

### Parameters
- **What:** the individual "learned" numbers inside an AI model. A model with
  7,000,000,000 of them is called a "7B" model (B = billion).
- **Analogy:** the brain-cells of the model. Training = adjusting them.

### fp16 / fp32
- **What:** how many bits are used to store each number.
- **fp32** = 32 bits per number ("full size").
- **fp16** = 16 bits per number ("half size"), little accuracy loss for AI.
- **Why it matters:** halving number size = fitting double the brain into the
  same VRAM. (bit = smallest unit of computer memory, 8 bits = 1 byte)

### CUDA
- **What:** NVIDIA's platform that lets software like PyTorch talk directly
  to an NVIDIA GPU.
- **cu124** (from `torch==2.6.0+cu124`) = "this PyTorch build speaks CUDA
  version 12.4."
- **MPS** = Apple's equivalent for Macs (M1/M2/M3/M4 chips).

### Tensor
- **What:** a multi-dimensional array of numbers (a grid of grids of grids…).
- 1D tensor = vector `[1, 2, 3]`; 2D = matrix; 3D+ = true tensors.
- **Why it matters:** EVERYTHING in AI is a tensor: images, audio, text —
  all tensors flowing through layers.

---

## 2. The Operating System layer

### Operating system (OS)
- The master program running your computer. Examples: Windows, macOS, Linux.

### Linux
- A free OS that most AI tools are written for first. Comes in flavours
  ("distributions"). Ours:
- **Ubuntu** = the flavour we installed. "24.04 LTS" = release number; LTS =
  Long-Term Support (maintained for 5 years). Boring = good for learning.

### WSL2 (Windows Subsystem for Linux, version 2)
- **What:** real Linux running *inside* Windows, in a window.
- **Analogy:** an apartment for Linux built inside the Windows house.
- **Command that built it:** `wsl --install -d Ubuntu-24.04`
- **How Linux sees Windows:** your `C:` drive = `/mnt/c` (a "bridge" folder).
  Slower to work in — that's why our code lives in Linux's own home, `~`.

### Terminal, shell, bash, prompt
- **Terminal** = the window. **Shell** = the program inside it that reads
  typed text and turns it into actions. **bash** = the shell Ubuntu gives
  you (name: "Bourne Again SHell").
- **Prompt** = the blinking `bufnita@DESKTOP-0L89NHP:~$` line. It is
  DECORATION: only what comes after `$` gets typed by you. Pasting the
  decoration = the mysterious "syntax errors" we met.

### Hidden files (names starting with `.`)
- Linux hides files like `.env`, `.venv`, `.bashrc` by default. Not secret —
  just quiet. Peek with `ls -a`.

### sudo (superuser do)
- "Do this as the administrator." Asks for your password but shows NOTHING
  as you type (no stars!). Linux is shy with passwords on purpose.

---

## 3. The daily commands (your word-vocabulary, with examples)

Try each inside Ubuntu in any folder:

| Command | Meaning | Try it | You'll see |
|---|---|---|---|
| `pwd` | print working directory ("where am I?") | `pwd` | `/home/bufnita/...` |
| `ls` | list files here | `ls` | `first_api_call.py  glossary.md ...` |
| `ls -la` | list all, with details | `ls -la` | sizes, dates, hidden files |
| `cd where` | change directory (`walk there`) | `cd ~` | prompt path changes |
| `cat file` | print file content | `cat lesson-log.md` | your lesson entries |
| `echo text` | print text; `>` sends it to a file | `echo hi > note.txt` | file created |
| `>>` | APPEND (`>` overwrites!) | `echo two >> note.txt` | adds a line |
| `rm file` | delete PERMANENTLY (no recycle bin) | `rm note.txt` | gone forever |
| `mv a b` | move/rename | `mv a.txt b.txt` | renamed |
| `mkdir d` | make directory (folder) | `mkdir scratch` | folder created |
| `head -n 5 file` | first 5 lines | `head -n 5 lesson-log.md` | oldest entries |
| `tail -n 5 file` | last 5 lines | same idea | newest entries |
| `grep word file` | search inside a file | `grep Lesson lesson-log.md` | matching lines |
| `date` | today's date/time | `date` | used in your journal lines |
| `nano file` | edit file in-terminal | `nano note.txt` | Ctrl+O write, Ctrl+X exit |

**Chaining tricks you already own:**
- `&&` = "and then, only if the previous succeeded": `mkdir scratch && cd scratch`
- `|` (pipe) = "feed the left command's output into the right":
  `git log --oneline | head -5` = "show log, but only first 5 lines"
- `$(...)` = "run this command and paste its result here":
  `echo "today is $(date +%F)"` → prints a date

---

## 4. The Python world

### Python
- The programming language most of AI is written in. Famous for reading
  like English. The sandbox runs version 3.12.
- **Version:** different releases coexist (Windows has 3.14, sandbox has
  3.12). Newest ≠ safest for libraries; 3.12 is the "all libraries expect
  it" version.

### pip, uv
- **pip** = Python's classic installer (`pip install numpy`). Slow, ancient,
  everywhere.
- **uv** = the modern turbo installer we use. Also manages Python versions
  (`uv python install 3.12`) and creates sandboxes (`uv venv`).

### venv (virtual environment) — THE SANDBOX
- **What:** a private folder with its own Python + its own libraries.
- **Why:** project A needs NumPy v1, project B needs v2 — sandboxes mean
  they never fight.
- **Commands:** `uv venv` (create), `source .venv/bin/activate` (badge ON),
  `deactivate` (badge off).
- **The badge `(ai-engineering-from-scratch)`** = proof your terminal talks
  to the sandbox NOW. New window? Badge gone → re-apply the two
  "good morning" lines (`cd ~/ai-engineering-from-scratch` then `source
  .venv/bin/activate`).

### Libraries installed so far
- **NumPy** = fast math on grids of numbers (`np.dot(a, a)` → 14, our first!)
- **matplotlib** = draws graphs/charts
- **jupyter** = the lab notebook (Lesson 05!)
- **PyTorch** = the AI math engine that uses your GPU
- **openai** = the SDK (see below) that talks to LLM servers

---

## 5. The JavaScript/Node world (the second language)

| Term | Plain meaning |
|---|---|
| **Node.js** | Runs JavaScript OUTSIDE the browser. We have v22.23.3. |
| **npm** | "Node Package Manager" — Node's original app store. |
| **pnpm** | a faster, disk-saving version of npm. This course uses it. |
| **fnm** | "Fast Node Manager" — the wardrobe where multiple Node versions live. |
| **TypeScript** | JavaScript with type-checking (helpful guardrails). Phase 13+. |

---

## 6. git & GitHub (the time machine)

### The core loop of your working life

```bash
git status                       # what changed?
git add file.txt                 # put it on the desk (STAGE it)
git commit -m "Add lesson log"   # GLUE a snapshot into the album
git push                         # UPLOAD the album to your GitHub
```

### Word-by-word

| Word | It means | Life analogy |
|---|---|---|
| **repo** (repository) | a project folder + its whole history | one photo album |
| **clone** | copy a repo from GitHub to disk | print your own copy of the album |
| **fork** | GitHub copies someone else's repo into YOUR account | fork a restaurant menu; you edit YOUR copy |
| **commit** | one snapshot in time | one glued album page + caption |
| **branch** | a parallel lane from a snapshot | a copied page you may scribble on freely |
| **merge** | take a branch's work into another branch | copying scribbles back to the main page |
| **origin** | "where MY pushes go" (your fork) | your own house |
| **upstream** | "the original repo I forked from" | the family home |
| **pull** | bring the original's updates down | order the original's new pages |
| **.gitignore** | the list of files git must NEVER track | the "do not photograph" list at the door |
| **PAT** (Personal Access Token) | a password cut FOR SOFTWARE (not for you to log in) | a key duplicate only your robot holds |
| **`git log --oneline`** | the timeline, one line per commit | the album index |
| **`git checkout -b name`** | create AND switch to a new branch | start a fresh copied page |

### Hard-won rules you already lived
- **`git check-ignore -v .env`** prints WHICH line of `.gitignore` protects a
  file. Prints nothing = NOT protected (that's how we caught the hole!).
- Untracked ≠ uploaded. But untracked + careless `git add .` someday = leak.
  Secrets belong in `.gitignore` from day one.
- Output text ("4 files changed...") is for READING, not for pasting back
  as commands. 🙂
- After deleting a key in the browser, your local `.env` does not auto-update
  — the file and the website are two separate worlds; YOU sync them.

---

## 7. APIs, internet-speak, keys (Lesson 04) — the restaurant

```
You (code)                          AI provider (their server)
   |                                       |
   |--- HTTP request ------------------->|
   |   (endpoint + API key + JSON body)   |
   |                                      | thinks (burns tokens!)
   |<------------------------------ HTTP response ------|
     (JSON: text answer + usage counts)
```

### The words

| Word | Plain meaning |
|---|---|
| **API** (Application Programming Interface) | the menu window between your code and their computer |
| **HTTP** (HyperText Transfer Protocol) | the language all websites/APIs speak |
| **URL / endpoint** | the address of one specific window (e.g. `/v1/messages`) |
| **JSON** (JavaScript Object Notation) | the text format of requests/replies: `{"key": "value"}` |
| **SDK** (Software Development Kit) | their pre-written helper library so you don't write raw HTTP |
| **base URL** | the root address — swapping it = talking to a different provider |
| **API key** | your password to their servers; proves your identity; enables billing |
| **environment variable** | a session "sticky note": a named value any program in that session can read |
| **`.env`** | a hidden FILE containing the key; `set -a && source .env && set +a` loads it |
| **token (billing)** | ~a word chunk; input and output tokens are counted separately |
| **max_tokens** | the answer-length budget; thinking models burn it invisibly! |
| **finish_reason** | why the answer stopped: `stop` = natural end, `length` = budget ran out |
| **rate limit** | max requests per minute/hour; error 429 = queue full |
| **streaming** | receiving the answer word-by-word as it is born |
| **bearer token** | a key presented inside a header — "whoever holds this is me" |

### The HTTP status zoo (collected live!)

| Code | Nickname | What it means |
|---|---|---|
| **200** | OK | smile, worked |
| **400** | Bad Request | your request text is malformed (we hit it with a leftover placeholder!) |
| **401** | Unauthorized | key missing / expired / wrong species |
| **404** | Not Found | wrong door |
| **429** | Too Many Requests | the queue is full (yours or everyone's) |
| **500** | Server Error | THEIR side broke, not yours |

### The lesson's great secret: provider-agnostic
- The pattern (endpoint + key + JSON in/out) is identical everywhere.
- Proof: our script swapped Google → OpenRouter with two `sed` lines.

---

## 8. Lesson 05 — the Jupyter lab (lived Oct 23 2026, 5/12 ✅)

Words we LIVED today, not just previewed:

| Term | Plain meaning | Lived proof |
|---|---|---|
| **JupyterLab** | the lab bench in your browser: code boxes + writing boxes + a hidden brain | the page the Launcher opened |
| **notebook file (.ipynb)** | IPython Notebook file — internally a JSON (JavaScript Object Notation) text file listing every box, its code and outputs | `my_first_notebook.ipynb` |
| **cell / box** | one small unit: a code box DOES, a text box EXPLAINS | our 7 boxes |
| **kernel** | the background Python brain-process behind the page (`ipykernel` = IPython kernel) | the top-right circle: white = idle, orange = busy |
| **Shift + Enter** | run this box and select the next one | the drumbeat 🥁 |
| **In [n]** | the run counter — how many times, in what order, boxes have run | the betrayal meter |
| **localhost** | "this very machine" — a website living on your own computer, not the internet | `localhost:8888` |
| **port** | a numbered door on your machine; Jupyter serves through its own door | `:8888` |
| **Markdown** | writing-with-formatting-code: `#` = big title, `##` = smaller, `**word**` = bold | "My Lab Notebook — Day 1" |
| **¶ (pilcrow)** | hover-anchor shown next to headings for linking; display-only decor | it appeared by your title |
| **magic command** | an order for the notebook itself (Python doesn't know these); starts with `%` | `%timeit` |
| **ms / μs / ns** | thousandth / millionth / billionth of a second (μ = Greek "mu") | 25.9 ms → 443 μs |
| **± (plus-minus)** | the wobble: how much repeated measurements differed from the mean | ± 15.8 μs |
| **vectorization** | hand the whole grid to NumPy in ONE gulp instead of looping yourself | the 58× speedup we measured |
| **np.int64** | NumPy's labeled whole number: 64 bits of storage width (bit = the 1/0 unit) | `np.int64(14)` |
| **out-of-order execution** | cells run in CLICK order, not PAGE order | the 200! |
| **hidden state** | the kernel remembers everything ever run, invisibly — even old boxes' answers change later | `mystery` 5 → 100 |
| **restart + Run All Cells** | kill the brain, wipe memory (RAM), replay the page as a clean script | the ⟳ ceremony |
| **.ipynb_checkpoints/** | Jupyter's autosave shadow-copies folder — belongs on git's no-photo list | now in `.gitignore` |

**The two truths (the lesson's core discovery):**

| How the page ran | Old box 2 answered | Trustworthy? |
|---|---|---|
| click-order (remix) | 200 | ❌ no — history scrambled |
| page-order (restart → run all) | 10 | ✅ yes — behaves like a script |

**The workflow law from the course:** *explore in notebooks, ship in scripts* — notebooks are scratch paper for discovery; finished work moves into `.py` files.

---

## 8½. Command anatomy — every character on trial (the Double-Entry Law, demonstrated)

### The punctuation zoo (every glyph that ever scared us)

| Character | Name | Plain meaning | Example |
|---|---|---|---|
| (space) | space | separates arguments; one space = one boundary | `git add file` |
| `.` | dot | 1) hidden-file prefix · 2) current folder · 3) Python's "reach inside" | `.env`, `np.dot` |
| `/` | slash | folder separator | `.venv/bin/activate` |
| `-` / `--` | dash, double-dash | tool options (flags) | `-n 5`, `--global` |
| `" "` | double quotes | make chunk/symbols one text piece — ⚠️ a `!` inside = bash history-expansion landmine ("event not found") | `"Lesson 05: ..."` |
| `' '` | single quotes | same, but NOTHING expands inside (safer around `!` and `$`) | |
| `>` | send-into | write output to a file, OVERWRITING it | `echo hi > f.txt` |
| `>>` | append-into | write output at the END of the file (what journals use) | `echo ... >> lesson-log.md` |
| `&&` | and-then | run the next command ONLY if the previous succeeded | the commit chain |
| `\|` | pipe | feed the left command's output into the right one | `git log \| head -5` |
| `$()` | command substitution | run the inner command, paste its RESULT here | `$(date +%F)` |
| `~` | tilde | "my home folder" (`/home/bufnita`) | `cd ~` |
| `%` | percent (Jupyter) | magic-command prefix | `%timeit` |
| `[ ]` | brackets (Python) | build a list | `[n*n for n in range(3)]` |
| `( )` | parentheses | 1) call a function with arguments · 2) pasted into bash = subshell syntax error | `np.dot(a, a)` |
| `**` | double star | 1) Python power: `x ** 2` = x² · 2) Markdown bold | |
| `_` | underscore in numbers | eye-friendly counting: `1_000_000` = 1000000 | |
| `±` | plus-minus | measurement wobble | `443 μs ± 15.8 μs` |

### Worked double-entries (real commands of this course)

**A) 🟢 paste-as-is**
```bash
echo ".ipynb_checkpoints/" >> .gitignore
```
**B) 🧠 anatomy**

| Piece | Meaning |
|---|---|
| `echo` | bash verb: "print the following text" |
| `".ipynb_checkpoints/"` | the text — quotes make it ONE chunk, spaces/symbols safe inside |
| `>>` | redirect-APPEND: write the text at the end of the target file (a single `>` would overwrite!) |
| `.gitignore` | target file (leading dot = hidden; name = "git ignore", the no-photo list) |

**A) 🟢 paste-as-is**
```bash
git add .gitignore my_first_notebook.ipynb lesson-log.md && git commit -m "Lesson 05: first notebook (cells, plot, magics, trap caught)" && git push
```
**B) 🧠 anatomy**

| Piece | Meaning |
|---|---|
| `git` | the version-control tool itself |
| `add` | stage: put the named files on the photography desk |
| (many names) | git accepts multiple files in one line |
| `&&` | "and-then, only if it worked" |
| `commit` | glue a snapshot into history |
| `-m` | flag: "the next quoted text = my caption" |
| `"Lesson 05: ..."` | the caption itself |
| `push` | upload the new history to GitHub (origin) |

**A) 🟢 paste-as-is**
```bash
source .venv/bin/activate
```
**B) 🧠 anatomy**

| Piece | Meaning |
|---|---|
| `source` | run a script INSIDE the current shell (a fresh copy would forget it immediately) — that's why the badge stays on |
| `.venv` | the sandbox folder (leading dot = hidden) |
| `bin` | bin = **binaries** — the folder where executable programs live |
| `activate` | the script that switches your Python to the sandbox |

**A) 🟢 paste-as-is**
```bash
uv pip install jupyterlab
```
**B) 🧠 anatomy**

| Piece | Meaning |
|---|---|
| `uv` | our turbo installer (also manages Pythons and sandboxes) |
| `pip` | Python's classic package-installer command; uv speaks its language |
| `install` | the verb: "fetch and set up" |
| `jupyterlab` | the package name (package names: lowercase, no spaces) |

---

## 8¾. Lesson 06 — Python environments & lockfiles (lived Oct 24 2026, 6/12 ✅)

| Term | Plain meaning | Lived proof |
|---|---|---|
| **dependency** | a library your project needs to work | numpy, pandas, requests |
| **dependency hell** | two projects fight over ONE shared Python's library versions | the lesson's villain |
| **transitive dependency** | a dependency of a dependency | invited 2 guests, 7 packages arrived (scipy, joblib etc. = luggage) |
| **version pin `==`** | "EXACTLY this version" — no drifting | `uv pip install "numpy==1.26.4"` |
| **isolation** | sandboxes don't share toys | lab-two answered 1.26.4, home answered 2.5.4 — same command |
| **pyproject.toml** | the project's ID card: name, version, required Python, shopping list | demo-project's card |
| **TOML** | simple config format: `[section]` headers + `key = "value"` | the card's language |
| **lockfile (uv.lock)** | the receipt: every package AND its luggage pinned to exact barcodes | `Resolved 7 packages in 323ms` |
| **reproducibility** | same receipt → identical setup on any machine, every time | what hashing makes possible |
| **wheel (.whl)** | pre-built ready-to-run package for one machine species | the long `wheels = [...]` lists |
| **sdist** | source distribution: raw code, build-it-yourself option | also recorded in the receipt |
| **sha256 hash** | the file's fingerprint — changes if even 1 bit changes (tamper-proofing) | `hash = "sha256:..."` everywhere |
| **cp312** | "built for CPython 3.12" — our Python species | stamp inside wheel names |
| **per-phase env strategy** | different course phases may need conflicting libs → separate sandboxes per phase | course plan for Phases 4+ |
| **badge ≠ folder** | the `(badge)` follows activation, not directory location | repo badge seen inside demo-project |

---

## 9. Error-reading cheat sheet (the debugging instinct)

When something shows red, ask in order:

1. **What KIND of error?** (missing file? permission? auth? network?)
2. **Which file / line did it blame?**
3. **Can I paste the last lines to my tutor verbatim?**

| Message | what it really means |
|---|---|
| `command not found` | the program doesn't exist here — typo, not installed, or shell not re-read (`source ~/.bashrc`) |
| `SyntaxError: unexpected '('` (in bash) | you pasted decoration/output text as a command |
| `ModuleNotFoundError` (Python) | library not installed **in the current sandbox** — check the badge is ON |
| `permission denied` | need `sudo`, or the file is read-only |
| `No such file or directory` | wrong folder, or the file was never created |
| `401 / AuthenticationError` | key expired / deleted / wrong type |
| `429 / RateLimitError` | queue full — retry later or switch model |
| `finish_reason: length` | truncated answer — raise `max_tokens` or account for thinking tokens |

---

## 10. Journal of proof (what you already verified yourself)

- `git log --oneline -5` → 5 snapshot lines = real history
- `git status` → "working tree clean" = nothing sticky
- `nvidia-smi` → your RTX 3050 is alive with 6 GB VRAM
- the benchmark → CPU vs GPU measured *honestly* (2–3×, and why)
- `first_api_call.py` → a REAL LLM answered YOUR question at $0
- `.gitignore` + `git check-ignore -v .env` → your key is GUARDED
- `my_first_notebook.ipynb` → cells ran, parabola drew, 25.9 ms vs 443 μs measured, the 200→10 betrayal caught, restart healed it

---

*Created Oct 2026 — Phase 0, 6/12 lessons complete. Keep appending!
Lessons 05 & 06 lived and documented (Jupyter Oct 23, environments Oct 24). Next: Lesson 07 — Docker for AI.*
