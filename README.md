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



## Design Decisions

### General Design
As a preface to the aspects that are more bespoke on the site, it needs to be stated that i've leaned quite heavily on the boutique ado project. As the only full ecommerce solution on the course and an ideal example of how to put together a django ecommerce site, it seemed like a natural source of a basis. This was discussed with my stand-in mentor to confirm this would be the case, and was told that it was expected, but should be stated outright here.

Otherwise, a fixed top navbar was selected so that a user can utilise the navigation even when midway down hundreds of products. On said navbar, the site has been split into it's shop, a homepage which acts as an informational guide, a recommendation page and a blog for more bespoke information from the site owners. (SPOTLIGHT ON SPECIFIC PRODUCTS?)


### Data Specific Design


#### Database Schema




### Wireframes



#### Desktop





#### Mobile





### Technologies used

- Gitpod - this was the chosen development platform.
- Bootstrap for site layout, container code, navbar functions - used throughout for rich content and responsive behaviour.
- JQuery addon used for rich function searching in order to appropriately target html and CSS for site functionality.
- GitHub - utilised for cloud backups and project progression.
- Realfavicongenerator.net - used to correctly generate site favicons.
- Mockplus Classic - Used for wireframes of the project - possibly the best free option so far in my opinion.
- Heroku - for deploying and hosting the application.  
- Creately - used to document the database schema.


## Testing

### Validation service

#### HTML




#### CSS




#### JavaScript



#### Python



#### Wave(WebAIM) validator




#### Internal custom validation
Note for future - code to disable form and test webhooks can be found in BA profile video 9, at the end. form.submit in stripe_elements.js.




### Page links



### Browsers





### Testing that Heroku version matches development version.




## Known issues
- I had a little trouble with wrapping my head around static files and django. I made a little workaround for images that were not uploaded via admin, such as the flavour wheel. This does not represent best practice amongst the way it was handled



## Future improvements
- Make tasting profile less of a magic number
- Thoroughly research the pairings, they currently are arbitary and could be more tailored. 

## Deployment Procedure

### Local Deployment



### Cloning this exact project



### Deployment via Heroku

Getting Heroku to deploy a version of this project is incredibly simple. The below steps can be followed:

- Ensure that the project is linked to a GitHub repository.
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



## Conclusion
 On a personal note, this course has been a superb experience. The intention was to utilise it to kickstart a career in software development and it has been successful in this regard already. For this reason, amongst others, I have had much less time available than I would want to do this final project justice. The idea is sound, the execution would have been well served by another couple of weeks of clear time to work on it. 


## Attribution
- Assistance with adding django messages found at [Ordinarycoders.com](https://www.ordinarycoders.com/blog/article/django-messages-framework)
- Assistance with deploying static files with heroku found at [dev.to](https://dev.to/developerroad/tutorial-deploying-a-django-app-on-heroku-4k6o) 
- Images resized for deployment using [Resizeimage.net](https://resizeimage.net/)
- Addition of select form assistance using [GeeksforGeeks](https://www.geeksforgeeks.org/choicefield-django-forms/)
- Assistance with getting a sample of Django data [Stackoverflow - lukeaus](https://stackoverflow.com/questions/22816704/django-get-a-random-object)
- Guide for addition of a blog to the site [DjangoCentral](https://djangocentral.com/building-a-blog-application-with-django/)
- Workaround for images that do not fall under the main static images found at [StackOverflow - prariedogg](https://stackoverflow.com/questions/433162/can-i-access-constants-in-settings-py-from-templates-in-django)
- Assistance with ideas for tasting notes from [Virgin Wines](https://www.virginwines.co.uk/hub/wine-guide/wine-basics/how-to-taste-wine/)



### Images

#### General
- noimage.jpg - [Wikimedia commons](https://commons.wikimedia.org/wiki/File:No_Image_Available.jpg) - Creative Commons Licence
- wine_wheel.jpg - [Wikimedia commons](https://upload.wikimedia.org/wikipedia/commons/a/a1/Wine_Aroma_Wheel.jpg) - Creative Commons Licence

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