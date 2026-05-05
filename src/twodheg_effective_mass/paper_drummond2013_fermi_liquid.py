"""paper_drummond2013_fermi_liquid - finite-size scaling and reliability claims."""
from gaia.lang import claim, deduction


gcn_219b34bd252c43fa = claim(
    "For Fermi-liquid parameters F_l, or F_l/m*, of the two-dimensional homogeneous electron gas computed in square periodic simulation cells, the leading systematic finite-size correction from long-range correlation effects scales as N^(-1/4). This supports thermodynamic-limit extrapolations of finite-N results with a form F_l(N)=c+a N^(-1/4), matching the long-range-correlation finite-size analysis associated with Holzmann et al. [@Drummond2013b].",
    title='N^-1/4 finite-size scaling for Landau parameters',
    lkm_id="gcn_219b34bd252c43fa",
    source_paper="paper:867749664370197342",
    provenance_source="lkm_no_chain",
    lkm_original="The proposition: For Fermi liquid parameters $F_l$ (or $F_l/m^{*}$) of the two-dimensional homogeneous electron gas (2D HEG) computed in square periodic simulation cells containing $N$ electrons, the leading systematic finite-size correction arising from long-range correlation effects scales asymptotically as $N^{\\gamma}$ with exponent $\\gamma=-1/4$ (i.e., a correction term proportional to $N^{-1/4}$), so that finite-$N$ results can be extrapolated to the thermodynamic limit by fitting to the form $F_l(N)=c+aN^{-1/4}$; this scaling is the same as that argued in the theoretical analyses of long-range-correlation finite-size effects (Holzmann et al.).",
    source_package="paper:867749664370197342",
)


gcn_3ceb44ae3f404964 = claim(
    "For Fermi-liquid-derived quantities of the two-dimensional homogeneous electron gas, such as angular-momentum Fermi-liquid parameters F_l or Fourier-projected F_l/m*, the leading finite-size error from long-range correlation is theoretically expected to scale as N^(-1/4), so fitting finite-N values to c+a N^(-1/4) estimates the thermodynamic-limit intercept [@Drummond2013b].",
    title='Theoretical N^-1/4 scaling premise',
    lkm_id="gcn_3ceb44ae3f404964",
    source_paper="paper:813209134949203971",
    provenance_source="lkm",
    lkm_original="For the two-dimensional homogeneous electron gas (2D HEG), the leading finite-size error in Fermi-liquid-derived quantities such as the angular-momentum Fermi liquid parameters F_l or the Fourier-projected quantities F_l/m^{*} behaves asymptotically as a power law in the finite-system particle number N with exponent -1/4; equivalently,\n      \\Delta F_l(N) \\equiv F_l(N)-F_l(\\infty) \\propto N^{-1/4},\n      so that fitting computed F_l(N) values to the form c + a N^{-1/4} yields an estimate of the thermodynamic-limit intercept c = F_l(\\infty). This statement adopts the theoretical asymptotic exponent \\gamma = -1/4 predicted for long-range-correlation-dominated finite-size errors.\n      Refs. 13,14",
    source_package="paper:813209134949203971",
)


gcn_3db07703d3684507 = claim(
    "DMC data for Fourier-projected Fermi-liquid quantities in the 2D HEG show large nonmonotonic finite-size fluctuations with N that exceed per-run statistical error bars. Although an N^(-1/4) finite-size scaling is globally consistent with the data, the fit quality is poor because shell-filling oscillations and related finite-size noise are not captured by the nominal statistical errors. Therefore, direct finite-cell QMC determination of Fermi-liquid parameters by simple power-law extrapolation has large uncertainties and can disagree with thermodynamic quantities inferred from ground-state energy parameterizations [@Drummond2013b].",
    title='Shell noise undermines direct FL extrapolation',
    lkm_id="gcn_3db07703d3684507",
    source_paper="paper:813209134949203971",
    provenance_source="lkm",
    lkm_original="The diffusion Monte Carlo data for Fourier-projected Fermi liquid quantities display large, nonmonotonic fluctuations as functions of finite-system particle number N that exceed the per-run statistical error bars: the statistical uncertainties from individual DMC runs are generally much smaller than the observed shell-filling oscillations and other finite-size \"noise.\" A theoretical finite-size scaling proportional to N^{-1/4} (the exponent -1/4 predicted for long-range-correlation-dominated finite-size errors) is consistent with all DMC data in a global fit (the best-fit common exponent found by simultaneous \\chi^2 fitting of the DMC data is \\gamma = -0.24(10)), but the fit quality is poor (\\chi^2 per data point \\gg 1) because the shell-filling oscillations and related finite-size noise are not captured by the statistical error bars; a naive ordinary least-squares fit with equal weighting of data points yields a very different effective exponent. Consequently, these finite-size effects constitute a serious obstacle to a quantitatively accurate, direct determination of Fermi liquid parameters from finite-cell QMC calculations: extrapolated Fermi liquid parameters obtained by simple power-law fits have large uncertainties and in many cases are inconsistent with related thermodynamic quantities obtained directly from parametrizations of the ground-state total energy per electron.",
    source_package="paper:813209134949203971",
)


