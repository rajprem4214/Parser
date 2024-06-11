# Flask Resume Parser API

This is a Flask application that uses the `pyresparser` library to parse resumes.

## Installation

1. Clone this repository.
2. Install the required packages using pip:

   pip install -r requirements.txt

3. Download the NLTK stopwords:

   python -m nltk.downloader stopwords

## Usage

Run the application:

python app.py

The application provides a `/parse_resume` endpoint that accepts POST requests. You can send a resume file as part of the request, and the application will return the parsed data.

## Deployment

You can deploy this application to a platform like Heroku, PythonAnywhere, AWS Elastic Beanstalk, or Google Cloud Platform. Remember to set the environment to production and disable debug mode when deploying your application.

## License

This project is licensed under the terms of the MIT license.
