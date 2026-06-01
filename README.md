# 🤖 Discord Bot - Complete Feature Set

A fully-featured Discord bot built with **discord.py 2.3.2** featuring a professional ticketing system, moderation tools, admin management, and many more commands.

## ✨ Features

✅ **Ticketing System** - Support tickets with custom categories and admin/mod pinging  
✅ **Moderation** - Ban, kick, timeout commands with reason logging  
✅ **Admin Tools** - Add admins, set prefix, autorole, admin list  
✅ **Music** - Play, pause, stop, resume commands  
✅ **AI Integration** - OpenAI ChatGPT integration  
✅ **Utility** - Minecraft server status, DM functions  
✅ **Automod & Antinuke** - Server protection systems  
✅ **Embed Help Menu** - Beautiful command listing  
✅ **Cog-based** - Organized command structure  
✅ **Owner-only** - Permission checks  
✅ **Welcome System** - Custom welcome messages  
✅ **Auto-responder** - Automated responses  

## 📋 Commands

### 📊 Info Commands
- `!botinfo` - Display bot information
- `!uptime` - Show bot uptime

### 🛡️ Moderation Commands
- `!ban <user> [reason]` - Ban a member
- `!kick <user> [reason]` - Kick a member
- `!timeout <user> <time> [reason]` - Timeout a member (format: 10m, 1h, 1d)

### ⚙️ Admin Commands
- `!setprefix <prefix>` - Change bot prefix
- `!addadmin <user>` - Add admin
- `!adminlist` - List all admins
- `!autorole <role>` - Set autorole for new members

### 🎵 Music Commands
- `!play <song>` - Play a song
- `!stop` - Stop music
- `!pause` - Pause music
- `!resume` - Resume music

### 🤖 AI Commands
- `!ai <question>` - Ask AI a question (requires OpenAI API key)

### 🆘 Ticket Commands
- `!ticketsetup` - Initialize ticket system in current channel
- `!closeticket` - Close current ticket

### 📨 Message Commands
- `!dm <user> <message>` - DM a user
- `!dmall <message>` - DM all members
- `!autoresponder <enable/disable> [message]` - Setup auto responder

### 🔧 Utility Commands
- `!mcstatus <server>` - Check Minecraft server status
- `!automod <enable/disable>` - Toggle automod
- `!antinuke <enable/disable>` - Toggle antinuke
- `!welcome` - Show welcome message

### 📚 Other Commands
- `!help` - Display help menu

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Discord Bot Token
- OpenAI API Key (optional, for AI commands)

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/OfficialSpookyMob/discord-bot.git
cd discord-bot
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure the bot**
Create a `.env` file in the root directory:
```env
TOKEN=your_bot_token_here
OWNER_ID=your_owner_id_here
PREFIX=!
OPENAI_API_KEY=your_openai_key_here
```

5. **Run the bot**
```bash
python main.py
```

## 📁 Project Structure

```
discord-bot/
├── main.py                    # Main bot file
├── config.py                  # Configuration
├── requirements.txt           # Dependencies
├── .env                       # Environment variables (create this)
├── .gitignore                 # Git ignore file
├── README.md                  # This file
├── cogs/
│   ├── __init__.py
│   └── commands/
│       ├── __init__.py
│       ├── botinfo.py         # Bot info commands
│       ├── moderation.py      # Moderation commands
│       ├── admin.py           # Admin commands
│       ├── utility.py         # Utility commands
│       ├── automod.py         # Automod & antinuke
│       ├── music.py           # Music commands
│       ├── fun.py             # Fun & AI commands
│       └── ticketing.py       # Ticketing system
└── utils/
    ├── __init__.py
    └── helpers.py             # Helper functions
```

## 🔐 Permissions Required

The bot requires these Discord permissions:
- Send Messages
- Embed Links
- Manage Messages
- Manage Channels
- Manage Roles
- Ban Members
- Kick Members
- Timeout Members

## 🎫 Ticketing System

The ticketing system features:
- **Dropdown Menu** - Users select from 4 categories
- **Auto Channel Creation** - Private channels created automatically
- **Admin/Mod Pinging** - Admins and Moderators are notified
- **Permission Management** - Only creator and staff can see tickets
- **Easy Closing** - Use `!closeticket` to close and delete

### Categories:
1. 🐛 Bug Report
2. ✨ Feature Request
3. 📞 Appeal Moderation
4. 🆘 General Support

## 🛡️ Admin Roles

For the ticketing system to work properly, create roles named:
- **Admin** - Full access
- **Moderator** - Moderation access

## 📝 Configuration Tips

- **Change Prefix**: Use `!setprefix <new_prefix>`
- **Add Admins**: Use `!addadmin <user>`
- **Set Autorole**: Use `!autorole <role>`
- **Enable Automod**: Use `!automod enable`

## 🤝 Contributing

Feel free to fork this repository and submit pull requests!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Support

For issues or feature requests, please create an issue on the GitHub repository.

---

**Made with ❤️ by SpookyMob**

**Discord.py Version**: 2.3.2  
**Python Version**: 3.8+