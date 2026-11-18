# translation-tibetan-to-french

The workshop for the BuddhistAI skill `translation-tibetan-to-french`: every variant we try, the runs, the provenance records and the ranking report. It does not hold the test data: that is in [buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks/tree/main/tasks/translation), pinned in `benchmark/benchmark.json`.

## Variants

| Variant | Version | What it is | Scored |
| --- | --- | --- | --- |
| [drupchen-method-units-v1](./variants/drupchen-method-units-v1/) | 0.1.0 | Two stages: meaning units from the Tibetan, then French written from the units without the Tibetan in view | Not yet |
| [drupchen-method-onepass-v1](./variants/drupchen-method-onepass-v1/) | 0.1.0 | The same rules in one pass, with the Tibetan in view | Not yet |

Both are our reading of the method of Drupchen ([@drupchen](https://github.com/drupchen)), from his papers in the knowledge base [Papers](https://buddhistai.github.io/knowledge-base/papers/README.html) (CC BY 4.0). Drupchen did not write these skills. The plan for the comparison (no skill, one pass, two stages) is the experiment [2026-11-tibetan-french-translation](https://github.com/BuddhistAI/knowledge-base/blob/main/experiments/2026-11-tibetan-french-translation/PLAN.md). The benchmark data (`bo-fr` v1, 30 colophons) is still being collected, so nothing is scored yet.

These variants were first drafts in buddhist-skills `drafts/` and moved here on 2026-11-18. When one wins on the benchmark, it is released in [buddhist-skills](https://github.com/BuddhistAI/buddhist-skills).

## Layout

```
benchmark/
  benchmark.json      the buddhist-benchmarks release used (repo, tag, path), never a copy of the data
  benchmark.json      (the run script is the task harness in buddhist-benchmarks: tasks/translation/harness/run.py)
variants/<name>/      SKILL.md (with metadata.version) + VARIANT.md (who made it, what is different)
results/              one output file + log (+ meta) per model and run
provenance/           one provenance record per leaderboard row: provenance/<run-id>.json
scripts/              summarize, to_result_json (leaderboard rows), provenance (records)
REPORT.md             the ranking and what we learned
```

## Provenance

Every leaderboard row has a record in [`provenance/`](./provenance/) in the standard format [buddhistai/provenance@1](https://buddhistai.github.io/knowledge-base/handbook/provenance.html): skill files with hashes, model and settings, prompt, benchmark tag and data hash, harness, libraries, command, run files and logs with hashes, tokens, cost and scores. buddhist-benchmarks keeps only the short `result.json`. Working example: [toc-extraction-tibetan](https://github.com/BuddhistAI/toc-extraction-tibetan/tree/main/provenance) (its `scripts/provenance.py` can be adapted).

## Run it

```bash
# from buddhist-benchmarks/tasks/translation:
python3 harness/run.py --arm units --skill ../../../translation-tibetan-to-french/variants/drupchen-method-units-v1 \
    --data data/bo-fr/v1/test.jsonl --model <model> --out runs/<run-id>/repeat-1
python scripts/to_result_json.py ... --benchmarks ../buddhist-benchmarks
python scripts/provenance.py --benchmarks ../buddhist-benchmarks && python scripts/provenance.py --check
```

Run each variant at least 3 times. Never tune on the test set.

## License

MIT, unless a variant says otherwise. Both variants are CC BY 4.0, because they follow Drupchen's CC BY 4.0 papers.
