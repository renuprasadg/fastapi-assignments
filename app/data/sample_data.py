from fastapi import FastAPI

employees = [
    {
        "id": 101,
        "name": "Praveen",
        "role": "DevOps Engineer",
        "experience": 5,
        "location": "Visakhapatnam",
    },
    {
        "id": 102,
        "name": "Rahul",
        "role": "SRE Engineer",
        "experience": 7,
        "location": "Hyderabad",
    },
    {
        "id": 103,
        "name": "Anil",
        "role": "SRE Engineer",
        "experience": 4,
        "location": "Hyderabad",
    },
]

servers = [
    {
        "id": 1,
        "hostname": "prod-web-01",
        "ip": "10.10.1.10",
        "environment": "prod",
        "application": "payments",
        "status": "running",
    },
    {
        "id": 2,
        "hostname": "prod-web-02",
        "ip": "10.10.1.11",
        "environment": "prod",
        "application": "orders",
        "status": "running",
    },
    {
        "id": 3,
        "hostname": "prod-app-01",
        "ip": "10.10.1.12",
        "environment": "prod",
        "application": "payments",
        "status": "stopped",
    },
    {
        "id": 4,
        "hostname": "dev-app-01",
        "ip": "10.10.2.10",
        "environment": "dev",
        "application": "payments",
        "status": "running",
    },
    {
        "id": 5,
        "hostname": "dev-app-02",
        "ip": "10.10.2.11",
        "environment": "dev",
        "application": "orders",
        "status": "stopped",
    },
    {
        "id": 6,
        "hostname": "test-web-01",
        "ip": "10.10.3.10",
        "environment": "test",
        "application": "payments",
        "status": "running",
    },
]

