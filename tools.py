from livekit.agents import RunContext, function_tool

from data_store import save_lead


@function_tool
async def create_tattoo_lead(
    context: RunContext,
    customer_name: str,
    phone_number: str,
    tattoo_idea: str,
    placement: str,
    size: str,
    budget: str,
    preferred_date: str,
) -> str:
    """Save a new tattoo inquiry lead for the studio."""
    lead = {
        "customer_name": customer_name,
        "phone_number": phone_number,
        "tattoo_idea": tattoo_idea,
        "placement": placement,
        "size": size,
        "budget": budget,
        "preferred_date": preferred_date,
    }

    save_lead(lead)
    return f"Lead saved for {customer_name}. The studio will follow up shortly."