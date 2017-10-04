import praw
import time
import random

reddit = praw.Reddit(user_agent= '',
                     client_id= '',
                     client_secret= '',
                     username= 'androidthemesbot',
                     password= '')

admin = 'hypercamel'
mods = ['cerealeater','yoseir2','kumquat_juice','Chiapanacas','Antabaka','HAPPYSADPERSON','anthonyvardiz','Multimoon','Hypercamel']
subreddit = reddit.subreddit('androidthemes')



#This code chooses a set of topic, description, and user for the weekly challenge post
def example():
    #open count.txt
    f1 = open("count.txt","r+")

    #set index to the integer value contained in the
    index = int(f1.read())

    #Question dict
    data = [{'topic':'Command line', 'description':'The best command-line/vintage computer theme', 'user': '-Tilde'}, {'topic':'Choose your own theme', 'description':'Choose you own theme and stick to it!', 'user': 'thetinygoat'}, {'topic':'Memes', 'description':'Make the crappiest low effort theme you can!', 'user': 'SuperScientistofDoom'}, {'topic':'Geocities', 'description':'A web hosting site mostly known for over the top 3D fonts, animated clip art, tiled background images and way too bright colours that are near impossible to distinguish from the background.', 'user': 'maunokki'}, {'topic':'Starry Skies', 'description':'A theme that gives you the feel of a vast open sky filled with stars. You can make it as barebones as you want, or try to add as much functionality as possible without taking away from the feel of the challenge.', 'user': 'maunokki'}, {'topic':'Diary/Notebook', 'description':'Turn your homescreen into a neat notebook! Whether your notebook is filled with stickers and pretty fonts, or you prefer to keep it neat and tidy with strict margins is up to you.', 'user': 'maunokki'}]

    #find the value at 0,0
    f1.seek(0,0)

    #Add 1 to the value of index and then write that value to the file
    f1.write(str(index + 1))

    #close the file
    f1.close()

    #return vars for future use
    return data[index]



#Start main script



#Sets variables to the selected dict values
result = example()

challengeTopic = result["topic"]

challengeDescription = result["description"]

challengeAuthor = result["user"]



#This is a repeat of the code in the function 'example'. It's main purpose is to store the weekl number so that it can be referenced in the title of the weekly challenge post
f1 = open("count.txt","r+")

index = int(f1.read())

challengeNumber = index + 1



#Get top 10 posts of the week
for post in reddit.subreddit('androidthemes').top(time_filter='week'):

    #if the css flair class on any of the posts is weeklychallenge, set the variables
        if '[WC]' in post.title:

            postTitle = (post.title)

            postURL = (post.url)

            postScore = (post.score)

            postAuthor = (post.author)

            postScore = (post.score)

            break


submissionTitle = ('Weekly Challenge #{}' .format(challengeNumber))

#This line is an absolute mess when it comes to code aesthetics, so please forgive me
postText = '\
#Welcome to the /r/androidthemes **Weekly Challenge**\n\n\
&nbsp;\n\n\
Last week\'s champion was **/u/{}** with **[{}]({})**\n\n\
Congratulations! You will be rewarded with a special flair for your efforts \n\n\
&nbsp;\n\n\
#This weeks theme is **{}**\n\n\
###Description:\n\
**{}**\n\n\
*This topic was submitted by /u/{}*\n\n\
&nbsp;\n\n\
The rules are the same as always, but in case you\'re new, here they are:\n\n\
* Themes must use completely original widgets that are **NOT** from a widget pack\n\n\
* Participants can **NOT** reuse themes made in the past\n\n\
* Users from /r/androidthemes and /r/iosthemes are eligible to participate\n\n\
**Reminder:**You MUST post resources or else your post will be taken down\n\n\
Posts will be accepted from the time of posting until exactly 1 week after this post.\n\n\
&nbsp;\n\n\
If you have any questions please send /r/androidthemes a modmail and we will try to respond ASAP.\n\n\
&nbsp;\n\n\
^^^I ^^^am ^^^a ^^^bot ^^^and ^^^this ^^^submission ^^^was ^^^automatically ^^^generated.  ^^^If ^^^I ^^^made ^^^an ^^^oopsie, ^^^please ^^^contact ^^^/u/hypercamel ^^^ASAP' .format(postAuthor, postTitle, postURL, challengeTopic, challengeDescription, challengeAuthor)



#post to subreddit
reddit.subreddit('androidthemes').submit(title=submissionTitle, selftext= postText, send_replies= 'false')

print('Sleeping for 15 seconds')
time.sleep(15)

#Moderator Actions
for submission in reddit.redditor('androidthemesbot').submissions.new(limit=1):

    submission.mod.distinguish(how='yes')

    submission.mod.sticky(state='true', bottom='true')

print('Submission has been distinguished and stickied')
