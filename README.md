# FromVin
Find Wines and Cheeses to your taste.


## Site Owner Goal
The site owner is looking to provide a platform for food lovers to purchase wine and cheese. 

If users know what they are looking to purchase, they can do so. For those who do not, they can head to 'recommend', select the type of wine or cheese that they know they like and receive recommendations on what to buy as a pairing.


## User Stories
A user will want to be able to do the following:
- Browse wine and cheese products
- Add wanted products to a basket
- Order and pay for said products to a stated delivery address
- Create a user account
- Access previous orders through said user account
- Find out information regarding cheese, wine
- Find out information regarding cheese and wine pairings


## Site Layout

### Guide

The layout isn't exactly as I was originally picturing when making the wireframes for this site. Unfortunately time constraints have shifted the scope a little. The guide was originally due to have additional content, with some storyboard style images of wine tasting. As it stands, it has a minor introduction into what you can find at FromVin, followed by a brief overview of the main points of tasting. I also located a wonderful royalty-free flavours image which deserved pride of place on the site. It does still serve the main purpose of being a guide, both to FromVin, and to Wine as something to be appreciated and explored. 

Users are guided to additional information should they want it on the blog section of the site. 


### Recommendation

Going forward there are some excellent things that can be done with the recommendation idea in my opinion. Currently the functionality stands at a straightforward process which allows the user to take broad tastes that they know they like, and translate that into a FromVin product that has been matched to it. Future expansion to this would allow different flavours to be picked and combined with the closest match product-wise being returned. This would require complex attribute mapping and a significantly greater number of products, but would be an interesting challenge. The current idea is much simpler but is an excellent start point in my opinion, and adds value to being more than just an online store.

### Store

I've covered this later in the Readme, but due to this being my only experience with something so large as an e-commerce site, i've leaned quite heavily on the boutique ado project for the store functionality. Hopefully this doesn't detract too much from the fact that the elements are wonderfully fit for purpose. User information storage, stripe implementation and excellent user feedback all comes together to ensure that any user wishing to purchase an item from this store, has as few barriers as possible to do so. 

The items are presented and filtered logically for the user, and they can amend this themselves also. Adding products is simple and feedback is given all along the way. 

### Account/Profile

Credit has to be given here to the well-roundedness of the Django application. From initial installation alone, the breadth of user-centric control via the built in admin makes dealing with an often complex back-end to a project, relatively simple. 


## Design Decisions

### General Design
As a preface to the aspects that are more bespoke on the site, it needs to be stated that i've leaned quite heavily on the boutique ado project. As the only full ecommerce solution on the course and an ideal example of how to put together a django ecommerce site, it seemed like a natural source of a basis. This was discussed with my stand-in mentor to confirm this would be the case, and was told that it was expected, but should be stated outright here.

Otherwise, a fixed top navbar was selected so that a user can utilise the navigation even when midway down hundreds of products. On said navbar, the site has been split into it's shop, a homepage which acts as an informational guide, a recommendation page and a blog for more bespoke information from the site owners.

The colour style of the site was chosen to reflect the products that it showcases, along with hopefully coming across as professional but not ostentatious. 

As mentioned above, the hope is that the recommendation aspect of the site can expand over time. I feel this is what gives a little extra to the site as it gives direction to customers who may not know quite as much about the products as others. 

The blog can be a powerful way to communicate with the users. Being able to present new information in a consistent manner was the reason for it's inclusion, and whilst most of the current information is just a sample - the potential of it speaks to it's inclusion. 


### Data Specific Design


#### Database Schema

The following was made with Creately. The postgres database viewer on Heroku is unfortunately quite limited, so some estimates have been made as to the relationships between some of these tables. In addition, the social tables have been created, but wouldn't be utilised until additional work is made on the project.

