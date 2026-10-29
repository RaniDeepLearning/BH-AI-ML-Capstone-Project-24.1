### Project Title: Predicting Significant Hazardous Liquid Pipeline Incidents

#### Executive summary

Pipeline failures can result in serious safety hazards, environmental damage, operational disruptions, and substantial financial losses. Proactively identifying pipeline operators at elevated risk of significant incidents can help improve pipeline integrity management and support more effective allocation of inspection and maintenance resources.

This project uses historical data from the Pipeline and Hazardous Materials Safety Administration (PHMSA) covering 2010–2025 to develop a machine-learning framework for predicting significant pipeline incidents one year in advance. By integrating annual pipeline infrastructure and operator information with historical incident outcomes, the project aims to identify patterns and risk factors associated with future pipeline failures.

#### Outline of project

- [Link to notebook](https://github.com/RaniDeepLearning/BH-AI-ML-Capstone-Project-24.1/blob/main/Pipeline_Cap.ipynb)

#### Data Sources
The project uses publicly available data from the Pipeline and Hazardous Materials Safety Administration (PHMSA), a U.S. Department of Transportation agency responsible for pipeline safety oversight.
The dataset covers 2010–2025 and combines historical pipeline incident records with pipeline infrastructure, operator, and operational information. After data integration and preprocessing, the dataset contains 9,633 operator-year records and 89 variables. The modeling dataset includes 7,571 records and 86 features.
The target variable indicates whether a pipeline operator experiences a significant incident in the following year. These data will be used for exploratory data analysis, feature engineering, and machine-learning model development to identify risk patterns and predict future significant incidents.

link to Datasource: 

https://www.phmsa.dot.gov/data-and-statistics/pipeline/source-data

https://www.phmsa.dot.gov/data-and-statistics/pipeline/distribution-transmission-gathering-lng-and-liquid-accident-and-incident-data



## What the notebook does
 
| Section | Content |
|---|---|
| 0–1 | Business understanding, imports and paths |
| 2–4 | Loads the annual reports and incident file, checks that incident years are complete |
| 5 | Builds the target: a significant incident in the following year |
| 6 | Data cleaning, missing values, outliers |
| 7 | Feature engineering, including the Part E pipe-age share |
| 8 | Exploratory analysis, with 95% intervals on the main comparisons |
| 9 | Baseline logistic regression and simple rules |
| 10 | Models: grouped cross-validation, grid search, forward feature selection, comparison, permutation importance and odds ratios |
| 11 | Threshold tuning: a cutoff chosen on the training years, checked once on the test years |
| 12–14 | Findings, recommendations and limitations |
 
**Training and test years.** Models are trained on 2010–2020 and tested on 2021–2024. The test years are used only for the final comparisons, never for choosing settings or features.

## Main results
 
- **Size matters most.** Operators in the largest quarter by miles had a 38.0% next-year rate, against 1.3% for the smallest quarter.
- **Past incidents matter.** Operators with four or more earlier significant incidents had a 60.3% rate, against 5.0% for operators with none.
- **Selected features.** Forward selection on the training years chose four features: pipeline size, the share of pipe in high-consequence areas, past incidents per mile, and significant incidents in the last three years.
- **Model comparison (2021–2024).** The selected logistic regression reached PR-AUC 0.644, against 0.588 for size alone and 0.615 for the baseline. Gradient boosting (0.645) and random forest (0.641) were about the same, so the simpler logistic regression was chosen.
- **Gain over size alone.** The bootstrap interval for the gain is 0.000 to 0.054, so the improvement is suggestive, not clearly established.
- **Pipe age.** The share of older pipe adds nothing once size and incident history are included.
- **Threshold rule.** A cutoff of 0.485 catches 80% of significant incidents on the training years. On the test years it flags 532 of 2,262 operator-years, with recall 0.805 and precision 0.380.

## Limitations
 
- The model works at the operator level. It says which operators are risky, not which pipe segment will fail.
- Pipe age is an estimate from the Part E decade columns. Their exact definition should be checked against PHMSA's form instructions.
- The test years contain only 251 significant incidents, so small differences between models are within the noise.
- Several candidate feature sets were compared on the test years, so the test results are slightly optimistic.
- Past incidents and the earlier-incident flag overlap (correlation about 0.78), so their odds ratios should be read together.
- The scores are balanced for class weight, so they rank operators but are not true probabilities.
- Only hazardous liquid pipelines are included. Gas pipelines are not covered.

## Optional: interactive explorer
 
`streamlit_app/app.py` shows the test-year risk scores in a browser. It lets you choose a year, flag the top N operator-years or everything above a cutoff, and see recall, precision and a trade-off curve.
 
To run it:
 
```
pip install streamlit pandas
cd streamlit_app
streamlit run app.py
```
 
The app is for learning and discussion. It is not a live prediction tool.


##### Contact and Further Information
**Author** Rani Kumari
