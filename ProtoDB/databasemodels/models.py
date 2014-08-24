from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    join_date = models.DateTimeField('date joined')
    #pass_hash #TODO
    affiliation = models.CharField(max_length=100)
    #comment_list = models.ForeignKey(Comment) # TODO: change to have User and Protocol reference the same comment space in db? store primary keys of protocol comments as integers?
    about = models.CharField(max_length=500) # short biography
    #picture = models.FileField() #TODO: use correct argument options
    #access_level #TODO: can this be done through django.contrib.auth?
    
    def __str__(self):
        return self.name
    

class Keyword(models.Model):
    word = models.CharField(max_length=25)
    
    def __str__(self):
        return self.word
    

class Protocol(models.Model):
    publisher = models.ForeignKey(User) # who published the protocol
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=100) # title of the protocol
    description = models.CharField(max_length=500) # short description for the protocol when browsing
    keywords = models.ManyToManyField(Keyword, blank=True) # keywords for searching for protocols, not required
    text = models.TextField() # all details and descriptions for the protocol
    #calc_methods = models.Field(CustomField) # calculator part - later! Within: need list of parameters and dependencies
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    protocol = models.ForeignKey(Protocol) # many comments for one protocol
    user = models.ForeignKey(User) # many comments for one user
    pub_date = models.DateTimeField('date published')
    text = models.TextField()
    
    def __str__(self):
        return self.pub_date # can change to something more useful
    

class Rating(models.Model):
    protocol = models.ForeignKey(Protocol) # many ratings for one protocol
    user = models.ForeignKey(User) # many given ratings for one user
    integer = models.PositiveSmallIntegerField() #rate between 1-5, e.g.
    text = models.TextField() # rant space for the rating
    
    def __str__(self):
        return user # can change to something more useful

