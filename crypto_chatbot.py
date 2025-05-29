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
            
        # This is where the main chatbot logic will be added later
        print("\nCryptoWise: I'm still learning about that! Let me check my crypto database...")

if __name__ == "__main__":
    main() 