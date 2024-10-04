# Readme
* static/css/main.css contains all the css.
* static/js/form.js contains the scripts used.
* app.py has the main logic of the API calls and the Flask routes.
* tests/ has the pytest unit tests
* templates/index.html has the main webpage
* datasets/ shows the final training set and validation set used to finetune the model.
* questions.py contains sample prompts to send to the bot in the form of buttons on the page

### Requirements
* Packages: listed in `requirements.txt` 
* Tested on Windows 10 on a virtual environemnt

### Build steps
* pip install -r requirements.txt
* python app.py

### Test steps
* python -m unittest tests/test_app.py will run the tests for the Flask app.
* python -m unittest tests/test_eval.py will run the tests for the BERTscore calculator.
* python app.py will run the app locally and can be seen in browser window.