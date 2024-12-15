# Top 50 Docker Commands for Real-World Usage

This document ranks the top 50 Docker commands by their real-world usage and provides detailed descriptions, examples, and scenarios for each. The commands are grouped by functionality and listed in order of frequency and importance in practical use.

---

## **1. Essential Docker Commands**

### 1.1 `docker run`

- **Description**: Run a new container from an image.
- **Example**:
  ```bash
  docker run -d -p 80:80 nginx
  ```
  - `-d`: Run in detached mode.
  - `-p`: Map host port to container port.

### 1.2 `docker ps`

- **Description**: List all running containers.
- **Example**:
  ```bash
  docker ps
  ```

### 1.3 `docker ps -a`

- **Description**: List all containers (running and stopped).
- **Example**:
  ```bash
  docker ps -a
  ```

### 1.4 `docker images`

- **Description**: List all available Docker images.
- **Example**:
  ```bash
  docker images
  ```

### 1.5 `docker stop`

- **Description**: Stop a running container.
- **Example**:
  ```bash
  docker stop <container_id>
  ```

### 1.6 `docker rm`

- **Description**: Remove a stopped container.
- **Example**:
  ```bash
  docker rm <container_id>
  ```

### 1.7 `docker rmi`

- **Description**: Remove an image by its name or ID.
- **Example**:
  ```bash
  docker rmi <image_id>
  ```

### 1.8 `docker pull`

- **Description**: Download an image from Docker Hub.
- **Example**:
  ```bash
  docker pull nginx:latest
  ```

### 1.9 `docker build`

- **Description**: Build an image from a Dockerfile.
- **Example**:
  ```bash
  docker build -t my-app .
  ```

### 1.10 `docker exec`

- **Description**: Execute a command in a running container.
- **Example**:
  ```bash
  docker exec -it <container_id> bash
  ```

---

## **2. Intermediate Commands**

### 2.1 `docker logs`

- **Description**: View logs of a container.
- **Example**:
  ```bash
  docker logs <container_id>
  ```

### 2.2 `docker inspect`

- **Description**: Display detailed information about a container or image.
- **Example**:
  ```bash
  docker inspect <container_id>
  ```

### 2.3 `docker network ls`

- **Description**: List all Docker networks.
- **Example**:
  ```bash
  docker network ls
  ```

### 2.4 `docker network create`

- **Description**: Create a new Docker network.
- **Example**:
  ```bash
  docker network create my-network
  ```

### 2.5 `docker network connect`

- **Description**: Connect a container to a specific network.
- **Example**:
  ```bash
  docker network connect my-network <container_id>
  ```

### 2.6 `docker-compose up`

- **Description**: Start services defined in a `docker-compose.yml` file.
- **Example**:
  ```bash
  docker-compose up
  ```

### 2.7 `docker-compose down`

- **Description**: Stop and remove containers, networks, and volumes defined in `docker-compose.yml`.
- **Example**:
  ```bash
  docker-compose down
  ```

### 2.8 `docker stats`

- **Description**: Display real-time resource usage of running containers.
- **Example**:
  ```bash
  docker stats
  ```

### 2.9 `docker system prune`

- **Description**: Remove unused containers, images, networks, and volumes.
- **Example**:
  ```bash
  docker system prune
  ```

### 2.10 `docker tag`

- **Description**: Assign a new tag to an image.
- **Example**:
  ```bash
  docker tag <image_id> my-app:v1
  ```

---

## **3. Advanced Commands**

### 3.1 `docker save`

- **Description**: Save an image to a tar archive.
- **Example**:
  ```bash
  docker save -o my-app.tar my-app:latest
  ```

### 3.2 `docker load`

- **Description**: Load an image from a tar archive.
- **Example**:
  ```bash
  docker load -i my-app.tar
  ```

### 3.3 `docker cp`

- **Description**: Copy files between a container and the host.
- **Example**:
  ```bash
  docker cp <container_id>:/path/to/file ./file
  ```

