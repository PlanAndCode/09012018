import json
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from post.receive import planCodeAPI




deneme_json = '''{  "$schema": "http://json-schema.org/draft-04/schema#",
       "title": "Response information",
       "type": "object",
       "description": "Contains method(method) and its execution status with description",
        "object_type": "tmp",
         "method": "build",
         "status": "TRUE",
         "description": "tmp",
         "project_name": "Please",
		 "github_login": "gtusoftware2017",
		 "github_password": "software2017",
		 "repository_url": "https://github.com/GtuDevOps/Please.git",
         "trello_api": "f76350738450d09229b56392d99b2a2c",
         "trello_token": "e33437ebf7ea4f97b74f208e830a161e21ce99c7a492d417f6e0dc3bed7655b5"
}'''


def main_function(json_file):
	json_file = json.loads(json_file)
	print(json_file)
	user_id = json_file['github_login']
	user_pass = json_file['github_password']
	repository_url = json_file['repository_url']
	repository_url = repository_url.split("/")[3]
	trello_api = json_file['trello_api']
	trello_token = json_file['trello_token']
	method_name = json_file['method']
	status = json_file['status']
	project_name = json_file['project_name']

	print("LOGIN:\n" + user_id + user_pass + "\n" + repository_url+"\n"+trello_api+"\n"+trello_token)
	pc=planCodeAPI(user_id, user_pass, repository_url)
	print("SELECTING PROJECT: " + project_name)
	pc.chooseProject(project_name)
	if method_name=="build":
		if status == "TRUE":
			pc.moveAllCardToTEST()
		else:
			pc.moveAllCardToDOING()
			
	elif method_name=="test":
		if status == "TRUE":
			pc.moveAllCardToDEPLOY()
		else:
			pc.moveAllCardToDOING()
	
	elif method_name=="deploy":
		if status == "FALSE":
			pc.moveAllCardToDOING()


main_function(json_file)
