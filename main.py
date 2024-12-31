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
    "10. Have I been either “over-cautious,” or “under-cautious”?",
    "11. Has my relationship with my associates in work been pleasant or unpleasant? If it has been unpleasant, has the fault been partly or wholly mine?",
    "12. Have I dissipated any of my energy through lack of concentration of effort?",
    "13. Have I been open-minded and tolerant in connection with all subjects?",
    "14. In what way have I improved my ability to render service?",
    "15. Have I been intemperate in any of my habits?",
    "16. Have I expressed, either openly or secretly, any form of egotism?",
    "17. Has my conduct toward my associates been such that it has induced them to respect me?",
    "18. Have my opinions and decisions been based upon guesswork, or accuracy of analysis and thought?",
    "19. Have I followed the habit of budgeting my time, my expenses and my income, and have I been conservative in these budgets?",
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
    answers = {}
    for i, question in enumerate(questions, start=1):
        answer = input(f"{i}. {question}\nYour answer: ")
        answers[f"Q{i}"] = answer
    return answers

def save_answers_to_file(answers, year):
    filename = f"answers_{year}.json"
    with open(filename, 'w') as file:
        json.dump(answers, file, indent=4)
    print(f"Answers saved to {filename}")

def main():
    year = input("Enter the year for this questionnaire (e.g., 2024): ")
    print("\nAnswer the following questions:")
    answers = collect_answers()
    save_answers_to_file(answers, year)

if __name__ == "__main__":
    main()
