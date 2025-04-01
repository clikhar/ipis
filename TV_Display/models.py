from django.db import models

# Create your models here.
class Train_Data():
    id:int
    trainNo:str
    trainName:str
    trainNameHindi:str
    EAT:str
    EDT:str
    A_D:str
    PFNo:str

class Train_Coach():
    id:int
    train_name:str
    coach_position:str