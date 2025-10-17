from twilio.rest import Client
account_sid = "AC63c82fc8d67ea6f1c0f3d36c03a1cff4"
auth_token = "09797cedfcc8ce4d47d624e47bd76d6b"
client = Client(account_sid, auth_token)
message = client.messages.create(
 from_="+19788787883",
 body="Olá estudante do IFB, é uma satisfação ter você aqui, aproveite a jornada.",
 to='+5561996666518='
)
print(message.sid)