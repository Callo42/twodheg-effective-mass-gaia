"""cross_paper - cross-paper supports and contradictions for the 2D HEG mass graph."""
from gaia.lang import contradiction, equivalence, support

from .paper_holzmann2008 import gcn_28b9e01bd2f8487f
from .paper_drummond2013_fermi_liquid import (
    gcn_219b34bd252c43fa,
    gcn_3db07703d3684507,
)
from .paper_drummond2013_effective_mass import (
    gcn_50e263dc961541e0,
    gcn_8df2cd5b49524aac,
    gcn_850fc9d9de314026,
    gcn_a981a2b787514e47,
)
from .paper_drummond2009_fermi_fluid import (
    gcn_318b062f17344859,
    gcn_4d1aad1470d54895,
    gcn_bf915935b1fd4326,
)
from .paper_drummond2012_effective_mass import gcn_b7a7d456a05d4129


n_quarter_scaling_supports_root = support(
    premises=[gcn_219b34bd252c43fa],
    conclusion=gcn_28b9e01bd2f8487f,
    reason=(
        "The Fermi-liquid-parameter claim independently identifies N^(-1/4) "
        "long-range-correlation finite-size scaling in the same 2D HEG "
        "simulation setting, supporting the root claim that slow finite-size "
        "corrections matter for effective-mass extrapolation."
    ),
    prior=0.82,
)
n_quarter_scaling_supports_root.metadata.update(
    {
        "judgment": "accepted",
        "justification": (
            "Accepted as a same-system support edge; it reinforces the finite-size "
            "scaling component of the root without duplicating the root evidence chain."
        ),
    }
)

excited_state_reoptimization_supports_root = support(
    premises=[gcn_850fc9d9de314026],
    conclusion=gcn_28b9e01bd2f8487f,
    reason=(
        "The excited-state reoptimization claim identifies a separate finite-cell "
        "mechanism that can bias excitation bandwidths and thus effective-mass "
        "extraction, supporting the root claim that finite-size treatment can "
        "change inferred m* behavior."
    ),
    prior=0.76,
)
excited_state_reoptimization_supports_root.metadata.update(
    {
        "judgment": "accepted",
        "justification": (
            "Accepted as a moderate same-method support edge because it concerns "
            "finite-cell DMC excitation-band bias in the same 2D HEG effective-mass workflow."
        ),
    }
)

band_fit_protocol_supports_benchmarks = support(
    premises=[gcn_a981a2b787514e47],
    conclusion=gcn_b7a7d456a05d4129,
    reason=(
        "The band-fit protocol claim states the extraction workflow that turns "
        "finite-N DMC band data into thermodynamic-limit m*(infinity) values; this "
        "directly supports the later benchmark claim reporting those extrapolated values."
    ),
    prior=0.84,
)
band_fit_protocol_supports_benchmarks.metadata.update(
    {
        "judgment": "accepted",
        "justification": (
            "Accepted as a strong same-paper/method support edge from the DMC band-fitting "
            "protocol to the reported thermodynamic-limit benchmark values."
        ),
    }
)

derivative_pathology_supports_wide_window = support(
    premises=[gcn_8df2cd5b49524aac],
    conclusion=gcn_50e263dc961541e0,
    reason=(
        "The near-k_F derivative-pathology claim explains why very narrow derivative "
        "estimates are unstable, directly supporting the wide-k-window premise used "
        "to stabilize quartic band fits."
    ),
    prior=0.88,
)
derivative_pathology_supports_wide_window.metadata.update(
    {
        "judgment": "accepted",
        "justification": (
            "Accepted as a same-paper mechanistic support edge from the diagnosed "
            "near-k_F pathology to the wide-window fitting prescription."
        ),
    }
)

occupied_band_supports_band_fit_protocol = support(
    premises=[gcn_bf915935b1fd4326],
    conclusion=gcn_a981a2b787514e47,
    reason=(
        "The older DMC occupied-band result shows that add/remove DMC energies can "
        "be represented by quartic band fits with meaningful curvature, supporting "
        "the later protocol that uses fitted band derivatives and finite-size extrapolation."
    ),
    prior=0.74,
)
occupied_band_supports_band_fit_protocol.metadata.update(
    {
        "judgment": "accepted",
        "justification": (
            "Accepted as moderate historical-method support because the older occupied-band "
            "calculation grounds the quartic band-fitting component of the later protocol."
        ),
    }
)

