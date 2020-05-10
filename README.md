# AiSec

## Overview

The inspiration for this example comes from a recent publication from Microsoft, "Secure the software development lifecycle with machine learning":
https://www.microsoft.com/security/blog/2020/04/16/secure-software-development-lifecycle-machine-learning/  

In this project the dataset contains 12 million work items and bugs. The ML model is built from classifying the dataset titles only. The goal was to separate security from non-security related bugs with high accuracy and of the security related ones labeling them into critical and high priority/non-critical. 

 We will be recreating a small example of this in code, but only for demo and educational purposes. The goal is to illustrate how this can be done and how AI can be used in the Security field. 

To be able to recreate an example of this we needed a sample dataset of bug reports labeled as security/non-security bugs. A dataset that suits the purpose has been published through this scientific article: ["Two datasets of defect reports labeled by a crowd of annotators of unknown reliability"](https://www.sciencedirect.com/science/article/pii/S2352340918303226). It is an open access article distributed under the terms of the Creative Commons [CC-BY license](https://creativecommons.org/licenses/by/4.0/), and the collected bug reports were categorized by a set of annotators of unknown reliability according to their impact from IBM's orthogonal defect classification taxonomy. 

We will be using the bug label "Integrity/Security " to represent the security label and all other labels are considered non-security. We extract only the fields that we will be using, the summary and label fields. The resulting dataset can be found in the "data" directory of this repository, in csv-format. It contains 962 rows. 


## How to guideline

1. Clone or download [this repository](https://github.com/cecilidw/aisec) - this way you'll have the assets available to run locally. You will need at least "AISec Tutorial.ipynb" locally
2. Follow the instructions for setting up an Azure Machine Learning Workspace from [MS documentation](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace). You will create Machine Learning resources in your Azure subscription 
3. Then the Azure Machine Learning environment is ready navigate to your resources and open Azure Machine Learning UI by clicking `Experiments -> Launch the studio (Preview)`. Now you will create dataset through this interface by uploading "secBugData.csv" located in "data" folder of cloned repository. Give a name "SecBugDataser" for your dataset. To do this follow these steps:
     * Choose `Create dataset -> from local files` under `Assets -> Datasets` menu on the left side
     ![Create dataset from local file](docs/images/createdataset0.jpg)
     * Give your dataset a name, "SecBugDataset" and leave other fields defaults. Press `Next`
     ![Give your data set a name](docs/images/createdataset1.jpg)
     * Choose `Previously created datastore` and `workspaceblobstore`. This is the default storage that was created with your workspace. Then under `Select files for your dataset` press `Browse` and upload file "secBugData.csv" located under "data" folder in the cloned repository. After file is uploaded you will see it under the `File name`. Press `Next`  
     ![Give your data set a name](docs/images/createdataset2.jpg)
     * On the next step `Settings and preview` you will see loaded data set as table with columns. Leave all settings defaults except `Column headers`. Choose `All files have same headers` under the `Column headers` in the dropdown menu. Press `Next`
     ![Give your data set a name](docs/images/createdataset3.jpg)
     * On the next step `Schema` go with the default settings and click `Next`
     ![Give your data set a name](docs/images/createdataset4.jpg)
     * On the last step review and confirm details by pressing `Create`
     ![Give your data set a name](docs/images/createdataset5.jpg)
     * You will see the confirmation that the data set has been created successfully.

4. Now it is a time to configure a development environment for Azure Machine Learning on your computer. Follow the instructions on how to set up from [Microsoft documentation](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#local). 
   
   **NOTE**: When you get to the step where you will start Jupyter by the command `jupyter notebook`, make sure you have navigated to the folder you cloned/downloaded in **Step 1**. Perform all the steps up until the section "Visual Studio Code". If, at any time during the execution of the notebook the system complains that you have incompatible versions of pyarrow and pandas, add this to one of the notebook cells and execute: `!pip install azureml-dataprep[pandas]`.

5. Now you are ready to run through the notebook with the example, from Jupyter on your local machine. If you've followed the instructions in **Step 4** you should be able to open the AISec Tutorial notebook by clicking on it:
![Give your data set a name](docs/images/runTutorialFromJupyter.jpg)

### [TODO]

1. Add **Step 6** with explanation of test case run
2. Add **Step 7** how to create model and get the endpoint URL to use for security actions

## Useful links and presentation for AiSec example

### [TODO]
1. Add links to useful materials and setup guidelines from this example
2. Add the link to the presentation
3. Something more?

