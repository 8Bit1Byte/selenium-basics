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
- An explicit wait is a wait for a certain condition to occur before proceeding further in the code.

#### INPUT BOXS AND OTHER WEB-ELEMENT
- Mainly class is same for various input box as their look is same apporx.
- To find multiple Input Box or Web-Element use `driver.elements()`.
- Using `element.send_keys()` we can fill the value into text-box.
- To ckeck the status of input box we can use Conditional Commands

#### ALERT AND FRAMES
- Just we have to switch between main window and alert window to access that window.
- Using `driver.switch_to_alert()` function will switch to alert window.
- By `driver.switch_to_alert().accept()/ .dismiss()` can be used to accept and dismiss it.
- To switch to frame we can use `driver.switch_to.frame` pass name or id as param.
- To switch between frames we have to go back to default frame using `driver.switch_to.default_contant()`

#### BROWSER WINDOW SWITCHING COMMANDS
- Every browser command have some id, some hex kind code which is unique map to each window.
- Unique handle value
- `driver.current_window_handle` returns current window handle.
- `driver.window_handles` returns all open windows handle.
- To switch between windows we can use `driver.switch_to.window(handle)`
- To quit a tab use `driver.close()` and to close browser use `driver.quit()`