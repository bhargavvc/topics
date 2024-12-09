In Docker, `CMD`, `ENTRYPOINT`, and `RUN` are key instructions in the **Dockerfile** that serve different purposes. Here's a clear explanation of each:

---

### **1. `CMD`**
- **Purpose**: Specifies the **default command** to execute when the container starts.
- **Behavior**:
  - Can be overridden when running the container using `docker run` by specifying a different command.
  - Typically used for commands that can vary or be user-defined at runtime.

- **Syntax**:
  - **Shell form**: 
    ```dockerfile
    CMD python app.py
    ```
    This runs the command as `/bin/sh -c "python app.py"`.
  - **JSON array form** (recommended):
    ```dockerfile
    CMD ["python", "app.py"]
    ```
    This ensures the command is passed directly without invoking a shell.

- **Example**:
  ```dockerfile
  CMD ["python", "app.py"]
  ```
  - If you run:
    ```bash
    docker run myimage
    ```
    The container will execute `python app.py`.

  - But you can override it:
    ```bash
    docker run myimage python another_app.py
    ```

---

### **2. `ENTRYPOINT`**
- **Purpose**: Defines the **main application** or **command** that always runs in the container.
- **Behavior**:
  - Cannot be easily overridden. Instead, arguments provided in `docker run` are passed as parameters to the `ENTRYPOINT` command.
  - Used for containers designed to perform a specific task or act like an executable.

- **Syntax**:
  - **Shell form**:
    ```dockerfile
    ENTRYPOINT python app.py
    ```
    This runs the command as `/bin/sh -c "python app.py"`.
  - **JSON array form** (recommended):
    ```dockerfile
    ENTRYPOINT ["python", "app.py"]
    ```

- **Example**:
  ```dockerfile
  ENTRYPOINT ["python", "app.py"]
  ```
  - If you run:
    ```bash
    docker run myimage
    ```
    It always executes `python app.py`.

  - To pass arguments:
    ```bash
    docker run myimage --debug
    ```
    This runs `python app.py --debug`.

---

### **3. `RUN`**
- **Purpose**: Executes a command during the **image build process**. Used for tasks like installing dependencies, configuring the environment, or creating files.
- **Behavior**:
  - Executes during the build stage, not at runtime.
  - Creates a new intermediate image layer each time it runs.

- **Syntax**:
  - **Shell form**:
    ```dockerfile
    RUN apt-get update && apt-get install -y python
    ```
  - **JSON array form**:
    ```dockerfile
    RUN ["apt-get", "install", "-y", "python"]
    ```

- **Example**:
  ```dockerfile
  RUN pip install flask
  ```
  - This installs Flask during the build process, so it is available when the container runs.

---

### **Key Differences**

| Aspect               | `RUN`                              | `CMD`                              | `ENTRYPOINT`                       |
|----------------------|-------------------------------------|-------------------------------------|-------------------------------------|
| **When Executed**    | During image build time.           | At container runtime.              | At container runtime.              |
| **Purpose**          | Install/setup software or environment. | Default command to run in the container. | Define the container's primary behavior. |
| **Overridable**       | Not applicable (build-time).       | Easily overridden with `docker run`. | Arguments are appended, but base command stays fixed. |
| **Format**           | Shell or JSON array.              | Shell or JSON array.              | JSON array recommended.            |

---

### **Combining `CMD` and `ENTRYPOINT`**
You can use `CMD` to provide **default arguments** for an `ENTRYPOINT`. This approach gives flexibility while ensuring a fixed command is always executed.

**Example**:
```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```
- If you run:
  ```bash
  docker run myimage
  ```
  It executes: `python app.py`.

- If you override:
  ```bash
  docker run myimage another_app.py
  ```
  It executes: `python another_app.py`.

---

### **Summary**
- Use `RUN` for tasks during image build (e.g., installing dependencies).
- Use `CMD` to specify the default command for the container at runtime, which can be overridden.
- Use `ENTRYPOINT` to define a fixed command that is the core functionality of the container, and optionally use `CMD` to provide default arguments.