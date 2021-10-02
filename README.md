# Grand Auto _"where every car is a steal"_

Python command-line application to manage car sales for a dealership knowing whom has entered in the data and the sales they have made for each day.
When 'python3 run.py' is entered into the terminal a prompt will appear to ask your name, when this is entered, a personalised message appears to 
ask you for car sales, it explains the way the data should be entered, how and where. Once you have correctly entered the data a message will
appear to say you have a valid entry, this will repeat until there is a valid entry. The sales worksheet will be updated accordingly
As you can see from the flow chart below the comand line application will ask user to enter the car sales for each day, for:
-  Sedan
-  Coupe
-  Sports car
-  station wagon
-  Hatch back
-  Sports suv

The comand-line application will update this information to the sales google sheet, update that google sheet below last data entry, tell you when this is
updated sucessfully. Then it moves onto calculating what cars are left from each day of sales by subtracting sales from stock worksheet and updates the unsold cars worksheet below the last data enrty and informs the user that this has been completed. Ater completing those tasks it advise of stock to replenish.

The live link can be found here - https://github.com/nedduc/Car-Sales

![Flow Chart](assets/images/flow_chart.png)

### Bugs to Fix

![Bugs to fix](assets/images/bug1.png) (assets/images/rbug2.png) (assets/images/bug3.png) (assets/images/readme/mobile.png)

- __The landing page__

  - Simple, unclutterd landing page colours inspired by pantone 2021 colours
  - Good layout of page items.

- __The input window__ 

  - When the page opens the cursor has been placed into the window input area so the user can immediately start typing a memo. 
  - The input window has place holder text reading 'Type task and hit enter' inserted to give user advice on what to do. The text colour has been lightened so the user knows it's a place to fill in text. 
  - If you do not enter text in this window and hit the enter key nothing will happen, you cannot have a empty line of text.

- __Font Awesome__

  - Icons used to indicate where to write, complete and delete.
  - https://fontawesome.com/

### Features Left to Implement

- Other features to implement to create three icon links to seperate Memo-It list into work, rest and play.
- Drag and drop feature for moving tasks between different lists.
- Set up local storage for items to remain on list until deleted.
- Sound effect on completed item.

## Testing 

Checks carried out on spelling, grammar and Punctuation. Most of the spelling and grammar will be inserted by user. I made sure that the input field worked and the item inserted would appear on the list. Title tags and meta data have good description for SEO.

Responsive on all screen sizes from desktop to mobile, media query added for mobile to give more real estate to keyboard for data entry. I have also included vertical scroll bar.

I discovered that on the toggle within javascript it did not like dealing with the font awesome icons that have a space. All variables used, have to be defined. Unexpected tokens are not allowed.

Bugs screen shots located in readme folder, they have been resolved. 


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
- JSHint
  - No errors were found when passing through the official [(JSHint) validator](https://jshint.com/)
- Lighthouse
  - Overall report was 100%  /workspace/Memo-It/testing/Lighthouse-Report.png
- DevTools
  - Responsiveness on all devices.


![Lighthouse](testing/Lighthouse-Report.png) 

### Unfixed Bugs
I was able to remove all bugs as they were easy enough to fix, once I did a bit of research to find out what each bug meant, most of my research was done on https://stackoverflow.com/ and https://www.w3schools.com/

![bugs found](assets/images/readme/bug3.png) 

## Deployment

In order for someone to access, I must deploy site to Github from Gitpod the container-based development platform I have been using: 
  - Make sure that I have "git added", "git commit -m" & "git push" to Github
  - Once in Github, I navigated to my sites repository - https://github.com/nedduc
  - Under my repository name, to the right of the screen click  Settings.
  - Under my repository name, to the right of the screen click Settings.
  - In the left sidebar, click Pages.
  - Under “GitHub Pages”, use the None or Branch drop-down menu and select a publishing source.
  - Optionally, use the drop-down menu to select a folder for my publishing source. 

The live link can be found here - https://nedduc.github.io/Memo-It/

## Credits 
(https://www.w3schools.com/)(https://www.youtube.com/channel/UC8n8ftV94ZU_DJLOLtrpORA)
(https://fontawesome.com/)(Patient and kind tutors from Code Institute)

### Content 

- The icons on the page were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The header image Photo by Sigmund on Unsplash https://unsplash.com/

## Reminders

* Code has been placed into the run.py
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.