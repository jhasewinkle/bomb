# bomb

External enumeration orchestrator (skeleton).

## Usage

### CLI

```bash
bomb --help
bomb example.com
bomb enum example.com -o outputs -v
bomb validate -v
bomb report -v
```

### Legacy script

```bash
python bomb.py example.com
```

## Notes

- The `enum` command runs the current pipeline skeleton and writes CSV/HTML outputs.
- `validate` and `report` are placeholders for future expansion.
