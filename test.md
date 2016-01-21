# Configuring a Django App to Connect to Microsoft SQL Server Database

**Revised: January 20, 2016 5:42 PM**

This document describes the the various steps performed to connect to MSSQL from Python/Django using pyodbc.

The steps outlined in this document have been tested on Mac OS X Yosemite with Django 1.9.1, Python 2.7.10., and Microsoft Sql Server 2012 on a windows 10 cpu.  

**Please read this document in its entirety before attempting the steps described below.**

## Requirements

1. A Mac CPU running:

	- Python 2.7.10
	
	- Django 1.9.1
	
	- virtualenv
	
	- pip package manager
	
	- home-brew package manager
  
2. A Django Project

3. A Microsoft SQL Server

## Prerequisites

1. Make sure HomeBrew package manager is installed.

	- Open a command prompt and type:  `brew help`

		If HomeBrew is installed you'll receive a response similar to:

			Example usage:
				brew [info | home | options ] [FORMULA…]
				brew install FORMULA...
				
	- Otherwise install HomeBrew by typing the following in a command prompt:

			ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”

2. Make sure Python is installed.

	- Open a command prompt and type: `python`
	
		If Python is installed you'll receive a response similar to:

			Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:40:30) [MSC v.1500 64 bit (AMD64)] on win32
			Type "help", "copyright", "credits" or "license" for more information.
			
	- Otherwise install python by typing the following in a command prompt:
	
			brew install python

3. Make sure PIP is installed.

	- Open a command prompt and type: `pip`
	
		If PIP is installed you'll receive a response similar to:

			Usage:   
  				pip <command> [options]
			
	- Otherwise install PIP by typing the following in a command prompt:
	
			sudo easy_install pip

4. Make sure virtualenv is installed.

	- Open a command prompt and type: `virtualenv`
	
		If virtualenv is installed you'll receive a response similar to:

			You must provide a DEST_DIR
			
	- Otherwise install virtualenv by typing the following in a command prompt:
	
			pip install virtualenv

4. If you do not have a Django project inside a virtualenv.

	- Make virtualenv directory.
	
		In command prompt type:  `virtualenv <yourenvnamehere>`
			
	- cd into virtualenv directory.
	
		In command prompt type:  `cd <yourenvnamehere>`

	- Activate virtualenv.
	
		In command prompt type:  `source bin/activate`
	
	- Install Django.
	
		In command prompt type:  `pip install django==1.9.1`

	- Start a project.
	
		In command prompt type:  `django-admin.py startproject <nameyourproject>`	

## Connection Setup

1. Install unixODBC.

		In command prompt type:  `brew install unixodbc —universal`	

2. Install FreeTDS with unixODBC.

		In command prompt type:  `brew install freetds --with-unixodbc`

	- Test the Libraries.
	
		In command prompt type:  `tsql -H host_ip -U username -P password -p <1433>`

		If libraries are installed you'll receive a response similar to:
		
			locale is "en_US.UTF-8”
			locale charset is "UTF-8"
			using default charset "UTF-8"
			1>
			
	- Edit `~/.freetds.conf`
	
			[db1]
			host = your host ip
			port = 1433 (your port)
			tds version = 8.0

	- Test the configuration.
	
		In command prompt type:  `tsql -S db -U username -P password`

		If configuration is correct you should receive an output similar to:
		
			locale is "en_US.UTF-8"
			locale charset is "UTF-8"
			using default charset "UTF-8"
			1>
			
	- Edit `~/.odbc.ini`
	
			[odbc1]
			Driver = /usr/local/lib/libtdsodbc.so
			Server = host_ip
			Port   = 1433

	- Test the configuration.
	
		In command prompt type:  `isql odbc1 username password -vvvv`

		You should receive an output similar to:
		
			+---------------------------------------+

			| Connected!                            |
			|                                       |
			| sql-statement                         |
			| help [tablename]                      |
			| quit                                  |
			|                                       |
			+---------------------------------------+
			SQL>

	- Edit `~/.odbcinst.ini`
	
			[FreeTDS]
			Driver = /usr/local/lib/libtdsodbc.so
			Setup = /usr/local/lib/libtdsodbc.so
			FileUsage = 1

	- Edit `~/.odbc.ini`
	
		Change:

			Driver = /usr/local/lib/libtdsodbc.so
			
		To:
		
			Driver = FreeTDS

3. Download, Edit, and install pyodbc



	


***
© 2016 Beastly - All rights reserved.
