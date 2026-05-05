"""paper_drummond2013_effective_mass - finite-cell effective-mass support claim."""
from gaia.lang import claim, deduction


gcn_850fc9d9de314026 = claim(
    "For finite periodic simulation cells of the two-dimensional homogeneous electron gas using Slater-Jastrow-backflow trial wave functions, reoptimizing variational Jastrow and backflow parameters for an excited-state configuration can lower the finite-cell DMC energy. Because the optimal short-range correlation functions should be unchanged by a single excitation in the thermodynamic limit, this lowering is a finite-size error that can reduce excitation bandwidths and amplify finite-size bias in quantities such as the quasiparticle effective mass [@Drummond2013a].",
    lkm_id="gcn_850fc9d9de314026",
    source_paper="paper:813250329280774145",
    provenance_source="lkm_no_chain",
    lkm_original="In finite periodic simulation cells for a two-dimensional homogeneous electron gas using Slater-Jastrow-backflow trial wave functions that contain variational parameters in the Jastrow and backflow factors, reoptimizing those variational parameters for an excited-state configuration (created by adding or removing an electron in a specified Bloch state) can yield a lower total DMC energy in that finite cell relative to using the ground-state-optimized parameters; because, in the thermodynamic limit, the optimal short-range correlation functions are unchanged by a single excitation, this finite-cell energy lowering is a manifestation of finite-size error and can reduce computed excitation bandwidths and therefore amplify finite-size bias in bandwidth-derived quantities such as the quasiparticle effective mass.",
    source_package="paper:813250329280774145",
)


gcn_c7b10e47e2ab45e1 = claim(
    "In finite periodic 2D HEG simulation cells using Slater-Jastrow-backflow trial wave functions, reoptimizing Jastrow and backflow parameters for an excited-state configuration can lower the total finite-cell DMC energy. For example, removing an electron from k=0 in a 26-electron paramagnetic 2D HEG at r_s=1 lowered the DMC total energy by 0.000854(4) hartree. This finite-cell lowering is a finite-size error that reduces computed excitation bandwidth and amplifies finite-size bias in effective-mass extraction, so the authors optimize those parameters in the ground state and reuse them for excited-state energies [@Drummond2013a].",
    lkm_id="gcn_c7b10e47e2ab45e1",
    source_paper="paper:813250329280774145",
    provenance_source="lkm",
    lkm_original="In finite periodic simulation cells using Slater-Jastrow-backflow trial wave functions (where the Jastrow and backflow factors each contain variational parameters), reoptimizing the Jastrow and backflow parameters for an excited-state configuration (an excitation produced by adding or removing an electron in a particular Bloch state) can lower the total DMC energy in that finite cell—for example, removing an electron from 𝗸=0 in a 26-electron paramagnetic 2D HEG at density parameter r_s=1 reduced the DMC total energy by 0.000854(4) hartree atomic units (a.u.)—but this finite-cell energy lowering is a manifestation of finite-size error and tends to reduce the computed excitation bandwidth and thus amplify finite-size bias in bandwidth-derived quantities such as the quasiparticle effective mass; therefore, to avoid introducing extra finite-size bias the Jastrow and backflow parameters are optimized in the ground state and then reused unchanged for excited-state energy evaluations.",
    source_package="paper:813250329280774145",
)


gfac_5f947643ac684742 = deduction(
    premises=[gcn_850fc9d9de314026],
    conclusion=gcn_c7b10e47e2ab45e1,
    reason="1. Define the Slater-Jastrow-backflow trial wave function and note that Jastrow/backflow parameters are optimized in the ground state and reused for excitations.\n2. Reoptimizing those parameters in an excited state can lower the finite-cell DMC energy, which is a finite-size artifact because a single excitation should not alter optimal short-range correlations in the thermodynamic limit.\n3. In a 26-electron paramagnetic HEG at r_s=1, reoptimization after removing a k=0 electron lowered the total DMC energy by 0.000854(4) hartree and reduced the finite-cell bandwidth. Fig. 1.\n4. Therefore the calculation avoids excited-state reoptimization to prevent extra finite-size bias in excitation energies and effective masses.",
    prior=0.95,
)
gfac_5f947643ac684742.metadata.update(
    {
        "judgment": "accepted",
        "justification": "Accepted as an LKM factor-derived warrant that upgrades the existing no-chain reoptimization mechanism into a chain-backed, quantitative finite-size-bias claim.",
    }
)


gcn_48797cba2bf44d90 = claim(
    "For a 2D HEG single-particle energy band E(k), fitting DMC-computed band values near k_F to the quartic polynomial E(k)=alpha_0+alpha_2 k^2+alpha_4 k^4 and evaluating dE/dk at k_F gives an analytic estimate of the derivative used in m*=k_F/(dE/dk)_{k_F}, provided the chosen k-window is neither too narrow nor too broad [@Drummond2013a].",
    lkm_id="gcn_48797cba2bf44d90",
    source_paper="paper:813250329280774145",
    provenance_source="lkm",
    lkm_original="For a single-particle energy band E(k) of a two-dimensional homogeneous electron gas, with scalar wave number k=|𝗸|, fitting discrete DMC-computed band values E(k_i) within the finite interval k∈[k_F−Δk,k_F+Δk] to the quartic polynomial E(k)=α_0+α_2 k^2+α_4 k^4 and then evaluating the derivative at k_F from the fit as (dE/dk)_{k_F}=2α_2 k_F+4α_4 k_F^3 provides an analytic approximation to the true thermodynamic-limit derivative at k_F suitable for estimating the quasiparticle effective mass m^*=k_F/(dE/dk)_{k_F}, provided the chosen Δk is neither so small that pathological near-k_F fluctuations dominate nor so large that physics beyond quartic band curvature is sampled.",
    source_package="paper:813250329280774145",
)


