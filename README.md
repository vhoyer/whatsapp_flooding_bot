WhatsApp flooding bot
=====================

This is a simple python script that uses the selenium driver to open the [webwhasapp](https://web.whatsapp.com/) in the Firefox web browser to run a loop that sends how many messages you want (we all hope your computer doesn't run out of memory). It finds the contact you want by the name you gave the person, and enter the message "Nº of msg left: [a number]". When it is over, it sends the message "The flood has been planted".

This is a project made for fun with no intention to harm anyone (except the target LOL), it is totally free, and you can read, modify, improve it, use in any way you want. If you made an improvement to it, just make a pull request, I'd be happy to see what you've done.

##How to:

######Recommendation:
- You probably have to have Firefox installed in your computer for it to work, I mean, I haven't tested it, but it shouldn't work.
- You probably don't want to close the Firefox when it opens, otherwise it will crash the script.

######step by step:

1. When the script starts, it will boot the Firefox browser, it will redirect to the `https://web.whatsapp.com/` page;
2. When the page load, take your phone, select the `WhatsApp Web` option in the "More" menu;
3. You'll start the WhatsApp Web app, When your contacts list appear, switch to the console;
4. You'll see the message "Insert target's name: ". That's when you type the contact name you want to target, because, it makes sense, right?;
5. After that, you enter the number of messages you want to spam, please insert an integer, otherwise, it will probably crash...;
6. Switch over to the browser and watch the chaos begin. xD
