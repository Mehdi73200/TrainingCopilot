# Project Title: Streamlit Project Targets Dashboard

This project is a Streamlit application designed to display project targets for your organization in a user-friendly manner. The application loads project targets from a CSV file and presents them in an interactive format.

## Project Structure

```
streamlit-app
├── app.py                # Main entry point of the Streamlit application
├── data
│   └── targets.csv       # CSV file containing project targets data
├── pages
│   ├── overview.py       # Overview page displaying a summary of project targets
│   └── details.py        # Details page providing in-depth information about each target
├── requirements.txt      # List of dependencies required to run the application
└── README.md             # Documentation for the project
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:
```
streamlit run app.py
```

Once the application is running, you can access it in your web browser at `http://localhost:8501`.

## Features

- **Overview Page**: Provides a summary of all project targets.
- **Details Page**: Allows users to click on individual targets for more detailed information.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.