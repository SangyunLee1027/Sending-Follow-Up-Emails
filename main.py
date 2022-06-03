from util import readcompany, sendemail

if __name__ == '__main__':
    list = readcompany()
    list = list.reset_index()
    for r in list.itertuples():
        name = r.Name
        email = r.Email
        client = r.Client
        sendemail(name, client, email)
    
        
    