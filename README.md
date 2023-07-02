# 4WheelSpace Django App

## Description
4WheelSpace is a Django-based web application for a car business owner who wants to showcase and sell his cars online. The website allows users to browse through the latest cars, search and filter them by model or price, and make inquiries about the cars they are interested in.

In addition to the frontend development using a Bootstrap template, the application focuses on customizing the default Django admin panel to create a feature-rich and visually appealing admin area. Implementing social login functionality with Google and Facebook is also adopted to enhance user experience.

Live demo: https://4wheelspace.vhtechinnovations.com/


## Requirements
- Python 3.8.x
- pip3
- Django 3.2

Refer to `requirements.txt` file for a full list of required dependencies.


## Installation and Setup
1. Clone the repository from GitHub.
   ```bash
   $ git clone https://github.com/vuxho789/Django-4WheelSpace.git
   ```

2. Navigrate to the working directory.
   ```bash
   $ cd Django-4WheelSpace
   ```

3. Create a virtual environment and install project dependencies.
   
   It is recommended to set up and install a Python *virtual environment* to protect the global environment and avoid dependency conflicts.
   Run the following commands to create a virtual environment (named **"venv"**), and install all required dependencies automatically.
   ```bash
   $ python -m venv venv
   $ source venv/Scripts/activate
   (venv)$ pip install -r requirements.txt
   ```
   
   Note: To deactivate the virtual environment and go back to the global environment. The command below can be used.
   ```bash
   (venv)$ deactivate
   $
   ```

4. Create an environment file.
   
   Using your preferred code editor to create `.env` file in the project folder (i.e. `Django-4WheelSpace` folder). Configure the `.env` file with the following environment variables:
   ```bash
   SECRET_KEY=
   DEBUG=1
   ALLOWED_HOSTS=
   
   DB_NAME=
   DB_USER=
   DB_PASSWORD=
   DB_HOST=
   
   EMAIL_HOST=
   EMAIL_PORT=
   EMAIL_USER=
   EMAIL_PASSWORD=
   EMAIL_TLS=1
   EMAIL_SSL=0

   # If running the media files are stored locally, set USE_S3 to 0 and remove other AWS variables
   USE_S3=
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   AWS_STORAGE_BUCKET_NAME=
   AWS_REGION=
   ```

5. Perform database migrations and create a super user.
   ```bash
   (venv)$ python manage.py migrate
   (venv)$ python manage.py createsuperuser
   ```

6. Run the application.
   
   The application can be run locally using the following command.
   ```bash
   (venv)$ python manage.py runserver
   ```
   The application will spin up on http://localhost:8000/
   
   The admin panel can be access via a secured login page (http://localhost:8000/secured-admin/)


## Contact Me
If you have any questions, please feel free to contact me.
<p align="left">
  <a href="https://www.linkedin.com/in/vutuanho"><img alt="LinkedIn" title="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:vuho.tech@gmail.com"><img alt="Gmail" title="Gmail" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
      

    
      
