# bomb – agent instructions

Goals:
- External enumeration tool, starting with subdomain enumeration + validation.
- Outputs: Markdown + txt/csv first, then JSON (For ingestion into documentation tools such as PlexTrac, Dradis, AttackForge, etc.)

Constraints:
- Keep changes incremental and reviewable.
- Prefer standard library; if adding deps, justify them.
- Add tests for non-trivial logic (normalization/dedupe/parsing).
- Run ruff + pytest after changes if config exists.
- Do not add “active” scanning features beyond DNS + HTTP probing without asking.