### 3.4 `docker diff`

- **Description**: Inspect changes made to a container’s filesystem.
- **Example**:
  ```bash
  docker diff <container_id>
  ```

### 3.5 `docker export`

- **Description**: Export a container’s filesystem as a tar archive.
- **Example**:
  ```bash
  docker export -o container.tar <container_id>
  ```

### 3.6 `docker import`

- **Description**: Import a tar archive as a Docker image.
- **Example**:
  ```bash
  docker import container.tar my-imported-image
  ```

### 3.7 `docker history`

- **Description**: Display the history of an image.
- **Example**:
  ```bash
  docker history nginx
  ```

### 3.8 `docker login`

- **Description**: Log in to a Docker registry.
- **Example**:
  ```bash
  docker login
  ```

### 3.9 `docker push`

- **Description**: Push an image to a Docker registry.
- **Example**:
  ```bash
  docker push my-app:latest
  ```

### 3.10 `docker pull`

- **Description**: Pull an image from a Docker registry.
- **Example**:
  ```bash
  docker pull my-app:latest
  ```

---

## **4. Real-World Workflow Commands**

### 4.1 `docker context`

- **Description**: Manage Docker contexts for multiple environments.
- **Example**:
  ```bash
  docker context ls
  ```

### 4.2 `docker swarm init`

- **Description**: Initialize a Docker Swarm.
- **Example**:
  ```bash
  docker swarm init
  ```

### 4.3 `docker service create`

- **Description**: Create a service in Docker Swarm.
- **Example**:
  ```bash
  docker service create --name my-service nginx
  ```

### 4.4 `docker service ls`

- **Description**: List services in a Docker Swarm.
- **Example**:
  ```bash
  docker service ls
  ```

### 4.5 `docker volume create`

- **Description**: Create a new volume.
- **Example**:
  ```bash
  docker volume create my-volume
  ```

### 4.6 `docker volume ls`

- **Description**: List all volumes.
- **Example**:
  ```bash
  docker volume ls
  ```

### 4.7 `docker volume rm`

- **Description**: Remove a volume.
- **Example**:
  ```bash
  docker volume rm my-volume
  ```

### 4.8 `docker container stats`

- **Description**: Show resource usage for a specific container.
- **Example**:
  ```bash
  docker container stats <container_id>
  ```

### 4.9 `docker container top`

- **Description**: Display running processes in a container.
- **Example**:
  ```bash
  docker container top <container_id>
  ```

### 4.10 `docker builder prune`

- **Description**: Remove unused build cache.
- **Example**:
  ```bash
  docker builder prune
  ```

---

This document lists the top 50 Docker commands ranked by real-world usage. Each command is described with practical examples to help you gain mastery over Docker in production environments. Additionally, handy commands for deleting all containers or images and other quick management tasks are included. Below are some of the most useful cleanup commands:

### **Handy Cleanup Commands**

#### **1. Delete All Containers**
- **Command**:
  ```bash
  docker rm $(docker ps -aq)
  ```
- **Description**: Deletes all stopped containers.

#### **2. Delete All Images**
- **Command**:
  ```bash
  docker rmi $(docker images -q)
  ```
- **Description**: Removes all Docker images.

#### **3. Delete All Unused Resources**
- **Command**:
  ```bash
  docker system prune -a
  ```
- **Description**: Deletes all unused containers, images, networks, and dangling volumes.





# Docker Compose: `up`, `build`, and `up --build`

This document provides an in-depth explanation of the `docker-compose build`, `docker-compose up`, and `docker-compose up --build` commands, along with examples and their practical usage scenarios.

---

## **1. `docker-compose build`**

### **Description**
- The `docker-compose build` command is used to build or rebuild the images specified in the `docker-compose.yml` file.
- It processes the `build` configuration for each service and creates the corresponding Docker images.

