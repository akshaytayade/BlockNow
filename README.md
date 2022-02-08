**Activate the virtual environment**
source blockchain-env/bin/activate

**Install packages**
pip3 install -r requirements.txt

**Run the tests**
Make sure to activate the virtual env
python3 -m pytests backend/tests

**Run the application and API**
Make sure to activate the virtual env
python3 -m backend.app

**Run a peer instance**
Make sure to activate the virtual env
export PEER=True && python3 -m backend.app
