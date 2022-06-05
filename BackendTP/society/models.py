from unicodedata import name
from django.db import models

SOCIETY_CHOICES = (
    ('lahore','DHA LAHORE'),
    ('gujranwala', 'DHA GUJRANWALA'),
    ('multan', 'DHA MULTAN'),
    ('peshawar','DHA PESHAWAR'),
    # ('quetta','QUETTA'),
    # ('bahawalpur', 'BAHAWALPUR'),
    # ('islamabad','ISLAMABAD'),
    ('lakecityl','LAKE CITY LAHORE'),
    ('nfcl', 'NFC LAHORE'),
    ('statelifel', 'STATE LIFE LAHORE'),
    ('ldacityl', 'LDA CITY LAHORE'),
    # ('parkviewi', 'PARK VIEW ISLAMABAD'),
    # ('eighteeni','EIGHTEEN ISLAMABAD'),
    ('etihadtownl','ETIHAD TOWN LAHORE'),
    ('capitalsmartcityi', 'CAPITAL SMART CITY ISLAMABAD'),
    ('lahoresmartcity', 'LAHORE SMART CITY'),
    ('palmcityl','PALM CITY LAHORE'),
    # ('citihousingmultan','CITI HOUSING MULTAN'),
    ('midcityl','MID CITY LAHORE'),
    ('kingtownl','KING TOWN LAHORE'),
    # ('defenceviewapartmentsl','DEFENCE VIEW APARTMENTS LAHORE'),
    ('wapdatownl','WAPDA TOWN LAHORE'),
    # ('lahorecantt','LAHORE CANTT'),
    ('valenciatown','VALENCIA TOWN'),              
    ('khayabaneamin','KHAYABAN E AMIN'),                
    ('gulberg','GULBERG'), 
    ('suigasphases','SUI GAS PHASES'),
    ('hbfcl','HBFC LAHORE'),
    ('chinarbaghl','CHINAR BAGH LAHORE'),              
    ('awtl','AWT LAHORE'),
    ('alkabirtown', 'AL KABIR TOWN'),
    ('bahriatown', 'BAHRIA TOWN')                
)

PROPERTY_CHOICES = (
    ('plot', 'Plot'),
    ('house', 'House'),
    ('file', 'File'),
    ('commercial', 'Commercial')
)

FILE_CHOICES = (
    ('na', 'N/A'),
    ('Residential Plot', 'Residential Plot'),
    ('Commercial Plot', 'Commercial Plot'),
)

class Plot(models.Model):

    id=models.AutoField(primary_key=True)
    society = models.CharField(max_length=30, choices=SOCIETY_CHOICES, default='lahore')
    phase = models.IntegerField(default=0)
    property_Type = models.CharField(max_length=30, choices=PROPERTY_CHOICES, default='plot')
    file_Type = models.CharField(max_length=40, choices=FILE_CHOICES, default='na')
    area=models.CharField(max_length=100, blank= False)
    price=models.CharField(max_length=100, blank= False)
    contact_Name=models.CharField(max_length=100, blank= False)
    contact_Num=models.CharField(max_length=100, blank= False)
    Note=models.CharField(max_length=120, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'"Society Code: " {self.society}, "Phase: " {self.phase}, {self.property_Type}'


class Video(models.Model):

    id=models.AutoField(primary_key=True)
    link=models.CharField(max_length=150, blank= False)
    video_title=models.CharField(max_length=100, blank= False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'Video Link {self.id}'