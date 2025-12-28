# Research Questions

This document details the five research questions addressed by this PhD research.

---

## RQ1: Meta-Multi-Fidelity Learning

**Question:** Can we meta-learn fidelity allocation policies that generalize across domains?

**Motivation:**
- Current multi-fidelity methods are domain-specific (Du 2025, Bussemaker 2025)
- Each new domain requires complete re-training
- No transfer of learned strategies

**Approach:**
- Apply MAML (Finn et al., 2017) to multi-fidelity optimization
- Learn meta-initialization θ that adapts quickly to new domains
- Inner loop: Task-specific fidelity allocation
- Outer loop: Meta-optimization across domains

**Expected Contribution:**
- First meta-learning framework for multi-fidelity optimization
- Theoretical analysis of generalization bounds
- Empirical validation across 4 domains

**Implementation:** `src/maml_mf/`

---

## RQ2: Causal Fidelity Discovery

**Question:** Which multi-fidelity relationships are causal (transferable) vs correlational (domain-specific)?

**Motivation:**
- Some fidelity relationships transfer across domains (causal)
- Others are domain-specific spurious correlations
- No existing method distinguishes between them

**Approach:**
- Use causal discovery (PC algorithm, GraN-DAG)
- Learn DAG G = (V, E) from multi-domain data
- Apply do-calculus interventions to test causality
- Identify domain-invariant vs domain-specific edges

**Expected Contribution:**
- Causal framework for multi-fidelity systems
- Method to identify transferable structures
- Theoretical guarantees under faithfulness assumption

**Implementation:** `src/causal_mf/`

---

## RQ3: Few-Shot Adaptation

**Question:** Can we adapt to new domains with <10 examples while maintaining performance guarantees?

**Motivation:**
- High-fidelity data is extremely expensive
- Want to transfer with minimal target domain data
- Need theoretical performance guarantees

**Approach:**
- Use meta-learned initialization from RQ1
- Adapt with k=5, 10 support examples
- Derive PAC-Bayes bounds on target performance
- Bound: R(θ') ≤ R(θ) + O(√(k log n / k))

**Expected Contribution:**
- Few-shot transfer for multi-fidelity optimization
- PAC-Bayes theoretical guarantees
- Empirical validation on fluid dynamics

**Implementation:** `src/fewshot_mf/`

---

## RQ4: Domain-Agnostic Active Learning

**Question:** Can we develop universal acquisition functions that account for domain shift?

**Motivation:**
- Standard acquisition functions don't transfer across domains
- Need to account for domain shift in uncertainty
- Want single acquisition function that works everywhere

**Approach:**
- Meta-learn acquisition function across domains
- Neural network: a_φ(x, m, D_train, D_domain)
- Account for:
  - Epistemic uncertainty (exploration)
  - Expected improvement (exploitation)
  - Cost-benefit analysis
  - Domain shift correction

**Expected Contribution:**
- First meta-learned acquisition for multi-fidelity
- Domain-shift aware uncertainty quantification
- Unified framework for active learning

**Implementation:** `src/metabaes/`

---

## RQ5: Theoretical Transfer Bounds

**Question:** What are PAC-Bayes bounds for multi-domain multi-fidelity transfer?

**Motivation:**
- Need theoretical guarantees on transfer
- Understand when transfer will succeed/fail
- Guide experimental design

**Approach:**
- Derive PAC-Bayes bounds for multi-task learning
- Account for:
  - Domain complexity
  - Number of source domains
  - Number of target examples
  - Fidelity structure
  
**Expected Results:**
- 5 theoretical theorems (see proposal)
- Sample complexity bounds
- Convergence guarantees

**Implementation:** Integrated in `src/cross_mfals/`

---

## Integration

All 5 RQs integrate into **CrossMFALS**:
1. RQ1 provides meta-initialization
2. RQ2 identifies transferable structure
3. RQ3 enables few-shot adaptation
4. RQ4 selects optimal experiments
5. RQ5 provides theoretical guarantees

Complete system in `src/cross_mfals/system.py`

