# Scenius Games

Scenius is a term coined by musician and producer Brian Eno to describe the intelligence and creativity that emerges from a group of people working together: 
Eno says that scenius is a more useful way to think about culture than the idea of "genius". He believes that good work is a collaboration, and that creativity is always the result of a mind connected to other minds. 

Scenius can emerge from conditions such as: Mutual appreciation, Risky moves are applauded, Friendly competition, Rapid exchange of tools and techniques, and Ideas flow quickly. 

Scenius Games is a collection of collaborative communication tools to help teams work better and shape their own scenius.

## Planning Poker

Planning poker is a good way to improve team understanding and estimation.

## Lean Coffee

Lean coffee is an open, structured approach to communication.

## Developer Notes

### Getting Started

#### Python

Scenius Games uses a python back-end built with Django.  It is build in VSCode on Windows using Ubuntu WSL based on a [Geeks for Geeks description](https://www.geeksforgeeks.org/integrating-django-with-reactjs-using-django-rest-framework/).  Python 3 should already be installed.

First create a virtual environment.
```
python3 -m venv venv
source venv/bin/activate
```
Now setup some tooling and create the backend.
```
pip install django
django-admin startproject backend
cd backend
python manage.py startapp scenius
```

Now let's make sure the defaults all work properly.
```
python manage.py migrate
python manage.py runserver
```

Navigate to the URL provided in the terminal and you should see the Django rocket and say 'The install worked successfully!  Cogratulations!'  Now terminate the server with `ctrl+c` in the terminal.

#### Javascript

Scenius Games uses a javascript frontend built with NextJS.  First install NodeJS and NPM using the package manager.
```
sudo apt install nodejs
sudo apt install npm
```

Now we setup our frontend.  When prompted for a project name just enter `frontend`.  I took all the defaults except for saying no to Typescript.
```
npx create-next-app@latest
```

Let's test that the default isntall works poperly.
```
cd frontend
npm run dev
```

Navigate to the URL provided in the terminal and you should see the default Next.JS page.  Now terminate the server with `ctrl+c` in the terminal.


### Backend

TODO:  Capture notes about backend setup and configuration.

### Frontend

TODO:  Capture notes about frontend setup and configuration.