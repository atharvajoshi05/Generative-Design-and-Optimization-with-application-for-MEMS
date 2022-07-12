﻿"""
# ==============================================================================
# ToPy -- Topology optimization with Python.
# ==============================================================================
"""

from .topology import *
from .visualisation import *
from .elements import *
from .topy_logging import *
from .optimisation import *

__version__ = "0.4.0"
__author__  = "William Hunter <whunter.za at gmail dot com>"

__all__ = (
	topology.__all__ +
	visualisation.__all__ +
	elements.__all__ +
	topy_logging.__all__ +
	optimisation.__all__
)
