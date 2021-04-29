# SNKRS News Bot

## Dependencies

- macOS Big Sur 11.0.1
- Python 3.9.0
- poetry 1.1.4
- ChromeDriver 86.0.4240.22

## Usage

### 1. Clone this repository

```
git clone https://github.com/shimech/snkrs-news-bot.git
cd snkrs-news-bot/
```

### 2. Install ChromeDriver

Access to [this page](https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/), and download the chromedriver which fits your environment.  
After unzip it, place it in the root of this repository.

### 3. Prepare .env

Input a command following below:

```
mv .env.sample .env
```

After that, write your `SLACK_API_TOKEN`, `CHANNEL` (name of your slack channel), and `TEST_CHANNEL` (name of your slack channel for debug)

### 4. Install packages and run by debug-mode

```
make install
make debug-run
```

This bot will be expected to post some messages to your test channel.  
You can post messages to your main channel by run a command following below:

```
make run
```

## Reference

- [SNKRS Web Site](https://www.nike.com/jp/launch)
