<h1 align="center">requesck</h1>
<p align="center">An integrated library for checking email if it is registered on social media</p>

![](https://img.shields.io/badge/SidraELEzz-orange?style=for-the-badge&logo=python.svg) 
<p align="center">
<a href="#"><img title="Made in UAE" src="https://img.shields.io/badge/MADE%20IN-UAE-red.svg?style=for-the-badge&logo=github"></a>
 
</p>
<p align="center">
<img alt="SidraELEzz' Github Stats" src="https://github-readme-stats.vercel.app/api?username=SidraELEzz&show_icons=true&include_all_commits=true&hide_border=true" />

</p>
<p align="center">
<a href="#"><img title="telegram Num" src="https://img.shields.io/badge/telegram%20Num-SidtaTools-red.svg?style=for-the-badge&logo=telegram"></a>
</p>
<p align="center">
<a href="https://github.com/SidraELEzz/followers"><img title="Followers" src="https://img.shields.io/github/followers/SidraELEzz?color=blue&style=flat-square"></a>
</p>

## Installation :
```
pip install requesck

```
## ***Domains are available***

⌯ Gmail 

⌯ Hotmail 

⌯ Outlook

⌯ Yahoo 

⌯ mail.ru

## ***Available social networking site***

⌯ snapchat 

⌯ instagram 

⌯ tiktok

⌯ twitter 

⌯ facebook
### To check the email if it is available on Instagram

``` python
from requesck import check 

email = "<Sidra454@gmail.com>"

checking = check.instagram(str(email))
if (checking) ==True:
	print ("The email is linked to the Instagram account")
	try:
		if ("@gmail.com") in email:
			response = check.gmail(str(email))
			if (response) ==True:
				print("Email is  available ")
			elif (response) ==False:
				print("Email is  available ")
	except:pass
	
elif (checking) ==False:
	print ("The email is not linked to the Instagram account")
 
```

### To get  email business

``` python
from requesck import check 

username = "< username >"
sessionid = "<sessionid>"
response = check.getmail(str(username),str(sessionid))
if str("'The resulting': 'True'") in str(response):
	email = response["email"]
	username = response["username"]
	print(email)
	print(username)
	
elif (response) ==False:
	print("username is not a business")


	
```

## Follow us on social media

[![Github](https://img.shields.io/badge/Github-SidraELEzz-orange?style=for-the-badge&logo=github)](https://github.com/SidraELEzz/)

[![Telegram](https://img.shields.io/badge/Telegram-SidraELEzz-orange?style=for-the-badge&logo=Telegram)](https://t.me/SidraTools)


