import asyncio
from temporalio.client import Client
from workflows import SampleWorkflow

async def main():
    client = await Client.connect("98.81.181.128:7233")  # Connect to Temporal Server
    handle = await client.start_workflow(
        SampleWorkflow.run,  # Call the workflow
        "Suyash",
        id="test-workflow-1",
        task_queue="sample-task-queue",
    )
    result = await handle.result()
    print(f"Workflow Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
