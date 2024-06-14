## Clone the project
```
git clone https://github.com/ragu101/python-hello-world.git
cd python-hello-world
```
## Setup python environment
```
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

```
## Run tests
```
python -m unittest discover

```
## Run application
```
python hello_world/main.py

```
## Run application with docker
```
docker build -t hello_world_app .
docker run --rm hello_world_app
```