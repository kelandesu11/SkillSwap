from pydantic import BaseModel


class MFASetupResponse(BaseModel):
    secret: str
    provisioning_uri: str
    message: str


class MFAVerifyRequest(BaseModel):
    code: str


class MFADisableRequest(BaseModel):
    code: str


class MFAStatusResponse(BaseModel):
    totp_enabled: bool
    message: str