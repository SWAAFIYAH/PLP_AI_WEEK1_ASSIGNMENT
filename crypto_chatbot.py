# Predefined Crypto Dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10,
        "description": "Bitcoin is the first cryptocurrency, known for its high market value but significant energy consumption due to proof-of-work.",
        "long_term_rating": "high"
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10,
        "description": "Ethereum is a leading smart contract platform that has transitioned to proof-of-stake, reducing its energy use.",
        "long_term_rating": "high"
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10,
        "description": "Cardano is a research-driven blockchain focused on sustainability and peer-reviewed technology.",
        "long_term_rating": "medium"
    },
    "Polkadot": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7 / 10,
        "description": "Polkadot enables interoperability between blockchains and has a growing ecosystem of parachains.",
        "long_term_rating": "medium"
    },
    "Solana": {
        "price_trend": "volatile",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 5 / 10,
        "description": "Solana offers fast and low-cost transactions, but has faced outages affecting investor confidence.",
        "long_term_rating": "medium"
    }
}


def display_welcome_message():
    """
    Displays the welcome message and introduces the chatbot
    """
    print("\n" + "="*50)
    print("🤖 Welcome to CryptoWise! Your Smart Crypto Advisor 🤖")
    print("="*50)
    print("\nHey there! I'm CryptoWise, your friendly guide to the world of cryptocurrency! 🌟")
    print("I'm here to help you find sustainable and profitable crypto investments.")
    print("Feel free to ask me about different cryptocurrencies, their trends, or sustainability scores!")
    print("\nSome things you can ask me:")
    print("- Which crypto is trending up? 📈")
    print("- What's the most sustainable coin? 🌱")
    print("- Tell me about Bitcoin's sustainability")
    print("- What's the best crypto for long-term investment?")
    print("\nType 'exit' anytime to end our conversation.")
    print("="*50 + "\n")

def get_user_input():
    """
    Gets input from the user and returns it in lowercase
    """
    return input("You: ").lower().strip()

def extract_crypto_name(user_input):
    """
    Returns the name of the crypto mentioned in the user input, or None if not found.
    """
    for coin in crypto_db:
        if coin.lower() in user_input:
            return coin
    return None

def give_crypto_advice(crypto_name, data):
    """
    Analyzes profitability and sustainability based on:
    - Profitability = rising + high market cap
    - Sustainability = low energy use + score > 7/10
    """
    profitable = data["price_trend"] == "rising" and data["market_cap"] == "high"
    sustainable = data["energy_use"] == "low" and data["sustainability_score"] > 0.7  # score is out of 1

    print(f"\nCryptoWise Advisor on {crypto_name}:\n")

    if profitable and sustainable:
        print(" This crypto is both *profitable* and *sustainable*. Great pick!")
    elif profitable:
        print(" This crypto looks *profitable*, but sustainability is a concern.")
    elif sustainable:
        print(" This crypto is *sustainable*, but may not be very profitable right now.")
    else:
        print(" This crypto might not be the best in terms of profitability or sustainability at the moment.")

    print("\n Disclaimer: Crypto is risky—always do your own research!")


def main():
    """
    Main function to run the chatbot
    """
    display_welcome_message()
    
    while True:
        user_input = get_user_input()
        
        if user_input == 'exit':
            print("\nCryptoWise: Thanks for chatting! Remember to always do your own research before investing. Goodbye! 👋")
            break
            
        # This is where the main chatbot logic starts
        # Get trending cryptos and list them
        if( "trend" in user_input or "up" in user_input) and "crypto" in user_input:
            recomment = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
            if recomment:
                print(f"CryptoWise: The following cryptocurrencies are currently trending up: {', '.join(recomment)}")
            else:
                print("CryptoWise: No cryptocurrencies are currently trending up.")
        else:
            crypto_name = extract_crypto_name(user_input)

            # Check for specific crypto name
            if crypto_name:
                info = crypto_db[crypto_name]
                # Check for crypto-name and sustainability pair
                if "sustainable" in user_input or "sustainability" in user_input:
                    print(f"CryptoWise: {crypto_name}'s sustainability score is {info['sustainability_score']*10}/10. "
                          f"Energy use: {info['energy_use']}.")
                    
                # Check for crypto-name and long-term investment pair
                elif "long-term" in user_input or "investment" in user_input:
                    print(f"CryptoWise: {crypto_name} is rated {info['long_term_rating']} for long-term investment. "
                          f"Market cap: {info['market_cap']}.")
                
                # Check for crypto-name and profitability pair
                elif "profitable" in user_input or "profitability" in user_input:
                    give_crypto_advice(crypto_name, info)
                    
                # Otherwise, just output the crypto's info
                else:
                    print(f"CryptoWise: {info['description']}")
                    
            # General sustainability question (no crypto name association)
            elif "sustainable" in user_input or "sustainability" in user_input:
                recomment = max(crypto_db, key=lambda item: crypto_db[item]["sustainability_score"])
                print(f"CryptoWise: The most sustainable cryptocurrency is: {recomment}")

            # General long-term investment question (no crypto name association)
            elif "long-term" in user_input or "investment" in user_input:
                recomment = max(crypto_db, key=lambda item: crypto_db[item]["long_term_rating"])
                print(f"CryptoWise: The best cryptocurrency for long-term investment is: {recomment}")

            # Default response for unrecognized input
            else:
                print("CryptoWise: I'm still learning about that! Let me check my crypto database...")
                print("CryptoWise: I can help you with trending cryptocurrencies, sustainability scores, or specific coins like Bitcoin or Ethereum. "
                      "Try asking about those topics!")
                

if __name__ == "__main__":
    main() 