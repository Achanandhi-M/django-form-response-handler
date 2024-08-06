# Django Form Response Handler

This project demonstrates how to handle Django form submissions and display custom messages based on the result. It covers creating a simple form, handling submissions, and rendering dynamic feedback on the same page.

## Features

- **Dynamic Form Handling**: Process form submissions and check for existing users.
- **Custom Messages**: Display messages based on the result of the form submission.
- **Single Page Display**: Show results on the same page without redirecting.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Django 5.x

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/django-form-response-handler.git
   cd django-form-response-handler
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## Project Structure

- `login/`
  - `models.py` - Contains the `Login` model.
  - `views.py` - Contains the `LoginView` class for handling form submissions.
  - `templates/`
    - `input.html` - The form input page.
    - `output.html` - The page for displaying form results.
- `twotier/`
  - `settings.py` - Django settings.
  - `urls.py` - URL routing configuration.

## Usage

1. **Access the Form:**

   Open `http://127.0.0.1:8000/user/login/` to view the form page.

2. **Submit the Form:**

   Enter a username and password, then submit the form. Depending on whether the username already exists, you'll see an appropriate message.


## Contributing

Feel free to submit issues, fork the repository, or send pull requests with improvements!
