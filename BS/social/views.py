from django.shortcuts import redirect, render_to_response

access_token = "2293640288.02a8e6b.5d32d22b328445e9959eda5a1423259e"
client_secret = "1654e3519ff34ed7a6496408f25fc509"
client_id = '02a8e6b1a2524215aa22c90d18f901a9'
client_ip='10.11.0.37'
redirect_uri = 'http://127.0.0.1:8000/social/instagram'

def Authorize_Instagram(request):
    #instagram_client = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    #r=instagram_client.get_authorize_url(scope=['basic'])
    #r='https://instagram.com/oauth/authorize/?client_id=02a8e6b1a2524215aa22c90d18f901a9&redirect_uri=http://127.0.0.1:8000/social/instagram&response_type=token&scope=likes+comments+relationships+basic'
    #g=instagram_client.get_authorize_login_url(scope=['basic'])
    r='127.0.0.1:8000'
    return redirect(r)


def Instagram(request):
    #code = request.REQUEST['code']
    #instagram_client = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,access_token=access_token)
    #api=instagram_client

    #access_token, instagram_user = instagram_client.exchange_code_for_access_token(code=code)
    g=8
    return render_to_response('social.html')
