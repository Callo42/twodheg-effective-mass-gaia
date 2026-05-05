# LKM Cold-Start Candidates: 2D HEG Effective Mass

Seed statement: The effective mass of the 2D homogeneous electron gas, especially at low density, is numerically delicate; correlation treatment and finite-size/extrapolation choices can even reverse whether m*/m is below or above unity.

## Root Candidates (chain-backed only)

| Option | LKM id | Source | Why it is a plausible root | Evidence |
|---|---|---|---|---|
| A | gcn_28b9e01bd2f8487f | Holzmann et al., `paper:867753636627743508` | Best match to the seed tension: finite-size corrections to excitation dispersion scale as N^{-1/4}, and wrong extrapolation can qualitatively reverse the sign and magnitude of m*-m. | `total_chains=1`; `input/round_0000_008r_evidence_gcn_28b9e01bd2f8487f_retry.json` |
| B | gcn_ac27a904ca704f09 | Azadi et al., `paper:1129109501803233307` | Directly frames finite-size extrapolation for paramagnetic 2D-UEL effective mass; reports empirical N^{-3/2} scaling and stronger finite-size errors at larger r_s. | `total_chains=1`; `input/round_0000_007_evidence_gcn_ac27a904ca704f09.json` |
| C | gcn_2feeb72d724846cf | Drummond and Needs, `paper:813250329280774145` | A precise chain-backed benchmark below unity: paramagnetic 2D HEG at r_s=1 gives m*(infinity)=0.955(2), with explicit method assumptions and model-selection uncertainty. | `total_chains=1`; `input/round_0000_015_evidence_gcn_2feeb72d724846cf.json` |
| D | gcn_678e0e02a7da4c85 | Drummond and Needs, `paper:813250329280774145` | A chain-backed finite-cell result above unity at r_s=5: m*_VMC=1.26(2) and m*_DMC=1.24(3) for N=50; useful for separating finite-N from thermodynamic-limit claims. | `total_chains=1`; `input/round_0000_009_evidence_gcn_678e0e02a7da4c85.json` |

Recommended root for this seed: Option A, because it is already about the mechanism that can flip the inferred sign of m*/m - 1. Option B is also strong if the intended graph should start from the newer 2025 QMC extrapolation protocol.

## No-chain Leads For Later Expansion

These are not valid cold-start roots under the SOP, but they should be revisited after a root is selected:

| LKM id | Evidence status | Why keep it |
|---|---|---|
| gcn_4589e711a3d4446d | `total_chains=0` | Ideal paramagnetic 2D HEG DMC result remains close to unity across r_s=1,5,10 and shows no strong low-density enhancement. |
| gcn_e24d7ff647144aee | `total_chains=0` | Paramagnetic r_s=5 thermodynamic-limit DMC value m*(infinity)=1.04(2). |
| gcn_61559eac3ef543c8 | `total_chains=0` | Paramagnetic r_s=10 thermodynamic-limit DMC value m*(infinity)=1.03(4). |
| gcn_d43e72a7274f420f | `total_chains=0` | Fully spin-polarized r_s=10 value m*(infinity)=0.70(3), below unity. |
| gcn_91358637d8e9481b | `total_chains=0` | Speculative FCI-vs-SJB correlation claim: including all static correlation could increase low-density effective mass beyond SJB estimates, but it is not numerically demonstrated. |
| gcn_5db5b479b43e45c2 | `total_chains=0` | Experimental GaAs/AlGaAs 2D electron Fermi liquid: measured mass increases as density decreases; useful for theory-vs-experiment/open-question expansion, but material/regime differs from ideal 2D HEG. |

## Retrieval Notes

- All raw LKM match/evidence responses are preserved under `artifacts/lkm-discovery/input/`.
- Transient `code=290001` responses were retained and retried once where needed.
- `retrieval_log.jsonl` records every LKM call; `graph_growth_log.jsonl` records package initialization and the open root-selection checkpoint.
