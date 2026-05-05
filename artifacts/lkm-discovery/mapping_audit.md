# Mapping Audit

| Frontier | Channel | Query / source | Candidate | Evidence status | Scope comparison | Proposed Gaia action | Rationale / next action |
|---|---|---|---|---|---|---|---|
| cold-start | root_discovery | finite-size/extrapolation search + evidence | `gcn_28b9e01bd2f8487f` | chain-backed | Same ideal/2D HEG broad system and same effective-mass quantity; focuses on finite-size correction mechanism rather than a single density value. | candidate root | Strongest match to seed claim that extrapolation can reverse below/above-unity conclusions. Await user selection. |
| cold-start | root_discovery | finite-size/extrapolation search + evidence | `gcn_ac27a904ca704f09` | chain-backed | Same quantity and computational role; newer 2D-UEL QMC protocol, metallic 1 <= r_s <= 5. | candidate root | Good root if graph should center on 2025 QMC finite-size protocol. Await user selection. |
| cold-start | root_discovery | below-unity search + evidence | `gcn_2feeb72d724846cf` | chain-backed | Same ideal paramagnetic 2D HEG and thermodynamic-limit m*; high-density r_s=1, below unity. | candidate root | Useful numerical benchmark, narrower than the seed tension. Await user selection. |
| cold-start | root_discovery | QMC effective-mass search + evidence | `gcn_678e0e02a7da4c85` | chain-backed | Same model and method family; finite N=50 at r_s=5 rather than thermodynamic limit. | candidate root | Good support-side root for finite-N above-unity behavior, but narrower and not thermodynamic. Await user selection. |
| cold-start | evidence_hydration | evidence fetch | `gcn_4589e711a3d4446d` | lkm_no_chain | Same ideal model and thermodynamic-limit aggregate conclusion. | later leaf/source claim | Important no-chain lead after cold start; not offered as root. |
| cold-start | evidence_hydration | evidence fetch | `gcn_5db5b479b43e45c2` | lkm_no_chain | Experimental quasi-2D GaAs/AlGaAs; same effective-mass direction but different material/width/disorder/protocol. | later open-question lead | Useful for theory-vs-experiment expansion after root selection. |

## Accepted Mappings

| LKM object | Gaia symbol | File | Decision | Notes |
|---|---|---|---|---|
| `gcn_da3eecec49114543` | `gcn_da3eecec49114543` | `src/twodheg_effective_mass/paper_holzmann2008.py` | accepted_claim | Chain premise with usable content; self-contained rewrite preserves original in `lkm_original`. |
| `gcn_28b9e01bd2f8487f` | `gcn_28b9e01bd2f8487f` | `src/twodheg_effective_mass/paper_holzmann2008.py` | accepted_claim | Selected cold-start root; self-contained rewrite preserves original in `lkm_original`. |
| `gfac_290d88db6d0d4237` | `gfac_290d88db6d0d4237` | `src/twodheg_effective_mass/paper_holzmann2008.py` | accepted_deduction | Factor-derived deduction with full LKM step reasoning and warrant prior 0.95. |

## Step 4 Support And Prior Decisions

| Decision | Scope | Rationale |
|---|---|---|
| support_not_found | root `gcn_28b9e01bd2f8487f` | Two support-channel queries were run. Hits did not provide an independent LKM-grounded endpoint suitable for a non-duplicative `support(...)` edge beyond the accepted factor-derived deduction. |
| prior_added | `gcn_da3eecec49114543` | Leaf premise prior seeded at 0.82 with TODO review note in `priors.py`. |

## Round 0001 Accepted Mappings

| LKM object | Channel | Evidence status | Gaia action | Rationale |
|---|---|---|---|---|
| `gcn_219b34bd252c43fa` | support | lkm_no_chain | claim + support | Same-system N^-1/4 finite-size scaling supports root without duplicating root factor. |
| `gcn_850fc9d9de314026` | support | lkm_no_chain | claim + support | Separate finite-cell excited-state reoptimization bias supports root finite-size-delicacy claim. |
| `gcn_b7a7d456a05d4129` + `gfac_59dedf8a0cba48b3` | open_question_conflict | chain-backed | claim + deduction | Later thermodynamic-limit benchmark claim anchors the revised near-unity side of the effective-mass tension. |
| `gcn_4d1aad1470d54895` | open_question_conflict | lkm_no_chain | claim | Older DMC enhancement side retained to make the scientific inconsistency explicit. |
| `older_dmc_enhancement_vs_revised_dmc_benchmarks` | open_question_conflict | accepted pair | accepted_contradiction | Same field-facing paramagnetic 2D HEG effective-mass question; older significant enhancement vs later near-unity thermodynamic benchmarks. relation_type=scientific_inconsistency. |

## Round 0002 Accepted Mappings

| LKM object | Channel | Evidence status | Gaia action | Rationale |
|---|---|---|---|---|
| `gcn_c7b10e47e2ab45e1` + `gfac_5f947643ac684742` | support/refinement | chain-backed | claim + deduction | Quantifies the excited-state reoptimization finite-size bias already represented by `gcn_850fc9d9de314026`. |
| `gcn_3db07703d3684507` + `gfac_b465826db1974ced` | conflict | chain-backed | claim + deduction | Shows N^-1/4 scaling is not enough for reliable direct Fermi-liquid-parameter extrapolation because shell-filling noise dominates. |
| `gcn_306f15c9d5814e23` + `gfac_4d2c6276f8304edb` | support/context | chain-backed | claim + deduction | Adds best-available parameter assembly as a pragmatic response to unreliable direct extrapolation. |
| `n_quarter_scaling_vs_shell_filling_noise` | conflict | accepted pair | accepted_contradiction | Same field-facing finite-size protocol question; N^-1/4 as usable extrapolation form vs shell-noise-limited unreliability. relation_type=scientific_inconsistency. |

## Round 0003 Accepted Mappings

| LKM object | Channel | Evidence status | Gaia action | Rationale |
|---|---|---|---|---|
| `gcn_a981a2b787514e47` + `gfac_fd7a3b1d2e1f4b07` | support | chain-backed | claim + deduction + support | Adds explicit DMC quartic-band-fit and finite-size-extrapolation protocol supporting benchmark values. |
| `gcn_8fdb8c6b76f74960` | duplicate review | chain-backed | dismissed | Semantically duplicates existing reoptimization-bias branch; not emitted to avoid double counting. |
