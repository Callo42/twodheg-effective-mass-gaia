"""paper_drummond2012_effective_mass - revised DMC thermodynamic-limit benchmarks."""
from gaia.lang import claim, deduction


gcn_a685639571304474 = claim(
    "When fitting finite-N effective-mass data to m*(N)=m*(infinity)+b N^(-gamma), repeated fits with Monte Carlo resampling of the statistical error bars provide uncertainty estimates for m*(infinity) that capture dominant statistical variability, while not necessarily covering all model-selection or systematic extrapolation errors [@Drummond2012].",
    lkm_id="gcn_a685639571304474",
    source_paper="paper:867751779943579657",
    provenance_source="lkm",
    lkm_original="When fitting the finite-\\(N\\) effective-mass data \\(m^{*}(N)\\) to the scaling form \\(m^{*}(N)=m^{*}(\\infty)+b\\,N^{-\\gamma}\\), the proposition is: performing repeated fits with Monte Carlo resampling of the statistical error bars on the input finite-\\(N\\) \\(m^{*}(N)\\) values yields uncertainty estimates for the fitted thermodynamic-limit parameter \\(m^{*}(\\infty)\\) that accurately capture the dominant contribution of the statistical variability in the data; these Monte Carlo-derived error bars are sufficiently conservative to represent the quoted statistical uncertainties in the extrapolated \\(m^{*}(\\infty)\\), while acknowledging that they may not fully account for model-selection or other systematic sources of error.",
    source_package="paper:867751779943579657",
)


gcn_17c63b5dc2154f15 = claim(
    "In the reported DMC effective-mass calculations for 2D HEGs, finite time-step checks and high-quality Slater-Jastrow-backflow trial wave functions indicate that residual fixed-node and time-step biases are small compared with uncertainties from finite-size extrapolation, so those residual biases are not expected to materially shift the reported thermodynamic-limit m*(infinity) values [@Drummond2012].",
    lkm_id="gcn_17c63b5dc2154f15",
    source_paper="paper:867751779943579657",
    provenance_source="lkm",
    lkm_original="Consider the reported DMC calculations carried out with finite DMC time steps (time steps of 0.04, 0.2, and 0.4 a.u. at \\(r_{s}=1,5,10\\) for paramagnetic HEGs and 0.01, 0.2, and 0.4 a.u. at \\(r_{s}=1,5,10\\) for ferromagnetic HEGs) and using single-determinant Slater-Jastrow-backflow trial wave functions that, according to extrapolation of variational Monte Carlo energies to zero energy variance, retrieve more than 99% of the correlation energy. The proposition is: the residual biases arising from the fixed-node approximation and from finite DMC time-step errors (noting that halving the time step was verified to have a negligible effect on the computed energy band) are small compared with the overall uncertainties introduced by the finite-size extrapolation procedure; therefore these residual numerical biases do not materially shift the reported extrapolated thermodynamic-limit effective masses \\(m^{*}(\\infty)\\).",
    source_package="paper:867751779943579657",
)


gcn_b7a7d456a05d4129 = claim(
    "Using a single-power-law finite-size extrapolation with exponent gamma=3/2, Drummond and Needs reported thermodynamic-limit DMC quasiparticle effective masses for clean continuum 2D HEGs: for the paramagnetic system, m*(r_s=1)=0.955(2), m*(r_s=5)=1.04(2), and m*(r_s=10)=1.03(4); for the fully spin-polarized system, m*(r_s=1)=0.851(5), m*(r_s=5)=0.74(1), and m*(r_s=10)=0.70(3) [@Drummond2012].",
    lkm_id="gcn_b7a7d456a05d4129",
    source_paper="paper:867751779943579657",
    provenance_source="lkm",
    lkm_original="Extrapolating the finite-size DMC effective-mass data to the thermodynamic limit using the single-power-law scaling with exponent \\(\\gamma=3/2\\) yields the following quasiparticle effective masses \\(m^{*}(\\infty)\\) expressed in Hartree atomic units (a.u.): for the paramagnetic (unpolarized) 2D HEG, \\(m^{*}(r_{s}=1)=0.955(2)\\), \\(m^{*}(r_{s}=5)=1.04(2)\\), and \\(m^{*}(r_{s}=10)=1.03(4)\\); for the fully spin-polarized (ferromagnetic) 2D HEG, \\(m^{*}(r_{s}=1)=0.851(5)\\), \\(m^{*}(r_{s}=5)=0.74(1)\\), and \\(m^{*}(r_{s}=10)=0.70(3)\\). These numerical values are the principal thermodynamic-limit benchmarks reported for clean, continuum-model 2D HEGs in this work.",
    source_package="paper:867751779943579657",
)


gfac_59dedf8a0cba48b3 = deduction(
    premises=[gcn_a685639571304474, gcn_17c63b5dc2154f15],
    conclusion=gcn_b7a7d456a05d4129,
    reason="1. Take the empirical finite-size scaling form m*(N)=m*(infinity)+b N^(-gamma), with gamma=3/2, as the basis for thermodynamic-limit extrapolation.\n2. Apply the quartic-fit-derived finite-N effective masses for each density and spin polarization to the gamma=3/2 finite-size fit, including Monte Carlo sampling of input error bars, to obtain m*(infinity) and uncertainties. Table II.\n3. Report the extrapolated thermodynamic-limit effective masses for paramagnetic and fully spin-polarized 2D HEGs. Table II.\n4. State that these values are the principal thermodynamic-limit benchmarks and that the revised paramagnetic values differ from earlier work because higher-precision data allowed systematic finite-size errors to be observed and removed.",
    prior=0.95,
)
gfac_59dedf8a0cba48b3.metadata.update(
    {
        "judgment": "accepted",
        "justification": "Accepted as an LKM factor-derived warrant with two usable premises, ordered evidence steps, and source-package provenance; warrant prior remains reviewer-calibrated at 0.95.",
    }
)
