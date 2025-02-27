**QuizApp Backend:**
A simple Django-based backend for a quiz application. The app allows users to take quizzes, and administrators to manage questions.

**Features**
1. Quiz Taking: Users can view a set of questions and select answers. Upon submission, the app calculates the correct answers.
2. Admin Authentication: Admin users can log in with a username and password to manage quizzes.
3. Rest API : Includes RESTful APIs to create, update, and list quizzes which works with Postman call for now. This will be integrated with frontend in future.

**Requirements**
1. Python
2. Django
3. Django REST Framework (for API functionality)
4. SQLite (database)

**API Endpoints:**
<br />
**1. create_quiz**
<br />
API endpoint for creating new quiz questions and choices.
Method: POST
<br />
Parameters:
<br />
question: The quiz question text.
<br />
choices: List of possible choices for the question.
<br />
correct_choice: The index of the correct choice in the choices list.

**2. list_questions**
<br />
API endpoint to list all quiz questions.
<br />
Method: GET

**3. update_quiz**
<br />
API endpoint to update an existing quiz question and its choices.
<br />
Method: PUT
<br />
Parameters:
<br />
question_id: The ID of the question to update.
<br />
question: The new question text.
<br />
choices: The new list of choices for the question.

**4. delete_quiz**
<br />
API endpoint to delete a quiz question.
Method: DELETE
Parameters:
question_id: The ID of the question to delete.

(Temporarily disabled CSRF for testing purposes)

**How to run in local?**
<br />
**1. Clone the repository:**
git clone https://github.com/Sushmitha26/QuizApp-Backend.git

**2. Navigate to the project directory:**
cd QuizApp-Backend

**3. Install dependencies:**
pip install

**4. Apply migrations:**
python manage.py makemigrations
python manage.py migrate

**6. Create a superuser (for admin access):**
python manage.py createsuperuser

**7. Start the development server:**
python manage.py runserver

8. Visit http://localhost:8000/home to access the app.

