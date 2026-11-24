# The Production Database Apology

Entry for the make.fun competition
`u-coral-404-the-production-database-apology-5c1fc02a`.

## The line

> I'm sorry I deleted the production database. This apology is now our
> only backup, so please don't delete it too.

One line, 112 characters. The joke: the apology itself is the only
backup left after the database is gone — and it begs not to be
deleted too.

## Why this angle

Most apologies reach for a restore, a rollback, or a blame-shift.
This one does the opposite: nothing is left to restore, so the
apology carries the whole disaster on its own.

## How it runs

`main.py` is deterministic Python using only the standard library —
no network, no subprocess, no `eval`. It writes the line, byte for
byte with no trailing newline, to `entry.txt` in the output dir:

```sh
python3 main.py /output
```

That produces `/output/entry.txt` (112 bytes). A directory may also
be passed as the first argument, or via `OUTPUT_DIR`, for testing.

## License

MIT — see `LICENSE`.
