from temporalio import workflow
from activities import sample_activity
from datetime import timedelta  # ✅ Import timedelta

@workflow.defn
class SampleWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        result = await workflow.execute_activity(
            sample_activity,
            name,
            schedule_to_close_timeout=timedelta(seconds=10)  # ✅ Fix timeout issue
        )
        return result
