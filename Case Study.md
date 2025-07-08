Case 1: Biased Hiring Tool (Amazon Example)
🟢 Scenario:
Amazon developed an AI recruitment system that penalized female candidates, especially for technical roles. The system was trained on historical resumes submitted over 10 years, mostly from men.

✅ Tasks:
1. Identify the source of bias:

Training Data Bias: The data reflected historical gender imbalances in tech roles.

Model Design: The model learned from biased examples, associating certain keywords (e.g., “women’s college”) with lower scores.

2. Propose three fixes to make the tool fairer:

Balanced Dataset: Retrain the model using a gender-balanced dataset with equivalent representation from different backgrounds.

Feature Filtering: Exclude sensitive features or proxies for gender (e.g., names, clubs, colleges).

Fairness-Aware Training: Use fairness constraints during model training (e.g., equal opportunity classifiers).

3. Suggest fairness metrics to evaluate post-correction:

Disparate Impact Ratio: Checks if outcomes differ significantly across gender.

Equal Opportunity Difference: Compares true positive rates across groups.

Statistical Parity Difference: Measures selection rates between groups.

 Case 2: Facial Recognition in Policing
🟢 Scenario:
Facial recognition systems used by law enforcement misidentify minorities more often, leading to wrongful arrests and discrimination.

✅ Tasks:
1. Discuss ethical risks:

Wrongful Arrests: Misidentification may lead to unjust legal consequences.

Lack of Consent: People are often scanned without permission.

Discrimination: Systems may reinforce systemic racial biases.

2. Recommend policies for responsible deployment:

Audit & Certification: Require independent bias audits before deployment.

Strict Use Guidelines: Limit use to specific, regulated scenarios (e.g., terrorism prevention).

Human-in-the-Loop: Always require human review before acting on AI identification.

Transparency Reports: Publish reports on accuracy rates and usage breakdown by race and gender.

