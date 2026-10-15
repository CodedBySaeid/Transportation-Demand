# Transportation Demand Modeling: Mode Choice Analysis

## Overview

This project develops a discrete choice model to analyze transportation mode choice behavior using Python and [Biogeme](https://biogeme.epfl.ch/). The model estimates how travel time, travel cost, and traveler characteristics influence the choice among different transportation alternatives.

The project uses a **Multinomial Logit (MNL) model** to estimate the utility of each transportation mode and identify the factors influencing travelers' decisions.

## Objectives

- Model transportation mode choice using discrete choice theory.
- Estimate the influence of travel time and travel cost on transportation decisions.
- Examine the effects of socioeconomic characteristics, including gender, age, education, occupation, and household income.
- Represent public transportation access, in-vehicle travel, and waiting times separately.
- Evaluate the role of different transportation alternatives in travel demand analysis.

## Transportation Alternatives

The model includes the following alternatives:

| Choice Code | Transportation Mode |
|---|---|
| 1 | Car Driver |
| 2 | Car Passenger |
| 3 | Metro |
| 4 | Bus Rapid Transit (BRT) |
| 5 | Bus |
| 6 | Taxi |
| 7 | Snapp |
| 8 | Phone Taxi |
| 9 | Motorcycle |
| 10 | Bicycle |
| 11 | Walking |
| 12 | Service |
| 99 | Scooter + Public Transportation |

The availability of alternatives is incorporated into the model using availability indicators defined in the dataset and the model specification.

## Model Specification

The model assigns a systematic utility function to each transportation alternative. The utility functions include alternative-specific constants (ASCs) and selected explanatory variables.

### Travel attributes

- Travel time
- Travel cost
- Public transportation access time
- Public transportation in-vehicle time
- Public transportation waiting time
- Public transportation access cost

### Socioeconomic characteristics

The car-driver utility function includes dummy variables representing:

- Gender
- Age groups
- Education levels
- Occupation categories
- Household income categories

These variables allow the model to account for differences in preferences across traveler groups.

### Model estimation

The model is estimated using the Multinomial Logit formulation. The probability of choosing an available alternative is determined by its systematic utility relative to the utilities of the other available alternatives.

The parameters are estimated through maximum likelihood using Biogeme.

## Technologies Used

- **Python** — Model implementation and analysis
- **Pandas** — Data loading and data manipulation
- **NumPy** — Numerical computing
- **Biogeme** — Discrete choice model specification and estimation
- **Math** — Mathematical operations

## Project Structure

```text
transportation-demand-model/
│
├── DATABASE1.csv       # Input dataset (not necessarily included in the repository)
├── ModeChoice.py             # Model specification and estimation
├── README.md           # Project documentation
└── .gitignore          # Files excluded from version control
```

The Python script may be named differently in the repository. Update `ModeChoice.py` in this structure to match the actual filename.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/CodedBySaeid/Transportation-Demand.git
cd YOUR-REPOSITORY
```

Replace the URL with your repository's actual address.

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install pandas numpy biogeme
```

## Dataset

The model reads the input dataset from `DATABASE1.csv`:

```python
df = pd.read_csv("./DATABASE1.csv")
```

The dataset must contain all variables referenced in the model, including transportation attributes, availability indicators, the observed choice variable (`FINAL_CHOICE`), and socioeconomic variables.

The variable names and alternative coding in the dataset must match those used in the Python script.

**Note:** If the dataset contains personal, confidential, or restricted information, do not upload it publicly. Instead, provide an anonymized sample dataset or instructions for obtaining access.

## Running the Model

After installing the dependencies and placing the dataset in the expected location, run:

```bash
python ModeChoice.py
```

The script will:

1. Load the dataset.
2. Initialize the Biogeme database.
3. Define model parameters and explanatory variables.
4. Construct utility functions for the transportation alternatives.
5. Define alternative availability conditions.
6. Specify the Multinomial Logit choice probability.
7. Estimate model parameters.
8. Display the estimation results and parameter table.

The estimated parameters can be used to examine the direction and magnitude of the relationships between transportation attributes and mode choice, subject to their statistical significance and the model specification.

## Outputs

The script prints the Biogeme estimation results and an estimated-parameter table containing the model coefficients and associated statistical information provided by Biogeme.

The results can be used for further analysis of:

- Travel time and cost sensitivity
- Differences in transportation mode preferences
- The influence of socioeconomic characteristics
- Transportation demand and mode choice behavior

## Limitations and Future Improvements

Potential extensions to the project include:

- Adding safety and comfort attributes to the utility functions.
- Examining additional socioeconomic interactions across transportation modes.
- Testing alternative model specifications, including nested or mixed logit models.
- Evaluating model fit and predictive performance using appropriate validation methods.
- Conducting sensitivity analysis and transportation policy scenarios.
- Improving the representation of first- and last-mile access to public transportation.

The current specification uses common coefficients for some attributes across multiple alternatives. Further model development may examine whether alternative-specific coefficients or additional interactions are appropriate.

## License

No license has been specified yet. If you intend to make this project open source, consider adding a suitable license file to the repository.

## Acknowledgments

This project uses [Biogeme](https://biogeme.epfl.ch/), a Python package for estimating discrete choice models.
