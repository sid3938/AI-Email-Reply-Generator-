# AI Email Reply Generator

## Overview

The **AI Email Reply Generator** is a Python-based application that uses the OpenAI API to generate professional email replies. The application allows you to enter email content, generates an appropriate reply using OpenAI's GPT model, and saves both the original email content and AI-generated reply in an SQLite database. The system also provides an interface to view saved replies.

## Features

- **AI-Generated Replies:** Generate professional, context-aware email replies using OpenAI's GPT model.
- **SQLite Database:** Save the original email, AI-generated reply, and timestamp in an SQLite database.
- **Interactive Console Interface:** Choose between generating new replies or viewing saved replies.

## Requirements

- Python 3.x
- `openai` library
- `sqlite3` library (comes pre-installed with Python)

### Install Python Dependencies

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/sid3938/AI-Email-Reply-Generator-.git
   cd AI-Email-Reply-Generator
