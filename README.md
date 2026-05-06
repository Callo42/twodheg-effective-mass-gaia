# 2D HEG Effective Mass Gaia Graph

![Gaia starmap](figures/starmap.svg)

This Gaia package maps why the quasiparticle effective mass of the two-dimensional homogeneous electron gas (2D HEG) is numerically delicate. The current graph has reached `round_0005`.

Current graph size:

- `43` visible starmap nodes and `40` starmap edges
- Gaia IR: `44 knowledge`, `15 strategies`, `2 operators`

## Main Open Questions

The final Gaia IR contains two contradiction-backed open questions. Both are intentionally weak, method-level scientific tensions rather than hard logical contradictions.

1. **Does the apparent paramagnetic low-density mass enhancement in earlier DMC survive the later high-precision finite-size extrapolation protocol?**

   Earlier DMC work suggested a significant enhancement of `m*` at low density. Later Drummond-Needs DMC benchmarks, using smaller statistical errors and more explicit finite-size extrapolation, find paramagnetic thermodynamic-limit masses close to one. The open question is whether the older enhancement was a real thermodynamic-limit feature or a finite-size/statistical artifact.

2. **When does the theoretical `N^(-1/4)` finite-size law become a reliable extrapolation protocol rather than only an asymptotic guide overwhelmed by shell-filling noise?**

   Long-range correlations imply slow `N^(-1/4)` finite-size behavior in Fermi-liquid-derived quantities. But direct QMC extrapolation can still be unreliable when shell-filling oscillations dominate nominal statistical errors. The open question is when the asymptotic law becomes operationally useful for finite datasets.

## Scientific Story

The graph begins with a finite-size mechanism: near the Fermi surface, finite simulation cells can distort the excitation dispersion used to extract `m*`. Holzmann et al. showed that slow finite-size corrections can be large enough to change the inferred sign and size of `m* - m`.

The Drummond-Needs workflow then turns this mechanism into a concrete numerical protocol. DMC total-energy differences define a single-particle band, the band is fitted around `k_F`, `m*(N)` is extracted from the fitted derivative, and the result is extrapolated to the thermodynamic limit. Under this protocol, the ideal paramagnetic 2D HEG has `m*` close to one across the studied `r_s=1,5,10` range.

The rest of the graph explains why this conclusion is fragile but coherent. Near-`k_F` numerical derivatives can show pathologies, so a wider fitting window is needed. Excited-state wave-function reoptimization can lower finite-cell DMC energies, but that lowering is itself a finite-size artifact. Fermi-liquid parameters expose a related problem: a correct asymptotic scaling law can still be practically unreliable when shell-filling noise is large. Finally, DMC occupied bands are not purely quadratic, so the effective mass should be understood as one local projection of a richer quasiparticle dispersion.

In short, the package does not merely ask whether `m*/m` is above or below one. It asks which numerical protocol legitimately connects finite-cell QMC data to the thermodynamic-limit effective mass.

## Review Notes

The two contradiction-backed open questions are retained as weak scientific tensions:

- the older-DMC versus revised-benchmark tension is best read as a methodological revision problem;
- the `N^(-1/4)` versus shell-noise tension is best read as a limitation on practical extrapolation, not as a claim that the asymptotic law is false.

Hypothesis-only questions stored under `.gaia/inquiry` are not counted as final graph open questions unless they are promoted to Gaia DSL `contradiction(...)` operators.

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
