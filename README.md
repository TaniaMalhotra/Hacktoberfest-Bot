<div align="center">

<img src ="https://github.com/TaniaMalhotra/Hacktoberfest-Bot/blob/master/logo.png">

# Hacktoberfest Bot

This is a Twitter bot to make the process of finding relevant issues for contribution easier. It tweets open and unassigned issues labeled with ```hacktoberfest``` label and thus you can easily choose the one you would like to contribute to!

Follow us!
<a href="https://twitter.com/Hacktoberfesti1" target="_blank"><img src="https://pbs.twimg.com/profile_images/1111729635610382336/_65QFl7B.png" height="20" ></a>
</div>


## How to run the bot in your terminal

- Clone the repository using ```git clone https://github.com/TaniaMalhotra/Hacktoberfest-Issues-Twitter-Bot```
- Navigate to the tweepy-bot directory
- You will need to set the values of the following four environment variables: ```consumer_key``` ```consumer_secret``` ```access_token``` ```access_secret```
- Go to your Twitter app's dashboard and set up a new app [here](https://developer.twitter.com/en/portal/projects-and-apps)
- Get the keys and authenticate
- Run ```python bot.py```


## How to set up your Twitter API

- Go to the [Twitter Developer's site](dev.twitter.com) and sign in with the Twitter account you want to associate with your app.
- After logging in, click on the downwards arrow next to your image and select "My Applications". This is where all your registered Twitter Apps will be shown.
- Create your application by clicking on the 'Create a new application' button.
- Fill in the relevant details in the application form, including your website URL in the website field. This is where your app will be hosted. The Callback URL field can be ignored for the time being. Read and accept the terms and conditions and click on the "Create Your Twitter Application" button and you're good to go!
- You will be taken to a new screen where you need to create an access token for yourself to authorize your Twitter app for your Twitter account. Click on "Create my access token" to do this. Note: You will need to generate a new token if you change app permissions at any future point of time. 
- After the token is generated, choose the type of access you require. Change it to 'read and write' to give the app permission to follow other accounts on your behalf. This will prompt a mobile verification with your Twitter account.
- You are done setting up your Twitter API. Keep a note of the following (which are to be kept secret):
    - Consumer Key
    - Consumer Secret
    - OAuth Access Token
    - OAuth Access Token Secret


## Troubleshooting

I am pretty new to this bot thing. Did you see any errors while running the bot? Consider opening up a new [issue](https://github.com/TaniaMalhotra/Hacktoberfest-Bot/issues)


## Contributing

- If you have any suggestions, drop your suggestions [here](https://github.com/TaniaMalhotra/Hacktoberfest-Bot/new/master).
- Read the Contribution guide [here](https://github.com/TaniaMalhotra/Hacktoberfest-Bot/blob/master/Contribution.md).


## License

Read our license [here](https://github.com/TaniaMalhotra/Hacktoberfest-Bot/blob/master/LICENSE)
