AWS Lambda: [
    To handle the business logic.,
    To process messages from SQS.(lambda is like a worker),
    To host individual microservices,
    To execute serverless functions.

    ]

API Gateway: [
    To expose and Create RESTful endpoints.,
    To route requests to the appropriate microservice.

]

DynamoDB: [
    As the `NoSQL database` to store blog posts.
    For storing processed data.

]

IAM: [
    For secure access and management.
]

Elastic Load Balancing (ELB): [
    To distribute incoming traffic.,
    To distribute incoming traffic across multiple EC2 instances.

]

EC2: [
    To automatically adjust the number of instances based on traffic.
]

Amazon SQS(broker like rabbitmq): [
    To decouple and buffer incoming requests.,
    For inter-service communication(SQS for point-to-point communication to ensure message delivery and decoupling),
    To queue notifications for reliability.
]
Amazon SNS(like provider(means celery)): [
    For inter-service communication(SNS for pub/sub patterns where services publish events).
    To publish notifications(user status updates like that).
]


Auto Scaling Groups (ASG) with EC2: [
    To automatically adjust the number of instances based on traffic. Define scaling policies in ASG to add or remove EC2 instances based on CPU utilization or request count.
    
]
Cloud watch: [
    To monitor and track metrics and EC2 Metrcis(Is metric only comes form ec2 ?) and logs. and queue length, Lambda invocation rates,
    To create CloudWatch Alarms(notify the team when certain thresholds are breached (e.g., high error rates, latency))
    Create CloudWatch dashboards to visualize key metrics and logs in a centralized view.
]
AWS CloudWatch Logs: [
    For centralized logging.
    
  ]
  - **AWS X-Ray:** [
    For distributed tracing.
    ]


RDS:[
    As the relational database
]
AWS Step Functions:[
    To orchestrate complex workflows.
]
 
Amazon SES or SNS Email/SMS : [
    For delivering notifications to users.
]

event bus (like AWS SNS or SQS) to publish events