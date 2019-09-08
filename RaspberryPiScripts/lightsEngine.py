from os import path
import qhue
from qhue import Bridge, QhueException, create_new_username
from requests import exceptions
#requests.exceptions.ConnectTimeout
#from requests.exceptions import ConnectTimeout
# the IP address of your bridge
BRIDGE_IP = "192.168.1.127"

# the path for the username credentials file
CRED_FILE_PATH = "qhue_username.txt"
# check for a credential file
if not path.exists(CRED_FILE_PATH):

    while True:
        try:
            username = create_new_username(BRIDGE_IP)
            break
        except QhueException as err:
            print("Error occurred while creating a new username: {}".format(err))

    # store the username in a credential file
    with open(CRED_FILE_PATH, "w") as cred_file:
        cred_file.write(username)

else:
    with open(CRED_FILE_PATH, "r") as cred_file:
        username = cred_file.read()

# create the bridge resource, passing the captured username
bridge = Bridge(BRIDGE_IP, username,1)

# create a lights resource
lights = bridge.lights


def lights(on):
    # query the API
    try:
        print(lights[1].state(on=on))
        print(lights[2].state(on=on))
        print(lights[3].state(on=on))
    except QhueException as error:
        print("error on light state")

def getSwitch():
    try:
        print(bridge.lights[1].state())
        return True
    except exceptions.RequestException as e:
        return False

