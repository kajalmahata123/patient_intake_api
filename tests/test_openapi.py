def test_all_five_endpoints_documented(client):
    paths = client.get("/openapi.json").json()["paths"]
    for suffix in ("", "/insurance", "/health", "/referral", "/additional-info"):
        assert f"/api/v1/patients/{{patient_id}}{suffix}" in paths
