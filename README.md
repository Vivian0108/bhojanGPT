# BhojanGPT: Explore Indian Cuisine with AI

Welcome to BhojanGPT, a Streamlit-based application that leverages artificial intelligence to explore over 6,000 Indian dishes from our Cleaned Indian Food Dataset. Users can input a list of ingredients, and BhojanGPT will generate a ranked list of dishes with matching ingredients. Choose any dish from the list to get detailed recipe instructions, including ingredient quantities and total calorie count.

## Getting Started

### Prerequisites

Python: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

API Key: An OPEN_API_KEY is required to run the application. Please add your own API key to line 19 of bhojanGPT.py

Python Packages: The application uses several Python packages specified in requirements.txt. The shell script should automatically install those packages when it's run.

### Installation

1. **Clone the Repository**
   
   Start by cloning this repository to your local machine:
   
   ```bash
   git clone https://github.com/Vivian0108/bhojanGPT.git
   cd bhojanGPT

2. **Open a terminal in the project directory**

3. **Run the following command to install the required packages:**
    ```bash
    sh run_app.sh

This will install the packages from requirements.txt and launch the Streamlit application using streamlit run bhojanGPT.py

### Usage

BhojanGPT creates a web interface accessible from a local endpoint in your web browser. To use it:

1. Open a web browser and navigate to the provided local URL (typically http://localhost:8501)

2. Enter a comma-separated list of ingredients in the text box.
Click the "Give me meal suggestions!" button.

3. The application will display a ranked list of dishes with their main ingredients matching your input. 

4. You can then input a dish from that list to view step-by-step recipe instructions, including ingredient quantities and total calories.

### Feedback
Your feedback is most welcome! Feel free to raise any issues or suggestions on the GitHub repository.

### Enjoy!
Let BhojanGPT help you discover delicious meals just from ingredients in your refrigerator using the power of AI and a vast Indian recipe database. Bon Appétit!