gcn_1e8fcb7ef934428d = claim(
    "For finite-system quasiparticle effective masses m*(N) obtained from DMC quartic-fit derivatives, the accessible N-dependence can be modeled by m*(N)=m*(infinity)+b N^(-gamma), with m*(infinity), b, and gamma estimated by least-squares fitting and Monte Carlo sampling of statistical error bars, subject to model adequacy over the sampled N range [@Drummond2013a].",
    lkm_id="gcn_1e8fcb7ef934428d",
    source_paper="paper:813250329280774145",
    provenance_source="lkm",
    lkm_original="For a sequence of finite-system quasiparticle effective masses m^*(N) computed from DMC quartic-fit derivatives for periodic simulation cells with electron counts N, the finite-size dependence over the accessible range of N can be modeled by the single power-law form m^*(N)=m^*(∞)+b N^{-γ} with parameters m^*(∞), b, and γ that can be meaningfully estimated by least-squares fitting and by Monte Carlo sampling of the quoted statistical error bars, with the proviso that the model is an approximation whose accuracy depends on the span and density of sampled N values and on the absence of crossover behaviors or multiple competing finite-size contributions over the fitted range.",
    source_package="paper:813250329280774145",
)


gcn_50e263dc961541e0 = claim(
    "For discrete DMC band data in a finite periodic 2D HEG cell, using a moderately wide k-window around k_F in the quartic fit reduces sensitivity to localized near-k_F anomalous fluctuations or outlier derivative estimates and produces per-size effective masses more stable for finite-size extrapolation [@Drummond2013a].",
    lkm_id="gcn_50e263dc961541e0",
    source_paper="paper:813250329280774145",
    provenance_source="lkm",
    lkm_original="For discrete DMC single-particle band data E(k_i) in a periodic finite simulation cell, performing a quartic fit over a moderately wide wave-number interval k∈[k_F−Δk,k_F+Δk]—meaning Δk large enough to include multiple quantized k points on both sides of k_F rather than being restricted to an infinitesimal neighborhood of k_F—reduces sensitivity to localized anomalous fluctuations or outlier derivative estimates in the immediate vicinity of k_F and produces per-size effective-mass estimates that are more stable with respect to statistical noise and more amenable to controlled finite-size extrapolation.",
    source_package="paper:813250329280774145",
)


gcn_a981a2b787514e47 = claim(
    "To obtain a thermodynamic-limit quasiparticle effective mass from finite-N DMC band data, one may fit isotropic band values E(k) near k_F to a quartic polynomial, compute m*(N)=k_F/(dE/dk)_{k_F} from the fitted derivative, and fit m*(N)=m*(infinity)+b N^(-gamma) across system sizes. When the quartic fit uses a sufficiently wide k-window around k_F, this procedure yields stable extrapolated m*(infinity) values [@Drummond2013a].",
    lkm_id="gcn_a981a2b787514e47",
    source_paper="paper:813250329280774145",
    provenance_source="lkm",
    lkm_original="To obtain the thermodynamic-limit quasiparticle effective mass from finite-N DMC band data one may (i) fit the computed isotropic band values E(k), with k = |𝗸|, in a finite interval k∈[k_F−Δk,k_F+Δk] about the Fermi wave vector k_F to the quartic polynomial E(k)=α_0+α_2 k^2+α_4 k^4 (with fit coefficients α_0, α_2, α_4), (ii) compute the band derivative at k_F from the fit as (dE/dk)_{k_F}=2α_2 k_F+4α_4 k_F^3 and define the quasiparticle effective mass by m^*=k_F/(dE/dk)_{k_F}, and (iii) evaluate m^*(N) for several simulation-cell electron counts N and fit the N dependence to the single power-law model m^*(N)=m^*(∞)+b N^{-γ} (with fit parameters m^*(∞), b, and γ) to obtain the thermodynamic-limit mass m^*(∞); when the quartic fit in step (i) is performed over a sufficiently wide Δk about k_F (so as not to be dominated by pathological near-k_F fluctuations) this three-step procedure yields stable extrapolated values m^*(∞).",
    source_package="paper:813250329280774145",
)


gfac_fd7a3b1d2e1f4b07 = deduction(
    premises=[gcn_48797cba2bf44d90, gcn_1e8fcb7ef934428d, gcn_50e263dc961541e0],
    conclusion=gcn_a981a2b787514e47,
    reason="1. Treat high-precision finite-N DMC bands as input data for effective-mass extraction.\n2. Fit E(k) at each density, spin polarization, and system size to a quartic polynomial in k around k_F.\n3. Define m* from the fitted derivative at k_F using m*=k_F/(dE/dk)_{k_F}.\n4. Fit the resulting finite-N m*(N) to m*(infinity)+b N^(-gamma), sampling input error bars to estimate uncertainty.\n5. Use a sufficiently wide k-window so near-k_F numerical derivative anomalies are averaged out.\n6. This procedure yields stable thermodynamic-limit effective masses when applied to the DMC data.",
    prior=0.95,
)
gfac_fd7a3b1d2e1f4b07.metadata.update(
    {
        "judgment": "accepted",
        "justification": "Accepted as a chain-backed method warrant for extracting thermodynamic-limit m* from finite-N DMC band data.",
    }
)
