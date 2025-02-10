import random
questions = [
    {"question": "What is the capital city of INDIA?",
     "options": ["A. Delhi", "B. Moscow", "C. Karachi", "D. Seoul"],
     "answer": "A"},

    {"question": "Which Country has the Highest Life Expectancy?",
     "options": ["A. India", "B. Finland", "C. Hong Kong", "D. Seoul"],
     "answer": "C"},

    {"question": "How many minutes are there in a full week?",
     "options": ["A. 10080", "B. 9860", "C. 60", "D. 10000"],
     "answer": "A"},

    {"question": "Which city is known as 'The Eternal City'?",
     "options": ["A. Paris", "B. Istanbul", "C. Busan", "D. Rome"],
     "answer": "D"},

    {"question": "Which planet has the most moons?",
     "options": ["A. Earth", "B. Saturn", "C. Jupiter", "D. Pluto"],
     "answer": "B"},

    {"question": "Which country did India score their lowest total against in the history of the ODI World Cup?",
     "options": ["A. West Indies", "B. England", "C. New Zealand", "D. Australia"],
     "answer": "D"},

    {"question": "Which cricketer had scored the most runs at the ODI World Cup until 2019?",
     "options": ["A. Sachin Tendulkar", "B. Mohammad Azharuddin", "C. Saurav Ganguly", "D. Rahul Dravid"],
     "answer": "A"},

    {"question": "Which is the longest river in the world?",
     "options": ["A. Nile", "B. Ganga", "C. Amazon", "D. Godavari"],
     "answer": "A"},

    {"question": "Who is the leader of BTS?",
     "options": ["A. Cha Eun-woo", "B. RM", "C. Rowoon", "D. V"],
     "answer": "B"},

    {"question": "Which animal is known as 'The Ship of the Desert'?",
     "options": ["A. Cat", "B. Camel", "C. Elephant", "D. Lion"],
     "answer": "B"}
]


print("\n\t\t\t🎤 🎯 KAUN BANEGA CROREPATI 🎯 🎤\n")
name = input("Enter Your Name: ").upper()
print("\n" + "=" * 50)
print(f"👋 Welcome, {name}!\n")
print("📜 GAME RULES:")
print("✅ You have 10 questions.")
print("✅ Each correct answer awards ₹1000.")
print("❌ A wrong answer will **end the game**.")
print("🔄 You can **quit anytime** by entering '0'.")
print("🎁 You can use a **50-50 lifeline once** (type 'lifeline').")
print("=" * 50)


random.shuffle(questions)

prize_money = 0
lifeline_used = False

# Function to provide a 50-50 lifeline
def use_lifeline(question):
    correct_answer = question["answer"]
    wrong_options = [opt for opt in ["A", "B", "C", "D"] if opt != correct_answer]
    random.shuffle(wrong_options)
    # Remove two wrong options
    removed_options = wrong_options[:2]
    filtered_options = [opt for opt in question["options"] if opt[0] not in removed_options]
    return filtered_options


for i, question in enumerate(questions, 1):
    print(f"\n Question {i}: {question['question']}")
    
    for option in question["options"]:
        print(option)

    while True:
        user_answer = input("\nEnter your answer (A/B/C/D or '0' to quit): ").strip().upper()

        # Quit Option
        if user_answer == "0":
            print("\n🚪 You chose to quit the game.")
            break

        # Lifeline Option
        if user_answer == "LIFELINE":
            if not lifeline_used:
                lifeline_used = True
                filtered_options = use_lifeline(question)
                print("\n🎁 50-50 Lifeline Used! Remaining Options:")
                for option in filtered_options:
                    print(option)
                continue  # Re-ask for the answer after showing filtered options
            else:
                print("\n⚠️ You have already used your lifeline!")
                continue

        # Check if the answer is valid
        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("❌ Invalid input! Please enter A, B, C, or D.")

    # Check Answer
    if user_answer == "0":
        break  # Exit game loop

    if user_answer == question["answer"]:
        print("\n✅ Correct Answer! You win ₹1000 🥳")
        prize_money += 1000
        print(f"💰 Total Prize Money: ₹{prize_money}")
        print("=" * 50)
    else:
        print("\n❌ Wrong Answer! You lose the game. 😞")
        print(f"📌 The correct answer was: {question['answer']}")
        print(f"💰 You won ₹{prize_money}")
        break  # End game

# Final message
print("\n🎊 Thank you for playing,", name, "!")
print(f"🏆 Your final prize money: ₹{prize_money} 🏆\n")
