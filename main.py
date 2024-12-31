import json
import os

# List of questions
questions = [
    "1. Have I attained the goal which I established as my objective for this year? (You should work with a definite yearly objective to be attained as a part of your major life objective.)",
    "2. Have I delivered service of the best possible quality of which I was capable, or could I have improved any part of this service?",
    "3. Have I delivered service in the greatest possible quantity of which I was capable?",
    "4. Has the spirit of my conduct been harmonious and cooperative at all times?",
    "5. Have I permitted the habit of procrastination to decrease my efficiency, and if so, to what extent?",
    "6. Have I improved my personality, and if so, in what ways?",
    "7. Have I been persistent in following my plans through to completion?",
    "8. Have I reached decisions promptly and definitely on all occasions?",
    "9. Have I permitted any one or more of the six basic fears [poverty, criticism, ill health, loss of love of someone, old age, death] to decrease my efficiency?",
    "10. Have I been either 'over-cautious' or 'under-cautious'?",
    "11. Has my relationship with my associates in work been pleasant or unpleasant? If it has been unpleasant, has the fault been partly or wholly mine?",
    "12. Have I dissipated any of my energy through lack of concentration of effort?",
    "13. Have I been open-minded and tolerant in connection with all subjects?",
    "14. In what way have I improved my ability to render service?",
    "15. Have I been intemperate in any of my habits?",
    "16. Have I expressed, either openly or secretly, any form of egotism?",
    "17. Has my conduct toward my associates been such that it has induced them to respect me?",
    "18. Have my opinions and decisions been based upon guesswork, or accuracy of analysis and thought?",
    "19. Have I followed the habit of budgeting my time, my expenses, and my income, and have I been conservative in these budgets?",
    "20. How much time have I devoted to unprofitable effort which I might have used to better advantage?",
    "21. How may I rebudget my time and change my habits so I will be more efficient during the coming year?",
    "22. Have I been guilty of any conduct which was not approved by my conscience?",
    "23. In what ways have I rendered more and better service than I was paid to render?",
    "24. Have I been unfair to anyone, and if so, in what way?",
    "25. If I had been the purchaser of my own services for the year, would I be satisfied with my purchase?",
    "26. Am I in the right vocation, and if not, why not?",
    "27. Has the purchaser of my services been satisfied with the service I have rendered, and if not, why not?",
    "28. What is my present rating on the fundamental principles of success? (Make this rating fairly, and frankly, and have it checked by someone who is courageous enough to do it accurately.)",
]

def collect_answers():
    """Ask questions and collect answers."""
    answers = []
    for question in questions:
        answer = input(f"{question}\nYour answer: ")
        answers.append({"question": question, "answer": answer})
    return answers

def save_answers_to_file(answers, year):
    """Save answers to a JSON file."""
    filename = f"answers_{year}.json"
    with open(filename, 'w') as file:
        json.dump(answers, file, indent=4)
    print(f"Answers saved to {filename}")

def load_answers_from_file(year):
    """Load answers from a JSON file."""
    filename = f"answers_{year}.json"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        print(f"No answers found for the year {year}.")
        return None

def review_answers(year):
    """Review answers for a given year."""
    answers = load_answers_from_file(year)
    if answers:
        print(f"\nReviewing answers for the year {year}:\n")
        for i, entry in enumerate(answers, start=1):
            print(f"{i}. Q: {entry['question']}\n   A: {entry['answer']}\n")
        return answers
    return []

def edit_answer(year):
    """Edit a specific answer."""
    answers = review_answers(year)
    if answers:
        try:
            choice = int(input("Enter the number of the question you want to edit: "))
            if 1 <= choice <= len(answers):
                new_answer = input(f"Enter your new answer for: {answers[choice-1]['question']}\nNew answer: ")
                answers[choice-1]["answer"] = new_answer
                save_answers_to_file(answers, year)
                print("Answer updated successfully.")
            else:
                print("Invalid choice. Returning to main menu.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def delete_answer(year):
    """Delete a specific answer."""
    answers = review_answers(year)
    if answers:
        try:
            choice = int(input("Enter the number of the question you want to delete: "))
            if 1 <= choice <= len(answers):
                removed = answers.pop(choice-1)
                save_answers_to_file(answers, year)
                print(f"Deleted the answer for: {removed['question']}")
            else:
                print("Invalid choice. Returning to main menu.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")            

def export_answers_to_text(year):
    """Export answers to a text file."""
    answers = load_answers_from_file(year)
    if answers:
        filename = f"answers_{year}.txt"
        with open(filename, 'w') as file:
            file.write(f"Answers for the Year {year}\n")
            file.write("=" * 50 + "\n")
            for i, entry in enumerate(answers, start=1):
                file.write(f"Q{i}: {entry['question']}\n")
                file.write(f"Answer: {entry['answer']}\n\n")
        print(f"Answers exported to {filename}")
    else:
        print(f"No answers found for the year {year}. Cannot export.")

def main():
    """Main menu for the questionnaire program."""
    while True:
        print("\nWhat would you like to do?")
        print("1. Answer questions")
        print("2. Review answers")
        print("3. Edit an answer")
        print("4. Delete an answer")
        print("5. Export answers to text")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            year = input("Enter the year for this questionnaire (e.g., 2024): ")
            print("\nAnswer the following questions:")
            answers = collect_answers()
            save_answers_to_file(answers, year)
        elif choice == "2":
            year = input("Enter the year to review answers for (e.g., 2024): ")
            review_answers(year)
        elif choice == "3":
            year = input("Enter the year to edit answers for (e.g., 2024): ")
            edit_answer(year)
        elif choice == "4":
            year = input("Enter the year to delete answers for (e.g., 2024): ")
            delete_answer(year)
        elif choice == "5":
            year = input("Enter the year to export answers for (e.g., 2024): ")
            export_answers_to_text(year)    
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
