## Instructions

- Activate env using pipenv `pipenv shell`
- Install dependencies `pipenv install`
- Run the project `python src/__main__.py`


### Config
You can extend the config file `src/config.json` to add new sites to test, or change the current tests (test is a single assertion to check if the ps5 is available or not, eg: check if buy button is enable, etc.)

- cycle: seconds between each iteration (run tests for each site)
- notify_url: webhook url used to post a notification or message (you can use IFTTT) https://betterprogramming.pub/how-to-send-push-notifications-to-your-phone-from-any-script-6b70e34748f6
- notify_method: HTTP method (POST, GET, etc)
- notify_message: message used on the notification (item_name key is replaced by the item name where the assertion occurs)
- items: array of items to test (name, url, selector (css), test_name). test_name refers to what kind of test the script should run against the result of the selector. Tests are defined into scpraper.py
