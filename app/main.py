"""Patient Intake Mock API - app setup and router registration."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routers import additional_info, health, insurance, patient, referral
from app.services.errors import PatientNotFoundError

API_PREFIX = "/api/v1"

app = FastAPI(
    title="Patient Intake Mock API",
    version="0.1.0",
    description=(
        "Read-only mock APIs for the five patient intake sections: patient, "
        "insurance, health, referral and additional info. All data is mock; "
        "there is no database."
    ),
)


@app.exception_handler(PatientNotFoundError)
async def patient_not_found_handler(_: Request, exc: PatientNotFoundError) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": str(exc)})


@app.get("/health", tags=["meta"], summary="Liveness check")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


for module in (patient, insurance, health, referral, additional_info):
    app.include_router(module.router, prefix=API_PREFIX)