### **Syntax**
```bash
docker-compose build [SERVICE_NAME]
```
- `SERVICE_NAME` (optional): Specifies the service(s) to build. If omitted, all services will be built.

### **Use Cases**
1. **Building Images Separately**: If you want to build Docker images before starting containers.
2. **Debugging Build Issues**: Useful for debugging when image builds fail.

### **Example**
Given the following `docker-compose.yml` file:
```yaml
version: '3.8'
services:
  app:
    build:
      context: ./app
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
```

- To build all services:
  ```bash
  docker-compose build
  ```
- To build only the `app` service:
  ```bash
  docker-compose build app
  ```

---

## **2. `docker-compose up`**

### **Description**
- The `docker-compose up` command starts the containers for services defined in the `docker-compose.yml` file.
- By default, it uses the previously built images (if available).

### **Syntax**
```bash
docker-compose up [OPTIONS] [SERVICE_NAME]
```
- `OPTIONS`:
  - `-d`: Run containers in detached mode.
  - `--remove-orphans`: Remove containers not defined in the current `docker-compose.yml` file.
- `SERVICE_NAME` (optional): Specifies the service(s) to start. If omitted, all services will start.

### **Use Cases**
1. **Start Services**: Use when images are already built, and you want to start containers.
2. **View Logs**: Runs containers in the foreground, displaying their logs.

### **Example**
- Start all services:
  ```bash
  docker-compose up
  ```
- Start services in detached mode:
  ```bash
  docker-compose up -d
  ```
- Start only the `app` service:
  ```bash
  docker-compose up app
  ```

---

## **3. `docker-compose up --build`**

### **Description**
- The `docker-compose up --build` command builds images **before starting containers**.
- It combines the functionality of `docker-compose build` and `docker-compose up` into a single command.

### **Syntax**
```bash
docker-compose up --build [SERVICE_NAME]
```
- `SERVICE_NAME` (optional): Specifies the service(s) to build and start. If omitted, all services are processed.

### **Use Cases**
1. **Update Images**: Use when the Dockerfile or source code has changed, and you need to rebuild images.
2. **Streamlined Workflow**: Simplifies the workflow by combining the build and start steps into one command.

### **Example**
- Build and start all services:
  ```bash
  docker-compose up --build
  ```
- Build and start only the `app` service:
  ```bash
  docker-compose up --build app
  ```
- Rebuild and start services in detached mode:
  ```bash
  docker-compose up --build -d
  ```

---

## **Comparison Table**
| Command                        | Purpose                                         | When to Use                     |
|--------------------------------|-------------------------------------------------|---------------------------------|
| `docker-compose build`         | Builds images for the services.                | If you only want to rebuild images without starting containers. |
| `docker-compose up`            | Starts containers using existing images.       | If no changes have been made to the Dockerfile or source code. |
| `docker-compose up --build`    | Builds images first, then starts containers.   | If the Dockerfile or source code has been updated. |

---

## **Workflow Example**
### Scenario: Updating a Web Application
1. **Initial Setup**:
   - Build images and start containers for the first time:
     ```bash
     docker-compose up --build
     ```
2. **Making Changes**:
   - After updating the code, rebuild the images:
     ```bash
     docker-compose up --build
     ```
3. **Debugging**:
   - If a build fails, focus on specific services:
     ```bash
     docker-compose build app
     ```
4. **Restart Services**:
   - If no changes were made to the code or images, simply restart the services:
     ```bash
     docker-compose up
     ```

---

## **Best Practices**
1. **Use `docker-compose up --build` for Changes**:
   - Always use this command after making changes to the `Dockerfile` or source code.
2. **Detach Mode for Production**:
   - Use `-d` to run containers in the background.
3. **Combine Commands for Efficiency**:
   - Use `--build` to simplify your workflow.
4. **Clean Up Resources**:
   - Stop and remove containers when not needed:
     ```bash
     docker-compose down
     ```

