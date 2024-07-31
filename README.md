# End-to-End-DevOps-Project (Ongoing)

Over the past few years, I've been actively learning DevOps technologies and principles during my free time. 
Recognizing the dynamic nature of the tech industry, I understood the importance of gaining practical experience in a role that aligns with my passion and career aspirations. 
This led me to invest in full-time studies to gain the skills I am passionate about.

The End-to-End DevOps Project is the culmination of this effort. The project aims to challenge me, enhance my skills, and consolidate my knowledge. 
It emphasizes the needs of a business and incorporates GitOps practices. While the solution is comprehensive, there are still areas for improvement that I am actively working on.

## Project Included
### Application:

The application is a financial tracking dashboard named FinTrack that provides users with tools to manage and analyze their financial data through visual representations such as bar charts, pie charts, and tables. 
Users can view their expenses in a table, edit details, and delete expenses as needed. All components of this project are containerized, ensuring a consistent and portable environment.

__expenses_app__ - A RESTful API built with Flask and Mongoengine, providing comprehensive CRUD operations for managing expenses. It handles incoming web requests, routes them to the appropriate handlers, and returns responses to the client.

__flask_auth_app__ - A Flask web application that handles user authentication and session management, leveraging Flask-Login for session management.

__front_app__ - The front-end of the application, which fetches expense data from a backend service and provides data visualization and table management features.

__MongoDB__ - Handles the role of the database for expenses using a NoSQL architecture consisting of collections and documents. Document models are defined using the mongoengine library. 
Later on I decided to switch to DocumentDB.

### Repositories:

__GitHub__ - A private monorepo on GitHub serves as the Single Source of Truth for my project.
I realize that it would have been easier to create separate repositories for ArgoCD, applications, etc., however I decided to use monorepo for your readability.

__DockerHub__ - A private container registry on DockerHub.

### Cloud Provider:

__AWS__ - Amazon Web Services (AWS) is the world’s most comprehensive and broadly adopted cloud, I decided to go with it even If I have more experience with Google Cloud Platform (GCP).

### Provisioning:

__Terraform__ -  To bootstrap the necessary infrastructure I decided to utilize Terraform. 
Due to dependency conflicts, I created two plays:
    - bootstrap_aws: Creates AWS resources and the EKS cluster.
    - bootstrap_cluster: Installs addons like SealedSecrets and ArgoCD.

### Orchiestration:

__EKS__ - Amazon Elastic Kubernetes Service serves as the orchestration tool for the project. I created two managed node groups: one for the application and one for addons like ArgoCD and SealedSecrets. Worker nodes are in private subnets and use a NAT Gateway for internet access.

### CI/CD Pipeline:

__CircleCI__ - Continuous integration tool for building Docker images, pushing them to Docker Hub, and updating Helm Chart values.

__ArgoCD__ - Utilized the App of Apps pattern with a generator to create three environments: dev, stage, and prod.


### TO-DO's:

__DocumentDB__ - Adjust the application and Helm charts replace MongoDB with DocumentDB. Terraform script is ready and tested.

__Vault__ - Implement HashiCorp Vault (Optional).

__Prometheus__ - Implement tools for observability.

__CI/CD__ - Implement branch-based deployment.

![Architecture Diagram](https://github.com/GrzegorzSychta/End-to-End-DevOps-Project/draw.png?raw-true)