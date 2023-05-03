import random


#TODO: implement get request from a website to view/modify
#       cookies and tracked data.

def glitch_shapeshift(gender, age, relationship_status, race):
    gender_options = ["male", "female", "non-binary"]
    age_options = ["18-24", "25-34", "35-44", "45-54", "55+"]
    relationship_options = ["single", "married", "divorced", "widowed"]
    race_options = ["white", "black", "asian", "latino", "other"]
    
    # Generate random tags based on input parameters
    tags = []
    tags.append(random.choice(gender_options) if gender else None)
    tags.append(random.choice(age_options) if age else None)
    tags.append(random.choice(relationship_options) if relationship_status else None)
    tags.append(random.choice(race_options) if race else None)
    
    # Remove any None values
    tags = [tag for tag in tags if tag is not None]
    
    return tags
