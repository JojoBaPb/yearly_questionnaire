# Yearly Questionnaire

A Python-based program designed to help you reflect on your year by answering 28 introspective questions. This tool allows you to document your progress, challenges, and achievements, and generates organized reports for future reference.

## Features

- **Interactive Questionnaire**: Answer 28 thoughtfully crafted questions directly in the program.
- **Save Answers**: Responses are saved in a JSON file for record-keeping.
- **View Full Reviews**: JSON files include both questions and answers for easy reviewing.
- **Export Reports**: Generate a clean, readable text file report of your answers.
- **Standalone Executable**: No Python installation needed to run the program (compiled `.exe` included).

## Getting Started

### Running the Program

1. **Download the Executable**:
   - Navigate to the `dist/` folder in this repository.
   - Download the `.exe` file.
2. **Run the Program**:
   - Double-click the executable file to launch the questionnaire.

### Answering Questions

1. Enter the year when prompted (e.g., `2024`).
2. Answer each question interactively.
3. Review your answers and export a report if desired.

### Example Output

- JSON File:

  ```json
  {
    "Q1": "Yes, I achieved my goal of improving my fitness.",
    "Q2": "I could have delivered better quality service by managing my time better."
  }
  ```

- Text Report:

  ```
  Year: 2024

  1. Have I attained the goal which I established as my objective for this year?
     - Yes, I achieved my goal of improving my fitness.

  2. Have I delivered service of the best possible quality of which I was capable, or could I have improved any part of this service?
     - I could have delivered better quality service by managing my time better.
  ```

## File Structure

- **Source Code**: `main.py` (Python file for developers).
- **Executable**: `dist/main.exe` (Standalone application for end-users).
- **Saved Answers**: `answers_YEAR.json` (e.g., `answers_2024.json`).
- **Reports**: `report_YEAR.txt` (e.g., `report_2024.txt`).

## Requirements

- **For Source Code**: Python 3.8 or higher.
- **For Executable**: Windows OS (compiled executable).

## Development

### Setting Up the Environment

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd yearly-questionnaire
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv yearly_questionnaire_venv
   .\yearly_questionnaire_venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the program:
   ```bash
   python main.py
   ```

### Compiling to an Executable

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Generate the executable:
   ```bash
   pyinstaller --onefile main.py
   ```
3. The `.exe` file will be located in the `dist/` folder.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements and new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

This project was created and maintained by JojoBaPb.
