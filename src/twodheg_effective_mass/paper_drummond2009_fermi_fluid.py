"""paper_drummond2009_fermi_fluid - earlier DMC band and mass claims."""
from gaia.lang import claim, deduction


gcn_4d1aad1470d54895 = claim(
    "Earlier DMC calculations for the two-dimensional homogeneous electron gas reported opposite density trends for different spin polarizations: in the paramagnetic 2D HEG, m* increased as r_s increased and showed significant enhancement at r_s=5 and r_s=10, whereas in the fully spin-polarized 2D HEG m* decreased as density was lowered; the reported trends were said to be quantitatively consistent with experimental observations [@Drummond2009].",
    title='Earlier DMC mass-enhancement trend',
    lkm_id="gcn_4d1aad1470d54895",
    source_paper="paper:811817724819800066",
    provenance_source="lkm_no_chain",
    lkm_original="The DMC-calculated quasiparticle effective mass exhibits opposite trends with density for the two spin polarizations studied: in the paramagnetic (unpolarized) 2D HEG $m^{*}$ increases with increasing $r_{s}$ (decreasing density), producing a significant enhancement at $r_{s}=5$ and $r_{s}=10$, whereas in the fully ferromagnetic (fully spin-polarized) 2D HEG $m^{*}$ decreases as density is lowered; these calculated trends are quantitatively consistent with the experimental observations of Tan et al. for paramagnetic systems and of Padmanabhan et al. for ferromagnetic or partially spin-polarized systems.",
    source_package="paper:811817724819800066",
)


gcn_f6686a4225a043a6 = claim(
    "For the interacting 2D HEG DMC energy-band data at r_s=1, 5, and 10, a quartic polynomial E(k)=alpha_0+alpha_2 k^2+alpha_4 k^4 captures the essential occupied-band curvature with fit residuals small compared with quoted uncertainties, so alpha_2, alpha_4, bandwidths, and derivative-derived m* estimates are accurate within stated errors [@Drummond2009].",
    title="Quartic fit captures occupied-band curvature",
    lkm_id="gcn_f6686a4225a043a6",
    source_paper="paper:811817724819800066",
    provenance_source="lkm",
    lkm_original="For the interacting 2D HEG energy-band data sets produced by DMC at the densities ($r_s=1,5,10$) and system sizes reported, truncating the band representation to a quartic polynomial in $k$, $\\mathcal{E}(k)=\\alpha_0+\\alpha_2 k^2+\\alpha_4 k^4$, captures the essential curvature: the least-squares fits yield residuals that are small compared with the quoted uncertainties, so that the fitted coefficients $\\alpha_2$ and $\\alpha_4$ and derived quantities (occupied bandwidth and derivative at $k_F$ used to obtain $m^{*}$) are accurate within the stated error bars and higher-order terms ($k^6$ and beyond) are negligible over the occupied $k$-range used for the reported extractions.",
    source_package="paper:811817724819800066",
)


gcn_fd7adbfff0f146ba = claim(
    "For the Slater-Jastrow-backflow nodal surfaces used in the 2D HEG DMC band calculations, fixed-node errors in total energies largely cancel in the many-body energy differences defining E(k), leaving residual node-driven bias in band values, bandwidths, and effective masses small compared with stated uncertainties [@Drummond2009].",
    title="Fixed-node errors mostly cancel in band differences",
    lkm_id="gcn_fd7adbfff0f146ba",
    source_paper="paper:811817724819800066",
    provenance_source="lkm",
    lkm_original="In fixed-node diffusion quantum Monte Carlo (DMC) the nodal surface of the trial wave function determines the fixed-node error in total energies; for the Slater-Jastrow-backflow nodal surfaces constructed from plane-wave determinants together with the reported Jastrow and backflow parameterizations at the studied densities and system sizes, the proposition is that the fixed-node error in total energies largely cancels in the many-body energy differences used to define the single-particle band $\\mathcal{E}(k)$, and the residual node-driven bias in the resulting band values and in derived quantities (occupied bandwidth and effective mass) is small compared with the stated uncertainties.",
    source_package="paper:811817724819800066",
)


gcn_bf915935b1fd4326 = claim(
    "The occupied single-particle energy band E(k) of the interacting 2D HEG was computed by DMC total-energy differences for adding or removing one electron in a plane-wave orbital, then described by a least-squares quartic E(k)=alpha_0+alpha_2 k^2+alpha_4 k^4. The fits show nonquadratic behavior: alpha_4 is positive for the paramagnetic fluid at r_s=5 and 10, negative for the ferromagnetic fluid at all studied densities, and nearly free-electron-like for the paramagnetic fluid at r_s=1 [@Drummond2009].",
    title="DMC occupied band shows nonquadratic curvature",
    lkm_id="gcn_bf915935b1fd4326",
    source_paper="paper:811817724819800066",
    provenance_source="lkm",
    lkm_original="The occupied single-particle energy band $\\mathcal{E}(k)$ of the interacting two-dimensional homogeneous electron gas (2D HEG) was computed using the diffusion quantum Monte Carlo (DMC) method by taking total-energy differences on adding or removing a single electron in a plane-wave orbital $\\exp(i\\mathbf{k}\\!\\cdot\\!\\mathbf{r})$; the resulting discrete DMC band values for the occupied states were described by a least-squares fit to the quartic form $\\mathcal{E}(k)=\\alpha_{0}+\\alpha_{2}k^{2}+\\alpha_{4}k^{4}$, where $\\alpha_{0}$, $\\alpha_{2}$, and $\\alpha_{4}$ are fitted coefficients.  These DMC calculations were performed for both the paramagnetic (unpolarized) and the ferromagnetic (fully spin-polarized) 2D HEGs at density-parameter values $r_{s}=1$, $5$, and $10$ (atomic units, where lengths are given in Bohr radii).  The fitted quartic shows clear nonquadratic behavior: for the paramagnetic fluid $\\alpha_{4}>0$ at $r_{s}=5$ and $r_{s}=10$, for the ferromagnetic fluid $\\alpha_{4}<0$ at all three densities studied, and for the paramagnetic fluid at $r_{s}=1$ the fitted DMC band is very close to the free-electron dispersion $\\mathcal{E}(k)=k^{2}/2$ (all energies in Hartree atomic units).",
    source_package="paper:811817724819800066",
)


gfac_de955cd831054c41 = deduction(
    premises=[gcn_f6686a4225a043a6, gcn_fd7adbfff0f146ba],
    conclusion=gcn_bf915935b1fd4326,
    reason="1. Use the established DMC add/remove protocol and quartic-band fitting approach.\n2. Define the DMC single-particle band from total-energy differences for adding or removing one electron in a plane-wave orbital.\n3. Use Slater-Jastrow-backflow trial wave functions and DMC calculations for paramagnetic and ferromagnetic 2D HEGs at r_s=1, 5, and 10.\n4. Fit occupied DMC band values to E(k)=alpha_0+alpha_2 k^2+alpha_4 k^4.\n5. Report nonquadratic band curvature: alpha_4>0 for paramagnetic r_s=5 and 10, alpha_4<0 for all ferromagnetic cases, and near-free-electron behavior for paramagnetic r_s=1.\n6. These quartic fits provide the band coefficients used for later bandwidth and effective-mass analysis.",
    prior=0.95,
)
gfac_de955cd831054c41.metadata.update(
    {
        "judgment": "accepted",
        "justification": "Accepted as an LKM factor-derived warrant for the earlier DMC occupied-band and quartic-curvature result.",
    }
)
