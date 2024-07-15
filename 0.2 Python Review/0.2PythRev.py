def create_vid(title,description,hashtags):
	new_vid = {"Title":title,"Description":description,"Likes":0,"Dislikes":0,"Comments":{"username":""},"Hashtags":hashtags}
	return new_vid

def like(vid):
	if "Likes" in vid:
		vid["Likes"] += 1

	return vid 

def dislike(vid):
	if "Dislikes" in vid:
		vid["Dislikes"] += 1

	return vid 
def comment(vid,text,username):
	vid["Comments"] = {username:text}
	return vid

def similar(vid1,vid2):
	

my_vid = create_vid("My Video","Good Video")
for i in range (495):
	like(my_vid)
for i in range (34):
	dislike(my_vid)

print(my_vid)