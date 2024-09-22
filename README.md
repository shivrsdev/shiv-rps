# Shiv's RPS
A full stack RPS game build in FastAPI and svelte.
If you do not know what RPS is, RPS stands for rock, paper, scissors.
The reason it is full stack is that I plan on adding more functionality such as users, leaderboards, multiplayer and so on, these changes will need, you guessed it... A backend!

### Contact shiv.rs.dev@gmail.com for more info

# Installation
First install [Python](https://www.python.org/) and [Node](https://nodejs.org/en), then enter into your terminal/cmd and follow the instructions.

## Backend
Enter into the ```backend/``` folder and run the following commands:
```
python3 -m venv .venv
```

This will create a virtual environment to then use to install the dependencies, to activate the virtual environment run the following commands based on your OS:
On Windows, run:
```
.venv\Scripts\activate
```

On Unix or MacOS, run:
```
source .venv/bin/activate
```

Now install the dependencies (only FastAPI):
```
pip install fastapi[standard]
```

Then run the backend app:
```
fastapi dev main.py
```

## Frontend
Enter into the ```frontend/``` folder and follow the instructions.
To install all of NPM's dependencies run the following command:
```
npm i
```

Then simply run the frontend server with the last command:
```
npm run dev
```

If you want to build the frontend into plain HTML, CSS and JS run this command:
```
npm run build
```

This command should build the Svelte code into a ```dist/``` folder.
