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
    request_id: str
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
            headers={
                "Authorization": authorization,
                "X-Request-ID": request_id,
            },
            timeout=settings.service_request_timeout_seconds,
        )
    except httpx.TimeoutException:
        logger.error(
            {
                "request_id": request_id,
                "downstream": "notification-service",
                "target": url,
                "success": False,
                "error": "timeout",
            }
        )
        return False
    except httpx.RequestError:
        logger.error(
            {
                "request_id": request_id,
                "downstream": "notification-service",
                "target": url,
                "success": False,
                "error": "request_error",
            }
        )
        return False
    
    logger.info(
        {
            "request_id": request_id,
            "downstream": "notification-service",
            "target": url,
            "success": response.status_code < 400,
            "status_code": response.status_code,
        }
    )

    if response.status_code >= 400:
        logger.error(
            "Notification Service returned error status=%s body=%s",
            response.status_code,
            response.text,
        )
        return False

    return True