from temporalio import activity
import asyncio

@activity.defn
async def sample_activity(name: str) -> str:
    await asyncio.sleep(2)  # Use asyncio sleep instead of time.sleep
    return f"Activity completed for {name}!"
