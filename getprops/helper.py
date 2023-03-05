
def find_status(property):
    if(property.status == 1):
        return "Sent to tenant"
    elif (property.status == 2):
        return "Accepted"
    elif (property.status == 3):
        return "Accepted with comment"
    else: 
        return None

def find_type(propertytype):
    pass