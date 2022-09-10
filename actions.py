import re
import os
import json

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from pymongo import MongoClient


def DataUpdate4proClient(prtype,entite,email,prcity,tele): 
    CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0.4cjd18h.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    db = client['chatbot']
    coll1 = db['chatbot']
    coll1.insert_one({"client_type":"professionnel",
                        "prtype":prtype,
                         "entite":entite, 
                         "email":email, 
                         "prcity":prcity, 
                         "tele":tele, 
                         })

def DataUpdate4parClient(CONV_ID,name,adress,email): 
    CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0.4cjd18h.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    db = client['chatbot']
    coll1 = db['chatbot']
    coll1.insert_one({"CONV_ID": CONV_ID,
                        "client_type":"particulier",
                        "name":name,
                         "adress":adress, 
                         "email":email, 
                         })

def DataUpdate4parClient_s(CONV_ID,type_,city): 
    CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0.4cjd18h.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    db = client['chatbot']
    coll1 = db['chatbot']
    myquery = {"CONV_ID": CONV_ID}
    newvalues = { "$set": {"op":"lld","type":type_, "city":city} }
    coll1.update_one(myquery, newvalues)
    
def DataUpdate4parClient_n(CONV_ID,type_,city): 
    CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0.4cjd18h.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    db = client['chatbot']
    coll1 = db['chatbot']
    myquery = {"CONV_ID": CONV_ID}
    newvalues = { "$set": {"op":"ls","type":type_, "city":city} }
    coll1.update_one(myquery, newvalues)
                   
def DataUpdate4parClient_a(CONV_ID,type_,budget,city): 
    CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0.4cjd18h.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    db = client['chatbot']
    coll1 = db['chatbot']
    myquery = {"CONV_ID": CONV_ID}
    newvalues = { "$set": {"op":"achat","type":type_, "budget":budget, "city":city} }
    coll1.update_one(myquery, newvalues)
                        

