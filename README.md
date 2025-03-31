# PRODT_ASSIGNMENT  

This repository consists of:  
1. Monitoring of Temporal Docker containers and Temporal Server using Prometheus and Grafana.  
2. Kubernetes manifest files for deploying Temporal Dashboard and Temporal Web UI.  
3. Sample Prometheus queries for monitoring Temporal Server.  
4. Grafana visualizations for Docker containers and Temporal Server metrics.  

## Table of Contents  
- [Overview](#overview)  
- [Steps Followed](#steps-followed)  
  - [Step 1: Setting Up the Environment](#step-1-setting-up-the-environment)  
  - [Step 2: Monitoring Docker Containers](#step-2-monitoring-docker-containers)  
  - [Step 3: Setting Up Worker and Workflows](#step-3-setting-up-worker-and-workflows)  
  - [Step 4: Deploying Temporal Server on Kubernetes](#step-4-deploying-temporal-server-on-kubernetes)  
  - [Step 5: Monitoring Temporal Server](#step-5-monitoring-temporal-server)  
- [Challenges Faced](#challenges-faced)  
- [What I Knew About Temporal](#what-i-knew-about-temporal)  
- [Next Steps](#next-steps)  

---

## Overview  

In this assignment, I was asked to:  
- ✅ Set up **Temporal Server and Temporal Web UI**.  
- ✅ Monitor **Docker containers and Temporal Server metrics**.  
- ✅ Use **EKS or any Kubernetes deployment** (I used Minikube instead of EKS).  
- ✅ Successfully deploy **Temporal Server and Temporal Web UI**.  
- ✅ Provide **Kubernetes manifests** (attached in this repo).  

---

## Steps Followed  

### Step 1: Setting Up the Environment  

1. **Launched an AWS EC2 instance** and installed Docker.  
2. **Deployed Temporal Server using Docker Compose.**  
3. **Verified Temporal Server and Web UI** were running.  

---

### Step 2: Monitoring Docker Containers  

To monitor Docker containers:  
1. Ensured all **targets were up** in Prometheus (checked endpoints).  
2. Confirmed that **Temporal Server was exposing metrics** (tested sample queries in Prometheus).  
3. Created a **Grafana dashboard** for Temporal Server metrics.  
4. Used **a predefined Docker dashboard** for monitoring containers.
5. to ckeck metrics exploration
    Get list of available targets in Prometheus:
      curl http://localhost:9090/api/v1/targets | jq
    To check the status of Prometheus targets and ensure that Prometheus is correctly scraping metrics
      curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {job: .discoveredLabels.job, health: .health, url: .scrapeUrl}'

### Step 3: Setting Up Worker and Workflows
     
     as mentioned i have taken the smaple workflow and sample worker in python and then build an image for deployment of temporal worker and pushed it to dockerhub

### Step 4: Deploying Temporal Server on Kubernetes

To deploy temporal server on kubernetes i have used minikube and have written manifest for 
  a. Temporal-server-deployment
  b. temporal-server-svc
  c. temporal-web-ui-deploy.yml
  d. temporal-web-ui-svc.yml
  e. namespace.yml


### Step 5: Monitoring Temporal Server
       To check the connectivity(temporal server is generating the metrics or not ) i have first tried running some basic queries in prometheus ui search bar for verifying metrics generation.
       Queries i run in prometheus for testing:
               temporal_workflow_task_queue_poll_empty
               temporal_activity_completed
               temporal_activity_failed
  Get ip of temporal server:
    kubectl get svc temporal-server -n temporal -o jsonpath='{.spec.clusterIP}'




### Challenges faced
       While setting up temporal and temporal worker i have faced the problems that there was a problem in the postgres connecting it was not accepting connections then i inspected and after checking logs i fixed that then after setting up the worker and workflows i have tried sample workflows and workers but there was issues as i was using ec2 so there was lot changes need to be done.and also while exposing temporal metrics it was giving error then after logging i fixed the error and then it was successfully exposing the metrics.


What i knew about Temporal platform

It is s used for managing workflows – kind of like an advanced task scheduler.
It has a server and workers – the server handles workflows, and workers execute tasks.
It stores data in a database – but not all databases work (SQLite didn’t work for us!).
It exposes metrics – which we can monitor using Prometheus & Grafana.
It runs on Docker & Kubernetes – and setting it up properly takes some effort.


# Workflows SetUp
![image](https://github.com/user-attachments/assets/42c85ad4-3674-4fb7-a9b3-22de28246578)

![image](https://github.com/user-attachments/assets/44bd2079-aaf4-4f1e-ab2c-5c4f98675ad7)

# Monitoring Docker  containers on Grafana
![image](https://github.com/user-attachments/assets/360b7abb-4b66-487e-b8e5-fa9382720561)
![image](https://github.com/user-attachments/assets/c38c41d1-1068-40b6-8777-abe7db1172af)
![image](https://github.com/user-attachments/assets/302a6284-b9b4-41a4-b7e5-f9867cae0da3)
![image](https://github.com/user-attachments/assets/98cae43d-d4ce-4bdf-9483-77b1c70b6556)

# Monitoring Temporal resources
![image](https://github.com/user-attachments/assets/25eaca1f-e7d1-4f8f-a576-b664b58e2c9f)
![image](https://github.com/user-attachments/assets/3bbd46e1-5c91-474a-832d-441f1ee612ce)
![image](https://github.com/user-attachments/assets/040d53ef-9860-4897-b6ff-a1266bee3b5f)

# Prometheus Query
![image](https://github.com/user-attachments/assets/54c0717d-6468-491d-8842-60a6ca18a5ef)










