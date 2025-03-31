import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from workflows import SampleWorkflow
from activities import sample_activity
from prometheus_client import start_http_server, Counter

# Define a Prometheus metric
workflow_completed_counter = Counter('workflow_completed_total', 'Number of completed workflows')

async def main():
    # Start Prometheus metrics server on port 8001
    start_http_server(8001)

    client = await Client.connect("98.81.181.128:7233")  # Temporal server

    worker = Worker(
        client,
        task_queue="sample-task-queue",
        workflows=[SampleWorkflow],
        activities=[sample_activity],
        prometheus_server="172.27.0.7:8001"
    )

    print("Worker started. Waiting for tasks...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
