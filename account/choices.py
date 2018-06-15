import datetime
AGE_CHOICES = [(i,i) for i in range(8, 125)]
    
GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
        )
RACE_CHOICES = (
        ('aboriginal indian', 'Aboriginal Indian'),
        ('asian', 'Asian'),
        ('black or african american', 'Black or African American'),
        ('white/caucasian', 'White/Caucasian'),
        ('hispanic or latino', 'Hispanic or Latino'))

EDUCATION_CHOICES = (
    ('did not complete highschool', 'Did not complete Highschool'),
    ('highschool/GED', 'Highschool/GED'),
    ('some college','Some College'),
    ('bachelor\'s degree', 'Bachelor\'s Degree'),
    ('master\'s degree', 'Master\'s Degree'),
    ('advanced or Ph.D', 'Advanced Graduate Work or Ph.D'))

YEARS_CHOICES = [(i,i) for i in range(1892, datetime.datetime.now().year)]
    