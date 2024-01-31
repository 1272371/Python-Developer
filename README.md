# Event Scheduler Application

### =====================================================================================

To run your Event Scheduler app and provide instructions in a GitHub README.md file, follow these steps:

1. Clone the Repository

Clone your GitHub repository to your local machine using the following command:

bash

git clone https://github.com/1272371/Python-Developer.git

2. Navigate to the Project Directory

Move into the project directory using the cd command:

bash

cd event_scheduler_app

3. Set Up the Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for your project to isolate its dependencies. If you haven't set it up yet, you can do so using virtualenv. Install virtualenv if you haven't already:

bash

pip install virtualenv

Then, create a virtual environment in your project directory:

bash

virtualenv .venv

Activate the virtual environment:

    On Windows:

bash

.venv\Scripts\activate

    On macOS and Linux:

bash

source .venv/bin/activate

4. Install Dependencies

Install the required Python dependencies listed in requirements.txt:

bash

pip install -r requirements.txt

5. Run the FastAPI Application

Execute the FastAPI application by running the main.py file:

bash

uvicorn main:app --reload

This command starts the FastAPI server with automatic reloading enabled, which means the server restarts automatically whenever you make changes to the code. 6. Access the Application

Once the server is running, you can access the application by navigating to http://localhost:8000 in your web browser. 7. Interacting with the Application

    You can add events by filling out the form provided on the main page.
    Existing events will be displayed in the sidebar.
    You can delete events by clicking on the delete button associated with each event.
    The search bar allows you to filter events by title.

8. Updating the Application
   The App is still being updated, recent updates will be included below
   \*\*
   Your Event Scheduler application is now ready to run,
