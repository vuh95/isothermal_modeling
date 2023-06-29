# Isothermal Modeling in Ion Exchange and Absorption

This repository contains the code and data for isothermal modeling of ion exchange and absorption processes. Isothermal modeling is a method to describe the equilibrium relationship between the adsorbate concentration in the solution phase and the adsorbent phase. Isothermal models can provide information about the adsorption mechanisms, the maximum adsorption capacity, and the affinity of the adsorbent for the adsorbate.

## Introduction

Ion exchange and absorption are two important adsorption processes that can be used for water and wastewater treatment, separation and purification, and recovery of valuable metals. Ion exchange is a reversible process in which ions of the same charge are exchanged between a solid phase (ion exchanger) and a liquid phase (solution). Absorption is a process in which a substance (adsorbate) is transferred from a gas or liquid phase to a solid phase (adsorbent) due to intermolecular forces.

Isothermal models can be classified into three categories: chemical, physical, and ion exchange models. Chemical models describe the monolayer adsorption process, such as the Langmuir model. Physical models represent the multilayer adsorption process, such as the Brunauer-Emmett-Teller (BET) model. Ion exchange models can model the ion exchange adsorption process, such as the Gaines-Thomas model.

## Methods

The code in this repository implements various isotherm models for ion exchange and absorption processes, such as:

- Langmuir model
- Freundlich model
- Sips model
- BET model
- Gaines-Thomas model
- Donnan model

The code also provides functions to fit the models to experimental data, calculate the model parameters, evaluate the model performance, and plot the isotherms.

The data in this repository are from published literature sources that report experimental results of ion exchange and absorption processes for different systems, such as:

- Adsorption of Cu(II) ions onto zerovalent iron nanoparticles ¹
- Adsorption of Pb(II) ions onto activated carbon ²
- Ion exchange of Na+ and Ca2+ ions in zeolite ³

## Usage

To use the code in this repository, you need to install Python 3 and the following packages:

- numpy
- scipy
- pandas
- matplotlib

You can run the code in a Python interpreter or an interactive notebook (such as Jupyter Notebook). You can import the modules from the `isotherm` package and use the functions to create and fit isotherm models. For example:

```python
# Import modules
from isotherm import langmuir, freundlich, sips

# Create isotherm models
langmuir_model = langmuir.Langmuir()
freundlich_model = freundlich.Freundlich()
sips_model = sips.Sips()

# Load experimental data
data = pd.read_csv("data/cu_ii_zvi.csv")

# Fit models to data
langmuir_model.fit(data["Ce"], data["qe"])
freundlich_model.fit(data["Ce"], data["qe"])
sips_model.fit(data["Ce"], data["qe"])

# Print model parameters
print(langmuir_model.params)
print(freundlich_model.params)
print(sips_model.params)

# Plot isotherms
langmuir_model.plot()
freundlich_model.plot()
sips_model.plot()
```