# twodheg-effective-mass-gaia

Gaia knowledge package for the effective-mass problem in the two-dimensional homogeneous electron gas (2D HEG), built from LKM evidence chains.

The package focuses on why numerical treatments of the 2D HEG quasiparticle effective mass can disagree about whether `m*/m` is below, near, or above unity. Current graph growth has reached `round_0004`.

## Starmap

![Gaia starmap](figures/starmap.svg)

Current rendered starmap:

- `39` visible starmap nodes
- `36` starmap edges
- Gaia IR: `40 knowledge`, `13 strategies`, `2 operators`

## Current Focus

Root claim:

`gcn_28b9e01bd2f8487f`

The root asserts that finite-size corrections to near-`k_F` excitation dispersion in a finite 2D HEG cell scale slowly enough that extrapolations assuming faster-vanishing errors can qualitatively change the inferred sign and magnitude of `m* - m`.

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
