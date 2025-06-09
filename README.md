# Form2PDF

Form2PDF is a minimal Django web application that converts user input from a form into a downloadable PDF document. It demonstrates using Django forms, session storage and the ReportLab library to create a PDF.

## Features

- Simple web form that accepts name, age, email, explanation and an optional image
- Generates a PDF with the provided information using ReportLab
- Saves the PDF on the server and allows the user to download it
- Uses a basic responsive layout for the form pages

## Requirements

- Python 3.11+
- Dependencies listed in `requirements.txt`

## Installation

1. Create and activate a virtual environment (recommended)::

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations and start the development server:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

The app will be available at `http://127.0.0.1:8000/form_data/`.

## Usage

1. Navigate to the form page and submit your details and optional picture.
2. The server generates a PDF and displays it in an iframe.
3. Use the *Download PDF* link to save a copy locally.

## Running Tests

This project currently contains placeholder tests. Run them with:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
