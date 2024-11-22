
**Introduction to PM2**

PM2 (Parallel Multithreaded Machine) is a popular production process manager for Node.js applications. It helps you manage and maintain your application processes, ensuring they run continuously and efficiently. PM2 offers features like automatic application restarts, load balancing, monitoring, and zero-downtime deployments, making it an essential tool for deploying Node.js applications in real-world scenarios.

---

**Brief Overview and Real-World Usage**

- **Process Management**: PM2 keeps your applications running by automatically restarting them if they crash or encounter an error. This ensures high availability and reliability in production environments.

- **Clustering and Load Balancing**: PM2 allows you to run multiple instances of your application across all available CPU cores, optimizing resource utilization and improving performance.

- **Zero-Downtime Reloads**: You can update your application code and reload processes without any downtime, ensuring uninterrupted service to users.

- **Monitoring and Logging**: PM2 provides real-time monitoring of your applications, including CPU and memory usage. It also manages logs, making it easier to debug and maintain applications.

- **Startup Scripts**: PM2 can generate startup scripts to automatically launch your applications when the server reboots, ensuring they are always up and running.

---

**Main Advantages of Using PM2**

1. **Reliability**: Automatically restarts applications if they crash or stop unexpectedly.

2. **Scalability**: Easily scales applications across multiple CPU cores using clustering.

3. **Efficiency**: Manages multiple applications and their versions seamlessly.

4. **Ease of Deployment**: Simplifies deployment processes with ecosystem configuration files.

5. **Monitoring**: Offers built-in tools for monitoring application performance and resource usage.

6. **Logging**: Centralizes and manages application logs, aiding in debugging and maintenance.

---

**Common PM2 Commands Used in Real-World Applications**

Below are some of the most frequently used PM2 commands, along with explanations and examples to help you understand how to use them effectively.

1. ### **Starting an Application**

   - **Basic Start**

     ```bash
     pm2 start app.js
     ```

     Starts the `app.js` application.

   - **Start with a Custom Name**

     ```bash
     pm2 start app.js --name my-app
     ```

     Starts the application and names the process `my-app`.

   - **Start in Cluster Mode**

     ```bash
     pm2 start app.js -i max
     ```

     Runs the app in cluster mode using all available CPU cores.

2. ### **Managing Processes**
  ![topic](#https://raw.githubusercontent.com/bhargavvc/topics/img/nodejs/pm2_microservice.png)


   - **List All Processes**

     ```bash
     pm2 list
     ```

     Displays a list of all PM2 managed processes.

   - **Stop a Process**

     ```bash
     pm2 stop my-app
     ```

     Stops the process named `my-app`.

   - **Restart a Process**

     ```bash
     pm2 restart my-app
     ```

     Restarts the `my-app` process.

   - **Delete a Process**

     ```bash
     pm2 delete my-app
     ```

     Deletes the `my-app` process from PM2's list.

3. ### **Monitoring Applications**
   ![topic](#https://raw.githubusercontent.com/bhargavvc/topics/img/nodejs/pm2_monitoring.png)

   - **View Logs**

     ```bash
     pm2 logs
     ```

     Streams logs for all PM2 processes.

   - **View Logs for a Specific Process**

     ```bash
     pm2 logs my-app
     ```

     Streams logs only for `my-app`.

   - **Real-Time Monitoring**

     ```bash
     pm2 monit
     ```

     Opens a real-time monitoring dashboard showing CPU and memory usage.

4. ### **Zero-Downtime Reloads**

   - **Reload All Processes**

     ```bash
     pm2 reload all
     ```

     Reloads all applications managed by PM2 without downtime.

   - **Reload a Specific Process**

     ```bash
     pm2 reload my-app
     ```

     Reloads `my-app` without downtime.

5. ### **Using Ecosystem Configuration File**

   PM2 allows you to define application configurations in an ecosystem file, typically named `ecosystem.config.js`.

   - **Sample `ecosystem.config.js`**

     ```javascript
     module.exports = {
       apps: [
         {
           name: 'my-app',
           script: './app.js',
           instances: 'max',
           exec_mode: 'cluster',
           env: {
             NODE_ENV: 'development',
           },
           env_production: {
             NODE_ENV: 'production',
           },
         },
       ],
     };
     ```

   - **Start Applications Using the Ecosystem File**

     ```bash
     pm2 start ecosystem.config.js
     ```

     Starts all applications defined in the configuration file.

   - **Specify Environment**

     ```bash
     pm2 start ecosystem.config.js --env production
     ```

     Starts applications using the `env_production` settings.

6. ### **Auto Start on System Boot**

   - **Generate Startup Script**

     ```bash
     pm2 startup
     ```

     Generates a startup script to run PM2 and its managed processes on boot.

   - **Save the Current Process List**

     ```bash
     pm2 save
     ```

     Saves the list of processes to be resurrected on system reboot.

7. ### **Environment Variables**

   - **Passing Environment Variables at Start**

     ```bash
     pm2 start app.js --env production
     ```

     Sets `NODE_ENV` to `production` for `app.js`.

   - **Setting Environment Variables in Ecosystem File**

     ```javascript
     env: {
       NODE_ENV: 'development',
       API_KEY: 'your-api-key',
     },
     ```

8. ### **Watching for File Changes (Development Mode)**

   - **Enable Watch Mode**

     ```bash
     pm2 start app.js --watch
     ```

     Restarts the application whenever a file change is detected.

   - **Exclude Specific Files or Directories**

     ```javascript
     watch_options: {
       ignored: ['node_modules', 'logs'],
     },
     ```

9. ### **Updating PM2**

   - **Update PM2 to the Latest Version**

     ```bash
     pm2 update
     ```

     Refreshes PM2's internal state and updates to the latest PM2 version.

10. ### **Other Useful Commands**

    - **Check PM2 Version**

      ```bash
      pm2 -v
      ```

    - **Get Process Information**

      ```bash
      pm2 describe my-app
      ```

      Provides detailed information about the `my-app` process.

    - **Kill All Processes**

      ```bash
      pm2 kill
      ```

      Stops and deletes all PM2 managed processes.

---

**Examples and Use Cases**

1. **Running Multiple Instances for Load Balancing**

   ```bash
   pm2 start app.js -i 4
   ```

   Starts 4 instances of `app.js`, allowing the application to handle more traffic.

2. **Graceful Shutdown**

   ```bash
   pm2 gracefulReload my-app
   ```

   Gracefully reloads `my-app`, ensuring all current requests are handled before stopping the old process.

3. **Integration with Deployment Tools**

   PM2 can be integrated with deployment tools like Git and CI/CD pipelines to automate application deployment and management.

---

**Conclusion**

PM2 is a powerful tool that simplifies the management of Node.js applications in production environments. Its ability to handle automatic restarts, clustering, monitoring, and zero-downtime deployments makes it an essential part of modern web application deployment strategies. By mastering the PM2 commands and understanding its features, you can ensure that your applications are robust, scalable, and maintainable.

---

Feel free to explore more advanced features of PM2, such as module system, keymetrics integration, and custom metrics, to further enhance your application's performance and reliability.