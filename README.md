### Project Title: Predicting and Explaining Severe Pipeline Incidents Using Machine Learning 

**Author** Rani Kumari

#### Executive summary

Pipeline failures can result in serious safety hazards, environmental damage, operational disruptions, and substantial financial losses. Proactively identifying pipeline operators at elevated risk of significant incidents can help improve pipeline integrity management and support more effective allocation of inspection and maintenance resources.

This project uses historical data from the Pipeline and Hazardous Materials Safety Administration (PHMSA) covering 2010–2025 to develop a machine-learning framework for predicting significant pipeline incidents one year in advance. By integrating annual pipeline infrastructure and operator information with historical incident outcomes, the project aims to identify patterns and risk factors associated with future pipeline failures.

#### Rationale
People should care about this question because a significant pipeline incident can cause fatalities, environmental damage, costly service disruptions, and millions of dollars in losses.
The value of this project is its focus on early warning rather than simply explaining past incidents. By using historical PHMSA data and machine learning, the project aims to identify patterns associated with future incidents, helping pipeline operators and regulators prioritize higher-risk areas and make more informed, data-driven decisions.

#### Research Question
Can machine learning models use historical PHMSA pipeline data, infrastructure characteristics, and operational indicators to predict whether a pipeline operator will experience a significant incident in the following year, and which factors are most strongly associated with that risk?

#### Data Sources
The project uses publicly available data from the Pipeline and Hazardous Materials Safety Administration (PHMSA), a U.S. Department of Transportation agency responsible for pipeline safety oversight.
The dataset covers 2010–2025 and combines historical pipeline incident records with pipeline infrastructure, operator, and operational information. After data integration and preprocessing, the dataset contains 9,633 operator-year records and 89 variables. The modeling dataset includes 7,571 records and 86 features.
The target variable indicates whether a pipeline operator experiences a significant incident in the following year. These data will be used for exploratory data analysis, feature engineering, and machine-learning model development to identify risk patterns and predict future significant incidents.

link to Datasource: 

https://www.phmsa.dot.gov/data-and-statistics/pipeline/source-data

https://www.phmsa.dot.gov/data-and-statistics/pipeline/distribution-transmission-gathering-lng-and-liquid-accident-and-incident-data


#### Methodology
The project will follow a structured machine-learning workflow:
1. Data cleaning and preprocessing: Handle missing values, remove inconsistencies, and prepare the integrated PHMSA dataset for analysis.
2. Exploratory data analysis (EDA): Examine incident trends, pipeline characteristics, and differences between operators with and without significant incidents.
3. Feature engineering: Create relevant predictors from historical incident records, infrastructure characteristics, and operational variables to forecast incidents one year ahead.
4. Model development: Establish a baseline using logistic regression and compare its performance with decision trees, random forests, and gradient-boosting models.
5. Model evaluation: Address class imbalance and evaluate performance using precision, recall, F1-score, precision-recall AUC, and balanced accuracy. Use chronological validation to assess performance on future years.
6. Interpretation and recommendations: Identify the most influential risk factors and translate model findings into actionable insights for pipeline safety and resource prioritization.
The ultimate goal is to develop a reliable, interpretable predictive model that helps identify operators at elevated risk of significant pipeline incidents before they occur.

#### Results
The exploratory analysis identified a class imbalance in the modeling dataset: 926 of 7,571 observations (12.23%) were associated with a significant pipeline incident in the following year, while 6,645 observations (87.77%) had no significant incident. This highlights the importance of using evaluation metrics beyond accuracy when developing predictive models.
The project has established a foundation for comparing machine-learning algorithms to predict future significant pipeline incidents using historical PHMSA data. The next steps are to evaluate model performance, identify the most influential risk factors, and determine how effectively the models can identify high-risk operators

#### Next steps
Complete model development: Train and compare logistic regression, random forest, and gradient-boosting models to identify the most effective approach for predicting significant pipeline incidents.
Address class imbalance: Apply appropriate techniques, such as class weighting or resampling, to improve the identification of operators at elevated risk.
Validate predictive performance: Use chronological validation to test how well the models predict incidents in future years, evaluating recall, precision, F1-score, and precision-recall AUC.
Identify key risk factors: Use feature importance and SHAP analysis to understand which infrastructure, operational, and historical incident characteristics contribute most to predictions.
Develop actionable recommendations: Translate the findings into risk-prioritization strategies that can help pipeline operators and regulators allocate inspection and maintenance resources more effectively.

#### Outline of project

- [Link to notebook](https://github.com/RaniDeepLearning/BH-AI-ML-Capstone-Project-24.1/blob/main/Pipeline_Cap.ipynb)

##### Contact and Further Information
For further information about this project, its methodology, findings, or potential applications of machine learning in pipeline safety, please contact the project author.

Project: Predicting Significant Oil and Gas Pipeline Incidents Using Machine Learning
Data Source: U.S. Department of Transportation, Pipeline and Hazardous Materials Safety Administration (PHMSA)
Further Information: Project documentation, exploratory data analysis, model development, and evaluation results will be available as the analysis progresses.
