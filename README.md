# 2D HEG Effective Mass Gaia

![Gaia starmap](figures/starmap.svg)

This document is a compact narrative view of the rendered Gaia graph. It follows
the graph's real open questions, defined by its accepted contradiction operators:

> Does the apparent paramagnetic low-density 2D HEG mass enhancement in earlier
> DMC survive the later high-precision finite-size extrapolation protocol?
>
> How should the 2013 Drummond-Needs extrapolation protocol be reconciled with
> the 2025 QMC treatment of Slater-Jastrow-backflow wave functions, band
> fitting, and finite-size extrapolation?

## 1. Accepted Open Questions

The graph contains two contradiction operators. Both are intentionally weak,
method-level scientific tensions rather than hard logical contradictions.

### Older DMC enhancement vs revised DMC benchmarks

The first side says that earlier DMC calculations found a significant
paramagnetic effective-mass enhancement at lower density.

The second side says that the 2013 Drummond-Needs high-precision DMC benchmarks,
with smaller statistical errors and explicit finite-size extrapolation, give
thermodynamic paramagnetic masses close to one at `r_s=1,5,10`.

The open question is whether the older enhancement survives the later
finite-size/statistical treatment, or whether it is best understood as a
methodological revision of the earlier interpretation.

This framing is limited to the branches currently represented in this graph.
More recent QMC work by Azadi, Drummond, Principi, Belosludov, and Bahramy
reports a paramagnetic effective mass that is close to one at `r_s=1` but
increases with `r_s`, reopening the low-density trend question within the
modern QMC literature.

### 2013 near-unity benchmark vs 2025 increasing trend

The first side says that the 2013 Drummond-Needs finite-size-extrapolated DMC
branch gives paramagnetic thermodynamic-limit masses close to one at
`r_s=1,5,10`.

The second side says that the 2025 Azadi-Drummond-Principi-Belosludov-Bahramy
QMC branch finds a paramagnetic 2D-UEL mass close to one at `r_s=1` but
increasing over `1 <= r_s <= 5`.

The open question is how to reconcile the two protocols: system sizes,
Slater-Jastrow-backflow treatment, band fitting, and finite-size extrapolation
must be compared before the low-density trend can be called settled.

## 2. Finite-Size Root

The root claim is:

> **Slow finite-size errors can flip `m* - m`**

It states that finite-cell corrections to near-`k_F` excitation dispersion can
be slow enough that extrapolations assuming faster-vanishing errors may change
the inferred sign and magnitude of `m* - m`.

This is the mechanism that makes the 2D HEG effective-mass problem delicate.

## 3. DMC Benchmark Side

The benchmark branch represented here argues that the 2013 Drummond-Needs
workflow gives a controlled thermodynamic-limit mass:

- finite-N DMC bands are computed from add/remove total-energy differences;
- the band is fitted around `k_F`;
- `m*(N)` is extracted from the fitted derivative;
- `m*(N)` is extrapolated to the thermodynamic limit;
- the resulting paramagnetic 2D HEG masses remain close to one for
  `r_s=1,5,10`.

This side explains why the 2013 branch weakens the older mass-enhancement
interpretation. It should not be read as the final current-literature verdict:
the 2025 QMC study reopens how the paramagnetic mass evolves with decreasing
density.

## 4. Protocol Fragility

The graph also shows why the benchmark is not a trivial number:

- near-`k_F` numerical derivatives can be pathological;
- wide `k` windows stabilize band fits;
- excited-state wave-function reoptimization lowers finite-cell energies but
  increases finite-size bias;
- fixed-node and time-step biases must be judged relative to finite-size
  extrapolation uncertainty;
- DMC occupied bands are not purely quadratic, so `m*` is only one local
  projection of a richer quasiparticle dispersion.

This branch is the graph's main explanation of how finite-cell data can be
converted into a thermodynamic-limit effective mass without overreading
near-`k_F` artifacts.

## 5. 2025 QMC Update

The 2025 branch reopens the low-density trend inside modern QMC. It adds:

- a paramagnetic 2D-UEL trend in which `m*` increases with `r_s` over
  `1 <= r_s <= 5`;
- an empirical `N^(-3/2)` finite-size extrapolation protocol for that data;
- a ferromagnetic trend moving oppositely with density, clarifying the
  spin-sector dependence of the mass.

This branch does not simply invalidate the 2013 benchmark. It reframes the
current question: the modern literature now asks which QMC extraction protocol,
finite-size treatment, and trial-wave-function choices determine the
paramagnetic low-density trend.

## 6. Fermi-Liquid-Parameter Reliability

The Fermi-liquid-parameter branch is no longer treated as an accepted open
question in the formal Gaia IR.

It says that `N^(-1/4)` scaling is physically motivated by long-range
correlation, while the same Drummond2013 analysis cautions that direct
finite-cell extrapolation of Fermi-liquid parameters is limited by shell-filling
oscillations and finite-size noise. These statements can both be true: the graph
now treats this branch as a practical reliability caveat, not as a
`contradiction(...)` between two mutually exclusive claims.

## 7. Graph-Level Meaning

The graph does not say simply "`m*/m` is above one" or "`m*/m` is below one."
It says:

> The ideal 2D HEG effective mass is a thermodynamic-limit Fermi-liquid
> quantity, but its finite-cell QMC extraction is highly protocol-sensitive.
> The graph now contains both the 2013 near-unity benchmark branch and the 2025
> increasing-trend branch, so the current question is how to reconcile their
> finite-size, band-fitting, and backflow treatments.

The two accepted contradictions mark places where the interpretation should
remain careful: one is a historical/methodological revision of earlier DMC
enhancement, and one is a current-literature reconciliation problem between
2013 and 2025 QMC protocols.

Hypothesis-only questions stored under `.gaia/inquiry` are not counted as final
graph open questions unless they are promoted to Gaia DSL `contradiction(...)`
operators.

## 8. Inference State

The rendered graph contains:

- 50 rendered science nodes.
- 46 starmap edges.
- 51 compiled knowledge entries.
- 18 strategy nodes.
- 2 contradiction operators.

The starmap filters out Gaia's internal `__conjunction_result_*` and
`__implication_result_*` helper nodes, so the visual graph is the
science-readable probability graph rather than a dump of lowering internals.

## Package Contents

- `src/twodheg_effective_mass/` — Gaia DSL claims, deductions, supports,
  contradictions, and priors.
- `references.json` — bibliographic references used by the package.
- `artifacts/lkm-discovery/` — raw LKM payloads, retrieval timeline, graph
  growth log, and mapping audits.
- `.gaia/` — compiled Gaia artifacts, beliefs, inquiry state, and starmap
  outputs.

## Quality Gates

The current package state passes:

```bash
gaia compile .
gaia check --brief .
gaia check --hole .
gaia infer .
gaia inquiry review --strict .
```

## Repository Name

This repository is named `twodheg-effective-mass-gaia` so it does not begin with a digit.