occupied_band_supports_nonquadratic_thermodynamics = support(
    premises=[gcn_bf915935b1fd4326],
    conclusion=gcn_318b062f17344859,
    reason=(
        "The occupied-band result establishes the fitted quartic DMC band curvature, "
        "which supports the later claim that nonquadratic curvature can modify "
        "thermodynamic properties depending on band integrals."
    ),
    prior=0.80,
)
occupied_band_supports_nonquadratic_thermodynamics.metadata.update(
    {
        "judgment": "accepted",
        "justification": (
            "Accepted as same-paper support from the observed quartic band curvature "
            "to its thermodynamic implication."
        ),
    }
)

older_dmc_enhancement_vs_revised_dmc_benchmarks = contradiction(
    gcn_4d1aad1470d54895,
    gcn_b7a7d456a05d4129,
    reason=(
        "The older DMC claim says paramagnetic 2D HEG m* shows significant "
        "enhancement at r_s=5 and r_s=10, while the later benchmark claim reports "
        "thermodynamic-limit paramagnetic values 1.04(2) and 1.03(4), close to unity. "
        "| open_problem: Does the apparent paramagnetic low-density 2D HEG mass "
        "enhancement in earlier DMC survive the later high-precision finite-size "
        "extrapolation protocol, or is it removed by revised finite-size/statistical treatment?"
    ),
    prior=0.84,
)
older_dmc_enhancement_vs_revised_dmc_benchmarks.content = (
    "not_both_true(older_paramagnetic_dmc_mass_enhancement, "
    "revised_near_unity_dmc_thermodynamic_benchmarks)"
)
older_dmc_enhancement_vs_revised_dmc_benchmarks.title = 'Older enhancement vs revised benchmarks'
older_dmc_enhancement_vs_revised_dmc_benchmarks.metadata.update(
    {
        "judgment": "accepted",
        "justification": (
            "Accepted as a weak scientific_inconsistency: the claims address the same "
            "field-facing paramagnetic 2D HEG effective-mass question, but the tension "
            "is best read as a methodological revision under improved finite-size/statistical treatment."
        ),
        "relation_type": "scientific_inconsistency",
    }
)

n_quarter_scaling_vs_shell_filling_noise = contradiction(
    gcn_219b34bd252c43fa,
    gcn_3db07703d3684507,
    reason=(
        "The N^(-1/4) scaling claim says finite-N Fermi-liquid-derived quantities "
        "can be extrapolated by fitting c+a N^(-1/4), while the shell-noise claim "
        "says the same nominal scaling is only globally consistent with poor fit "
        "quality because shell-filling oscillations exceed statistical errors and "
        "make direct Fermi-liquid-parameter extrapolations quantitatively unreliable. "
        "| open_problem: When does the theoretical N^(-1/4) finite-size law become "
        "a reliable extrapolation protocol rather than only an asymptotic guide "
        "overwhelmed by shell-filling noise?"
    ),
    prior=0.82,
)
n_quarter_scaling_vs_shell_filling_noise.content = (
    "not_both_true(n_quarter_finite_size_scaling_as_extrapolation_protocol, "
    "shell_filling_noise_makes_direct_extrapolation_unreliable)"
)
n_quarter_scaling_vs_shell_filling_noise.title = 'N^-1/4 scaling vs shell-filling noise'
n_quarter_scaling_vs_shell_filling_noise.metadata.update(
    {
        "judgment": "accepted",
        "justification": (
            "Accepted as a weak scientific_inconsistency: both claims address the same "
            "Fermi-liquid-parameter extrapolation protocol, but the tension is a limitation "
            "on practical use of the asymptotic law rather than a dispute over whether the law exists."
        ),
        "relation_type": "scientific_inconsistency",
    }
)
