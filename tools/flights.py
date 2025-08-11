from agents import function_tool

@function_tool
def get_fights(destination: str):
    return f"Flight found to the {destination}: PKR 70000 to PKR 100,000"



@function_tool
def suggest_hotels(destination: str):
    return f"Hotels in the {destination}: Pearl Continental, Marriot, Cafe Aylanto, Xanders"