# Open Questions And Candidate Tensions

No executable Gaia contradictions have been admitted yet because the workflow is paused at root selection. The following tensions should guide the first expansion round.

| Tension | Candidate claims | Current verdict |
|---|---|---|
| Finite-size scaling protocol | `gcn_28b9e01bd2f8487f` says missing-small-q finite-size corrections scale as N^{-1/4} and can flip m*-m; `gcn_ac27a904ca704f09` uses empirical N^{-3/2} scaling for 2025 VMC/DMC data. | Open question: which correction/extrapolation model applies to which estimator, band fit, system size, and density regime? |
| Finite-N above unity vs thermodynamic near unity | `gcn_678e0e02a7da4c85` gives finite-cell r_s=5 values around 1.24; no-chain `gcn_e24d7ff647144aee` gives thermodynamic r_s=5 value 1.04(2). | Not a contradiction yet; likely a finite-size-to-thermodynamic relation. |
| Ideal 2D HEG vs experimental 2D electron liquids | no-chain `gcn_4589e711a3d4446d` reports no strong ideal-system enhancement; no-chain `gcn_5db5b479b43e45c2` reports mass enhancement as density decreases in GaAs/AlGaAs wells. | Candidate theory-vs-experiment open question, with material/finite-width/disorder/spectroscopic protocol scope differences. |
| Correlation treatment uncertainty | no-chain `gcn_91358637d8e9481b` speculates FCI could increase low-density m* beyond SJB estimates. | Keep as hypothesis/search lead; no executable contradiction without stronger evidence. |

## Step 3 Mapping Decisions After Root A Selection

| Candidate | Evidence | Open problem | Verdict | Why no Gaia contradiction yet |
|---|---|---|---|---|
| `gcn_ac27a904ca704f09` | chain-backed | Which finite-size correction or extrapolation law correctly applies to 2D HEG effective-mass estimates when comparing N^{-1/4} analytic excitation corrections with empirical N^{-3/2} QMC mass extrapolations? | hypothesis_only | Scope mismatch or finite-N/thermodynamic-limit distinction requires a matched reanalysis before an executable `contradiction(...)` is warranted. |
| `gcn_678e0e02a7da4c85` | chain-backed | Can finite-cell 2D HEG effective masses above unity at r_s=5 be reconciled quantitatively with thermodynamic-limit values near unity once the same band fitting, finite-size correction, and extrapolation protocol are applied? | hypothesis_only | Scope mismatch or finite-N/thermodynamic-limit distinction requires a matched reanalysis before an executable `contradiction(...)` is warranted. |
| `gcn_5db5b479b43e45c2` | lkm_no_chain | Do ideal strictly 2D HEG calculations that find little thermodynamic-limit mass enhancement and quasi-2D experimental electron liquids that show density-dependent mass enhancement become consistent after finite width, disorder, temperature, and measurement protocol are matched? | hypothesis_only | Scope mismatch or finite-N/thermodynamic-limit distinction requires a matched reanalysis before an executable `contradiction(...)` is warranted. |

## Round 0001 Accepted Contradiction

| Pair | Open problem | Decision | relation_type | DSL action |
|---|---|---|---|---|
| `gcn_4d1aad1470d54895` vs `gcn_b7a7d456a05d4129` | Does the apparent paramagnetic low-density 2D HEG mass enhancement in earlier DMC survive the later high-precision finite-size extrapolation protocol, or is it removed by revised finite-size/statistical treatment? | accepted_contradiction | scientific_inconsistency | `older_dmc_enhancement_vs_revised_dmc_benchmarks` |

## Round 0002 Accepted Contradiction

| Pair | Open problem | Decision | relation_type | DSL action |
|---|---|---|---|---|
| `gcn_219b34bd252c43fa` vs `gcn_3db07703d3684507` | When does the theoretical N^(-1/4) finite-size law become a reliable extrapolation protocol rather than only an asymptotic guide overwhelmed by shell-filling noise? | accepted_contradiction | scientific_inconsistency | `n_quarter_scaling_vs_shell_filling_noise` |
