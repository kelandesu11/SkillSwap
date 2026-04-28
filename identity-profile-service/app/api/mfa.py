import pyotp
from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session

from app.api.auth import get_current_user, get_db
from app.models.user import User
from app.schemas.mfa import (
    MFASetupResponse,
    MFADisableRequest,
    MFAStatusResponse,
    MFAVerifyRequest,
)

router = APIRouter(prefix="/api/v1/mfa", tags=["mfa"])


@router.post("/setup", response_model=MFASetupResponse)
def setup_mfa(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if current_user.totp_secret:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="MFA is already enabled",
        )

    secret = pyotp.random_base32()

    current_user.totp_secret = secret
    db.commit()
    db.refresh(current_user)

    provisioning_uri = pyotp.totp.TOTP(secret).provisioning_uri(
        name=current_user.email,
        issuer_name="Skillswap",
    )

    return MFASetupResponse(
        secret=secret,
        provisioning_uri=provisioning_uri,
        message="Scan the provisioning URI with an authenticator app and verify with a code.",
    )

@router.post("/verify", response_model=MFAStatusResponse)
def verify_mfa(
    payload: MFAVerifyRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if not current_user.totp_secret:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="MFA is not enabled",
        )
    
    totp = pyotp.TOTP(current_user.totp_secret)

    if not totp.verify(payload.code):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid MFA code",
        )
    
    current_user.totp_enabled = True
    db.commit()
    db.refresh(current_user)

    return MFAStatusResponse(
        totp_enabled=current_user.totp_enabled,
        message="MFA has been enabled successfully.",
    )


@router.post("/disable", response_model=MFAStatusResponse)
def disable_mfa(
    payload: MFADisableRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if not current_user.totp_enabled or not current_user.totp_secret:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="MFA is not enabled",
        )
    
    totp = pyotp.TOTP(current_user.totp_secret)

    if not totp.verify(payload.code):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid MFA code",
        )
    
    current_user.totp_enabled = False
    current_user.totp_secret = None
    db.commit()
    db.refresh(current_user)

    return MFAStatusResponse(
        totp_enabled=current_user.totp_enabled,
        message="MFA has been disabled successfully.",
    )