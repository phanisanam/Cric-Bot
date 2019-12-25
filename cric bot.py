import requests
from datetime import datetime
class scoreget:
    def __init__(self):
        self.url_get_all_matches="http://cricapi.com/api/matches"
        self.url_get_scores="http://cricapi.com/api/cricketScore"
        self.apikey="o92d54OkgEWBaIWDxpXBfMCYaKJ2"
        self.unique_id=""
    def get_unique_id(self):
        uri_params={"apikey":self.apikey}
        resp=requests.get(self.url_get_all_matches,params=uri_params)
        resp_dict=resp.json()
        uid_found=0;
        
        for i in resp_dict['matches']:
            if(i['team-1']=="Delhi" or i['team-2']=="india" and i['matchStarted']):
                todays_date=datetime.today().strftime('%Y-%m-%d')
                if todays_date==i['date'].split("T")[0]:
                    self.unique_id=i['unique_id'];
                    uid_found=1
                    break
        if not uid_found:
            self.unique_id=-1;
        send_data=self.current_score(self.unique_id);
        return send_data;
                    
    def current_score(self,unique_id):
        data=""
        if unique_id==-1:
            data="NO india matches today"
        else:
            uri_params={"apikey":self.apikey,"unique_id":unique_id}
            resp=requests.get(self.url_get_scores,params=uri_params)
            resp_dict=resp.json()
            try:
                data="Here the score is:\n"+resp_dict['stat']+"\n"+resp_dict['score']
            except KeyError as e:
                print(e)
        return data


if __name__=="__main__":
     ob_score=scoreget()
     whatsapp_msg=ob_score.get_unique_id();
     print(whatsapp_msg)
     from twilio.rest import Client
     a_sid="ACf684ba82c43de1865fbd151977fce4a8"
     auth_token="123bdeb15ed8079804aa458c5826d959"
     client=Client(a_sid,auth_token)
     print("executed");
     message=client.messages.create(body=whatsapp_msg, from_='whatsapp:+14155238886',to='whatsapp:+919640751504')

    
    
    

                
            
            
                
        
        
        

