# Function Vending Machine

A web-based application that generates functions based on user specifications, with a cyberpunk vending machine themed UI.

## Features

-   **Function Generation:** Automatically generates functions in the specified language based on user input for function name, description, inputs, and outputs.
-   **Cyberpunk UI:** A dark mode, cyberpunk vending machine themed user interface with neon colors and glowing effects.
-   **Loading Indicator:** A modal popup with a glowing spinner is displayed while the function is being generated.
-   **Copy to Clipboard:** Easily copy the generated function code to the clipboard.
-   **Input Preservation:** The user's input is preserved and displayed in the output block for context.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/function-vending-machine.git
    cd function-vending-machine
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set the environment variable:**

    Create a `.env` file in the root directory and add your Google API key:

    ```
    GOOGLE_API_KEY=your-api-key
    ```

## Usage

1.  **Run the Flask application:**

    ```bash
    flask run
    ```

2.  Open your web browser and go to `http://127.0.0.1:8080`.

3.  Fill in the form with the desired function specifications and click "Dispense Code".
