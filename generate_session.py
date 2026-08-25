from pyrogram import Client

api_id = 9466310
api_hash = "a2b1f38f9ca7f0e630ffec26dca7360d"

with Client("temp_session", api_id=api_id, api_hash=api_hash) as app:
    print("\n\nआपकी Session String नीचे है, इसे कॉपी करके संभाल लें:\n")
    print(app.export_session_string())
  
