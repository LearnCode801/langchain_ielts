from langcorn import create_service

app = create_service(
    "api.llm_chain:chain"
)
@app.get("/")
async def introduction():
    return "wellcome to the IELTS Api"

@app.get("/questions/")
async def Question():
    return {
        '1':"What is your full name?", 
        '2':"Can I see your ID?",
        '3':"When you go shopping, do you prefer to pay for things in cash or by card? Why?",
        '4':"Do you ever save money to buy special things? Why/Why not?",
        '5':"Would you ever take a job which had low pay? Why/Why not?",
        '6':"Would winning a lot of money make a big difference to your life? Why/Why not?",
        '7':"Describe a toy you liked in your childhood.What it was? Who gave it to you? What it looked like? Explain why it was a special toy for you?",
        '8':"Do you think toys really help in children's development?",
        '9':"Does modern technology have an influence on children's toys?",
        '10':"In general, do children today have many toys?",
        '11':"How do you think toys will change in the future?"
    }

