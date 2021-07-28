#### WEBDRIVER BASIC COMMANDS
###### driver can be any `driver` from `webdriver.Chrome` to `webdriver.Firefox`
- Use `driver.get()` function to go to that url or get page from that url.
- Use `driver.title` function to get title of the page.
- Use `driver.close()` function to close the driver or tab corrosponding to driver.
- Use `driver.current_url` function return url of the page.
- Use `driver.page_source` function to close the driver.
- Use `driver.quit()` to quit the browser.

#### ACCESS HTML OBJECT USING THEIR ATTRIBUTE AND PATHS FROM HTML LOGIC
- Use `driver.get_` put the path into it and use that tag for our use.
- Use `driver.get_element()` take a `By` class object and corrosopind webelement finding data.

#### NAVIGATION COMMANDS
- Use `driver.back()` to navigate to previous page.
- Use `driver.forward()` to navigate to front page.

#### CONDITIONAL COMMANDS
- Use `driver.is_enabled` to ckeck enable or not and can be used with any web element.
- Use `driver.is_displayed` to ckeck it is displayed or not and can be used with any web element.
- Use `driver.is_selected` to ckeck selected or not and it is used with `Checkbox` and `Radio Buttons` only.

#### WAIT COMMANDS
- With the help of _Syncorization_ we can achive balance between `Code Execution` and `Page Response`
- Two ways
    - Make app fast (beyond best logic there are lots of other factor which can affect speed)
    - Place some wait for response and show on screen.
- For `Implicit Wait` use `driver.implicitly_wait()` this make code execution wait for pass argument time.
    - If the element get loaded before that time then excution flow will start.
    - _Implicit Wait_ is use only when we want web-element to be load.
    - This is based to time. Exact or less time to wait but explicit is based on condition.
- An explicit wait is a wait for a certain condition to occur before proceeding further in the code