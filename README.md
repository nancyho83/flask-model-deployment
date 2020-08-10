# Capstone Flask App Template

## Requirements

This repo uses Python 3.8.5. All python packages can be found in the `requirements.txt` file.  The requirements are in `pip` style, because this is supported by Heroku.

To create a new `conda` environment to use this repo, run:
```bash
conda create --name flask-env pip
conda activate flask-env
pip install -r requirements.txt
```

You will likely need to install additional packages to support your deployment.  With the `flask-env` activated, you can run `pip install <package-name>`.  **Once you are ready to deploy**, you can generate your own `requirements.txt` for reproducibility purposes with:
```bash
pip freeze > requirements.txt
```

(You don't need to do this last step until you're ready to push changes and deploy)

## Running the Flask Application

To run in a development environment (on your local computer)
```bash
export FLASK_ENV=development
env FLASK_APP=app.py flask run
```

To run in a production environment (used for deployment, but test it out locally first):
```bash
export FLASK_ENV=production
python app.py
```
