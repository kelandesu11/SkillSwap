import logging

import httpx

from app.core.config import get_settings

settings = get_settings()
logger = logging.getLogger(__name__)


def create_notification(
    profile_id: int,
    message: str,
    notification_type: str,
    authorization: str,
) -> bool:
    url = f"{settings.notification_service_url}/api/v1/notifications"

    payload = {
        "profile_id": profile_id,
        "message": message,
        "type": notification_type,
        "status": "pending",
    }

    try:
        response = httpx.post(
            url,
            json=payload,
            headers={"Authorization": authorization},
            timeout=settings.service_request_timeout_seconds,
        )
    except httpx.TimeoutException:
        logger.error("Notification Service timed out")
        return False
    except httpx.RequestError:
        logger.error("Notification Service is unavailable")
        return False

    if response.status_code >= 400:
        logger.error(
            "Notification Service returned error status=%s body=%s",
            response.status_code,
            response.text,
        )
        return False

    return True