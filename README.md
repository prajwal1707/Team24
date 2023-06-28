# Team24
Problem Statement:
Develop a comprehensive resource tracking solution that provides quick access and listing of all the resources across multiple Google Cloud Platform (GCP) accounts and regions. Extend the solution to support multiple Amazon Web Services (AWS) accounts, enabling users to retrieve consolidated resource information from both cloud providers. The objective is to empower users to efficiently track and manage resources across GCP and AWS, regardless of the account or region.

Approach:
1. In our project, we have used HTML and CSS for designing the UI of the dashboard which will be used by the user to search and filter as per the problem statement. 
2. For the backend we have used Python language to fetch the data from the AWS S3 bucket to the dashboard. In the bucket, we have the data of different users using different types of AWS services in different regions.
3. Using AWS CodeWhisperer, we tried to write the code for fetching data and getting the instances.
4. By using AWS CodeWhisperer, we addressed code complexity and improved code quality.
 
Prerequisites:
• Python 3.6 or higher
• Pip package manager
• AWS SDK for Python (Boto3)
• AWS Account

Instructions to run the code:
1. Unzip the folder named Team24 to get the files. Inside the folder, The index.html can be run using Live Server on VSCode to open the dashboard UI for interaction.
2. The file (app.py) has Python code to get the data from the AWS bucket.