gfac_b465826db1974ced = deduction(
    premises=[gcn_3ceb44ae3f404964],
    conclusion=gcn_3db07703d3684507,
    reason="1. Finite simulation cells discretize wave vectors and do not fully capture long-range Coulomb and correlation effects.\n2. Computed Fermi-liquid parameters show large shell-filling oscillations with N that exceed nominal DMC statistical error bars.\n3. Global fits using N^(-1/4) scaling give an exponent consistent with -1/4, but the reduced chi-squared remains poor because shell-filling noise is not represented by the per-run error bars.\n4. Unweighted fits give substantially different effective exponents, showing that the exponent is not robustly determined by the data alone.\n5. The authors use the theoretical exponent as a practical choice while explicitly retaining large extrapolation uncertainty.\n6. Consequently, direct finite-cell QMC extraction of Fermi-liquid parameters remains quantitatively unreliable without improved finite-size treatment.",
    prior=0.95,
)
gfac_b465826db1974ced.metadata.update(
    {
        "judgment": "accepted",
        "justification": "Accepted as an LKM factor-derived warrant: the evidence chain provides a usable N^(-1/4) premise, ordered method diagnostics, and a source-package anchor.",
    }
)


gcn_836bae7457044c7a = claim(
    "Combining published DMC quasiparticle effective masses with QMC-based ground-state energy parameterizations and Landau relations can yield pragmatic best-available estimates of 2D HEG Fermi-liquid parameters when direct thermodynamic-limit extrapolation of discrete-angle DMC F_l data is unreliable [@Drummond2013b].",
    title='Assembling best-available FL parameters',
    lkm_id="gcn_836bae7457044c7a",
    source_paper="paper:867749664370197342",
    provenance_source="lkm",
    lkm_original="The proposition: Taking quasiparticle effective masses $m^{*}$ reported in prior DMC energy-band calculations (for example, numerical values reported in the literature) and combining them with isothermal compressibility and spin-susceptibility ratios computed from QMC-based ground-state total-energy parameterizations, then solving the Landau relations\n      $$\n      \\frac{\\kappa}{\\kappa^{*}}=\\frac{1}{m^{*}}+\\frac{F_{0}^{s}}{m^{*}},\\qquad\n      \\frac{\\chi}{\\chi^{*}}=\\frac{1}{m^{*}}+\\frac{F_{0}^{a}}{m^{*}},\\qquad\n      m^{*}=1+F_{1}^{s}\\ \\text{(paramagnetic) or}\\ m^{*}=1+F_{1}\\ \\text{(ferromagnetic)},\n      $$\n      yields numerical values of the Fermi liquid parameters $F_0^{s}$, $F_0^{a}$, $F_1^{s}$ (paramagnetic) and $F_0$, $F_1$ (ferromagnetic) that serve as pragmatic “best available” recommendations when direct thermodynamic-limit determinations of $F_l$ from discrete-angle DMC data are unreliable; here all quantities are evaluated at the same density parameter $r_s$ and spin polarization $\\zeta$.\n      Ref. 11",
    source_package="paper:867749664370197342",
)


gcn_306f15c9d5814e23 = claim(
    "Because direct thermodynamic-limit extrapolation of discrete-angle DMC Fermi-liquid parameters proved unreliable, Drummond and Needs assembled best-available numerical recommendations by combining published DMC effective masses, QMC-based ground-state correlation-energy parameterizations, and Landau relations for compressibility, spin susceptibility, and effective mass [@Drummond2013b].",
    title='Recommended 2D HEG Fermi-liquid parameters',
    lkm_id="gcn_306f15c9d5814e23",
    source_paper="paper:867749664370197342",
    provenance_source="lkm",
    lkm_original="Because direct thermodynamic-limit extrapolation of the discrete-angle DMC-determined Fermi liquid parameters proved unreliable, a set of “best available” numerical recommendations for the Fermi liquid parameters was assembled by combining independently published QMC results for related quantities: quasiparticle effective masses $m^{*}$ obtained from DMC energy-band calculations and smooth QMC-based parameterizations of the ground-state correlation energy.  Using the literature effective masses together with compressibility and spin-susceptibility values derived from the total-energy parameterizations and the Landau relations yields recommended values such as, for the paramagnetic 2D HEG: at $r_{s}=1$, $F_{0}^{s}=-0.495(2)$, $F_{0}^{a}=-0.346(2)$, $F_{1}^{s}=-0.053(3)$; at $r_{s}=5$ and $10$ analogous recommended values are provided; and for the ferromagnetic 2D HEG recommended values include at $r_{s}=1$, $F_{0}=-0.428(2)$ and $\\bar{F}_1=-0.159(3)$.  These assembled values combine ground-state energy parameterizations and published effective masses to provide pragmatic numerical recommendations when direct thermodynamic-limit determinations of $F_l$ from discrete-angle DMC data are unreliable.",
    source_package="paper:867749664370197342",
)


gfac_4d2c6276f8304edb = deduction(
    premises=[gcn_836bae7457044c7a],
    conclusion=gcn_306f15c9d5814e23,
    reason="1. Direct thermodynamic extrapolation of DMC-determined Fermi-liquid parameters proved unreliable.\n2. The authors combine quasiparticle effective masses from earlier DMC band calculations with QMC correlation-energy parameterizations from the literature.\n3. Landau relations connect effective mass, compressibility, spin susceptibility, and Fermi-liquid parameters, enabling assembled estimates.\n4. The resulting best-available values are tabulated for paramagnetic and ferromagnetic 2D HEGs.\n5. The assembled values are recommended as practical benchmarks while preserving the caveat that they combine multiple data sources rather than a single direct thermodynamic-limit Landau-parameter calculation.",
    prior=0.95,
)
gfac_4d2c6276f8304edb.metadata.update(
    {
        "judgment": "accepted",
        "justification": "Accepted as an LKM factor-derived warrant for the best-available Fermi-liquid-parameter recommendation claim.",
    }
)
