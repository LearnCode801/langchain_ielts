from langcorn import create_service

app = create_service(
    "api.llm_chain:chain"
)
@app.get("/")
async def introduction():
    return "wellcome to the IELTS Api"
