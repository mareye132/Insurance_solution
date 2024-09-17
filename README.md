# Insurance_solution 

## Project Overview
This repository contains code and documentation for analyzing and modeling insurance data. The project involves tasks like Exploratory Data Analysis (EDA), Data Version Control (DVC), A/B Hypothesis Testing, and Statistical Modeling.

## Task 1: Git and GitHub
- **Repository Setup**:
  - Created a new Git repository and set up a `README.md` file.
  - Configured CI/CD with GitHub Actions for automated testing and deployment.
- **Branch Management**:
  - Created a branch called `task-1` for initial analysis.
  - Committed work with descriptive messages.
- **Key Features**:
  - Added files for exploratory data analysis: `Insurance_EDA.py` and `Insurance_Visualization.ipynb`.
- **KPIs**:
  - Demonstrated setup and usage of Git and GitHub effectively.

## Task 2: Data Version Control (DVC)
- **DVC Setup**:
  - Installed DVC using `pip install dvc`.
  - Initialized DVC in the project directory with `dvc init`.
  - Configured local remote storage for DVC with `dvc remote add -d localstorage /../storage`.
  - Added and committed data files using `dvc add MachineLearningRating.txt.
  - Pushed data to the local remote with `dvc push`.
- **Branch Management**:
  - Merged `task-1` into the main branch.
  - Created a new branch `task-2` for DVC tasks.
- **KPIs**:
  - Successfully managed data versions and tracked changes.

## Task 3: A/B Hypothesis Testing
- **Hypothesis Testing**:
  - Tested null hypotheses regarding risk differences across provinces, zip codes, and between genders.
  - Selected metrics, segmented data into control and test groups, and performed statistical tests (e.g., chi-squared, t-tests).
  - Analyzed and reported findings.
- **Branch Management**:
  - Merged `task-2` into the main branch.
  - Created a new branch `task-3` for hypothesis testing.
- **KPIs**:
  - Effectively applied statistical testing to evaluate hypotheses.

## Task 4: Statistical Modeling
- **Data Preparation**:
  - Handled missing data, engineered new features, encoded categorical data, and split data into training and test sets.
- **Modeling Techniques**:
  - Implemented Linear Regression, Decision Trees, Random Forests, and XGBoost.
- **Model Evaluation**:
  - Evaluated model performance using accuracy, precision, recall, and F1-score.
  - Analyzed feature importance and used SHAP or LIME for interpretability.
- **Branch Management**:
  - Merged `task-3` into the main branch.
  - Created a new branch `task-4` for modeling tasks.
- **KPIs**:
  - Successfully built, evaluated, and interpreted statistical models.
