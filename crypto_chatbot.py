# COINBUDDY/crypto_chatbot.py
import os
from crypto_data_utils import get_price_trend


DATA_DIR = "/home/lamech/COINBUDDY/crypto_dataset"

crypto_db = {
    "Bitcoin": {
        "file": "BTC.csv",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "file": "ETH.csv",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "file": "ADA.csv",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# Fetch 7-day trend per coin
for coin, info in crypto_db.items():
    file_path = os.path.join(DATA_DIR, info["file"])
    trend = get_price_trend(file_path)
    crypto_db[coin]["price_trend"] = trend

def chatbot_response(user_input):
    query = user_input.lower()

    if "sustainable" in query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f" {best} is the most sustainable option with a score of {crypto_db[best]['sustainability_score']}/10."

    elif "trending" in query or "rising" in query:
        rising = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f" Trending up: {', '.join(rising)}" if rising else "No coins are trending up right now."

    elif "growth" in query or "long-term" in query:
        candidates = [coin for coin, data in crypto_db.items()
                      if data["price_trend"] == "rising" and data["market_cap"] in ["medium", "high"]]
        return f" For long-term growth, consider: {', '.join(candidates)}"

    elif "energy" in query or "eco" in query:
        low_energy = [coin for coin, data in crypto_db.items() if data["energy_use"] == "low"]
        return f" Low-energy cryptos: {', '.join(low_energy)}"

    elif "help" in query:
        return (" Ask me things like:\n"
                "- Which crypto is trending?\n"
                "- What’s the most sustainable coin?\n"
                "- Suggest one for long-term growth\n"
                "- Which coins use low energy?")

    else:
        return " Sorry, I didn’t understand. Try asking about trends, growth, or sustainability."

if __name__ == "__main__":
    print(" Hello there, I’m CoinBuddy!!! A modern Chatbot and Cryto Advisor ,,Ask me about crypto trends and eco-investments.")
    print("Type 'exit' to end.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("CoinBuddy: Auf Wiedersehen!!!,,,Goodbye and good luck with your investments! ")
            break

        print(f"CoinBuddy: {chatbot_response(user_input)}")

