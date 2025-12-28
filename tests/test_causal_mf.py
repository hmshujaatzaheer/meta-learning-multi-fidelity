"""
Unit tests for CausalMF

To be implemented during PhD.
"""

import pytest
from src.causal_mf import CausalDiscovery


def test_causal_discovery_initialization():
    """Test causal discovery initialization"""
    causal_model = CausalDiscovery(algorithm='pc', alpha=0.05)
    assert causal_model.algorithm == 'pc'
    assert causal_model.alpha == 0.05


def test_discover_structure():
    """Test causal structure discovery"""
    # To be implemented
    # Will test PC algorithm / GraN-DAG on synthetic data
    pass


def test_interventional_distribution():
    """Test do-calculus interventions"""
    # To be implemented
    # Will test do(X=x) interventions
    pass


def test_transfer_score():
    """Test transferability score computation"""
    # To be implemented
    # Will test edge transferability across domains
    pass
