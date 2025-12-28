# Meta-Learning for Cross-Domain Multi-Fidelity Optimization

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Research Framework](https://img.shields.io/badge/status-research%20framework-orange.svg)]()

> PhD Research Framework: Learning Transferable Fidelity Allocation Strategies Across Physical Domains

---

## 🎯 Overview

This repository contains the **complete framework** for my PhD research on **meta-learning for multi-fidelity optimization**. Unlike existing single-domain approaches, this work develops **domain-agnostic frameworks** that transfer across aerospace, robotics, materials science, and fluid dynamics.

### **Core Innovation**

Can we identify **causal (domain-invariant)** vs **correlational (domain-specific)** multi-fidelity relationships? Using causal discovery and meta-learning, we learn transferable strategies for combining cheap simulations with expensive experiments.

---

## 🔬 Research Questions

This framework addresses **five novel research questions**:

### **RQ1: Meta-Multi-Fidelity Learning**
Can we meta-learn fidelity allocation policies that generalize across domains?

**Framework:** `MAML-MF` - Model-Agnostic Meta-Learning for Multi-Fidelity  
**Location:** [`src/maml_mf/`](src/maml_mf/)

### **RQ2: Causal Fidelity Discovery**
Which multi-fidelity relationships are causal (transferable) vs correlational (domain-specific)?

**Framework:** `CausalMF` - Causal Multi-Fidelity Discovery  
**Location:** [`src/causal_mf/`](src/causal_mf/)

### **RQ3: Few-Shot Adaptation**
Can we adapt to new domains with <10 examples while maintaining performance guarantees?

**Framework:** `FewShotMF` - Few-Shot Multi-Fidelity Transfer  
**Location:** [`src/fewshot_mf/`](src/fewshot_mf/)

### **RQ4: Domain-Agnostic Active Learning**
Can we develop universal acquisition functions that account for domain shift?

**Framework:** `MetaBAES` - Meta-Learned Bayesian Experimental Selection  
**Location:** [`src/metabaes/`](src/metabaes/)

### **RQ5: Theoretical Transfer Bounds**
What are PAC-Bayes bounds for multi-domain multi-fidelity transfer?

**Framework:** `CrossMFALS` - Cross-Domain Multi-Fidelity Active Learning System  
**Location:** [`src/cross_mfals/`](src/cross_mfals/)

---

## 📁 Repository Structure

```
meta-learning-multi-fidelity/
│
├── src/                          # Source code for all frameworks
│   ├── maml_mf/                  # RQ1: MAML-MF
│   ├── causal_mf/                # RQ2: Causal Discovery
│   ├── fewshot_mf/               # RQ3: Few-Shot Learning
│   ├── metabaes/                 # RQ4: Active Learning
│   ├── cross_mfals/              # RQ5: Complete System
│   └── utils/                    # Shared utilities
│
├── experiments/                  # Experiment scripts for 4 domains
│   ├── aerospace/                # CFD, Wind Tunnel, Flight Tests
│   ├── robotics/                 # Sim-to-Real Transfer
│   ├── materials/                # DFT + Lab Synthesis
│   └── fluids/                   # RANS, LES, DNS
│
├── data/                         # Placeholder datasets
│   ├── placeholders/             # Sample data for each domain
│   └── meta_splits/              # Meta-train/meta-test splits
│
├── docs/                         # Documentation
│   ├── research_questions.md     # Detailed RQ descriptions
│   ├── methodology.md            # Methods for each RQ
│   ├── validation_plan.md        # 4-domain validation strategy
│   └── publication_strategy.md   # 10-12 publication roadmap
│
├── tests/                        # Unit tests for all frameworks
└── notebooks/                    # Jupyter notebook demos
```

---

## 🧪 Validation Strategy

### **Meta-Training (Months 1-24)**
- **Aerospace:** 1000 CFD simulations, 20 wind tunnel tests, 5 flight tests
- **Robotics:** 5000 rigid sims, 100 deformable sims, 20 real robot tests
- **Materials:** 2000 force field calcs, 50 DFT calcs, 10 lab syntheses

### **Meta-Testing (Months 25-36)**
- **Fluid Dynamics:** 500 RANS sims, 10 LES sims, 2 DNS sims
- **Few-Shot Adaptation:** k=5, 10 examples

### **Full Validation (Months 37-48)**
- Complete validation across all 4 domains
- Final experiments: 5 flights, 20 robots, 10 materials, 2 DNS

---

## 🚀 Key Features

### **1. Domain-Agnostic Framework**
- ✅ Learn on aerospace, robotics, materials
- ✅ Transfer to fluid dynamics with <10 examples
- ✅ Reduce expensive experiments by 80-90%

### **2. Causal Multi-Fidelity Analysis**
- ✅ Identify transferable (causal) relationships
- ✅ Separate domain-specific correlations
- ✅ Theoretical guarantees on transfer

### **3. Few-Shot Learning**
- ✅ Adapt to new domains rapidly
- ✅ Maintain performance with minimal data
- ✅ Meta-learned initialization strategies

### **4. Active Learning Integration**
- ✅ Meta-learned acquisition functions
- ✅ Domain-shift aware selection
- ✅ Bayesian uncertainty quantification

### **5. Theoretical Foundations**
- ✅ PAC-Bayes transfer bounds
- ✅ Convergence guarantees
- ✅ Sample complexity analysis

---

## 📊 Expected Impact

### **Computer Science Contributions**
- 5 theoretical results (PAC-Bayes bounds, convergence theorems)
- 5 CS theory publications (NeurIPS, ICML, ICLR, JMLR)
- New meta-learning paradigm for multi-fidelity optimization

### **Domain Applications**
- **Aerospace:** Reduce flight tests from 50 to 5 (90% cost reduction)
- **Robotics:** Reduce real robot trials from 100 to 10 (90% cost reduction)
- **Materials:** Reduce lab syntheses from 100 to 10 (90% cost reduction)
- **Fluids:** Reduce DNS from 20 to 2 (90% cost reduction)

### **Publications**
- 10-12 total papers across CS and domain venues
- Theory: NeurIPS, ICML, ICLR, JMLR
- Applications: AIAA, IEEE T-RO, Nature Comp. Materials, JCP
- Workshops: ICML-WS, CoRL, AAAI

---

## 🛠️ Installation

### **Requirements**
- Python 3.8+
- PyTorch 2.0+
- NumPy, SciPy
- GPyTorch (for Bayesian optimization)
- NetworkX (for causal graphs)

### **Setup**

```bash
# Clone repository
git clone https://github.com/[hmshujaatzaheer]/meta-learning-multi-fidelity.git
cd meta-learning-multi-fidelity

# Create conda environment
conda env create -f environment.yml
conda activate meta-mf

# Install package
pip install -e .
```

---

## 📚 Usage Examples

### **Example 1: Train MAML-MF on Aerospace**

```python
from src.maml_mf import MAMLOptimizer
from src.utils import load_domain_data

# Load aerospace data
train_tasks = load_domain_data('aerospace', split='train')

# Initialize MAML-MF
maml = MAMLOptimizer(
    inner_lr=0.01,
    outer_lr=0.001,
    num_inner_steps=5
)

# Meta-train
maml.meta_train(train_tasks, num_iterations=1000)

# Save meta-learned initialization
maml.save('checkpoints/maml_aerospace.pth')
```

### **Example 2: Few-Shot Transfer to Fluids**

```python
from src.fewshot_mf import FewShotAdapter

# Load pre-trained MAML model
adapter = FewShotAdapter.from_pretrained('checkpoints/maml_aerospace.pth')

# Few-shot adaptation with k=5 examples
fluids_support = load_domain_data('fluids', split='support', k=5)
adapter.adapt(fluids_support, num_steps=10)

# Evaluate on query set
fluids_query = load_domain_data('fluids', split='query')
performance = adapter.evaluate(fluids_query)

print(f"Few-shot performance: {performance}")
```

### **Example 3: Causal Discovery**

```python
from src.causal_mf import CausalDiscovery

# Load multi-domain data
domains = ['aerospace', 'robotics', 'materials']
multi_domain_data = [load_domain_data(d) for d in domains]

# Discover causal structure
causal_model = CausalDiscovery(algorithm='pc')
causal_graph = causal_model.discover(multi_domain_data)

# Identify transferable relationships
transferable = causal_model.identify_transferable(causal_graph)
print(f"Transferable relationships: {transferable}")
```

---

## 🧪 Running Experiments

### **Aerospace Experiments**

```bash
# CFD simulations (low fidelity)
python experiments/aerospace/cfd_simulation.py --num_samples 1000

# Wind tunnel tests (medium fidelity)
python experiments/aerospace/wind_tunnel.py --num_samples 20

# Flight tests (high fidelity)
python experiments/aerospace/flight_test.py --num_samples 5
```

### **Robotics Experiments**

```bash
# Rigid body simulations
python experiments/robotics/rigid_sim.py --num_samples 5000

# Deformable simulations
python experiments/robotics/deformable_sim.py --num_samples 100

# Real robot experiments
python experiments/robotics/real_robot.py --num_samples 20
```

### **Materials Experiments**

```bash
# Classical force field
python experiments/materials/force_field.py --num_samples 2000

# DFT calculations
python experiments/materials/dft_calc.py --num_samples 50

# Lab synthesis
python experiments/materials/lab_synthesis.py --num_samples 10
```

### **Fluid Dynamics Experiments**

```bash
# RANS (low fidelity)
python experiments/fluids/rans_simulation.py --num_samples 500

# LES (medium fidelity)
python experiments/fluids/les_simulation.py --num_samples 10

# DNS (high fidelity)
python experiments/fluids/dns_simulation.py --num_samples 2
```

---

## 📖 Documentation

Detailed documentation available in [`docs/`](docs/):

- [Research Questions](docs/research_questions.md) - Detailed description of all 5 RQs
- [Methodology](docs/methodology.md) - Methods for addressing each RQ
- [Validation Plan](docs/validation_plan.md) - 4-domain validation strategy
- [Publication Strategy](docs/publication_strategy.md) - 10-12 publication roadmap

---

## 🎓 Citation

If you use this framework in your research, please cite:

```bibtex
@misc{zaheer2025metalearning,
  author = {Zaheer, H M Shujaat},
  title = {Meta-Learning for Cross-Domain Multi-Fidelity Optimization},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/[hmshujaatzaheer]/meta-learning-multi-fidelity}}
}
```

---

## 📧 Contact

**H M Shujaat Zaheer**  
PhD Applicant - Meta-Learning & Multi-Fidelity Optimization  
Email: [shujabis.com]  


---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

This research framework builds upon recent advances in:
- Meta-learning (Finn et al., 2017; Nichol et al., 2018)
- Multi-fidelity optimization (Peherstorfer et al., 2018; Forrester et al., 2007)
- Causal inference (Pearl, 2009; Peters et al., 2017)
- Transfer learning (Pan & Yang, 2010; Weiss et al., 2016)

Special thanks to the research communities in machine learning, aerospace engineering, robotics, materials science, and computational fluid dynamics.

---

## 🚀 Status

**Current Status:** Research Framework (Pre-PhD)

This repository contains the **planned framework structure** for PhD research. All code templates are prepared and ready for implementation during the PhD program.

**Timeline:** 48 months (2025-2029)  
**Budget:** $210K-$250K  
**Expected Output:** 10-12 publications, 5 theoretical results, 4 domain validations

---

**🌟 Star this repository if you find it interesting!**

**🔔 Watch for updates as the research progresses!**

---

**Last Updated:** December 2024  
**Version:** 1.0.0 (Research Framework)
