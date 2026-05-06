# 2D HEG Effective Mass Gaia

![Gaia starmap](figures/starmap.svg)

This document is a compact narrative view of the rendered Gaia graph. It follows
the graph's real open questions, defined by its accepted contradiction operators:

> Does the apparent paramagnetic low-density 2D HEG mass enhancement in earlier
> DMC survive the later high-precision finite-size extrapolation protocol?
>
> When does the theoretical `N^(-1/4)` finite-size law become a reliable
> extrapolation protocol rather than only an asymptotic guide overwhelmed by
> shell-filling noise?

## 1. Accepted Open Questions

The graph contains two contradiction operators. Both are intentionally weak,
method-level scientific tensions rather than hard logical contradictions.

### Older DMC enhancement vs revised DMC benchmarks

The first side says that earlier DMC calculations found a significant
paramagnetic effective-mass enhancement at lower density.

The second side says that later high-precision DMC benchmarks, with smaller
statistical errors and explicit finite-size extrapolation, give thermodynamic
paramagnetic masses close to one at `r_s=1,5,10`.

The open question is whether the older enhancement survives the later
finite-size/statistical treatment, or whether it is best understood as a
methodological revision of the earlier interpretation.

### `N^(-1/4)` scaling vs shell-filling noise

The first side says that long-range correlations lead to `N^(-1/4)` finite-size
scaling in Fermi-liquid-derived quantities.

The second side says that direct finite-cell extrapolation can still be
quantitatively unreliable when shell-filling oscillations dominate the nominal
DMC error bars.

The open question is when the asymptotic law becomes an operationally reliable
extrapolation protocol, rather than only a formal guide limited by finite-size
noise.

## 2. Finite-Size Root

The root claim is:

> **Slow finite-size errors can flip `m* - m`**

It states that finite-cell corrections to near-`k_F` excitation dispersion can
be slow enough that extrapolations assuming faster-vanishing errors may change
the inferred sign and magnitude of `m* - m`.

This is the mechanism that makes the 2D HEG effective-mass problem delicate.

## 3. DMC Benchmark Side

The benchmark branch argues that the later Drummond-Needs workflow gives a
controlled thermodynamic-limit mass:

- finite-N DMC bands are computed from add/remove total-energy differences;
- the band is fitted around `k_F`;
- `m*(N)` is extracted from the fitted derivative;
- `m*(N)` is extrapolated to the thermodynamic limit;
- the resulting paramagnetic 2D HEG masses remain close to one for
  `r_s=1,5,10`.

This side explains why the later graph branch weakens the older
mass-enhancement interpretation.

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

## 5. Fermi-Liquid-Parameter Reliability

The Fermi-liquid-parameter branch gives the second accepted open question.

It says that `N^(-1/4)` scaling is physically motivated by long-range
correlation, but direct finite-cell extrapolation of Fermi-liquid parameters is
limited by shell-filling oscillations and finite-size noise. The graph therefore
treats `N^(-1/4)` as a necessary asymptotic guide, not automatically as a
sufficient practical extrapolation protocol.

## 6. Graph-Level Meaning

The graph does not say simply "`m*/m` is above one" or "`m*/m` is below one."
It says:

> The effective mass of the ideal 2D HEG is a protocol-dependent
> thermodynamic-limit quantity. The strongest current branch supports a
> near-unity paramagnetic benchmark, but that conclusion is meaningful only
> together with the finite-size, band-fitting, and extrapolation machinery that
> produces it.

The two accepted contradictions mark places where the interpretation should
remain careful: one is a historical/methodological revision of earlier DMC
enhancement, and the other is a limitation on practical use of an asymptotic
finite-size law.

Hypothesis-only questions stored under `.gaia/inquiry` are not counted as final
graph open questions unless they are promoted to Gaia DSL `contradiction(...)`
operators.

## 7. Inference State

The rendered graph contains:

- 43 rendered science nodes.
- 40 starmap edges.
- 44 compiled knowledge entries.
- 15 strategy nodes.
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
