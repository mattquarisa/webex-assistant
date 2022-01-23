## Webex Assistant

This repository contains sample code that builds out the functionality of a Webex Bot. The goal of this repository is to provide a single location where Webex bot example code from various sources can be found, and to encourage users to experiment with Webex functionality. A prescriptive guide will be provided within each subfolder describing how to run the project.

A guide can be found below introducing how to create a Webex bot account, installing prequisite libraries within your virtual environment, and making sure you have the right tools installed on your local workstation. A summary of each subfolder and source of code is also provided. These references will be included in README files within each subfolder for their respective project as well.



## Getting Started

Have you ever ran a python file before within your local environment? Go to the link below that corresponds to your local operating system for instructions on installing common developer tools. You can also find some reading below overviewing what a development environment is.

#### Reading
[What is a development environment and why do you need one?](https://developer.cisco.com/learning/tracks/containers/containers-dev-env-setup/containers-dev-what/step/1)

#### Setting up your Local Environment

Please select the relevant operating system based on your local workstation below.

[Setting up your MacOS workstation](https://developer.cisco.com/learning/tracks/containers/containers-dev-env-setup/containers-dev-mac/step/1)

[Setting up your Windows workstation](https://developer.cisco.com/learning/tracks/containers/containers-dev-env-setup/containers-dev-win/step/1)

[Setting up your Linux (Ubuntu) Workstation](https://developer.cisco.com/learning/tracks/containers/containers-dev-env-setup/containers-dev-ubuntu/step/1)

[Setting up your Linux (CentOS) workstation](https://developer.cisco.com/learning/tracks/containers/containers-dev-env-setup/containers-dev-centos/step/1)


#### Downloading and Installing Prequisites

Clone this repository into your local Environment

```
git clone https://github.com/mattquarisa/webex-assistant
```

Create and activate your virtual Environment

```
cd webex-assistant
python3 -m venv env
source env/bin/activate
```

Install prerequisite libraries

```
pip3 install -r requirements.txt
```



## Creating a Webex Bot

Sign in at 'Webex for Developers', and open the "My Webex Apps" menu entry under your avatar. You will then be presented the "My Apps" page:

![S1](https://developer.cisco.com/learning/posts/files/collab-webex-botl-ngrok/assets/images/Step1_my_apps.png)

Click the Create a New App button, and choose "Create a Bot":

![S2](https://developer.cisco.com/learning/posts/files/collab-webex-botl-ngrok/assets/images/Step1_bot.png)

Fill in a name and a unique email identifier for your bot.

![S3](https://developer.cisco.com/learning/posts/files/collab-webex-botl-ngrok/assets/images/Step1_my_awesome_bot.png)

Click Add Bot to create your Bot account. Once the page refreshes, your bot details are displayed. Your bot's access token is accessible on top of the page. Copy / paste your bot's token into a text file or document to store.

![S4](https://developer.cisco.com/learning/posts/files/collab-webex-botl-ngrok/assets/images/Step1_token.png)

At this point, your bot can be added to any Webex space by specifying its email, just as with a regular user.



## Sub Project Overview

The list of projects within this repository are overviewed below:

|  File / Folder  |  Description  |
|  ---  |  ---  |
|  [Out of Office Alerts](/webex-ooo-notice) |  This project creates a webex bot that will send pre-configured "out of office" alerts to users when the host is direct messaged over Webex. |
|  [Generating an OAuth2 User Access Token](/webex-ooo-notice/OAuth-flow) |  This project overviews how to create an application that issues an OAuth2 user access token. This token can be used by applications, such as our out of office Webex bot, to allow it to run for up to 14 days within a new identity token being needed. Please see the Webex out of office bot sub folder for details. |



## References / Sources

[Creating a Webex Bot](https://developer.cisco.com/learning/tracks/collab-cloud/automating-webex-teams-appdev/collab-webex-chatops-bot-itp/step/1)

[Understand the OAuth flow of a Webex Integration](https://developer.cisco.com/learning/modules/creating-webex-integrations-sd/collab-webex-auth/step/1)

[Webex out of office bot](https://blogs.cisco.com/developer/webexoutofofficeautoreply01)

[Understanding Webex API access Tokens](https://developer.cisco.com/learning/modules/webex-extensibility-sd/collab-webex-security-itp/step/2)



## Getting help

- [Webex developer support](https://developer.webex.com/support)

- [Cisco DevNet Developer Support](https://developer.cisco.com/site/support/)



## Contact

For any questions or comments on the code compiled here, please reach out to Matthew Quarisa (mquarisa@cisco.com).
