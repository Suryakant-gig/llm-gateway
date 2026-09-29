from decimal import Decimal


PRICING = {
    "openai/gpt-oss-20b": {
        "input": Decimal("0.075"),
        "output": Decimal("0.30"),
    },
    "gemini-3.5-flash-lite": {
        "input": Decimal("0.30"),
        "output": Decimal("2.50"),
    },
}


def calculate_cost(
    model: str,
    input_tokens: int,
    output_tokens: int,
) -> Decimal:

    price = PRICING[model]

    input_cost = (
        Decimal(input_tokens) / Decimal("1000000")
    ) * price["input"]

    output_cost = (
        Decimal(output_tokens) / Decimal("1000000")
    ) * price["output"]

    return input_cost + output_cost