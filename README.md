# Setting Up Amazon Braket for Grover's Algorithm

## Set Up AWS IAM Account
1. Establish an IAM account with the following policies: “AmazonBraketFullAccess", "AmazonBraketJobsExecutionPolicy", and “AmazonS3FullAccess".
2. After creating the IAM account, download the credentials CSV file.

## Enable Amazon Braket Service
1. In the Amazon Braket console, enable third-party devices in the Permissions and Settings, General tab section.
2. In the Execution Roles tab, enable "create service-linked role" and then enable "create default role”.

## IAM User Amazon Braket Quantum Execution Setup
1. Navigate to the Amazon Braket Console.
2. Click on Notebooks, then click on the advanced notebook section, and finally click on the Configure button.
3. This will create an EC2 instance of a Notebook.
4. Fill in the required fields, such as the name of the instance, select the standard instance type (ml.t3.medium), volume, use the initial IAM role created earlier, and click on the Launch button to create the instance and make it up.
5. It may take some time to get the instance up and running.

## Access Jupyter Notebook from the Launched Braket Instance
1. Click on the link in the instance to access the Jupyter Notebook.
2. Create a notebook and enter the Grover's Code in the Notebook.
3. The Grover's Algorithm will be imported in the created Notebook with the number of shots and the AWS Braket quantum simulator.
4. Once it's run, the results can be identified in the Amazon S3 bucket in the JSON format.
5. In the Quantum Tasks tab, the Grover's Task run with different numbers of shots can be found.

## Execute the Quantum Service Locally Using a Local Simulator
1. Install conda and create a virtual environment with the desired Python version.
2. Install the Qiskit package using pip.
3. Install the Matplotlib package using pip.
4. Run the code by typing "python grovers_algo.py" in the command line.
5. The results will be displayed in the form of a graph.
