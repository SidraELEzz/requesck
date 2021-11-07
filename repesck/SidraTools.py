try:
	import requests , os , sys , user_agent , json , secrets
	from user_agent import generate_user_agent
	
except ImportError:
	os.system('pip install requests')
	os.system('pip install user_agent')
	
class check:
	
	def gmail(email):
		
		url = "https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=404581&rt=j"
		
		headers = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '3893',
		'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
		'cookie': str(secrets.token_hex(8)*2),
		'google-accounts-xsrf': '1',
		'origin': 'https://accounts.google.com',
		'referer': 'https://accounts.google.com/AddSession/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': str(generate_user_agent()),
		'x-chrome-id-consistency-request': '',
		'x-client-data': 'CI22yQEIorbJAQjBtskBCKmdygEIlqzKAQj4x8oBCKTNygEI3NXKAQj69coBCKicywEI1ZzLAQjknMsBCKmdywEIj57LARj6uMoBGNrDygE=',
		'Decoded': 'message ClientVariations{//Active client experiment variation IDs.repeated int32 variation_id = [3300109, 3300130, 3300161, 3313321, 3315222, 3318776, 3319460, 3320540, 3324666, 3329576, 3329621, 3329636, 3329705, 3329807];// Active client experiment variation IDs that trigger server-side behavior.repeated int32 trigger_variation_id = [3316858, 3318234];',
		'x-same-domain': '1'}
		
		data = {
		'continue': 'https://myaccount.google.com/?utm_source=sign_in_no_continue',
		'service': 'accountsettings',
		'f.req': f'["{email}","AEThLlyp7e8ZsnZVwqW6O6dyrUGthqFi3KgSDIKQ-jIN-HJog_ECd1rQ289cSyeWpvYWmjHgASDBl5ljNHwIWNYfM6YFjUr1qawgVmBEBzgob0Tqp3lsbCDkBo1eTwz319csjVy8B_PfeU41-yRSDTdCwDLcX95Y06Q-qmthw5UvWZtR2AO65Hl_j9y3dGOcyYHlcIqelFau_3w5ckfIhsN_OOoDEpBolrsyqKpRbI7l37prdSp7LT-OFMRA8R9t9nv2ozxQqink",[],null,"SA",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{email}",null,null,null,true,true,[]]',
		'bgRequest': '["identifier","!fX6lfjLNAAVYPFQiWELoHEqEce7DhzsAKQAjCPxG3Usnx0Mt4oCV2WuMmMPNAmHqjS8FF9FLfr_DNs9Ee3KRD9bnAgAAAPFSAAABJ2gBB5kDxcfo1I4QFOC0hQL4sji6wB59zG3NRM8ajk9u0FF3LfCAAkJXofy8ZwjWcqE3xYQA6L4Yygpo75Cd07R4paBKZkGvT15KsoAADsPpXNQDEbZLd8_becZDkV8NecNncn13sId3_E__Nk5cBe9VNTVkCLgxIojVK-ZAH_YFx1cWWVQbUewGgvk-4e7fmV3PLhQTWSNmgb7CafarU4OV1vxY33ru4p9PFQxYI5uTzwzn5ulBCDZq2z8tfLq2Sk8lWIZzjCGpXgcHiZkf9_rLmfLew7JlZjX7o2ggX6uUIgCuWZ0yGWonvBzfYBvkb8PF5VkBERPSUc05peo8ZXDPkVH0Y8PTEsfovcbXn3HPS_91PtTmg2Mtq1Sv8nm0T155kcHuYJMDUnZoz5N1-HjDjeR73rogzDleiRUq90_2qQ0fXEZa3NX2pqusrK_q7NIGCyaXF-kb82jEaFo_l38UBoA25exc6v3tXudke4CYW8AmSr4DmnGXAgsfdiLjTy6KBStGZSRpjljOJLvsI7NxSOxTSG-NtnzoqAo4_pCJkrcCqfQXgAyF_-giWOZd2LCeVHsXigVCXKYnwPjqwTq6AHnzG8VkNPATaRLTusnIXCYWqE6h6ZW3n3LD-ZMvptZefM5HZR4NdEVTm0yEhCUhJqytGxxGRDppzebgNndVHl2_zVSQXbw84sEJKqzMYS1uieJ-cXhAidCN4vZM9VQDeESLJaPR-khrlYzPL5SzcWSBHH-4AcJOd3zo4c-YiSVSU9LRIduito8MaC4iBpCIQRwmsYvRVlVljCmTMcB-CstK7TH7rw2LfW1rVm79QZvpyCuX0vYdrlWo5lzMuIAtQLyoRxsAUIcHDh9b0SKHboABH9WZQMLcx_7WjqkJ4HTf723AVwrhUREmXcomNWG4m6Yd39kejtb_k_tjzz6eVNuBrP1pV4haQ5zflRsf62e3qYtfeMkzcg8bYrKkQievTXaas7dlUBiJEpfJGrB-1ztmyKRq-c_PvaCjJ1eRURTujrS188v6pd6EXCY0cNprrtXgKWDEMQBTJIBYHTP_9djO7XUdNNMlZsIRwNOaVpjJRXO9i0RpyFh_6EO5paqFdtwaVPYPvNyIfl1rydThZNth3jjrP4UZts5SD5M68SvHZNulr5W5vKKfkE9iY2srgJVQMbkjheXT4rycnwZmLjgVP0b7VZvRsgzV4oSgoG9oa4MV4lz74ELZYJXcYoNnWWXMFP6hSkdjDQzhx8QC4PHmqeSfXlx5YG5gswZocfNcVbXloVBsUlmH"]',
		'at': 'AFoagUXYzuwuqMYsRm5RMqDomQCtdHo6Yg:1613081767804',
		'azt': 'AFoagUWgWYFtaBKM-_bHqckBRCFYh-zFbA:1613081767805',
		'cookiesDisabled': 'false',
		'deviceinfo': '[null,null,null,[],null,"SA",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,1,null,false]',
		'gmscoreversion': 'undefined',
		'checkConnection': 'youtube:353:0',
		'checkedDomains': 'youtube',
		'pstMsg': '1'}
		
		response = requests.post(url, data=data, headers=headers)
		
		if (',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[]') in response.text:
			
			return True
		
			
		else:
			
			return False
			
		
			
	def hotmail(email):
		
		url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
		
		headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": str(generate_user_agent()),
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
		
		data = ""
		
		response = requests.post(url, data=data, headers=headers)
		
		if ("Neither") in response.text:
			
			return True
		
		else:
			
			return False
		
		
        
    
    
	def outlook(email):
		
		url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
		
		headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": str(generate_user_agent()),
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
		
		data = ""
		
		response = requests.post(url, data=data, headers=headers)
		
		if ("Neither") in response.text:
			
			return True
		
		else:
			
			return False
		
		
			
	def mailur(email):
		
		url = "https://account.mail.ru/api/v1/user/exists"
		
		headers = {
		"User-Agent": str(generate_user_agent())}
		
		data = {'email': str(email)}
		
		response = requests.post(url, data=data, headers=headers)
		
		if str(response.json()['body']['exists']) == 'False':
			
			return True
		
		else:
			
			return False
		
		
		
	def yahoo(email):
		
		url = "https://login.yahoo.com/?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com"
		
		headers = {
	    'Accept': '*/*',
	    'Accept-Encoding': 'gzip, deflate, br',
	    'Accept-Language': 'en-US,en;q=0.9',
		'Connection': 'keep-alive',
		'Content-Length': '1415',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie': 'B=134vcn5g2bbpe&b=3&s=qj; GUC=AQEBAQFgJwBgL0IbewRH; A1=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE; A3=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE; A1S=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE&j=US; APID=UP41556690-6cb8-11eb-b3a4-0efff797295b; AS=v=1&s=6TWShzYC&d=A60274359|fsC2pD_.2SrPGM4_bsUz35krL9lhVhDkgjs9oXhsOxLn_6Pc8hBjqHW0tTZUOKxW1Y1zSIIqV8njXb.PBOrxDRrXfhwt_k3YX3tVb81JTLriH_Tszus2YORvYGHtNqXPE9F3yHfGj1tRrEMx3QS.xMnEUgRFk9i7ryR0Yf4bO6UwBY4r9bm8AQ.ASviERdysUeNgsFL6cnVVXVGvohfu9Bixh1Dhcc.hiQbM3oiuT6i1Guq0OA.B.gbjd5uXDRZWa0TyIcA8o9NWtu4Xwkod651B5mJVX7OKf8dgbZ.WuLfII7hGEuJIQumcrF0lYSa00bdoHOJITDfIdrZsEOMwapuC8PgyQ7TdTSE7Se2StSmyHt_OHimT4ok1EBYs7obzq9djkL8sdqhQN09zuM.P0vAZbVbbRKNm26l4_7tX8TvedU5dU.XVEOaEfsRKNGvwIhGRO2q7Moz548rof9QZ2j0UkWnjxx4gsEg_63pSZBdZdOiTfkYVYG.D0NO9AWtKGxpheNXOVt8Wxbx_140af0gQ5xSP1cnJU0SjUmj5Ru9doNFEZRGBniEM5cgPEB35OJH3.53XBu52SHyBa7AyJb7eedqqLgadHLn0SmgY8MX56DWB81WOIquyAgMknkBsf6MztjUZISotk83.TPxF93mIfVUWGQ2JsLKC1y_HFDE5JKNx0zoUs7X4MGDCZOQ6jHxB_Ay5TL_vBBZNiWTPzx1WZqow478Le27Q1YoypN5DY_eUfEtfvRJYPtgkHTyS3vABoI8FDC8sLMuuGhc_UjISybNAec2MNdBue96hR8Ni_B1GtP9Vcxfb18x4aZPan.j5.SP4jIYb_wIaIzxjVWYQ6sAJ5NKWWkzHpvxLEinGMde9mfqfBhcOk_rsAEf8XvNv3Ng-~A|C6027014a|FdYuFQD.2Ro5V4q.0EICg_TJUsTz2fCnS0hMzUGvjdLSyX_oe5h3q4pMKSj6upQIIsoS4ZGwTPbxmSx2tRJ7K0ASoA8nNws0p1Qhj7VLTdCTg0zvsfWcgRbzmA0TsCev.pDmairFLmKeHRGB5KsiPOQ1gp3gE_uYOCsMI_X.u.j0p70ia_YSl2jN04k3C50BMKFnfHloILTsDqu87JQF3xDv1LQS8fZICBqfQFEKsUHiRG6L.RCDLHle6V7Zfw170TuTyk5RojQHApkSAGNxyjuSyogaUBcO78_7DlZ3sH4jPeT5poE5M7vi1iyKDS0J0cLHV3kvaJJ_BwY.5pSMfl3XFl.tXlGZQ46RNXoffG7JkBPIQIqLtdiBRA5CU7oVKHFNVQzr24hOhTBx1H9nSeIbniTdnMA214dJ0yxQaxJ7m99RBq8O0vRzqSUmJ2rwSJZREkF3WIk7YAk4GB1BBDle91xLMqMqneJV3PmeTeRjIebH5fFQXjtek3lm1TkRJtt8XUU0U8Lpb5tjHE.LCN9rI_e..bLssuRUZXPZPMqE.8.abHk_VgDnsFf3hn81hopLbddNv11YkwAYO3m7bZQ8Ac5ko9eGUMQA5seI1nLX2ePDXp48qW__nG2e4r0BcevG68vtN4oezAS9W.k4prsy3fLEZiIeLgOcij_18OJAdEZsz.5keMZpxnlwmg5vZL.65dP5gFMfhd9WfgPSBLUM4DS7FiN.R9QgqfR.MD8MSI.yA27JorZqNyCZvBonkFkdv_SjVx67wmwsD0ExysXXz13W12.pAHKPD6HXWhvEw7VAJFPTV_vJm6p3Th8OPrgKgLhgqzwZgeM4ST0gOXwJfuIaspB2zJkjL7ZaZ_RMYsp7nuc29Qmx6k.y.lTVDwCCJzF70A5tQxKPRUMZPJCW8xRlpev2uzp3RbE_0qxPFogAdpqdxn.hZD10GT_fkZfQdNOwT99g87NCV1gQ79GDE_K41cynxh1acViZYWjJUOps8rIO2.MUgbMJiK5URAhdUKU9x7dYN9ozxrMJDDMLdx2iQGm1UJWfz7PBkEVZhJD1SDH2uvBhbn6tLhhU0tIylDoJkRXMPZgW3II-~A; APIDTS=1613099483',
		'Host': 'login.yahoo.com',
		'Origin': 'https://login.yahoo.com',
		'Referer': 'https://login.yahoo.com/?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': str(generate_user_agent()),
		'X-Requested-With': 'XMLHttpRequest'}
		
		data = {
		'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":0,"timezone":"UTC","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":1,"hasLiedBrowser":0,"touchSupport":{"points":10,"event":0,"start":0},"fonts":{"count":33,"hash":"edeefd360161b4bf944ac045e41d0b21"},"audio":"124.04347527516074","resolution":{"w":"1456","h":"818"},"availableResolution":{"w":"778","h":"1456"},"ts":{"serve":1613099481853,"render":1613099482712}}',
		'crumb': 'uQN26u0FMre',
		'acrumb': '6TWShzYC',
		'sessionIndex': 'QQ--',
		'displayName': '',
		'deviceCapability': '{"pa":{"status":false}}',
		'username': str(email),
		'passwd': '',
		'signin': 'Berikutnya',
		'persistent': 'y'}
		
		response = requests.post(url, data=data, headers=headers)
		
		if ('"error":"messages.INVALID_USERNAME"') in response.text:
			
			return True
		
		else:
			
			return False
		
		
			
	
			
	def snapchat(email):
		
		url = "https://accounts.snapchat.com/accounts/merlin/login"
		
		requests.Session().headers = {
        'Host': 'accounts.snapchat.com',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-XSRF-TOKEN': 'missing',
        'Content-Type': 'application/json',
        'Origin': 'https://accounts.snapchat.com',
        'User-Agent': str(generate_user_agent()),
        'Connection':'keep-alive',
        'Referer': 'https://accounts.snapchat.com/accounts/merlin/login'
        }
		
		cookies = {
        'xsrf_token':'missing'
        }
		data = {
        'email':str(email),
        'app':'BITMOJI_APP'
        }
		
		response = requests.post(url, cookies=cookies, json=data)
		
		if response.text.find("hasSnapchat") >= 0 :
			
			return True
		
		else:
			
			return False
		
	def instagram(email):
		
		url = "https://www.instagram.com/accounts/login/ajax/"
		headers ={
        'authority': 'www.instagram.com',
        'method': 'POST',
        'path': '/accounts/login/ajax/',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7',
        'content-length': '277',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=45246725385; csrftoken=u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(generate_user_agent()),
        'x-csrftoken': 'u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '7a3a3e64fa87',
        'x-requested-with': 'XMLHttpRequest'}
		
		data ={
        'username': str(email),
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'}
		
		response = requests.post(url, data=data, headers=headers)
		
		if ('"message":"There was an error with your request. Please try again."') in response.text:
			
			return True
		
		else:
			
			return False
			
	def tiktok(email):
		
		url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/?residence=AE&device_id=6923575826752275974&os_version=14.3&app_id=1233&iid=6951746276598204161&app_name=musical_ly&pass-route=1&vendor_id=EF3C1478-2AFC-4B8E-8030-C608120AECF9&locale=ar&pass-region=1&ac=WIFI&sys_region=US&ssmix=a&version_code=17.2.0&vid=EF3C1478-2AFC-4B8E-8030-C608120AECF9&channel=App%20Store&op_region=AE&os_api=18&idfa=00000000-0000-0000-0000-000000000000&install_id=6951746276598204161&idfv=EF3C1478-2AFC-4B8E-8030-C608120AECF9&device_platform=iphone&device_type=iPhone9%2C4&openudid=3ce553bec09070081e5a698d3a14a988f3642ac4&account_region=&tz_name=Asia%2FDubai&tz_offset=14400&app_language=ar&carrier_region=AE&current_region=AE&aid=1233&mcc_mnc=42402&screen_width=1242&uoo=1&content_language=&language=ar&cdid=FBF67CFE-39E1-4556-A3EB-624A20A434E1&build_number=172025&app_version=17.2.0&resolution=1242%2A2208"
		headers = {
       'Host':'api16-normal-c-alisg.tiktokv.com', 
	   'Connection':'close', 
	   'Content-Length':'76', 
	   'Cookie':'sessionid=b0b2ed352b9394eefc29754dfe80926c', 
       'x-Tt-Token':'2c593820065f9a47b9bf51281eda9604-1.0.0', 
	   'Content-Type':'application/x-www-form-urlencoded', 
	   'x-tt-passport-csrf-token':'b0b2ed352b9394eefc29754dfe80926c', 
       'sdk-version':'2', 
	   'passport-sdk-version':'5.12.1'}
		
		data = {
        'account_sdk_source':'app', 
	    'email':str(email), 
	    'mix_mode':'1', 
	    'type':'31'}
		
		response = requests.post(url, data=data, headers=headers)
		
		if ('"message":"success"') in response.text:
			
			return True
		
		else:
			
			return False
			
	def twitter(email):
		
		url = "https://twitter.com/users/email_available?email="
		headers = {
	    'Host': 'twitter.com',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'User-Agent': str(generate_user_agent()),
		'Cookie': 'personalization_id="v1_6TNKT0FSMkPP7CfzL5Rkfg=="; guest_id=v1%3A159789135703778252; _ga=GA1.2.490437195.1597891367'}
		
		data = {
        'account_sdk_source':'app', 
	    'email':str(email), 
	    'mix_mode':'1', 
	    'type':'31'}
		
		response = requests.get(f'{url}{email}',headers=headers)
		
		if ('"taken":false') in response.text:
			
			return False
		
		else:
			
			return True
			
	def facebook(email):
		
		url ="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+str(email)+"&locale=en_US&password=password&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
	   	
		
		response = requests.get(url)
		
		if ("The password you entered is incorrect. Please try again.") in response.text:
			
			return True
		
		else:
			
			return False
			
	def getmail(username,sessionid):
		
		url = "https://i.instagram.com/api/v1/users/" + str(username) + "/usernameinfo/"
		headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid=4423; shbts=1615496141.469795; rur=VLL; csrftoken=XX5WFM9vN6cYyi5Im4JBcBpKUnZp6uAR; ds_user_id=46476825483; sessionid=" + str(sessionid) + "; fbsr_124024574287414=vmuDaql2sHq2XOVERzyAN3anhRE7rA3ny16i8ToIDP8.eyJ1c2VyX2lkIjoiMTAwMDMyOTg1NDEwMzcwIiwiY29kZSI6IkFRRERReU5zVnRaYTNDOXQ5ZU5oVEpXQ0g0Y0VBb3NtZmRoeTRhWXdLMnNadG1FNVlvMDBSQVBiUmlYTUVnOUlGdHprZWs3enRfQmZGZHBKWEtjbGx1cVdSQXRUVFIxc2RWcFJmbGtLVUwtVFFuN3JRYnNjaGJRSnhBOFVycXhwWUpzWnY0MjJmMXlxcWQ3WlVKc0ZhbHJKR1pCbDQtazRIbFN2b2ZiWUZQc3lKTGg3UzlpX1QyaGN4NWpKX1JSMzlGUXoyTUpWLW1mWF81SlZrUERiUnM4dG9kMFdsbmV4ekZVb181WkRKMFN1WFlVQVQ2Qlp5dVp5UF9IWU93bkR6WGxKYjBhXzlpNmdaN3hFT1YycVNSWmVrSFZ3RkpOQWRHejQ5bWtSQWo0WkctVllZSm9laERkTlZJZk9lekNrVTlJamZscnFPSnp2Rno3VVNta0VlTEtBIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFyTkdaQWYwSjM2WkFwZklKQU9zdlpBbDFubEVhbTk0QU9Kb2ZMeVpCU09SWkMwakc5V0QxWGFoMlFvMVQ1ZUdkVnZ1Z2xGcW9xVnByT1FGYmVJcWxkaVpCeFpBUHljS2NxNk1XbDN6bXJZRXZhZElNcFdaQ3VVTnhaQzRQWkFzVFhrSFJnSnhaQU1ZbFpBeGwwQTZPVHo3MlVXZDM2ZmREblh5dDNFZ0hpMmFKQnQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTYxNTcwMjUyMH0",
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)"}
		
		payload =""
		
		response = requests.Session().get(url, data=payload, headers=headers)
		business = str(response.json()['user']['is_business'])
		if (business == "True"):
			email = str(response.json()["user"]["public_email"])
			if str("@") in email:
				data = {
                'username':username,
                'email':email,
               'The resulting':'True',}
				return data
				
		else:
			return False
		
	#print
	