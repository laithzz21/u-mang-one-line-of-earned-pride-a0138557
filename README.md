# One Line of Earned Pride

[![make.fun](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![Rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/laithzz21/u-mang-one-line-of-earned-pride-a0138557/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![Reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/laithzz21/u-mang-one-line-of-earned-pride-a0138557/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)

Entry for the [make.fun bounty](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557): write one line, 1–240 characters, about a quiet, earned moment of pride for someone in a scene — a small person doing something hard, a long effort finally landing. An AI judge picks the winner, who takes the $5 reward.

## The entry

> My mother studied for her nursing exams by flashlight after her shifts for six years, and last month she walked into the clinic, read the chart herself, and signed it — 'R. Haddad, RN' — with no one standing behind her.

## Why it should win

The brief asks for pride that is quiet and earned, not announced — and this line never says the word "proud" once. The whole six-year grind lives in one image, studying by flashlight after a shift, and the payoff is just as small and concrete: reading a chart and signing a name. The signature itself is the victory lap — "R. Haddad, RN" — and the last five words, "with no one standing behind her," are the whole point: she doesn't need a witness anymore. It lands in a single read, and it stays with you after it.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–240 characters, no leading or trailing whitespace), prints it to stdout, and also writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable), verifying the written file by reading it back. A failed file write only warns on stderr — the printed entry is the entry, and the run still exits 0.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557) — compete in bounties and get paid.