![database schema](https://user-images.githubusercontent.com/61311614/123555148-d1753200-d77b-11eb-840a-9ef8ffd979f2.png)


### Wireframes


#### Desktop

Home/Guide Page
![desktop1](https://user-images.githubusercontent.com/61311614/123558441-29b52f80-d78e-11eb-8584-6b64d708e8f6.png)
![desktop2](https://user-images.githubusercontent.com/61311614/123558442-2a4dc600-d78e-11eb-845e-315235a994cb.png)
![desktop3](https://user-images.githubusercontent.com/61311614/123558443-2c178980-d78e-11eb-8769-5d19ade8b323.png)
![desktop4](https://user-images.githubusercontent.com/61311614/123558447-2d48b680-d78e-11eb-8664-b032c44f8eaa.png)

Recommendation Page

![desktop5](https://user-images.githubusercontent.com/61311614/123558449-2e79e380-d78e-11eb-8316-25c880a52846.png)
![desktop6](https://user-images.githubusercontent.com/61311614/123558450-2fab1080-d78e-11eb-8ea1-d91af7063a0e.png)
![desktop7](https://user-images.githubusercontent.com/61311614/123558451-3174d400-d78e-11eb-8b95-6ad359c0781e.png)
![desktop8](https://user-images.githubusercontent.com/61311614/123558452-333e9780-d78e-11eb-956e-08df59a339d0.png)
![desktop9](https://user-images.githubusercontent.com/61311614/123558454-35a0f180-d78e-11eb-84d8-0f0e7f3077c3.png)

Store Page

![desktop10](https://user-images.githubusercontent.com/61311614/123558455-39cd0f00-d78e-11eb-8353-ddc01106858f.png)
![desktop11](https://user-images.githubusercontent.com/61311614/123558456-3b96d280-d78e-11eb-825c-687b3f77ab3a.png)

Checkout Page

![desktop12](https://user-images.githubusercontent.com/61311614/123558457-3d609600-d78e-11eb-89dc-c665d5647f97.png)
![desktop13](https://user-images.githubusercontent.com/61311614/123558460-3f2a5980-d78e-11eb-954b-b4515da2c9dd.png)




#### Mobile

Guide/Home Page

![mobile1](https://user-images.githubusercontent.com/61311614/123558527-a516e100-d78e-11eb-844b-1263f3f4217a.png)
![mobile2](https://user-images.githubusercontent.com/61311614/123558531-ac3def00-d78e-11eb-9f29-3187dea69aca.png)
![mobile3](https://user-images.githubusercontent.com/61311614/123558532-acd68580-d78e-11eb-9e96-228c8621c71f.png)
![mobile4](https://user-images.githubusercontent.com/61311614/123558534-ae07b280-d78e-11eb-8076-7e624311e7b5.png)

Recommendation Page

![mobile5](https://user-images.githubusercontent.com/61311614/123558537-aea04900-d78e-11eb-8525-1d8b6eeae1c7.png)
![mobile6](https://user-images.githubusercontent.com/61311614/123558538-afd17600-d78e-11eb-9d0f-77ee505034ea.png)

Store Page

![mobile7](https://user-images.githubusercontent.com/61311614/123558540-b364fd00-d78e-11eb-984b-5efe92d5e04f.png)
![mobile8](https://user-images.githubusercontent.com/61311614/123558543-b4962a00-d78e-11eb-9c1a-25fa8435b291.png)

Checkout Page

![mobile9](https://user-images.githubusercontent.com/61311614/123558544-b5c75700-d78e-11eb-8bff-1b5e68721f49.png)
![mobile10](https://user-images.githubusercontent.com/61311614/123558546-b6f88400-d78e-11eb-8cec-323fee875906.png)
![mobile11](https://user-images.githubusercontent.com/61311614/123558547-b8c24780-d78e-11eb-9b98-d3ff378f1841.png)




### Technologies used

- Gitpod - this was the chosen development platform.
- Bootstrap for site layout, container code, navbar functions - used throughout for rich content and responsive behaviour.
- JQuery addon used for rich function searching in order to appropriately target html and CSS for site functionality.
- GitHub - utilised for cloud backups and project progression.
- Realfavicongenerator.net - used to correctly generate site favicons.
- Mockplus Classic - Used for wireframes of the project - possibly the best free option so far in my opinion.
- Heroku - for deploying and hosting the application.  
- Creately - used to document the database schema.
- Cloudinary - utilised to serve media files on the deployed site.
- Whitenoise - used to serve static files on the deployed site. 


## Testing

### Validation service

#### HTML

The [HTML Validator](https://validator.w3.org/) picked up several issues, such as:

- the 'rel' link for the android favicon did not have the term 'icon' in it. This was addressed.
- the 'li' items in the navigation threw an error as being ouside of an 'ul' element. this turned out to be a missing <ul> tag in mobile_top_header and was resolved.
- there is a 'type' warning for a javascript resource, this was in the quantity adjustment script and was removed. This actually appeared in several applications such as checkout and products. 

I then got to a stage where sign in was needed, so proceeded to copy and paste HTML across into the validator for page such as checkout/checkout_success.html. The validator objected to the python template text primarily, but was otherwise fine.

![image](https://user-images.githubusercontent.com/61311614/123807424-bd4e4380-d8e7-11eb-984a-a09c0d379d8a.png)

Eventually, all errors save for the python templates were resolved.
![image](https://user-images.githubusercontent.com/61311614/123807991-41a0c680-d8e8-11eb-888a-969b32090f77.png)


#### CSS

The [CSS Validator](https://jigsaw.w3.org/css-validator/) picked up primarily issues with the bootstrap css, which is expected behaviour by now. 

There was one further one, that a webkit control is an unknown vendor extension:

![image](https://user-images.githubusercontent.com/61311614/123809153-474adc00-d8e9-11eb-9848-c37e6fe7217e.png)

On a quick search of the [forums](https://www.sitepoint.com/community/t/css-validation-unknown-vendor-extensions/125616), this is another error akin to the bootstrap ones, where the validator doesn't recognise it, but it is not necessarily incorrect. As such, the code was left intact. 


#### JavaScript

The [Javascript Validator](https://jshint.com/) primarily located several missing semi-colons - these were all added.

In adddition, the following was noted:

- Template literal syntax is only supported on some versions - this should be fine for our purposes.
![image](https://user-images.githubusercontent.com/61311614/123812105-b9242500-d8eb-11eb-8537-4dac1a7666d3.png)
- 'let' is again only supported on some versions, but should be fine for our purposes.

Otherwise there were no further errors - only warnings regarding utilisation of the '$' tag of JQuery, which again is fine. 

#### Python

As a preface, I did not check the built-in migration files and the like, as there isn't much I can really do about any errors within them.

Regarding the aspects that can be controlled, I have to say that the gitpod built-in linter was excellent. I recall on the previous project having hundreds of errors, primarily regarding line length. The linter within gitpod allowed these to be addressed within the IDE and validated on the spot. As such, the [Python Validator](http://pep8online.com/) found...

- Trailing whitespace in checkout/models.py

![image](https://user-images.githubusercontent.com/61311614/123814396-90049400-d8ed-11eb-8b59-079c364b719c.png)

- Line too long in settings.py - I've decided to leave this particular one, as splitting it up will actually reduce readability, (as it's just long dot notation so should ideally be inline) instead of increasing it in my opinion. The PEP8 syntax rules being all about ease of reading makes me think that this is the correct decision.
- The blank line at the end of the file was removed.

![image](https://user-images.githubusercontent.com/61311614/123817459-1621da00-d8f0-11eb-91d6-1ebc42f1f440.png)

The remainder of the Python code received the 'All Right' status:

![image](https://user-images.githubusercontent.com/61311614/123820461-86315f80-d8f2-11eb-9e6a-cb08c03ccf5d.png)

#### Wave(WebAIM) validator

In previous projects, I have found value in a UX validator called [WebAim Wave](https://wave.webaim.org/). This site assesses accessibility for users who may require screen readers, or struggle with contrast against elements. 

Prior to running the site through, one thing I will raise from a UX side as a self criticism - I really like the button design and colouring throughout the site. I do however readily admit that proceed and cancel buttons next to each other of the same colour is not ideal, and would find something that looks equally good, but is more distinct in future.

On running the validator, most aspects are positive however a couple of negatives are apparent:

- There are missing aria elements on the search box. Aria-label additions resolve this well. 
- The contrast between the black header links and the deep red navbar is 'Very Low'

![image](https://user-images.githubusercontent.com/61311614/123821796-9d248180-d8f3-11eb-85a8-f007713788dc.png)

In regards to the latter issue, there are two ways to deal with it, choose a lighter colour for the navbar, or for the links. 

For the navbar, increasing the lightness so that the contrast validator passes gives the following:

![image](https://user-images.githubusercontent.com/61311614/123817196-dbb83d00-d8ef-11eb-8f69-722121a66399.png)

Personally, I am not a fan of this and feel that it detracts from the overall look of the site. 

The other option is as follows:

![image](https://user-images.githubusercontent.com/61311614/123828001-03f86980-d8f9-11eb-8956-c23cbe177447.png)

Whilst I still prefer the black icons, the white is much preferable to the lighter navbar in my opinion.

On making the change, the validator suggests that the change is much better:

![image](https://user-images.githubusercontent.com/61311614/123829399-56865580-d8fa-11eb-98f3-db920617d0ef.png)

This is somewhat limited as you'd struggle to get to pages that require a login, but the exercise is useful, in my opinion.

#### Internal custom validation

Unfortunately I have not been able to write a suite of automated test cases for the project. These wouldn't be a substitute for manual testing on a project such as this and time has limited me to manual only, on this occasion.

One of the main redundancies that was taught in in the Code Institute course in reference to an e-commerce site, is a backup for payments should the form not submit. I've carried these redundancies over into this project and have tested here by removing the form.submit() call in stripe_elements.js. The webhook successfully substitutes in and allows the payment to complete.


In addition, a combination of django built in validation, stripe authentication and redundancies in the views means that most of the vulnerabilities you would see in a site like this are handled. For example:

![image](https://user-images.githubusercontent.com/61311614/123861010-90695300-d91e-11eb-9743-04d93d5fd550.png)

![image](https://user-images.githubusercontent.com/61311614/123861167-c27ab500-d91e-11eb-8baf-dd17d811d57d.png)

![image](https://user-images.githubusercontent.com/61311614/123861229-d9210c00-d91e-11eb-8a42-8497c0f00430.png)

![image](https://user-images.githubusercontent.com/61311614/123861324-f1912680-d91e-11eb-8b42-c2ffadc291d6.png)

![image](https://user-images.githubusercontent.com/61311614/123861528-31f0a480-d91f-11eb-988b-582fdbf7a7c2.png)

![image](https://user-images.githubusercontent.com/61311614/123861565-3c12a300-d91f-11eb-9a8a-c1ec2e51703c.png)





### Page links

#### FromVin logo 

Should navigate back to home (guide) page - confirmed.

#### Navigation Bar 

Content dropdown - should expand to show 'Guide', 'Recommend' and 'Blog' links - confirmed.

Guide - should lead to the homepage - confirmed.

Recommend - should lead to recommendation page - confirmed.

Blog - should lead to Blog page - confirmed.

Shop - should lead to the products page - confirmed.

My Account (Logged Out) - Should be presented with a dropdown showing 'Register' and 'Login' - confirmed.

Register - should lead to the signup page - confirmed. 

Login - should lead to the signin page - confirmed.

My Account (Logged In) - should be presented with a dropdown showing 'My Profile' and 'Logout' - confirmed.

My Profile - should lead to the profile page - confirmed.

Logout - should lead to the logout page - confirmed.

My Account (Logged In Superuser) - should have the additional dropdown option of 'Product Management' - confirmed.

Product Management - should lead to add product page - confirmed. 

Bag - should lead to the user's bag, and update when items added - confirmed.

Search box - should take a query from a user, and apply it as a product filter - confirmed.


#### Secondary 'Products' Navigation

All Products - should dropdown to show 'By Price', 'By Category', 'All Products' filters - confirmed.

By Price - should lead to products with a 'price high to low' filter - confirmed.

By Category - should lead to products with a 'category A-Z' filter - confirmed.

All Products - should lead to the products page - confirmed.

Wines - should dropdown to show 'Red Wines', 'White Wines', 'Dessert Wines', 'All Wines' filters - confirmed.

Red Wines/White Wines/Dessert Wines/All Wines - should lead to products with the respective filter applied - confirmed.

Cheeses - should dropdown to show 'Hard Cheeses', 'Soft Cheeses', 'All Cheeses' filters - confirmed.

Hard Cheeses/Soft Cheeses/ All cheeses - should lead to products with the respective filter applied - confirmed.

Accompaniments - should dropdown to show 'All Accompaniments' - confirmed.

All Accompaniments - should lead to products with an 'extras' filter applied - confirmed. 

#### Guide Page

Recommend Button - should lead to recommendation page - confirmed.

Shop - should lead to products page - confirmed.

Blog - should lead to the blog page - confirmed.

#### Recommend Page

Find me Cheese button - should take the value of the above dropdown and return appropriate products (based on tasting profile) below - confirmed.

Find me Wine button - should take the value of the above dropdown and return appropriate products (based on tasting profile) below - confirmed.

Product cards - Once present, clicking on the image should lead to the appropriate product details page - confirmed.


#### Blog Page

Read more - should lead to the appropriate post details page - confirmed.

#### Blog Details Page

Back To Blog - should return to the blog page - confirmed. 


#### Products Page

Product cards - clicking on the product image should lead to the appropriate product details page - confirmed. 

Product cards (as superuser) - should have an edit and delete option to amend the appropriate product - confirmed.

Edit - should lead to the edit page for the appropriate product - confirmed.

Delete - should remove the appropriate product from the database - confirmed.

Top of page button - should return to the top of the page - confirmed.

Sort box - should add filter to products based on selection - confirmed.


##### Product Details Page

(As Superuser) Edit and Delete buttons - should behave the same as on the products page - confirmed.

Quantity selector - should allow amendments to the amount of products - confirmed.

Keep Shopping - should go back to the products page - confirmed.

Add to Bag - should add selected quantity of product to the bag - confirmed.


#### Bag Page

Quantity selector - should behave the same as on the product details page - confirmed.

Keep Shopping - should go back to the products page - confirmed

Secure Checkout - should go to the checkout page - confirmed.


#### Checkout Page

(Logged Out) Sign In/ Register links should go to their respective namesake pages - confirmed.

(Logged In) Save Information checkbox - when checked should add form information to user profile - confirmed.

Adjust Bag - should go back to bag page - confirmed.

Complete Order - should submit form data to stripe payments, and send user an email if successful - confirmed.


#### Checkout Success Page

Back to Shop - should lead to products page - confirmed.


#### Profile Page (Logged in)

Update Information - should take the above form data and log any changes against the user's account - confirmed.

Order number links - should lead to the respective checkout success page - confirmed.


#### Product Management Page (Logged In - Superuser)

Choose File - should open an uploader window for a product image - confirmed

Cancel - should lead to the products page - confirmed.

Add Product - should take the form data and input a product into the database - confirmed.

#### Sign In Page

Sign up link - should lead to the sign up page - confirmed.

Forgot password - should lead to the password reset page - confirmed.

Sign In - should log the user in if the credentials are correct - confirmed.

Remember Me checkbox - should store the username and password of the user if they choose - confirmed.


#### Sign Out Page

Sign Out - Should remove the session for the user and lead to the homepage - confirmed.

#### Sign Up Page

Sign In link - should lead to the sign in page - confirmed.

Sign Up - should take the form data and insert a new user into the database, then trigger a verification email - confirmed.

Verification email link - should verify the user and lead back to the site - confirmed.


#### Password Reset Page

Reset My Password - should send a reset link to the chosen email if they are registered - confirmed.

Reset email link - should lead to the set password page if the key is valid, if not then should divert to a 'Bad key' page - confirmed by using an expired link.


#### Set Password Page

Change Password - should take the password form data and set a new password for the user - Getting 500 server error:

![image](https://user-images.githubusercontent.com/61311614/123853070-edf8a200-d914-11eb-9c68-4c1b240362a7.png)


After some research, it transpired that in amending settings.py to fit the PEP8 line length standards, the auth password validators were moved down a line to fit. This unfortunately breaks this functionality, so the changes have been reverted. Now the status is successful:

![image](https://user-images.githubusercontent.com/61311614/123852391-28157400-d914-11eb-94dc-6614ce99c2b4.png)

### Browsers

The below browsers have had the website opened, navigated through and confirmed to be functional, alongside going through the above testing points:

- Firefox

It was noted that there is a console error on Firefox in relation to the content security policy. [stackoverflow](https://stackoverflow.com/questions/37298608/content-security-policy-the-pages-settings-blocked-the-loading-of-a-resource/37308542) suggests that a fix can be made in the meta in the page header, however the security is there for a reason and should probably be preserved. As an investigation however, I added 'unsafe-inline' as a Content Security Policy in the meta and the errors did stop. A better solution found on [csper.oi](https://csper.io/blog/no-more-unsafe-inline) suggests that just moving the javascript to .js files would be a better solution. 

Due to time pressures, I have removed the unsafe-inline tag (for security), will add the javascript move to known issues and have confirmed that the stripe payments, which seem to be at least one of the causes, still function on FireFox - confirmed. 

- Chrome
- Microsoft Edge


### Responsiveness

With the inclusion of the mobile navbar from boutique ado, in conjunction with heavy use of built-in bootstrap spacing classes, the content remains mostly centred in the page and stacks well regardless of device. 

The only major difficulty is setting the spacing needed for the page content when the navbar enlarges on smaller devices. This has been handled with media queries.

This has been tested using the following settings on Chrome Developer Tools: Iphone 5, Iphone 6, Pixel 2 XL, iPad, Surface Duo.

### Testing that Heroku version matches development version.

The Heroku version links very well with GitHub publishes, deploying a new version on each commit which is wonderful functionality. The main difference between the two has been the serving of media files. I'm certain that there is a logical way around the issue, but in order to ensure that images served via cloudinary, uploaded via admin and images that are uploaded straight into cloudinary function, I have had to add a bespoke settings variable and context processor to handle it. 

As such, the production environment is working as required, but it has had a detrimental effect on the images in the local environment. I believe this is primarily down to how Cloudinary adds additional characters to the end of the uploaded images. Should I go through and make everything match, there is a possibility that development images would function once more.

Otherwise, the environments line up well, with the same functionality on both. There was some difficulty in exporting the sqlite database into postgres, but with some effort they eventually lined up. 


## Known issues
- I had a little trouble with wrapping my head around static files and django. I made a little workaround for images that were not uploaded via admin, such as the flavour wheel. This does not represent best practice amongst the way it was handled
- As such, the favicon will only show on pages where the image link has been passed into the context. This does not feel like best practice and perhaps a custom context processor for this would have been much better to make it available sitewide. Update: Information found in the Django documentation suggested that Django supports the MEDIA_URL setting sitewide, so images were updated to utilise this however it caused complications with the product images. A custom context processor was then added to address this. 
- On loading images to Cloudinary, they did not keep their original names, which means they are not found locally. Renaming the local versions, or the Cloudinary hosted versions would fix this. 
- Despite having the site set on admin as 'FromVin', the password emails still appear to use 'example.com'
- the db.json export should not really have been added to the git repository. On checking, all the passwords were hashed but even so, database copies with personal details should not be available. 
- Gitpod states that several objects within views do not have an 'objects' attribute, this appears to be incorrect as the code functions correctly. 
- This is also true for 'lineitems' within checkout/models.py
- On removing size from checkout/models.py - the port refuses to open. This may be migration related.
- Line length error in settings.py (password validation settings) has been left, as readability has been prioritised.
- Decouple removed from settings but not from requirements.txt.
- There is a content security policy error on firefox due to the use of inline javascript. The JS has been left due to time pressures, but the reasoning and research has all been explained under the 'Browsers' part of this Readme.  


## Future improvements
- A validation message should be present on the Delete option for products. Even better would be an 'Undo' option, as this will allow for repairing of mistakes and less impactful mass-deletions, should they be necessary through the GUI. 
- Make tasting profile less of a magic number
- Thoroughly research the pairings, they currently are arbitary and could be more tailored. 
- Make amendments to secondary action buttons. From a UX perspective, whilst they may look good, my concern is that a user may click the wrong one by accident. 

## Deployment Procedure

### Local Deployment

Starting a project such as this using the chosen IDE, in this case Gitpod.io is quite simple.

- Create a new workspace in Gitpod
- Install django using 'pip3 install Django'
- Start a new project using `django-admin startproject {enter site name here}`
- From this point, apps can begin to be created as needed using `python3 manage.py startapp {enter app name here}`
- A database is created by default, but any changes to models will require migrations. These can be prepared with `python3 manage.py makemigrations`, followed by `python3 manage.py migrate` once you have confirmed these to be correct. The `--plan` and `--dry-run` tags are advised to be used in confirming this (see Django [documentation](https://docs.djangoproject.com/en/3.2/ref/django-admin/) for more details).
- Create a .gitignore file so that sensitive data (database, settings) is not stored publically on git.
- Create a requirements.txt file, which lists the dependencies of the project. The command for this is `pip3 freeze > requirements.txt`
- Create a Procfile (spelt exactly like this), which sets where the application should commence. For Django, it's usual to install a program by the name of 'Gunicorn' to assist with this. This is primarily used for live deployment, but is a good habit to get into. The command is `pip3 install gunicorn` and the Procfile content should be `web: gunicorn {insert project name}.wsgi`.

From here, running the app via your IDE will start up a version of the application that can be viewed, and built upon. The command for this in Gitpod is `python3 manage.py runserver`.

In this particular project, the local site cannot be found at a consistent web address as it is based on the workspace instance, which for gitpod is a sequence of random words.


### Cloning this exact project

- Navigate to the following GitHub Repo - https://github.com/WrightDanG/FromVin
- Click the dropdown that states 'Code':
![image](https://user-images.githubusercontent.com/61311614/109667885-839f4300-7b68-11eb-9b2e-a61242788e79.png)
- You should have several options to open/download the code. Personally I had 'Open with Visual Studio', 'Open with GitHub Desktop', 'Download ZIP'
- The first two options will launch the respective clients (if installed) where you can trigger a clone operation.
- The last option allows you to copy+paste/drag+drop physical copies of the code into your respective IDE. You will need to extract the data first most likely. This requires more manual work but is an equally valid way to clone the project for local use. 

You may note that on the above image, there is a 'GitPod' option. This is due to the GitPod extension installed on my browser. If the user were to also do this (tested working on Chrome and Firefox), log into their respective gitpod account and click this button, they would be able to launch an instance of this project also.

### Deployment via Heroku

Getting Heroku to deploy a version of this project is incredibly simple. The below steps can be followed:

- Ensure that the project is linked to a GitHub repository.
- Confirm that the Procfile has been successfully created per the 'local' instructions above. Heroku will require this for a live deployment.
- Create a Heroku Login.
- Create a Heroku application - it must have a unique name.
- Install heroku into your project via command line (pip3 install django-heroku)
- Under 'Deploy', click 'Connect to GitHub' and link it to the repository.
- Under 'Settings', 'Reveal Config Vars' and add your IP, Port, Secret Key and stripe details.
- Back under 'Deploy', 'Enable Automatic Deploys' can be now be selected so the project will deploy every time there is a new GitHub commit.
- Ensure that the new url is added to the 'ALLOWED_HOSTS' in settings.py
- From here it's as simple as clicking 'Open App' for a instance of the application to run.

For this particular project, the site can be found at: https://fromvin.herokuapp.com/

The local sqlite database will not be sufficient for deployment purposes, so a Heroku Postgres database can be added via Heroku addons. Heroku will handle the environment details for this, but the data will need to be exported from sqlite, and imported into Postgres. 

The following procedure is taken from Code Institute on how to do this:

- Make sure your manage.py file is connected to your mysql database
- Use this command to backup your current database and load it into a db.json file:
    ./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
- Connect your manage.py file to your postgres database
- Then use this command to load your data from the db.json file into postgres:
    ./manage.py loaddata db.json


This then gets a little more complicated due to how Django deals with static files. Whilst they are served correctly by Gitpod locally, when it comes to a live deployment, additional infrastructure is required. 

Code Institute recommends using Amazon AWS to serve static files, and whilst these are a known entity with a robust infrastructure, personally I decided not to go with them.

This was for two reasons. One was that I had followed the boutique ado project closely up until that point and wished to try something new for experience. The other was that I had read that AWS had been charging people without warning for going over a media cap and wished to avoid this possibility. 

I chose [Cloudinary](https://cloudinary.com/) as a provider for media files, primarily due to their integration with Heroku and reasonably well-reviewed status. [Whitenoise](http://whitenoise.evans.io/en/stable/) was the chosen application by many to go hand in hand with this to serve the remaining static files (CSS/ Javascript).

The following steps were taken:

- Navigate to 'Add-ons' once within your heroku project, on the heroku portal
- Search for 'Cloudinary'
- Click install, and enter heroku payment details if required. Choose the free version however, the payment details should not be needed to be used. 
- Install both cloudinary and whitenoise into the project via console command (pip3 install cloudinary django-cloudinary-storage whitenoise)
- Ensure the requirements are added to requirements.txt (pip3 freeze > requirements.txt)
- Ensure they are added to installed apps in settings.py
- Add the following to middleware to support Whitenoise 'whitenoise.middleware.WhiteNoiseMiddleware'
- The cloudinary portal will have a url with the needed keys. This url can be added to heroku settings and accessed via settings.py. 
Personally, I have been using dj_database for database settings and have used the following to get the postgres database to link up: 'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))

Static files locations can be set in settings.py - the code from this project is as follows:

# Heroku static collection settings
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files served in live via Cloudinary

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.getenv('CLOUDINARY_URL', '')
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
IMAGE_URL = # Custom cloudinary url

Generally speaking that additional IMAGE_URL setting should not be necessary, but I personally had a little trouble with serving some specific media files, so used this as a solution. The other settings allow cloudinary to serve media files and whitenoise to serve the other static files and barring any issues, the live site should now match the local site.



## User story walkthroughs

When a user finds their way to FromVin, they are greeted with the guide page. Here they are immediately presented with what the site is for, and where they can go to access it's features, along with reasonings why they would want to.

![Screenshot_1](https://user-images.githubusercontent.com/61311614/123704377-7f0c4200-d85d-11eb-80c6-834a5104374d.png)

On scrolling down, FromVin gives a little description in what a user should look for when it comes to wine tasting. As this is a part of the FromVin experience, it was thought that everyone should have a place to jump on to the experience with. Future improvements would expand the information on offer, either here in the guide, in the blog, or ideally both.

![Screenshot_2](https://user-images.githubusercontent.com/61311614/123704379-7fa4d880-d85d-11eb-81c4-da0809d071ae.png)

Whilst the site is meant to look clean and professional, I couldn't resist adding the eye-catching coloured wheel of wine flavours. I found it to be both informative and interesting. The hope is that the user would also, as it would give them flavour ideas to look for, for the new. Also perhaps novel ones for the experienced. 

![Screenshot_3](https://user-images.githubusercontent.com/61311614/123704380-7fa4d880-d85d-11eb-95d3-313e3b7f7e87.png)

I've addressed elsewhere in this readme that the guide was intended to be bigger, but this small summary section is meant to promote a sense of cameraderie between FromVin, and the user. In future it would cap off the end of a more thorough tasting guide.

![Screenshot_4](https://user-images.githubusercontent.com/61311614/123704382-80d60580-d85d-11eb-8d3e-2663ad21b853.png)

Back up the page, the user has then several options of where to go. The 'How it works' section suggests heading to one of three places. We'll take the blog first, which is an extension to the guide. It can be accessed via the button link on the page, or under 'content' in the navigation. 

![Screenshot_5](https://user-images.githubusercontent.com/61311614/123704389-829fc900-d85d-11eb-8806-ba47f97d0c66.png)

Within the blog page, the user is presented with a list of the most recent blog entries. The titles are prominent to give them an idea of what they are looking at, and they are able to click into each one to expand the information.

![Screenshot_6](https://user-images.githubusercontent.com/61311614/123704391-83385f80-d85d-11eb-9c91-d96324b1eb52.png)

The content at present is mostly representational, but going forward the user would be able to look at additional tasting guides, spotlights on new products and announcements from the FromVin team. Current content credit goes to WineFolly (see attribution below).

![Screenshot_7](https://user-images.githubusercontent.com/61311614/123704392-83385f80-d85d-11eb-8980-89378995c45b.png)

The user can then head over to the recommendation page. The idea here is that a user may know what kind of wine or cheese that they like, or have, and are able to find a cheese or wine respectively that will go well with it. This is detailed to them in another 'How it works' section, for clarity.

![Screenshot_8](https://user-images.githubusercontent.com/61311614/123704393-83385f80-d85d-11eb-98c7-3b59484271b6.png)

The user is presented with simple, broad options for what they know that they already like. 

![Screenshot_9](https://user-images.githubusercontent.com/61311614/123704394-83d0f600-d85d-11eb-9c3c-8aaec768240e.png)

They are then presented with three options that FromVin determines that would go well with what they have selected. The site utilises a 'tasting profile' category assigned to each product. As it stands, this is just a categorisation number, but scaled up it could expand to multiple options matching against a relational database of mapped flavours. 

![Screenshot_10](https://user-images.githubusercontent.com/61311614/123704396-83d0f600-d85d-11eb-9b57-6a9fbc44fa39.png)

The user is able to click into each product, and are directed to the product details page where they are able to select a quantity and add them to a basket. 

![Screenshot_11](https://user-images.githubusercontent.com/61311614/123704399-84698c80-d85d-11eb-8c6b-236736367615.png)

The user is presented with feedback that their addition was successful.

![Screenshot_12](https://user-images.githubusercontent.com/61311614/123704400-85022300-d85d-11eb-84c0-75e44c9adc30.png)

Now that shopping has commenced, the user is able to 'Keep Shopping' via the labelled button here, or in the navigation. The shop link was kept out of a dropdown to be readily accessible at all times. 

![Screenshot_13](https://user-images.githubusercontent.com/61311614/123704403-85022300-d85d-11eb-938c-4e175959ab41.png)

The user is able to utilise the sort function to manipulate the order of the products presented to them.

![Screenshot_14](https://user-images.githubusercontent.com/61311614/123704406-859ab980-d85d-11eb-884e-e4b7ed40ac2a.png)
![Screenshot_15](https://user-images.githubusercontent.com/61311614/123704411-86335000-d85d-11eb-8ce3-913f3ad21446.png)

The suberb dropdown category list has also been carried over from the boutique ado project. This allows the user to filter the products down by category for a tailored shopping experience. 

![Screenshot_16](https://user-images.githubusercontent.com/61311614/123704413-86cbe680-d85d-11eb-9899-abe3c7cc2fd5.png)
![Screenshot_17](https://user-images.githubusercontent.com/61311614/123704415-87647d00-d85d-11eb-958d-eb86f79d60e0.png)

On clicking the basket (bag) button at the top right of the page, the user can navigate to the items that they have in their basket, ready for checkout once they are ready using the 'Secure Checkout' button. 

![Screenshot_18](https://user-images.githubusercontent.com/61311614/123704420-8895aa00-d85d-11eb-833c-c3fe6a1d7bfa.png)

The user is presented with delivery details to enter, a summary of the order and a space for payment details via the stripe text boxes. Whilst the user is able to checkout as a guest, they benefit from taking the option here of making an account as their information will be saved.

![Screenshot_19](https://user-images.githubusercontent.com/61311614/123704421-892e4080-d85d-11eb-9d98-f577c5e8a80b.png)

On clicking 'Create Account' - they are directed to the sign up page, where FromVin will collect their details. 

![Screenshot_20](https://user-images.githubusercontent.com/61311614/123704422-892e4080-d85d-11eb-8295-504191e4e56a.png)

Note that validation is present on this form, the fields are required.

![Screenshot_21](https://user-images.githubusercontent.com/61311614/123704424-892e4080-d85d-11eb-8871-96b307e517d0.png)

Also note that under 'My Account', no account details are yet present, due to the user not having an account/is not logged in.

![Screenshot_22](https://user-images.githubusercontent.com/61311614/123704425-89c6d700-d85d-11eb-937c-330a4d21ef37.png)

On sign up, django has a built-in verification process, where the user is sent an email seeking confirmation that the email is correct and active.

![Screenshot_23](https://user-images.githubusercontent.com/61311614/123704427-89c6d700-d85d-11eb-8334-8fb9f47433c3.png)

The email follows the below format and arrived almost immediately. The format is clear, concise and the process is simple.

![Screenshot_24](https://user-images.githubusercontent.com/61311614/123704428-89c6d700-d85d-11eb-9c96-0ff7a5a3d955.png)

The link takes them to a confirm page, with a clear call to action.

![Screenshot_25](https://user-images.githubusercontent.com/61311614/123704430-8a5f6d80-d85d-11eb-8b15-14e8849ef3c0.png)

They are then presented with the call to sign in with their new credentials.

![Screenshot_26](https://user-images.githubusercontent.com/61311614/123704431-8a5f6d80-d85d-11eb-8995-0042ab962265.png)

The user now has a profile on the 'My Account' drop down menu.

![Screenshot_27](https://user-images.githubusercontent.com/61311614/123704433-8a5f6d80-d85d-11eb-9133-8d0990174fc5.png)

Back at the checkout, there is now the option to have the delivery credentials saved. The user is required to fill these in to proceed with the order.

![Screenshot_28](https://user-images.githubusercontent.com/61311614/123704437-8af80400-d85d-11eb-8dd4-4eaedb8b1b32.png)

On completion (and after a fun loading spinner), the user is presented with confirmation and a message stating success.

![Screenshot_29](https://user-images.githubusercontent.com/61311614/123704439-8af80400-d85d-11eb-86fa-a1466353f7b4.png)

The below is just to show that stripe successfully received and processed the information sent over by the user. The validation presented by the boutique ado project is all present so that should this not work, the user is informed and orders do not go through.

![Screenshot_30](https://user-images.githubusercontent.com/61311614/123704441-8b909a80-d85d-11eb-8830-fc5455fe9059.png)
![Screenshot_31](https://user-images.githubusercontent.com/61311614/123704444-8b909a80-d85d-11eb-9ea4-d4954d74be49.png)

The user is then sent a custom email detailing their order. Going forward, this would utilise additional styling to reflect the company brand. 

![Screenshot_32](https://user-images.githubusercontent.com/61311614/123704445-8c293100-d85d-11eb-8935-759afb4d7400.png)

On now visiting the profile, the user is presented with this saved delivery information, along with a link to the order that was just made.

![Screenshot_33](https://user-images.githubusercontent.com/61311614/123704446-8c293100-d85d-11eb-890e-9b944564b269.png)

The order details are reflected here, with information that the order is in the past. 

![Screenshot_34](https://user-images.githubusercontent.com/61311614/123704448-8c293100-d85d-11eb-8a30-7f828b11a2c8.png)

Should additional products be desired, if the user has a specific type or product in mind then they are able to utilise the searchbox on the page from wherever they are. 

![Screenshot_35](https://user-images.githubusercontent.com/61311614/123704450-8cc1c780-d85d-11eb-954c-9358e5ebd802.png)

This then collapses to a more compact version on mobile view, catering to as many device types and customers as possible.

![Screenshot_36](https://user-images.githubusercontent.com/61311614/123704453-8d5a5e00-d85d-11eb-8814-1862f14ba61d.png)

The session can be terminated using the 'Sign Out' option, under 'My Account'.

![Screenshot_37](https://user-images.githubusercontent.com/61311614/123704455-8d5a5e00-d85d-11eb-9071-4e881b7650fb.png)

The user is again presented with a successful confirmation message. 

![Screenshot_38](https://user-images.githubusercontent.com/61311614/123704458-8d5a5e00-d85d-11eb-9ade-a97847ad4f09.png)

Should a user forget their password, Django has excellent functionality for this and the user is able to select that they have forgotten their password when they go to sign in.

![Screenshot_39](https://user-images.githubusercontent.com/61311614/123704459-8df2f480-d85d-11eb-93bf-5c3619533d34.png)

They simply enter their email address as a first step.

![Screenshot_40](https://user-images.githubusercontent.com/61311614/123704463-8df2f480-d85d-11eb-88c2-c49b371a5309.png)

Receive confirmation and direction that they should check their email.

![Screenshot_41](https://user-images.githubusercontent.com/61311614/123704465-8df2f480-d85d-11eb-9228-fa956ca9af45.png)

Are provided with a simple link to go back to reset their password.

![Screenshot_42](https://user-images.githubusercontent.com/61311614/123704469-8e8b8b00-d85d-11eb-9939-8da92e4b4ac0.png)

If they should utilise the link more than once, Django has functionality pre-built for this also. The user will get the below and are able to try again.

![Screenshot_43](https://user-images.githubusercontent.com/61311614/123704472-8e8b8b00-d85d-11eb-8d2e-c3e8aed9a177.png)

On success however, the user is prompted to enter a new password, and confirm it. These are required to match.

![Screenshot_44](https://user-images.githubusercontent.com/61311614/123704474-8f242180-d85d-11eb-9f50-328544f97a6a.png)

Once again, feedback is presented in a pleasant way. 

![Screenshot_45](https://user-images.githubusercontent.com/61311614/123704475-8f242180-d85d-11eb-9e69-4e30b1253fe5.png)

Should that user be mamrked as an admin, there is additional functionality available. For a start there is a 'Product Management' section that is unavailable to users without appropriate permissions.

![Screenshot_46](https://user-images.githubusercontent.com/61311614/123706795-a7e20680-d860-11eb-9da2-84b6cc257939.png)

Here, an admin user is able to create a product entry that, once submitted, will be added to the database. 

![Screenshot_47](https://user-images.githubusercontent.com/61311614/123706820-af091480-d860-11eb-9c47-c083f18e48ca.png)

When browsing products, they are also able to Edit, or Delete products. 

![Screenshot_48](https://user-images.githubusercontent.com/61311614/123706821-af091480-d860-11eb-85e8-574351333452.png)

Edit will take them to a similar page to 'Create', where the current details are populated, and can be amended. 

![Screenshot_49](https://user-images.githubusercontent.com/61311614/123706824-b03a4180-d860-11eb-8047-43419a38ef5a.png)

For this, test products have been added.

![Screenshot_50](https://user-images.githubusercontent.com/61311614/123706826-b0d2d800-d860-11eb-9dfa-0355202325cc.png)

The admin user is provided feedback that their deletion was successful, and the entry is removed from the database. 

![Screenshot_51](https://user-images.githubusercontent.com/61311614/123706831-b16b6e80-d860-11eb-8307-7dda407da28f.png)

One of the wonderful aspects of Django is that the admin users have much, much more scope within the built-in admin backend. Here they can control almost every aspect of the site. The majority here is quite standard for an e-commerce site, but tasting profiles and blogs are site-specific. There presently isn't much to the tasting profiles but adding a new blog entry is incredibly simple via this admin backend.

![Screenshot_52](https://user-images.githubusercontent.com/61311614/123706834-b2040500-d860-11eb-8529-db99e26d3780.png)

On clicking into Blogs, the admin can view what and when articles were created, along with whether they are live or not.

![Screenshot_53](https://user-images.githubusercontent.com/61311614/123706835-b2040500-d860-11eb-9ce1-3f6a734f06de.png)

Adding or changing then becomes as simple as inserting your content and clicking 'Save'.

![Screenshot_54](https://user-images.githubusercontent.com/61311614/123706836-b29c9b80-d860-11eb-8d77-6b9badf55410.png)

## Conclusion

In my opinion, the journey...

 On a personal note, this course has been a superb experience. The intention was to utilise it to kickstart a career in software development and it has been successful in this regard already. For this reason, amongst others, I have had much less time available than I would want to do this final project justice. The idea is sound, the execution would have been well served by another couple of weeks of clear time to work on it. 


## Attribution
- External links to wine tasting guides found at the [WineFolly](https://winefolly.com/) resource. 
- Assistance with adding django messages found at [Ordinarycoders.com](https://www.ordinarycoders.com/blog/article/django-messages-framework)
- Assistance with deploying static files with heroku found at [dev.to](https://dev.to/developerroad/tutorial-deploying-a-django-app-on-heroku-4k6o) 
- Images resized for deployment using [Resizeimage.net](https://resizeimage.net/)
- Addition of select form assistance using [GeeksforGeeks](https://www.geeksforgeeks.org/choicefield-django-forms/)
- Assistance with getting a sample of Django data [Stackoverflow - lukeaus](https://stackoverflow.com/questions/22816704/django-get-a-random-object)
- Guide for addition of a blog to the site [DjangoCentral](https://djangocentral.com/building-a-blog-application-with-django/)
- Workaround for images that do not fall under the main static images found at [StackOverflow - prariedogg](https://stackoverflow.com/questions/433162/can-i-access-constants-in-settings-py-from-templates-in-django)
- Assistance with ideas for tasting notes from [Virgin Wines](https://www.virginwines.co.uk/hub/wine-guide/wine-basics/how-to-taste-wine/)
- Information on custom context processors located here [stackoverflow - bchhun](https://stackoverflow.com/questions/433162/can-i-access-constants-in-settings-py-from-templates-in-django)



### Images

#### General
- noimage.jpg - [Wikimedia commons](https://commons.wikimedia.org/wiki/File:No_Image_Available.jpg) - Creative Commons Licence
- wine_wheel.jpg - [Wikimedia commons](https://upload.wikimedia.org/wikipedia/commons/a/a1/Wine_Aroma_Wheel.jpg) - Creative Commons Licence
- cheers.jpg - [photostockeditor](https://photostockeditor.com/image/wine-group-of-people-holding-footed-glasses-glass-19025) - Creative Commons Licence

#### Red Wines
- merlot1 image - [Wikimedia commons](https://commons.wikimedia.org/wiki/File:Estepa_Merlot_Red_Wine_Series_(4532104130).jpg) - Creative Commons Licence
- penfolds1 - [Pxhere.com](https://pxhere.com/en/photo/1151043) - Creative Commons Licence
- bordeaux1 - [Pxhere.com](https://pxhere.com/id/photo/868424) - Creative Commons Licence
- werken1 - [Pxhere.com](https://pxhere.com/fi/photo/694393) - Creative Commons Licence
- thalia1 - [hippopx.com](https://www.hippopx.com/en/wine-bottle-red-wine-fruit-wine-red-cork-bottle-52248)- Creative Commons Licence
- swartland1 - [pixabay.com](https://pixabay.com/photos/wine-alcohol-drink-glass-bottle-3180220/) - stevepb
- kalimna1 - [pixabay.com](https://pixabay.com/photos/bottle-beverage-wine-drink-alcohol-50571/) - Holgi
- smithhook1 - [pixabay.com](https://pixabay.com/photos/wine-bottle-alcohol-drink-party-3916274/) - pixexid
- nuits1 - [pixabay.com](https://pixabay.com/photos/dinner-salad-wine-glass-bottle-732057/) - TesaPhotography
- coupage1 [pixapay.com](https://pixabay.com/photos/bottle-wine-red-wine-drink-glass-2975864/) - wjsm1978
- bordeaux2 [pixabay.com](https://pixabay.com/photos/wine-red-wine-alcohol-france-drink-360286/) - luctheo
- portalegre1 [pixabay.com](https://pixabay.com/photos/wine-red-wine-portugal-reserve-4556413/) - mariadasdores

#### White Wines
- waterside1 [pixabay.com](https://pixabay.com/photos/wine-wineglass-leisure-drink-2789280/) - stevepb
- schoffit1 [pixabay.com](https://pixabay.com/photos/wine-alcohol-drink-bottle-liquid-3092944/) - Sponchia
- leopardsleap1 [pixabay.com](https://pixabay.com/photos/white-wine-drink-alcohol-bottle-3185546/) - stevepb
- boutari1 [pixabay.com](https://pixabay.com/photos/wine-wine-bottle-white-wine-bottle-1209623/) - Free-Photos
- nobilo1 [pixabay.com](https://pixabay.com/photos/wine-bottle-white-lemons-plums-1576564/) - ponce_photography
- tojaki1 [pixabay.com](https://pixabay.com/photos/wine-white-wine-vineyard-glass-2479720/) - 5519128
- riesling1 [pixabay.com](https://pixabay.com/photos/white-wine-bottle-sky-clouds-76834/) - 12019
- pineau1 - [pixabay.com](https://pixabay.com/photos/wine-white-wine-pineau-drink-4094235/) - stefangrage
- lugana1 [pixabay.com](https://pixabay.com/photos/white-wine-glass-grapes-stones-4606960/) - Rene1905
- williamette1 [pixabay.com](https://pixabay.com/photos/willamette-valley-vineyards-oregon-4280364/) - Olichel
- granger1 [pixabay.com](https://pixabay.com/photos/cheese-and-wine-wine-bottle-glass-3490303/) - jeanvdmeulen
- privat1 [pixabay.com](https://pixabay.com/photos/wine-wine-bottle-wine-glass-5154598/) - ReinhardThrainer


#### Dessert Wines
- sauternes1 [pixabay.com](https://pixabay.com/illustrations/sweet-white-wine-ivan-gan-2383801/) - wendy-chan
- sauternes2 [pixabay.com](https://pixabay.com/photos/wine-white-wine-sauterne-bordeaux-360299/) - luctheo
- delaforce1 [pixabay.com](https://pixabay.com/photos/drink-wine-alcohol-bottle-glass-3377626/) - DonnaSenzaFiato
- cruz1 [pixabay.com](https://pixabay.com/photos/port-wine-porto-cruz-wine-tourism-2264096/) - Gentle07
- ferreira1 [pixabay.com](https://pixabay.com/photos/bottle-wine-port-tequila-porto-4571546/) - AlLes


#### Soft Cheeses
- soft1 [pixabay.com](https://pixabay.com/photos/oven-baked-cheese-cheese-baked-2817144/) - Couleur
- soft2 [pixabay.com](https://pixabay.com/photos/breadbasket-soft-cheese-creamy-3704381/) - Couleur
- soft3 [pixabay.com](https://pixabay.com/photos/cheese-platter-food-snack-grapes-6153716/) - Mammiya
- soft4 [pixabay.com](https://pixabay.com/photos/cheese-k%C3%A4seplatte-food-cheese-plate-4016647/) - ReinhardThrainer
- soft5 [pixabay.com](https://pixabay.com/photos/cheese-k%C3%A4seplatte-buffet-food-eat-4059250/) - congerdesign
- soft6 [pixabay.com](https://pixabay.com/photos/cheese-soft-cheese-food-eat-hearty-4107310/) - ThorstenF
- soft7 [pixabay.com](https://pixabay.com/photos/cheese-soft-cheese-brie-cheese-3686070/) - lucas_holiday
- soft8 [pixabay.com](https://pixabay.com/photos/soft-cheese-camembert-blue-cheese-822350/) - EME
- soft9 [pixabay.com](https://pixabay.com/photos/cheese-brie-curds-cracker-knife-1081082/) - dbreen
- soft10 [pixabay.com](https://pixabay.com/photos/soft-cheese-camembert-blue-cheese-822346/) - EME
- soft11 [pixabay.com](https://pixabay.com/photos/epoisse-cheese-cheese-fruit-pairing-2256023/) - Jaques2017
- soft12 [pixabay.com](https://pixabay.com/photos/st-pat-cheese-milk-product-food-3540/) - PDPhotos

#### Hard Cheeses
- hard1 [pixabay.com](https://pixabay.com/photos/cheese-jarlsberg-norway-semi-soft-739735/) - pixel1
- hard2 [Pxhere](https://pxhere.com/en/photo/1637327) - Creative Commons Licence
- hard3 [pxhere](https://pxhere.com/en/photo/1624743) - Creative Commons Licence
- hard4 [pixabay.com](https://pixabay.com/photos/cheese-cheese-loaf-market-stall-4021659/) - ReinhardThrainer
- hard5 [Pixnio](https://pixnio.com/food-and-drink/cheese/red-dragon-cheese#) - Jon Sullivan
- hard6 [pixabay.com](https://pixabay.com/photos/hard-cheese-home-production-928848/) - Fotovektor
- hard7 [pixabay.com](https://pixabay.com/photos/wood-knife-cheese-food-hard-slice-3794057/) - 6342722
- hard8 [Pixnio](https://pixnio.com/food-and-drink/cheese/red-windsor-cheese#) - Jon Sullivan
- hard9 [pixabay.com](https://pixabay.com/photos/cheese-semi-hard-cheese-gouda-1029190/) - Peggy_Marco
- hard10 [pixabay.com](https://pixabay.com/photos/cheese-milk-product-cheese-loaf-4752609/) - moritz320
- hard11 [Pixnio](https://pixnio.com/food-and-drink/cheese/pecorino-romano-cheese#) - Jon Sullivan
- hard12 [Pixnio](https://pixnio.com/food-and-drink/cheese/port-salut-cheese#) - Jon Sullivan

#### Accompaniments
- chutney1 - [pxhere](https://pxhere.com/en/photo/119408) - Creative Commons Licence
- chutney2 - [pxhere](https://pxhere.com/en/photo/816936) - Creative Commons Licence
- chutney3 - [pxhere](https://pxhere.com/en/photo/1408223) - Creative Commons Licence
- crackers1 - [pxhere](https://pxhere.com/en/photo/1247287) - Creative Commons Licence
- crackers2 - [pxhere](https://pxhere.com/en/photo/1132679) - Creative Commons Licence
- bread1 - [pxhere](https://pxhere.com/en/photo/595291) - Creative Commons Licence
- bread2 - [pxhere](https://pxhere.com/en/photo/1221989) - Creative Commons Licence
- bread3 - [pxhere](https://pxhere.com/en/photo/25751) - Creative Commons Licence
- bread4 - [pxhere](https://pxhere.com/en/photo/399077) - Creative Commons Licence