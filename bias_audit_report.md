We analyzed the COMPAS Recidivism Dataset using IBM’s AI Fairness 360 toolkit. The primary focus was to evaluate racial bias in the risk assessment scores used to predict recidivism.

Our bias metrics showed:

Disparate Impact value significantly below 1, indicating unfair treatment toward the unprivileged group (typically Black individuals).

Mean Difference also confirmed the scoring disparities, which may result in unjustly high risk classifications.

This kind of algorithmic bias can lead to real-world harms, such as extended prison sentences or parole denials for certain racial groups.

To mitigate this:

Reweighing algorithms like the one in AIF360 can balance the dataset.

Removing sensitive features during training can reduce bias propagation.

Human-in-the-loop systems should validate AI decisions.

Fairness auditing is critical to prevent institutionalizing racial discrimination through AI. Continuous monitoring and transparent reporting are essential.

