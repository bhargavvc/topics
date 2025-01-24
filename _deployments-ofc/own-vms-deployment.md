### 1. **Code Pushed to `dev` Branch**
   - **Trigger Jenkins Pipeline**: Automatically triggered via webhook or poll.
   - **Build and Push Docker Image**:
     ```bash
     docker build -t my-registry.com/my-app:dev-123 .
     docker push my-registry.com/my-app:dev-123
     ```
   - **Update Kubernetes for Dev**:
     - **Option 1**: Modify YAML and apply:
       ```bash
       sed -i 's|PLACEHOLDER|my-registry.com/my-app:dev-123|' deployment.yaml
       kubectl apply -f deployment.yaml --namespace=dev
       ```
     - **Option 2**: Directly set the image:
       ```bash
       kubectl set image deployment/my-app my-app=my-registry.com/my-app:dev-123 --namespace=dev
       ```

### 2. **PR Accepted and Merged to `master`**
   - **Build and Push Production Docker Image**:
     ```bash
     docker build -t my-registry.com/my-app:prod-456 .
     docker push my-registry.com/my-app:prod-456
     ```
   - **Update Kubernetes for Prod**:
     - **Option 1**: Modify YAML and apply:
       ```bash
       sed -i 's|PLACEHOLDER|my-registry.com/my-app:prod-456|' prod-deployment.yaml
       kubectl apply -f prod-deployment.yaml --namespace=prod
       ```
     - **Option 2**: Directly set the image:
       ```bash
       kubectl set image deployment/my-app my-app=my-registry.com/my-app:prod-456 --namespace=prod
       ```

These commands ensure the correct image is deployed to the respective environment during each stage.



Here’s a list of **easy-to-medium-level questions and answers** based on the deployment workflow described:

----------------------

### **General CI/CD Workflow Questions**
1. **Q: What triggers a Jenkins pipeline for the `dev` branch?**  
   **A:** A webhook configured in the source control (e.g., GitHub, GitLab) triggers the pipeline when code is pushed to the `dev` branch.

2. **Q: What does Jenkins do after the code is pushed to the `dev` branch?**  
   **A:** Jenkins builds and tests the code, creates a Docker image, pushes it to a container registry, and updates the Kubernetes deployment.

3. **Q: How does Jenkins ensure Kubernetes uses the latest Docker image?**  
   **A:** Jenkins updates the Kubernetes Deployment YAML or directly runs `kubectl set image` with the new image tag.

---

### **Docker and Image Management Questions**
4. **Q: Where is the Docker image stored after Jenkins builds it?**  
   **A:** It is stored in a container registry like DockerHub, AWS ECR, or a private registry.

5. **Q: How is the Docker image tagged in Jenkins?**  
   **A:** The image is tagged with a unique identifier like `my-app:dev-<build_number>` for `dev` or `my-app:prod-<build_number>` for `prod`.

6. **Q: Why do we use tags like `dev-<build_number>` or `prod-<build_number>` for Docker images?**  
   **A:** Tags ensure each image is unique and can be tracked back to a specific build or commit.

---

### **Kubernetes-Specific Questions**
7. **Q: What command is used to apply a Deployment YAML in Kubernetes?**  
   **A:** `kubectl apply -f deployment.yaml --namespace=<namespace>`.

8. **Q: How does Kubernetes handle rolling updates when the image is updated?**  
   **A:** Kubernetes gradually replaces old Pods with new Pods, ensuring no downtime. New Pods must pass readiness checks before serving traffic.

9. **Q: What is the difference between `kubectl apply` and `kubectl set image`?**  
   **A:** `kubectl apply` applies the entire YAML configuration, while `kubectl set image` directly updates the image in an existing Deployment.

10. **Q: How does Kubernetes know a new Docker image is available?**  
    **A:** Jenkins explicitly updates the Deployment with the new image tag using `kubectl apply` or `kubectl set image`.

---

### **Pipeline Questions**
11. **Q: What are the key stages in a typical Jenkins pipeline for deployment?**  
    **A:** Clone the repository, build & test, build the Docker image, push the image to the registry, and deploy to Kubernetes.

12. **Q: How does Jenkins wait for Kubernetes to complete the deployment?**  
    **A:** By using the command `kubectl rollout status deployment/<deployment-name>`.

13. **Q: How is the production deployment triggered?**  
    **A:** A manual trigger in Jenkins is used after the PR is merged into the `master` branch.

14. **Q: What is the purpose of readiness probes in Kubernetes?**  
    **A:** To ensure that a Pod is healthy and ready to accept traffic before Kubernetes routes requests to it.

---

### **AWS-Specific Deployment Workflow Questions**
15. **Q: Which AWS service can store Docker images for Kubernetes deployments?**  
    **A:** Amazon Elastic Container Registry (ECR).

16. **Q: How is AWS CodePipeline used in this workflow?**  
    **A:** CodePipeline triggers the pipeline on changes in the `dev` or `master` branch, builds the Docker image using CodeBuild, and deploys to EKS.

17. **Q: How do you update an image in an AWS EKS Deployment?**  
    **A:** Use `kubectl set image` or update the Deployment YAML and apply it.

---

### **Conceptual/Best Practices Questions**
18. **Q: Why is a manual trigger used for production deployment?**  
    **A:** To ensure human oversight and verify stability before deploying to production.

19. **Q: Why are separate namespaces (e.g., `dev` and `prod`) used in Kubernetes?**  
    **A:** To isolate environments and avoid accidental changes affecting production.

20. **Q: What is the role of a container registry in this deployment workflow?**  
    **A:** It acts as a central store for Docker images, making them accessible to Kubernetes for deployment.

---

This set of questions covers foundational knowledge of CI/CD workflows, Docker, Kubernetes, Jenkins pipelines, and AWS-based deployment. You can mix and match for quizzes, interviews, or self-assessments!


#how to set up a webhook
Webhooks are **not defined in the Jenkins pipeline itself**. They are typically configured **outside Jenkins**, in the source control system (e.g., GitHub, GitLab, or Bitbucket) to notify Jenkins when a specific event occurs (like a push or pull request).

### Webhook Configuration Steps:
1. **In Source Control (GitHub/GitLab/Bitbucket)**:
   - Go to your repository settings.
   - Add a webhook with the Jenkins URL (e.g., `http://<jenkins-server>/github-webhook/`).
   - Choose the events that should trigger the webhook (e.g., "push", "pull request").
   
2. **In Jenkins**:
   - Install the required plugin (e.g., GitHub Plugin for GitHub or Bitbucket Plugin for Bitbucket).
   - Configure the job/pipeline to use webhooks by selecting **Build Triggers**:
     - Enable the option like **GitHub hook trigger for GITScm polling** (GitHub) or similar for other services.
   - The webhook will notify Jenkins, and Jenkins will trigger the pipeline automatically.

Webhooks are essentially **set in the source control tool**, and Jenkins listens to these notifications to start the pipeline.