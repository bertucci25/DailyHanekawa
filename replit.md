# Discord Bot Project

## Overview
This is a Discord bot written in Python that monitors messages and performs automated moderation. The bot deletes messages containing the word "senjo" and sends a playful response.

## Recent Changes
- **October 16, 2025**: Initial setup in Replit environment
  - Configured Python 3.12 environment with uv package manager
  - Dependencies: discord.py 2.6.4, python-dotenv 1.1.1
  - Set up workflow to run the bot
  - Added DISCORD_TOKEN secret management

## Project Architecture

### Main Components
- **main.py**: Main bot file containing all bot logic
  - Uses discord.py library for Discord API interactions
  - Command prefix: `&`
  - Logging to discord.log file

### Features
1. **Welcome Messages**: Sends DM to new server members
2. **Message Moderation**: Deletes messages containing "senjo" and sends a response
3. **Event Handlers**: 
   - `on_ready`: Confirms bot is online
   - `on_member_join`: Welcomes new members
   - `on_message`: Monitors and moderates messages

### Dependencies
- **discord.py**: Discord API wrapper
- **python-dotenv**: Environment variable management

### Configuration
- **DISCORD_TOKEN**: Required secret for bot authentication
- **Command Prefix**: `&` (can be changed in main.py)
- **Intents**: message_content and members enabled

## Setup Instructions
1. Add your Discord bot token as a secret named `DISCORD_TOKEN`
2. Run the bot using the configured workflow
3. Invite the bot to your Discord server with appropriate permissions

## User Preferences
- Language: Spanish (bot messages are in Spanish)
- Logging: Debug level logging to discord.log file
