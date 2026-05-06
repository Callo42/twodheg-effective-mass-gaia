"""paper_azadi2025_effective_mass - 2025 QMC effective-mass update."""
from gaia.lang import claim, deduction


gcn_21f80773b87f444c = claim(
    "For paramagnetic 2D-UEL with spin polarization zeta=0 and density parameters 1 <= r_s <= 5, Slater-Jastrow-backflow trial wave functions, quartic or Pade band fitting, and empirical finite-size extrapolation m*(N)=m*(infinity)+beta N^(-3/2) applied to N=146, 218, and 302 data yield thermodynamic-limit effective masses that increase monotonically with r_s [@Azadi2025].",
    title="2025 paramagnetic m* increases with r_s",
    lkm_id="gcn_21f80773b87f444c",
    source_paper="paper:1129109501803233307",
    provenance_source="lkm_no_chain",
    lkm_original="For the paramagnetic two-dimensional uniform electron liquid (2D-UEL) with spin polarization ζ = 0 and for density parameters in the metallic interval 1 ≤ r_s ≤ 5, applying Slater–Jastrow–backflow (SJB) trial wave functions, band fitting (quartic or Padé), and the empirical finite-size extrapolation m*(N) = m*(∞) + β·N^{-3/2} to data at N = 146, 218, and 302 yields extrapolated thermodynamic-limit values m*(∞) that form a monotonic increasing function of r_s across the studied discrete points.",
    source_package="paper:1129109501803233307",
)


gcn_ac27a904ca704f09 = claim(
    "For paramagnetic 2D-UEL, finite-N QMC effective masses show a systematic size dependence well described by m*(N)=m*(infinity)+beta N^(-3/2); using this empirical scaling permits controlled thermodynamic-limit extrapolation, with finite-size errors growing as density is reduced [@Azadi2025].",
    title="2025 N^-3/2 m*(N) extrapolation",
    lkm_id="gcn_ac27a904ca704f09",
    source_paper="paper:1129109501803233307",
    provenance_source="lkm",
    lkm_original="The computed quasiparticle effective mass m* for paramagnetic 2D-UEL exhibits a systematic dependence on the simulation-cell electron number N that is empirically well described by the form m*(N) = m*(∞) + β·N^{-3/2} for some constant β; applying this N^{-3/2} empirical scaling to finite-N VMC and DMC data (for example N = 146, 218, 302) permits controlled extrapolation to estimates of m*(∞) in the thermodynamic limit. Observationally in the reported datasets, finite-size errors of m* are smaller in VMC than in DMC and the finite-size errors grow as the density is reduced (larger r_s).",
    source_package="paper:1129109501803233307",
)


gcn_cb512194b0bc4df2 = claim(
    "For paramagnetic 2D-UEL QMC band-derivative estimates at N=146, 218, and 302 electrons over 1 <= r_s <= 5, the finite-size dependence of m*(N) is taken to follow the empirical form m*(N)=m*(infinity)+beta N^(-3/2), which is then used to extrapolate m*(infinity) [@Azadi2025].",
    title="2025 finite-size ansatz for m*(N)",
    lkm_id="gcn_cb512194b0bc4df2",
    source_paper="paper:1129109501803233307",
    provenance_source="lkm",
    lkm_original="For the two-dimensional uniform electron liquid (2D-UEL) model consisting of N interacting electrons of charge −e and bare mass m in a finite periodic simulation cell of area A (so that the density is ρ = N/A) and with density parameter r_s = (1/(πρ))^{1/2}a_B^{-1} (using atomic units with Bohr radius a_B = 1), the finite-size dependence of the quasiparticle effective mass m*(N) obtained from quantum Monte Carlo band-derivative estimates is taken to follow the empirical form\n      m*(N) = m*(∞) + β·N^{-3/2}\n      for some constant β, and this empirical scaling relation is applied to the authors' simulation data obtained at N = 146, 218, and 302 electrons to extrapolate m*(∞) for densities in the metallic range 1 ≤ r_s ≤ 5.\n      Holzmann et al., Theory of finite size effects for electronic quantum Monte Carlo calculations of liquids and solids, Phys. Rev. B 94, 035126 (2016).",
    source_package="paper:1129109501803233307",
)


gfac_9f7e49ccca424495 = deduction(
    premises=[gcn_cb512194b0bc4df2],
    conclusion=gcn_ac27a904ca704f09,
    reason="1. Finite simulation cells discretize available k-space and make direct finite-N mass estimates ambiguous.\n2. The authors compute paramagnetic 2D-UEL bands at N=146, 218, and 302 electrons across 1 <= r_s <= 5.\n3. Plotting extracted effective masses against N^(-3/2) yields an approximately linear finite-size trend.\n4. Finite-size errors are smaller in VMC than DMC and grow as density is reduced.\n5. The N^(-3/2) empirical scaling is therefore used as a controlled extrapolation protocol for this 2025 dataset.",
    prior=0.90,
)
gfac_9f7e49ccca424495.metadata.update(
    {
        "judgment": "accepted",
        "justification": "Accepted as a chain-backed 2025 QMC finite-size extrapolation warrant, but with a lower prior than older exact-factor deductions because it is empirical and estimator-specific.",
    }
)


gcn_f431f49f19b44cf1 = claim(
    "For fully spin-polarized 2D-UEL in the metallic range 1 <= r_s <= 5, 2025 VMC and fixed-node DMC calculations indicate that m* decreases as r_s increases, opposite to the paramagnetic trend over the same density interval [@Azadi2025].",
    title="2025 ferromagnetic m* decreases with r_s",
    lkm_id="gcn_f431f49f19b44cf1",
    source_paper="paper:1129109501803233307",
    provenance_source="lkm",
    lkm_original="For the fully spin-polarized (ferromagnetic, ζ = 1) two-dimensional uniform electron liquid (2D-UEL) studied in the metallic density range 1 ≤ r_s ≤ 5, VMC and fixed-node DMC calculations performed for simulation cells containing N = 151 electrons indicate that the quasiparticle effective mass m* decreases as r_s increases (i.e., m* is suppressed as the density is reduced), a trend opposite to that found for the paramagnetic case over the same density interval.",
    source_package="paper:1129109501803233307",
)
