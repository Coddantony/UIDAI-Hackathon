"""Compact QR payload builder that carries no raw identity attributes."""
import json,base64
def encode(transaction_id:str,challenge:str)->str:
    data={'v':1,'tx':transaction_id,'challenge':challenge};raw=json.dumps(data,separators=(',',':')).encode()
    return base64.urlsafe_b64encode(raw).decode()
