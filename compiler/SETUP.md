# Running the MEDIAN compiler on your Mac

Phases 0–3 need only Python and pandoc. Phase 4 additionally needs the
Anthropic SDK and an API key.

---

## 1. Where pip installs things

**The short answer: into a virtual environment inside this repo, not into your
system Python.**

macOS ships its own Python that the operating system depends on. Installing
packages into it with `sudo pip` is how people break their machines, and newer
macOS versions block it outright with an "externally-managed-environment"
error. A virtual environment is a self-contained folder holding its own Python
and its own packages. Delete the folder and everything is undone — nothing
leaks into the rest of your system.

Open Terminal and run these one at a time:

```bash
cd ~/Documents/GitHub/median

python3 -m venv .venv
```

That creates `.venv/` in the repo. It is already gitignored.

```bash
source .venv/bin/activate
```

Your prompt now starts with `(.venv)`. **That prefix is the whole game** — it
means `pip` and `python` refer to the environment, not to system Python. You
need to run `source .venv/bin/activate` again in every new Terminal window.

```bash
pip install -e "compiler[extract]"
```

That installs the compiler in editable mode — so `median-compile` becomes a
command and edits to the source take effect immediately — plus the Anthropic
SDK that Phase 4 needs.

If you only want Phases 0–3, `pip install -e compiler` is enough. The provider
SDK is deliberately optional: the deterministic phases must run without it.

Check it worked:

```bash
median-compile status build/v0.5
```

You should see the Phase 0–3 artifacts listed.

### If something goes wrong

**`command not found: median-compile`** — the environment isn't active. Run
`source .venv/bin/activate` and try again.

**`externally-managed-environment`** — you're outside the venv. Same fix.
Never work around this with `--break-system-packages` on your own machine.

**`pandoc: command not found`** — install it with `brew install pandoc`. If you
don't have Homebrew, get it from https://brew.sh.

**Wrong Python version** — check with `python3 --version`. The compiler needs
3.10 or newer. macOS 13+ ships 3.9 in some configurations; if so,
`brew install python@3.12` and create the venv with `python3.12 -m venv .venv`.

**`Multiple top-level packages discovered in a flat-layout`** — fixed as of
1 August 2026. `compiler/` holds `median_compile/` alongside `prompts/` and
`schemas/`, and setuptools refused to guess which was the package.
`pyproject.toml` now declares the package list explicitly. If you hit this,
`git pull` and retry.

---

## 2. Getting and applying an API key

### Get the key

1. Go to **https://console.anthropic.com**
2. Sign in, then open **API keys** in the left sidebar
3. **Create key**, name it something like `median-compiler`
4. Copy it immediately — it starts with `sk-ant-` and **is shown only once**

You'll also need credit on the account. Console → **Billing**. The full corpus
extraction is estimated at **$3.86**, the pilot at **$0.42**, so a small
starting balance covers this comfortably.

### Apply the key

**Never put the key in a file inside the repo.** Anything in the repo can be
committed by accident, and a leaked key can be used by whoever finds it.

**For one session** — fine for the pilot:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
export ANTHROPIC_EXTRACTION_MODEL="claude-opus-5"
```

These last until you close the Terminal window.

**Permanently** — add to your shell profile:

```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
echo 'export ANTHROPIC_EXTRACTION_MODEL="claude-opus-5"' >> ~/.zshrc
source ~/.zshrc
```

macOS uses zsh by default. If `echo $SHELL` says bash, use `~/.bash_profile`.

Verify without printing the key:

```bash
echo "key set: ${ANTHROPIC_API_KEY:+yes}"
echo "model:   $ANTHROPIC_EXTRACTION_MODEL"
```

If the key ever leaks, revoke it in the console and issue a new one. That is
the whole remedy — there is nothing else to clean up.

---

## 3. Running the pilot

Always dry-run first. It makes no calls and costs nothing:

```bash
median-compile extract build/v0.5 --source SPEC_HOME --dry-run
```

Then the real thing, one source at a time:

```bash
median-compile extract build/v0.5 --source SPEC_HOME
median-compile extract build/v0.5 --source RULE_BSA
```

Records land in `build/v0.5/records/`, the call log in
`build/v0.5/logs/calls.jsonl`, and a run entry in `build/v0.5/logs/build_record.jsonl`.

**Re-running is free.** Results are cached on the chunk hash plus the prompt,
schema, provider and model versions. Run the same command twice and the second
costs $0.00 — the `cached` column will show it. Tokens are spent again only
when something genuinely changed.

### If a call fails

**`response hit the N-token output ceiling`** — a chunk produced more records
than the ceiling allowed. The raw text is kept in
`build/v0.5/.cache/extract/<key>.raw.txt` so nothing is lost. Raise
`providers.extraction.max_output_tokens` in `config.yaml`, or pass
`--max-tokens 48000`. The default is 32,000.

**`Streaming is required for operations that may take longer than 10 minutes`**
— fixed as of 1 August 2026. The SDK refuses a non-streaming request whose
output ceiling implies it could run past ten minutes, which a 32,000-token
ceiling does. The provider now always streams. `git pull` and retry.

A failed call is never cached as a success, so re-running retries it. Chunks
that already succeeded stay cached and cost nothing on the retry.

Extraction prints a dot every couple of thousand characters as the response
streams in, then the record count for each chunk. A chunk taking two or three
minutes is normal.

To see what a call would look like without an API key at all:

```bash
median-compile extract build/v0.5 --source SPEC_HOME --fake
```

That uses a deterministic stand-in provider. Useful for checking plumbing;
the records it produces are nonsense and should be deleted before a real run.

---

## 4. Command reference

```bash
median-compile status       build/v0.5    # which phases have run
median-compile log          build/v0.5    # full build history
median-compile check-stale  build/v0.5    # inputs changed since last run?

median-compile manifest        build/v0.5   # Phase 0
median-compile probe           build/v0.5   # Phase 0 classification evidence
median-compile normalize-full  build/v0.5   # Phase 1
median-compile normalize-lean  build/v0.5   # Phase 2
median-compile chunk           build/v0.5   # Phase 3
median-compile extract         build/v0.5   # Phase 4  ← costs money
```

Every command takes `--source <ID>` to run against one source, and `extract`
takes `--dry-run` and `--fake`.
