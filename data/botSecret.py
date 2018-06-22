def bot_token():
    token = 'NDU5NTQzMzY3MDkzNzE0OTU0.Dg4WRw.HNa_NQcFUwyI3dQlAHpGp8aDGnM'
    if token == None:
        print('Please add bot token at above in src/botSecret.py')
        exit()
    else:
        return token