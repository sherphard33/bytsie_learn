css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://firebasestorage.googleapis.com/v0/b/chitiviri-c0a3d.appspot.com/o/WhatsApp-Image-2020-12-02-at-15.56.52.jpeg?alt=media&token=e5b59647-c06e-4d84-a665-17e05bbc7015" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://firebasestorage.googleapis.com/v0/b/chitiviri-c0a3d.appspot.com/o/wiseredge_logo.png?alt=media&token=20c0a45d-ffdb-4ecf-80de-9c7107326d2c">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
