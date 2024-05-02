# Introduction

This document exists so that there is a step-by-step way of installing the foundations of this project. 

The source is in src/
If you have git cloned the directory, the source and everything comes with the clone.

# Pre-reqs 

## You have npm, git, python3 and venv module of python on your system

## You have git cloned https://github.com/icdev2dev/betaassi
## You have git cloned https://github.com/icdev2dev/luften



# Short Way

## Backend

### Create a venv
python3 -mvenv ~/envs/demo
source ~/envs/demo/bin/activate     # to activate the virtual environment

### install python libraries

pip install -e betaassi
cd psychic-eureka/src/backend
pip install -r requirements.txt

source ~/creds/openai_personal   # openai api key

### run backend
python core.py

## Frontend 

### configure frontend
cd ../../frontend
npm install

### run frontend
npm run dev











## Long Way

We have two TOP level aspects in the project. Both aspects should be installed under src/.

### Frontend 
The stuff that interacts with the browser. This stuff is written in svelte **without** SvelteKit. Let's install svelte. 

#### Prereqs
You must figure out how to install npm on your system. This is beyond the scope of this document.

#### Install Base Svelte
npm create vite@latest

Name the project: frontend

Choose svelte
  and Javascript

##### Test Base Svelte

cd frontend
npm install
npm run dev

##### Verify
Open browser and see that http://localhost:5173/ actually brings up something

##### Shutdown frontend
CTRL^C out of npm run dev

#### Install Suppporting Libraries
We are going to need two helper libraries: svelte-routing and socket.io-client. More about them in another document.

npm install svelte-routing 
npm install socket.io-client

#### Your foundation for frontend is READY!

npm run dev



### Backend 
The stuff that the frontend interacts with. This backend is also responsible for interacting with the LLM providers (such as OpenAI) to provide answers for the front end. In this manner, the frontend has NO exposure to any keys for the LLM providers. The backend for this project is written in python. 

#### Prereqs
You must install python, pip and the ability to create a virtual environment (through venv) prior; which is **beyond the scope** of this document. You must also have the OPENAI_API_KEY in your environment.


#### git clone betaassi parallel to this project
git clone https://github.com/icdev2dev/betaassi

#### Create a virtual environment outside this project
python3 -mvenv ~/envs/luften

#### Activate that environment on the command prompt
source ~/envs/luften/bin/activate

#### Install betaassi from source (NOT pip install)
pip install ../betaassi


#### Install Flask, Flask-Cors and Flask-SocketIO
pip install Flask
pip install Flask-Cors
pip install Flask-SocketIO

#### 
#### Your foundation for backend is READY!



