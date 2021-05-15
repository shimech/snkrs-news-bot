# SNKRS News Bot

## Dependencies

- Python 3.9.0
- poetry 1.1.4

## Usage

### 1. Clone this repository

```sh
git clone https://github.com/shimech/snkrs-news-bot.git
cd snkrs-news-bot/
```

### 2. Install ChromeDriver

Access to [this page](https://chromedriver.chromium.org/downloads), and download the chromedriver which fits your environment.  
After unzip it, place it in the root of this repository.

### 3. Prepare .env

Input a command following below:

```sh
cp .env.sample .env
```

After that, write your `SLACK_API_TOKEN`, `CHANNEL` (name of your slack channel), and `DEBUG_CHANNEL` (name of your slack channel for debug)

### 4. Install packages and run by debug-mode

```sh
make install
make debug
```

This bot will be expected to post some messages to your debug channel.  
You can post messages to your main channel by run a command following below:

```sh
make run
```

## Reference

- [SNKRS Web Site](https://www.nike.com/jp/launch)
