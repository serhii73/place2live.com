[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/serhii73/place2live.com/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-python](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![GitHub contributors](https://img.shields.io/github/contributors/serhii73/place2live.com.svg)](https://GitHub.com/serhii73/place2live.com/graphs/contributors/)
[![GitHub stars](https://img.shields.io/github/stars/serhii73/place2live.com.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/serhii73/place2live.com/stargazers/)
![GitHub forks](https://img.shields.io/github/forks/serhii73/place2live.com.svg?style=social)
[![GitHub issues](https://img.shields.io/github/issues/serhii73/place2live.com.svg)](https://GitHub.com/serhii73/place2live.com/issues/)
[![Build Status](https://travis-ci.org/serhii73/place2live.com.svg?branch=master)](https://travis-ci.org/serhii73/place2live.com)
[![Maintainability](https://api.codeclimate.com/v1/badges/47e4016232ba87ac5d4e/maintainability)](https://codeclimate.com/github/serhii73/place2live.com/maintainability)
[![BCH compliance](https://bettercodehub.com/edge/badge/serhii73/place2live.com?branch=master)](https://bettercodehub.com/)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/serhii73/place2live.com.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/serhii73/place2live.com/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/serhii73/place2live.com.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/serhii73/place2live.com/context:python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/64ddc9cc228b4fc485f0d08a55f41977)](https://app.codacy.com/app/serhii73/place2live.com?utm_source=github.com&utm_medium=referral&utm_content=serhii73/place2live.com&utm_campaign=Badge_Grade_Dashboard)
[![Python 3](https://pyup.io/repos/github/serhii73/place2live.com/python-3-shield.svg)](https://pyup.io/repos/github/serhii73/place2live.com/)
[![Updates](https://pyup.io/repos/github/serhii73/place2live.com/shield.svg)](https://pyup.io/repos/github/serhii73/place2live.com/)

# place2live.com

## Running This Project

1. Install [python3](https://www.python.org/downloads), [pipenv](https://github.com/pypa/pipenv#installation) and [git](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/)
2. Clone this repository  
   `git clone https://github.com/serhii73/place2live.com`
3. Get in the `place2live.com` and create a environment  
   `pipenv --python 3.7`
4. Spawn a shell with the dependencies of this project  
   `pipenv shell`
5. Run the Django migrations to set up your models
   ```
   python manage.py makemigrations
   python manage.py makemigrations polls
   python manage.py migrate
   ```
6. Start the development server  
   `python manage.py runserver`
7. In your browser, go to http://localhost:8000

    