class pa_form_fr(FormAction):
 def name(self):
  return "pa_form_fr"

 def required_slots(self,tracker) -> List[Text]:
  return ["name_fr","adress_fr","email_fr"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
 	return {
            "name_fr": [
                self.from_text(),
            ],
            "adress_fr": [
                self.from_text(),
            ],
            "email_fr": [
                self.from_text(),
            ]
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    DataUpdate4parClient(tracker.sender_id,tracker.get_slot("name_fr"),tracker.get_slot("adress_fr"),tracker.get_slot("email_fr"))
    return []

class saison_form_fr(FormAction):
 def name(self):
  return "saison_form_fr"

 def required_slots(self,tracker) -> List[Text]:
  return ["type_fr","city_fr"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
 	return {
            "type_fr": [
                self.from_text(),
            ],
            "city_fr": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    DataUpdate4parClient_s(tracker.sender_id, tracker.get_slot('type_fr'), tracker.get_slot('city_fr'))
    return []

class n_saison_form_fr(FormAction):
 def name(self):
  return "n_saison_form_fr"

 def required_slots(self,tracker) -> List[Text]:
  return ["ntype_fr","city_fr"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
 	return {
            "ntype_fr": [
                self.from_text(),
            ],
            "city_fr": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    DataUpdate4parClient_n(tracker.sender_id ,tracker.get_slot('ntype_fr'),tracker.get_slot('city_fr'))
    return []

class achat_form_fr(FormAction):
 def name(self):
  return "achat_form_fr"

 def required_slots(self,tracker) -> List[Text]:
  return ["atype_fr","budget_fr","city_fr"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
 	return {
            "atype_fr": [
                self.from_text(),
            ],
            "budget_fr": [
                self.from_text(),
            ],
            "city_fr": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    DataUpdate4parClient_a(tracker.sender_id,tracker.get_slot('atype_fr'),tracker.get_slot('budget_fr'),tracker.get_slot('city_fr'))
    if tracker.get_slot('atype_fr') in ["Bureau","Local commercial","Entrepôt"]:
        dispatcher.utter_template("utter_linkMsg01_fr", tracker)
    elif tracker.get_slot('atype_fr') in ["Ferme","Terrain agricole","Terrain habitable"]:
        dispatcher.utter_template("utter_linkMsg02_fr", tracker)
    else:
        dispatcher.utter_template("utter_linkMsg03_fr", tracker)
    return []

class pr_form_fr(FormAction):
 def name(self):
  return "pr_form_fr"

 def required_slots(self,tracker) -> List[Text]:
  return ["prtype_fr","entite_fr","email_fr","prcity_fr","tele_fr"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
 	return {
            "prtype_fr": [
                self.from_text(),
            ],
            "entite_fr": [
                self.from_text(),
            ],
            "email_fr": [
                self.from_text(),
            ],
            "prcity_fr": [
                self.from_text(),
            ],
            "tele_fr": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    DataUpdate4proClient(tracker.get_slot("prtype_fr"),tracker.get_slot("entite_fr"),tracker.get_slot("email_fr"),tracker.get_slot("prcity_fr"),tracker.get_slot("tele_fr"))
    return []



class pa_form_ang(FormAction):
    def name(self):
     return "pa_form_ang"
   
    def required_slots(self,tracker) -> List[Text]:
     return ["name_ang","adress_ang","email_ang"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
               "name_ang": [
                   self.from_text(),
               ],
               "adress_ang": [
                   self.from_text(),
               ],
               "email_ang": [
                   self.from_text(),
               ]
           }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
       DataUpdate4parClient(tracker.sender_id,tracker.get_slot("name_ang"),tracker.get_slot("adress_ang"),tracker.get_slot("email_ang"))
       return []
   
class saison_form_ang(FormAction):
    def name(self):
     return "saison_form_ang"
   
    def required_slots(self,tracker) -> List[Text]:
     return ["type_ang","city_ang"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
               "type_ang": [
                   self.from_text(),
               ],
               "city_ang": [
                   self.from_text(),
               ],
           }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
       DataUpdate4parClient_s(tracker.sender_id, tracker.get_slot('type_ang'), tracker.get_slot('city_ang'))
       return []
   
class n_saison_form_ang(FormAction):
    def name(self):
     return "n_saison_form_ang"
   
    def required_slots(self,tracker) -> List[Text]:
     return ["ntype_ang","city_ang"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
               "ntype_ang": [
                   self.from_text(),
               ],
               "city_ang": [
                   self.from_text(),
               ],
           }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
       DataUpdate4parClient_n(tracker.sender_id ,tracker.get_slot('ntype_ang'),tracker.get_slot('city_ang'))
       return []
   
class achat_form_ang(FormAction):
    def name(self):
     return "achat_form_ang"
   
    def required_slots(self,tracker) -> List[Text]:
     return ["atype_ang","budget_ang","city_ang"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
               "atype_ang": [
                   self.from_text(),
               ],
               "budget_ang": [
                   self.from_text(),
               ],
               "city_ang": [
                   self.from_text(),
               ],
           }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
       if tracker.get_slot('atype_ang') in ["Office","Commercial space","Storehouse"]:
        dispatcher.utter_template("utter_linkMsg01_ang", tracker)
       elif tracker.get_slot('atype_ang') in ["Farm","Agricultural land","Habitable land"]:
        dispatcher.utter_template("utter_linkMsg02_ang", tracker)
       else:
        dispatcher.utter_template("utter_linkMsg03_ang", tracker)
       DataUpdate4parClient_a(tracker.sender_id,tracker.get_slot('atype_ang'),tracker.get_slot('budget_ang'),tracker.get_slot('city_ang'))
       return []
   
class pr_form_ang(FormAction):
    def name(self):
     return "pr_form_ang"
   
    def required_slots(self,tracker) -> List[Text]:
     return ["prtype_ang","entite_ang","email_ang","prcity_ang","tele_ang"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
               "prtype_ang": [
                   self.from_text(),
               ],
               "entite_ang": [
                   self.from_text(),
               ],
               "email_ang": [
                   self.from_text(),
               ],
               "prcity_ang": [
                   self.from_text(),
               ],
               "tele_ang": [
                   self.from_text(),
               ],
           }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
       DataUpdate4proClient(tracker.get_slot("prtype_ang"),tracker.get_slot("entite_ang"),tracker.get_slot("email_ang"),tracker.get_slot("prcity_ang"),tracker.get_slot("tele_ang"))
       return []

class pa_form_ar(FormAction):
    def name(self):
     return "pa_form_ar"
   
    def required_slots(self,tracker) -> List[Text]:
     return ["name_ar","adress_ar","email_ar"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
               "name_ar": [
                   self.from_text(),
               ],
               "adress_ar": [
                   self.from_text(),
               ],
               "email_ar": [
                   self.from_text(),
               ]
           }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
       DataUpdate4parClient(tracker.sender_id,tracker.get_slot("name_ar"),tracker.get_slot("adress_ar"),tracker.get_slot("email_ar"))
       return []
   
class saison_form_ar(FormAction):
    def name(self):
     return "saison_form_ar"
   
    def required_slots(self,tracker) -> List[Text]:
     return ["type_ar","city_ar"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
               "type_ar": [
                   self.from_text(),
               ],
               "city_ar": [
                   self.from_text(),
               ],
           }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
       DataUpdate4parClient_s(tracker.sender_id, tracker.get_slot('type_ar'), tracker.get_slot('city_ar'))
       return []
   
class n_saison_form_ar(FormAction):
    def name(self):
     return "n_saison_form_ar"
   
    def required_slots(self,tracker) -> List[Text]:
     return ["ntype_ar","city_ar"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
               "ntype_ar": [
                   self.from_text(),
               ],
               "city_ar": [
                   self.from_text(),
               ],
           }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
       DataUpdate4parClient_n(tracker.sender_id ,tracker.get_slot('ntype_ar'),tracker.get_slot('city_ar'))
       return []
   
class achat_form_ar(FormAction):
    def name(self):
     return "achat_form_ar"
   
    def required_slots(self,tracker) -> List[Text]:
     return ["atype_ar","budget_ar","city_ar"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
               "atype_ar": [
                   self.from_text(),
               ],
               "budget_ar": [
                   self.from_text(),
               ],
               "city_ar": [
                   self.from_text(),
               ],
           }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
       DataUpdate4parClient_a(tracker.sender_id,tracker.get_slot('atype_ar'),tracker.get_slot('budget_ar'),tracker.get_slot('city_ar'))
       if tracker.get_slot('atype_ar') in ["مكتب","محل تجاري","مستودع"]:
        dispatcher.utter_template("utter_linkMsg01_ar", tracker)
       elif tracker.get_slot('atype_ar') in ["مزرعة","أرض زراعية","أرض سكنية"]:
        dispatcher.utter_template("utter_linkMsg02_ar", tracker)
       else:
        dispatcher.utter_template("utter_linkMsg03_ar", tracker)
       return []
   
class pr_form_ar(FormAction):
    def name(self):
     return "pr_form_ar"
   
    def required_slots(self,tracker) -> List[Text]:
     return ["prtype_ar","entite_ar","email_ar","prcity_ar","tele_ar"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
               "prtype_ar": [
                   self.from_text(),
               ],
               "entite_ar": [
                   self.from_text(),
               ],
               "email_ar": [
                   self.from_text(),
               ],
               "prcity_ar": [
                   self.from_text(),
               ],
               "tele_ar": [
                   self.from_text(),
               ],
           }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
       DataUpdate4proClient(tracker.get_slot("prtype_ar"),tracker.get_slot("entite_ar"),tracker.get_slot("email_ar"),tracker.get_slot("prcity_ar"),tracker.get_slot("tele_ar"))
       return []