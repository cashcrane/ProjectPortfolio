# Construction Schedule Subcontractor Trade ML Classification System

## Overview
Schedulers at Brasfield & Gorrie, a **$7B+** General Contractor in the Southeast US, faced a significant challenge in assigning trade contractors to schedule activities—a task that required analyzing thousands of activities weekly and manually assigning trade labels. This process was time-intensive, prone to human error, diverted attention from higher-value scheduling tasks, and many times did not get done.

To address this, I developed a machine learning solution that automates the classification of scheduling activities by trade contractor. Using a Random Forest Classifier trained on **500,000+** records, the model achieves **98%** accuracy, ensuring reliable trade assignments with minimal effort.

Key client needs addressed:

Efficiency: Eliminated the **1.5-hour** weekly manual process per project scheduler.
Accuracy: Reduced errors by leveraging a robust machine learning model optimized for trade classification.
Scalability: Enabled the processing of thousands of schedule activities in seconds, making it suitable for large-scale projects.
The solution integrates seamlessly into existing workflows via a Vue.js-powered web app, allowing schedulers to upload Excel schedules exported from Primavera P6 scheduling software and receive trade-labeled outputs instantly. This innovation not only saves over **3,000** man-hours annually but also enables the data to be used for other purposes such as: Monte-Carlo Risk Simulations, ability to analyze Sub-Contractor's performance, create historical durations, and lay the foundations for automating professional construction schedule generation with AI.

## Tools & Technologies:
- **Python**: Pandas, numpy, Scikit-Learn, NLTK, re
- **ML File Handling**: pickle, h5
- **DataBricks SQL**: Cloud Data Storage
- **FastAPI**: Back-end deployment
- **Vue.js**: Front-end
- **Docker**: Containerization

## Data
The dataset includes 500,000 records of construction scheduling activities in every market vertical (Hospitals, Infrastructure, Apartments, Multi-Family, Data Centers, Office Buildings, etc.). Data was sourced from the clients proprietary data set of commercial construction projects all over the US.
- **Activity Name**: Text describing the work being done.
- **WBS Name**: Text describing the Work Breakdown Structure.
- **Trade Label**: The assigned sub-contractor scope of work (Electrical, Mechanical, etc.) (target variable). There were ~ 50 classes.
