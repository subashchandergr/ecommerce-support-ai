import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")

SYSTEM_PROMPT = """
You are Nova, the customer support assistant for NovaShop.

You help customers with:
- Product questions
- Orders
- Shipping
- Returns
- Refunds
- Damaged products
- Escalation

Rules:
1. Be concise and professional.
2. Never invent order information.
3. If order information is unavailable, ask for the order ID.
4. If the customer asks for a human, offer escalation.
5. Never invent company policies.
"""

while True:

    question = input("\nCustomer: ")

    if question.lower() in ["exit", "quit"]:
        break

    response = client.responses.create(
        model=MODEL,
        instructions=SYSTEM_PROMPT,
        input=question
    )

    print("\nNova:", response.output_text)