import re
import requests
import mysql.connector
import numpy as np
import cv2 
import  imutils
import pytesseract
import pandas as pd
import time
import mysql.connector

import time
import requests


def exitMessage():
    url = "https://www.fast2sms.com/dev/bulkV2"

    amount = 35
    upiID = "sumukhjadhav007@okaxis"
    upiUrl = "https://upayi.ml/{}/{}".format(upiID, amount)
    # mycursor.execute("select pnumber from userInfo where vnumber = %s", (text,))

    # number = int(re.sub("[^0-9]", "", str(mycursor.fetchone())))
    number = 9945848007
    message = "Your parking fee is {}. Please pay it using below link {}".format(amount, upiUrl)
    querystring = {"authorization":"CD1rsoVcqH0ROQgafUhPlA9xwMpSWTyXub7I2Nn6tKzkiLdejBu6YyQgJEskzrnwl7ZdxKe8W4a0cLAb",
                    "message":message,
                    "language":"english",
                    "route":"q","numbers":number}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)



# entryMessage()
exitMessage()