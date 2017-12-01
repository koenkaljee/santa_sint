#from geolocation.google_maps import GoogleMaps
#key='AIzaSyA_m4QfJvt6wRwVQQuljj3RVhaHEqN-cto'

#def coordinates(address):
#    coord=[]
#    google_maps=GoogleMaps(api_key=key)
#    location=google_maps.search(location=address)
#    my_location=location.first()
#    coord.append(my_location.lat)
#    coord.append(my_location.lng)
#    return coord

import requests
import json
#from geoloc import coordinates

client_id="c11b1a5fa64a4064911f4558b821bba0"                              #client ID
client_secret="f6f61baf081b4fd4b28d8415af87cfa1"                          #client Secret
redirect_uri="http://localhost"                                           #redirect uri. I've set mine to localhost. This can be changed
grant_type="authorization_code"                                           #default option provided by Instagram

def get_access_token():
    auth_url="https://api.instagram.com/oauth/authorize/?client_id=" + client_id + "&redirect_uri=" + redirect_uri + "&response_type=code"
    print (auth_url)
    print ("Take this url and paste in your browser. Authorize the app: "+auth_url)   #authorization step. need a better way to do this

    redirected_url = input("Now enter the url returned after authorization.\n")    #browser will redirect to a new page whose url will have the code as a response
    code=redirected_url.split('code=')[1]
    
    req_params={"client_id":client_id, "client_secret":client_secret, "redirect_uri":redirect_uri, "grant_type":grant_type, "code":code}
    
    request_url="https://api.instagram.com/oauth/access_token"
    r=requests.post(request_url, data=req_params)                      #making a POST request with the client details as parameters

    data=json.loads(r.text)
    access_token=str(data["access_token"])
    return access_token

def media_search(lat,lng,access_token):
    url="https://api.instagram.com/v1/media/search?lat="+lat+"&lng="+lng+"&distance=5000"+"&access_token="+access_token
    print (url)
    r=requests.get(url)
    resp=json.loads(r.text)
    for i in range(10):                                                         #just getting 10 images. can be changed
        pic_url=resp['data'][i]['images']['standard_resolution']['url']         #getting the image url
        p=requests.get(pic_url)
        f_name=str(location)+ ' pic '+str(i)+'.jpg'
        with open(f_name,'wb') as f:
            f.write(p.content)
            f.close()
        print ("got one")

#location=input("Enter location.\n")
#c=coordinates(location)
#lat=str(c[0])
#lng=str(c[1])

access_token=get_access_token()
media_search([52.428316, 4.738178][52.304989, 5.012917], access_token)

