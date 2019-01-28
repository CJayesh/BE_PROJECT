def proceed(t_id):
    import tweepy 
    from ibmWatson import ibms
    from grphy import gplot
    # Fill the X's with the credentials obtained by  
    # following the above mentioned procedure. 
    consumer_key = "##############################" 
    consumer_secret = "################################"
    access_key = "#######################################"
    access_secret = "########################################"
      
    # extract tweets 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    tweet_count = 5

    stuff = api.user_timeline(screen_name = t_id, include_rts=True, count = tweet_count, tweet_mode='extended')

    toa = []    #tweet to analyze

    for status in stuff:
        toa.append(status.full_text)
        
    #print(toa)

    ########################################################################
    #IBM
    emotion = []
    for i in range(tweet_count):
        emotion.append(ibms(toa[i]))

    #emotion = ['anger','sadness','joy','analytical','neutral','anger','sadness','joy']    
#a = proceed('thevirdas')
    #conversion to integer
    em_int = []
    for i in range(tweet_count):      
        if emotion[i] in ['neutral','tentative']:
            em_int.append(0)
        elif emotion[i] in ['analytical','confident']:
            em_int.append(1)
        elif emotion[i] == 'joy':
            em_int.append(3)
        elif emotion[i] == 'anger':
            em_int.append(-1)
        elif emotion[i] == 'worry':
            em_int.append(-2)
        elif emotion[i] == 'sadness':
            em_int.append(-3)
            
    ########################################################################
    #graph plot
    gplot(em_int)

    return dict(zip(toa,emotion))
