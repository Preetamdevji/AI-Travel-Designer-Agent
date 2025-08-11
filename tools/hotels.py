from agents import function_tool


@function_tool
def suggest_hotels(destination: str):
    return f"Hotels in the {destination}: Pearl Continental, Marriot, Cafe Aylanto, Xanders"