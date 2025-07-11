# Store File in Amazon S3 bucket using Boto3

# Create a new IAM user or use existing one (Skip this step if you already have an IAM User)

This user would use python to configure AWS using Boto3

# Steps to Create a IAM user:

  1.Search AMI in AWS Console
  
  <img width="1347" height="862" alt="image" src="https://github.com/user-attachments/assets/d7864e2d-c733-46fe-b248-e1ed7b36a473" />

  2.Select Users on the interface on right side
  
  <img width="1270" height="819" alt="image" src="https://github.com/user-attachments/assets/9e6ac4c9-242c-4e45-8b74-8f15bc941222" />

  3. Click Create User
     
  <img width="1543" height="815" alt="image" src="https://github.com/user-attachments/assets/78075bd2-7297-4d96-b62e-69e59aaff549" />

  4. Enter any user name and press next
     
  <img width="1814" height="826" alt="image" src="https://github.com/user-attachments/assets/0cd5139b-a5c5-48f3-8d95-56e3ac8817ef" />

  5. Select "Attach policies directly , search for AmazonS3 , select "AmazonS3FullAccess" and click next
     
  <img width="1768" height="780" alt="image" src="https://github.com/user-attachments/assets/0bcd26fd-f010-4d5d-86d4-86973753d2a0" />

  6. Review the details and click Create user
      
  <img width="1692" height="715" alt="image" src="https://github.com/user-attachments/assets/a0f03058-7fe7-4d0a-8044-a08f2b6565c5" />

# Connect our System to AWS (Skip this step if you have already configured AWS CLI)

  !Install AWS CLI from here: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
   Boto3 Library: pip install Boto3
  
  1. Now Go Back to AMI Console -> Users and Click on newly created User

  <img width="1319" height="474" alt="image" src="https://github.com/user-attachments/assets/a2e9ade9-354c-459f-8814-5f0e831ab1e1" />

  2. Select 'Security Credentials Tab' , scroll down and click on Create access key

  <img width="1512" height="689" alt="image" src="https://github.com/user-attachments/assets/2bae8ef9-95b4-415f-b484-80ffbc85436e" />

  3. Select CLI , check the recommendation box and click next

  <img width="1375" height="783" alt="image" src="https://github.com/user-attachments/assets/55204583-bbe9-4f01-8f2f-228375775302" />

  4. Click on 'Create Access Key'

  5. Copy the Access Key

  <img width="1144" height="512" alt="image" src="https://github.com/user-attachments/assets/8640eddd-8cad-48a8-bd1f-d614c83f669a" />

  6. Once you have installed AWS CLI from above link, open the terminal in vs code write commands as follows:

  <img width="570" height="114" alt="image" src="https://github.com/user-attachments/assets/bab3077e-31f5-4e52-8c8b-b4cb33cbeb43" />

  7. Enter your Access Key that you copied , press enter and copy the secret access key from AMI , and regionL: us-east-2 or any

  <img width="653" height="81" alt="image" src="https://github.com/user-attachments/assets/e39b5aa5-2d59-4238-a149-352497931023" />

  <img width="688" height="199" alt="image" src="https://github.com/user-attachments/assets/830cf499-1e9f-44e4-871b-9b09d167decf" />

  <img width="712" height="166" alt="image" src="https://github.com/user-attachments/assets/5ff2d385-0f16-4268-af95-befad6739657" />

  <img width="442" height="55" alt="image" src="https://github.com/user-attachments/assets/991a3e81-2c57-4cfd-aed1-602ff6a130c2" />

  Now we have connected our system to AWS 

# Copy Python script or clone the repository

  1. Enter your own bucket name or use already existing bucket (Comment create function bucket in this case)
  2. Enter your own region in region variable or just keep it the same if you followed the AWS CLI configuration above
  3. You can enter the name you want for your file in S3 bucket in variable "file_name"
  4. Add full path to your file in "file_path" variable (don't forget to use '/' instead of '\')

  


  


  

     

  



  

  




  



  





