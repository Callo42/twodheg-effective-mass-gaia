"""priors.py - leaf-claim priors for this package."""
from .paper_holzmann2008 import gcn_da3eecec49114543
from .paper_drummond2013_fermi_liquid import (
    gcn_219b34bd252c43fa,
    gcn_3ceb44ae3f404964,
    gcn_836bae7457044c7a,
)
from .paper_drummond2013_effective_mass import (
    gcn_1e8fcb7ef934428d,
    gcn_48797cba2bf44d90,
    gcn_50e263dc961541e0,
    gcn_850fc9d9de314026,
)
from .paper_drummond2009_fermi_fluid import gcn_4d1aad1470d54895
from .paper_drummond2012_effective_mass import (
    gcn_17c63b5dc2154f15,
    gcn_a685639571304474,
)

PRIORS = {
    gcn_da3eecec49114543: (
        0.82,
        "LKM chain premise from Holzmann et al. 2008 analytic finite-size correction; specific derivation claim with clear provenance, pending reviewer calibration. TODO:review",
    ),
    gcn_219b34bd252c43fa: (
        0.78,
        "LKM no-chain source claim from Drummond/Needs Fermi-liquid-parameter work; same-system finite-size scaling statement with clear provenance, but no standalone evidence chain. TODO:review",
    ),
    gcn_850fc9d9de314026: (
        0.76,
        "LKM no-chain source claim from Drummond/Needs effective-mass context; plausible finite-cell DMC bias mechanism, but no standalone evidence chain. TODO:review",
    ),
    gcn_4d1aad1470d54895: (
        0.68,
        "LKM no-chain source claim summarizing earlier DMC effective-mass enhancement trend; kept with lower confidence because later finite-size extrapolation appears to revise it. TODO:review",
    ),
    gcn_a685639571304474: (
        0.75,
        "LKM chain premise about Monte Carlo resampling uncertainty for finite-size extrapolation; clear but model-selection caveat remains. TODO:review",
    ),
    gcn_17c63b5dc2154f15: (
        0.72,
        "LKM chain premise about residual fixed-node/time-step biases being small relative to finite-size extrapolation uncertainty; method-specific numerical judgment. TODO:review",
    ),
    gcn_3ceb44ae3f404964: (
        0.78,
        "LKM chain premise for theoretical N^(-1/4) finite-size scaling of 2D HEG Fermi-liquid-derived quantities; scope-limited by later shell-filling-noise caveat. TODO:review",
    ),
    gcn_836bae7457044c7a: (
        0.74,
        "LKM chain premise for assembling best-available Fermi-liquid parameters from effective masses, energy parameterizations, and Landau relations when direct extrapolation is unreliable. TODO:review",
    ),
    gcn_48797cba2bf44d90: (
        0.78,
        "LKM chain premise for quartic-band derivative extraction of m* from finite-N DMC band data; method-specific and pending reviewer calibration. TODO:review",
    ),
    gcn_1e8fcb7ef934428d: (
        0.75,
        "LKM chain premise for single-power-law finite-size extrapolation of m*(N); carries model-adequacy caveats. TODO:review",
    ),
    gcn_50e263dc961541e0: (
        0.76,
        "LKM chain premise that a moderately wide k-window stabilizes quartic-band effective-mass fits against near-k_F fluctuations. TODO:review",
    ),
}
