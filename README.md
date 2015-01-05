Django-Microblogger
===================

Blogging system built from the ground up with Django and PostgreSQL. 
Based on my Sinatra-Microblogger -- I realized it could be made better with a more robust framework.

<b>Features:</b>
* User login/logout authentication, individual profiles
* Creating, editing, and deleting posts featuring author, title, content, edit date/time, images
* Comment section for each individual post with username, content, date/time
* Post 'like' count and comment upvoting/downvoting
* Flash notice/error/info/success messages
* Search bar: Search across all post titles, authors and content returning list of relevant posts
* Heroku hosting
* Planned: Amazon S3 Storage for persistent image hosting
* Planned: Tag cloud: Easily view frequency of topics across the site

LIVE DEMO: [ https://django-microblogger.herokuapp.com/ ]

<i>Please note that since the heroku hosting is on a free plan, if the site is not accessed within 15 minutes it will temporarily shut down. There will be a few seconds delay when loading the site for the first time, after which it will act normally.</i>
