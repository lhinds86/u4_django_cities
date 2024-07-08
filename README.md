### SEBR 0429

# Django Djourneys

![](https://tv-fanatic-res.cloudinary.com/iu/s--7b3Gi-fc--/t_xlarge_l/cs_srgb,d_tv-fanatic-placeholder-square.png,f_auto,fl_strip_profile.lossy,q_auto:420/v1371235958/the-simpsons-in-nyc.png)



For this lab we are going to create a mock travel database, with a number of attractions across a number of cities, all of which have a number of reviews

In this lab, we'll build an app called Djourneys, an app for tracking travel attractions across cities.

## Instructions


1. Set up your virtual environment and activate it.
1. Install dependencies.
1. Follow the Django set up instructions!
1. Fulfill the listed requirements.



## Setup

Read through the setup instructions from our previous labs

The goal of this app is to have a full-CRUD application with a functioning Admin panel

In your SQL file, create a Database called "Djourneys", with a user of "DjourneyUser", and make sure to grant them all permissions

### Pt 1: 

1) Create a Django project with 3 related models, Cities -> Attractions -> Reviews
2) Add whatever properties you think each model should have, but each should have at least 3 different properties with at least 2 different field types
3) There should be at least 2 cities, with 3 attractions each. Add at least 2 reviews to at least 2 attractions

### Pt 2 -> Do NOT attempt this until we cover DRF and Serializers!

1) Convert this project to a RESTful API using the Django Rest Framework
2) Each Model should have an Index/List route, and a Show/Detail route to view

### Bonus

1) Use a front end engine (React or Vanilla JS) and the Axios library to pull, render, and style this data on your browser!
