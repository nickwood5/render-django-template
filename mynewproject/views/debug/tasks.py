from celery import shared_task
import logging


logger = logging.getLogger()


@shared_task
def demo_celery_task(message: str) -> None:
    logger.info(f"Message from Celery demo task: '{message}'")
