# Scenius Games

Scenius is a term coined by musician and producer Brian Eno to describe the intelligence and creativity that emerges from a group of people working together: 
Eno says that scenius is a more useful way to think about culture than the idea of "genius". He believes that good work is a collaboration, and that creativity is always the result of a mind connected to other minds. 

Scenius can emerge from conditions such as: Mutual appreciation, Risky moves are applauded, Friendly competition, Rapid exchange of tools and techniques, and Ideas flow quickly. 

Scenius Games is a collection of collaborative communication tools to help teams work better and shape their own scenius.

## Assumptions

We will assume that all team members have their own browser and are in a physical room or virtual meeting with voice (and perhaps video).  Each person's browser is private from other team members.

## Planning Poker

Planning poker is a good way to improve team understanding and estimation.  A story is presented to the team for discussion then each team member privately assigns a story point value.  Once all values are submitted they are revealed in unison.  The objective is to identify and resolve misunderstandings to refine the definition of the story for a common understanding.

## Lean Coffee

Lean coffee is an open, structured approach to communication.  An area of discussion is established and individuals are given 5 minutes to write down specific topics or questions within the defined area on cards.  Cards are then ordered to stack duplicates.  The team is then given 5 minutes to vote by placing dots on cards.  Each team member has 3 dots they can place wherever they choose.  After all votes are collected, topics are rank ordered based on vote count and discussed in a kanban with 5 minutes on each card.  At the end of the 5 minute block for a card the team votes:
- Thumbs up:  I have more to learn or share in this discussion and would like 5 more minutes.
- Thumbs down:  I've learened all I need in this discussion and would like to move on.
- Neutral:  I defer to my peers.

## Priority Bake Sale

Priority bake sale is a collective voting approach to establish priorities.  Every team member gets some amount of money which they can put against an item.  The more money an item gets by the end of the sale, the higher it's priority.

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