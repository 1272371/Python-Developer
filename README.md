Event Scheduler Application

The Event Scheduler application allows users to manage events efficiently. Follow the instructions below to set up and run the application on your local machine.
Running the Event Scheduler App
Clone the Repository

Clone this GitHub repository to your local machine using the following command:

bash

git clone https://github.com/1272371/Python-Developer.git

Navigate to the Project Directory

Move into the project directory using the cd command:

bash

cd event_scheduler_app

Set Up the Virtual Environment (Optional but Recommended)

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

Install Dependencies

Install the required Python dependencies listed in requirements.txt:

bash

pip install -r requirements.txt

Run the FastAPI Application

Execute the FastAPI application by running the main.py file:

bash

uvicorn main:app --reload

This command starts the FastAPI server with automatic reloading enabled, which means the server restarts automatically whenever you make changes to the code.
Running the Flask Application

To run the Flask application, follow these steps:

    Make sure you have Python installed on your system. You can download it from python.org.

    Navigate to the project directory:

    bash

cd event_scheduler_app

Set up a virtual environment (recommended):

bash

python -m venv venv

Activate the virtual environment:

    On Windows:

bash

venv\Scripts\activate

    On macOS and Linux:

bash

source venv/bin/activate

Install the required Python dependencies:

bash

pip install -r requirements.txt

Run the Flask application by executing app.py:

bash

    python app.py

    Access the application by opening a web browser and navigating to http://localhost:5000.

    You can interact with the application by adding, viewing, and deleting events using the provided interface.

Interacting with the Application

    You can add events by filling out the form provided on the main page.
    Existing events will be displayed in the sidebar.
    You can delete events by clicking on the delete button associated with each event.
    The search bar allows you to filter events by title.

Updating the Application

The application is continually being updated. Recent updates will be included in the repository.

Your Event Scheduler application is now ready to run and manage your events effectively!
