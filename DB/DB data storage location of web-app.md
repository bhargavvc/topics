Here's a structured breakdown of where data is stored when you connect to a production database installed on a virtual machine (VM) with PostgreSQL:

1. **VM's Disk**:
   - **Purpose**: Stores all data for the PostgreSQL database.
   - **Contents**: Includes data files, transaction logs, and other database management files.
   - **Details**: This storage contains tables, indexes, and various database structures as defined in your schemas.

2. **PostgreSQL Server**:
   - **Location**: Operates as a software component on the VM.
   - **Function**: Manages access to and manipulation of the data files on the VM’s disk.
   - **Process**: Handles queries from clients, executing data retrieval and modification operations.

3. **Local Disk (Client Side)**:
   - **Interaction**: Does not store any of the PostgreSQL data simply through a connection.
   - **Role**: Used for running client applications that connect to the database, not for data storage.
   - **Communication**: Exchanges data with the PostgreSQL server via network connections, with all data remaining on the VM's disk.

**Summary**: The actual data storage takes place exclusively on the VM’s disk where PostgreSQL is installed, not on your local disk or any external server outside of the VM. Your local machine functions only as a client, issuing SQL commands and receiving results through a network link to the PostgreSQL server on the VM.