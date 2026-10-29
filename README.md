### Project Title: Predicting Significant Hazardous Liquid Pipeline Incidents

#### Executive summary

Pipeline failures can result in serious safety hazards, environmental damage, operational disruptions, and substantial financial losses. Proactively identifying pipeline operators at elevated risk of significant incidents can help improve pipeline integrity management and support more effective allocation of inspection and maintenance resources.

This project uses historical data from the Pipeline and Hazardous Materials Safety Administration (PHMSA) covering 2010–2025 to develop a machine-learning framework for predicting significant pipeline incidents one year in advance. By integrating annual pipeline infrastructure and operator information with historical incident outcomes, the project aims to identify patterns and risk factors associated with future pipeline failures.

#### Outline of project

- [Link to notebook](https://github.com/RaniDeepLearning/BH-AI-ML-Capstone-Project-24.1/blob/main/notebook/Pipeline_Cap.ipynb)

## Research question
 
Using each operator's annual report and incident history up to year *t*, can we rank hazardous liquid pipeline operators by their chance of a significant incident in year *t+1*, and which factors drive that ranking?
 
A significant incident is one with a fatality, a hospitalised injury, at least $50,000 in damage (1984 dollars), a large release, or a liquid release that causes a fire or explosion. This is PHMSA's own definition, taken from the `SIGNIFICANT` flag in the incident file.

## Data sources
 
The project uses publicly available data from PHMSA, a U.S. Department of Transportation agency responsible for pipeline safety oversight.
 
| Source | Files | Used for |
|---|---|---|
| PHMSA hazardous liquid annual reports, 2010–2025 | `data/raw/annual/annual_hazardous_liquid_YYYY.xlsx` | Operator size, volume, commodities, HCA miles, pipe installation decades (Part E) |
| PHMSA hazardous liquid incident file, 2010–present | `data/raw/incident/hl2010toPresent.xlsx` | Incident history and the next-year label |
 
The unit of analysis is the **operator-year**: one row per operator per year. After cleaning there are 8,135 operator-years. The modeling table has 7,571 operator-years from 2010–2024, of which 926 (12.2%) were followed by a significant incident the next year. The 2025 rows are held out for scoring. Incidents from 2026 were excluded because that year is only partly reported.
 
Source links:
- https://www.phmsa.dot.gov/data-and-statistics/pipeline/source-data
- https://www.phmsa.dot.gov/data-and-statistics/pipeline/distribution-transmission-gathering-lng-and-liquid-accident-and-incident-data

## Methodology
 
1. **Cleaning:** removed duplicate operator-years, checked for negative values and constant columns, and handled missing values.
2. **Target:** whether an operator had a significant incident in the following year.
3. **Split:** models are trained on 2010–2020 and tested on 2021–2024. The 2025 rows are held out.
4. **Exploratory analysis:** rates by pipeline size, earlier incidents, and Part E pipe share, with 95% intervals and chi-square tests.
5. **Feature engineering:** pipe age from the Part E decade columns, significant incidents in the last three years, and past incidents per mile.
6. **Feature selection:** forward selection on the training years only, using grouped cross-validation so that no operator appears in both training and validation folds. The selected features were stable across three fold seeds.
7. **Models:** logistic regression, gradient boosting, and random forest, each tuned by grid search with grouped cross-validation.
8. **Evaluation:** PR-AUC is the main metric, because only about 12% of rows are positive and accuracy would be misleading. ROC-AUC is a secondary check. Bootstrap intervals show whether differences are reliable.
9. **Interpretation:** odds ratios from logistic regression and permutation importance from gradient boosting.
10. **Threshold tuning:** a cutoff chosen on the training years to catch 80% of significant incidents, then checked once on the test years.

    
## Results
 
- **Size matters most.** Operators in the largest quarter by miles had a 38.0% next-year rate, against 1.3% for the smallest quarter.
- **Past incidents matter.** Operators with four or more earlier significant incidents had a 60.3% rate, against 5.0% for operators with none.
- **Selected features.** Forward selection chose four features: pipeline size, the share of pipe in high-consequence areas, past incidents per mile, and significant incidents in the last three years.
- **Model comparison (2021–2024).** The selected logistic regression reached PR-AUC 0.644, against 0.588 for size alone and 0.615 for the baseline. Gradient boosting (0.645) and random forest (0.641) were about the same, so the simpler logistic regression was chosen.
- **Gain over size alone.** The bootstrap interval for the gain is 0.000 to 0.054, so the improvement is suggestive, not clearly established.
- **Robustness.** Removing the two largest operators from both training and test years does not change the picture. Gradient boosting scores 0.601 with and without them.
- **Pipe age.** The share of older pipe adds nothing once size and incident history are included.
- **Threshold rule.** A cutoff of 0.485 catches 80% of significant incidents on the training years. On the test years it flags 532 of 2,262 operator-years, with recall 0.805 and precision 0.380.

## Next steps
 
- Measure risk per mile, so that large operators are not flagged only because they run more pipe.
- Score the 564 held-out 2025 operator-years with the final model, and check the results when the full 2026 incident data is available.
- Move to segment-level data (pipe age, material, and pressure by segment), which the original question needs.
- Extend the analysis to gas transmission pipelines.
- Add SHAP explanations if a more complex model is adopted later.

## Limitations
 
- The model works at the operator level. It says which operators are risky, not which pipe segment will fail.
- Pipe age is an estimate from the Part E decade columns. Their exact definition should be checked against PHMSA's form instructions.
- The test years contain only 251 significant incidents, so small differences between models are within the noise.
- Several candidate feature sets were compared on the test years, so the test results are slightly optimistic.
- Past incidents and the earlier-incident flag overlap (correlation about 0.78), so their odds ratios should be read together.
- The scores are balanced for class weight, so they rank operators but are not true probabilities.
- Only hazardous liquid pipelines are included. Gas pipelines are not covered.

## How to run the notebook
 
1. Install the libraries listed below.
2. Open `notebook/Pipeline_Cap.ipynb`. Start Jupyter from inside the `notebook` folder, because the notebook finds the project folder one level up.
3. Choose **Kernel → Restart & Run All**.
The notebook takes a few minutes, mostly for reading the Excel files and the cross-validation grid search. Random seeds are fixed, so results are repeatable.

## Optional: interactive explorer
 
`streamlit_app/app.py` shows the test-year risk scores in a browser. It lets you choose a year, flag the top N operator-years or everything above a cutoff, and see recall, precision and a trade-off curve.
 
To run it:
 
```
pip install streamlit pandas
cd streamlit_app
streamlit run app.py
```
 
The app is for learning and discussion. It is not a live prediction tool.


## Contact and Further Information

For more about this project, its methodology, findings, or applications of machine learning in pipeline safety, please contact the project author.
 
Data source: U.S. Department of Transportation, Pipeline and Hazardous Materials Safety Administration (PHMSA)

**Author:** Rani Kumari, UC Berkeley

