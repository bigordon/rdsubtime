# rdsubtime
a dockerfile to check how much time is left on real debrid sub and push to discord via webhook.

Setup:
1. cd to folder of choice and run:
git clone

2. replace RD api and webhook url in config.json file
3. make any changes in .py file such as amount of days left until youd like to be notified (default is 30)
4. build the dockerfile
   example: docker build -t rd_sub_time .
5. run the container DETATCH
   example: docker run -d --name RDSubTime rd_sub_time

