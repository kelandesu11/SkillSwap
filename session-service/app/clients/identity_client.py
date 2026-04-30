import httpx
from fastapi import HTTPException, status

from app.core.config import get_settings

settings = get_settings()


def validate_profile_exists(profile_id: int, authorization: str) -> dict:
    url = f"{settings.identity_service_url}/api/v1/profiles/{profile_id}"

    try:
        response = httpx.get(
            url,
            headers={"Authorization": authorization},
            timeout=settings.service_request_timeout_seconds,
        )
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Identity Service timed out while validating profile",
        )
    except httpx.RequestError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Identity Service is unavailable",
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Profile {profile_id} does not exist",
        )

    if response.status_code in (401, 403):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token rejected by Identity Service",
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Identity Service returned an error",
        )

    return response.json()