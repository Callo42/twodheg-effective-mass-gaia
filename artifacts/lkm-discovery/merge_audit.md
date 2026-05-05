# Merge Audit

| Pair / risk | Verdict | Rationale | Gaia action |
|---|---|---|---|
| `paper:867753636627743508` and `paper:811872228453908481` | keep_distinct_reference_anchors | LKM returned both arXiv and journal metadata for Holzmann et al. Renormalization factor/effective mass. The executable root uses the arXiv `source_package` from the accepted evidence chain; no duplicate claim was emitted. | No `equivalence(...)` yet; revisit if journal-chain evidence is admitted. |
| Support-channel hits on Holzmann finite-size/effective-mass wording | no_extra_support | Hits appear same-paper/same-result or scope-lateral relative to the selected chain-backed factor. Extra support edges would double-count the already admitted LKM deduction. | `support_not_found` logged for independent support beyond the chain backbone. |
