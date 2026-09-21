# Experiment records

Create one directory per experiment:

```text
experiments/YYYY-MM-DD-short-name/
  README.md       # completed copy of TEMPLATE.md
  summary.json    # compact machine-readable metrics, when applicable
  figures/        # selected plots worth preserving
```

Large raw outputs belong in ignored `artifacts/`, `runs/`, `checkpoints/`, or `videos/` directories. A tracked manifest should state where they were stored and include checksums for important files.
