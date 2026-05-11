# OAuth 2.0 Lab - GitHub Login

## Description
A Flask web application that implements OAuth 2.0 authentication
using GitHub as the identity provider.

## Tech Stack
- Python 3
- Flask
- Authlib
- GitHub OAuth 2.0

## Installation Guide

1. Clone the repository:
```bash
   git clone https://github.com/daniellavillamer/oauth-lab.git
```
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Add your GitHub Client ID and Secret inside app.py

4. Run the app:
```bash
   python app.py
```
5. Open browser at `http://localhost:5000`

## Routes
| Route | Description |
|-------|-------------|
| `/` | Home page with login link |
| `/login` | Redirects to GitHub OAuth |
| `/callback` | Handles GitHub response |
| `/profile` | Protected profile page |
| `/logout` | Clears session |

## Contributors
| Name |
|------|
| Daniella Villamer