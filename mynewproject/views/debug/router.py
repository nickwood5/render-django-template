from ninja import Router
from mynewproject.views.debug.tasks import demo_celery_task
from mynewproject.views.debug.schema import PingResponse
from django.utils import timezone
from datetime import timedelta

debug_router = Router()


@debug_router.get("/ping")
def ping(
    request,
):
    return PingResponse(message="Hello World!")


@debug_router.get("/demo_celery_task")
def celery_task(request, message: str = "Default message"):
    scheduled_time = timezone.now() + timedelta(seconds=1)

    demo_celery_task.apply_async(args=[message], eta=scheduled_time)  # type: ignore
