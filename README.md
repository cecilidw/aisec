# aisec

The inspiration for this example comes from a recent publication from Microsoft, "Secure the software development lifecycle with machine learning":
https://www.microsoft.com/security/blog/2020/04/16/secure-software-development-lifecycle-machine-learning/  

In this project the dataset contains 12 million work items and bugs. The ML model is built from classifying the dataset titles only. The goal was to separate security from non-security related bugs with high accuracy and of the security related ones labeling them into critical and high priority/non-critical. 

 We will be recreating a small example of this in code, but only for demo and educational purposes. The goal is to illustrate how this can be done and how AI can be used in the Security field. 

To be able to recreate an example of this we needed a sample dataset of bug reports labeled as security/non-security bugs. A dataset that suits the purpose has been published through this scientific article: 
https://www.sciencedirect.com/science/article/pii/S2352340918303226 It is  an open access article distributed under the terms of the Creative Commons CC-BY license, and the collected bug reports were categorized by a set of annotators of unknown reliability according to their impact from IBM's orthogonal defect classification taxonomy. We will be using the bug label "Integrity/Security " to represent the security label and all other labels are considered non-security. We extract only the fields that we will be using, the summary and label fields. The resulting dataset can be found in the "data" directory of this repository, in csv-format. It contains 962 rows. 


How to:

1. Clone or download this repo - this way you'll have the assets available to run locally.  

2. Follow the instructions for setting up an Azure Machine Learning Workspace from here: https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace 

3. Create a dataset through the AML Workspace UI by uploading the csvfile you find in the data folder of the repo. Call your dataset "SecBugDataset".

4. Instructions on how to set up to run on your local computer can be found here: https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#local. Perform all the steps up until the section "Visual Studio Code". If, at any time during the execution of the notebook the system complains that you have incompatible versions of pyarrow and pandas, add this to one of the notebook cells and execute:
!pip install azureml-dataprep[pandas] .

5. Now you are ready to run through the notebook with the example, from Jupyter on your local machine: 
