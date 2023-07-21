# Testing


## [HTML Validator](https://validator.w3.org/)

HTML was validated by copying the page source and pasting into the validator.

- <details>
  <summary>Index Results</summary>
  There are some errors showing in the HTML Checker that should be fixed in future iterations. 

    ![Index results](readme-docs/testing/html-validation/index.png)
  </details>

- <details>
  <summary>Home Results</summary>

  ![Home results](readme-docs/testing/html-validation/home.png)
  </details>

- <details>
  <summary>My Meals Results</summary>

  ![My Meals results](readme-docs/testing/html-validation/mymeals.png)
  </details>

- <details>
  <summary>Register Results</summary>

  ![Register results](readme-docs/testing/html-validation/signup.png)
  </details>

- <details>
  <summary>Login Results</summary>

  ![Login results](readme-docs/testing/html-validation/login.png)
  </details>

- <details>
  <summary>Admin Panel Results</summary>

  ![Admin Panel results](readme-docs/testing/html-validation/adminpanel.png)
  </details>

- <details>
  <summary>Admin Create Results</summary>

  ![Admin Create results](readme-docs/testing/html-validation/admin-create.png)
  </details>

- <details>
  <summary>Admin Edit Results</summary>

  ![Admin Edit results](readme-docs/testing/html-validation/admin-edit.png)
  </details>
  - <details>
  <summary>Admin Edit Results</summary>


## [CSS Validator](https://jigsaw.w3.org/css-validator/)

CSS was validated by copying the CSS file into the validator. No errors were reported. There were 220 warnings related to vendor extensions and bootstrap classes.

- Results for style.css:
  - ![CSS results](readme-docs/testing/css.png)
  - <p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>


## JavaScript Testing

JSHint was used for validating the JavaScript for the modals and email. 


## Python Testing

The project was tested for pep8 compliance using pycodestyle. [autopep8](https://pypi.org/project/autopep8/) was used to aid compliance. # noqa was used in a small number of cases where necessary. At time of writing no problems or errors were found.


## Lighthouse

The site was tested using Lighthouse in Chrome DevTools to check performance, accessibiltiy, best practices and SEO. The final testing on Lighthouse was run on incognito mode. The results are below.

<details>
<summary>Index - Not Logged In</summary>

![Index - Not logged in](readme-docs/lighthouse/index.png)
</details>

<details>
<summary>Home - Index Logged In</summary>

![Home](readme-docs/lighthouse/home.png)
</details>

<details>
<summary>My Meals</summary>

![My Meals](readme-docs/lighthouse/mymeals.png)
</details>

<details>
<summary>Admin Panel</summary>

![Admin Panel](readme-docs/lighthouse/adminpanel.png)
</details>

<details>
<summary>Login</summary>

![Login](readme-docs/lighthouse/signin.png)
</details>

<details>
<summary>Signup</summary>

![Signup](readme-docs/lighthouse/signup.png)
</details>


## Manual Testing

### User Story Testing

- As a Site User I can view the home page so that I can see the site's goal and be encouraged to sign up
<details>
<summary>Testing Results</summary>
This passes the testing because the sign up button is clearly visible and the site goal is implied by the nature of the image. 

![Index](readme-docs/testing/user-story-1.png)

</details>
- As a Site User I can register for an account so that I can log in to gain access to the site's features
<details>
<summary>Testing Results</summary>
This passes the testing because the registration form is clear and easy to understand and easily accessible.

![Signup](readme-docs/testing/user-story-2.png)

</details>
- As a Site User I can log in so that I can gain access to the site's features
<details>
<summary>Testing Results</summary>
This passes the testing because the login is easy to access and clear and simple to understand. 

![Login](readme-docs/testing/user-story-3.png)

</details>
- As a Site User I can Log Out so that I can let someone else log in on my computer, leave myself signed out on public spaces or change accounts
<details>
<summary>Testing Results</summary>
This passes the testing because the logout option is easy to find, and simple to understand

![Logout](readme-docs/testing/user-story-4.png)

</details>
- As a Site User I can view the Home page when logged in so that I can pin meals
<details>
<summary>Testing Results</summary>
This passes the testing because you are automatically redirected to the Home page after login

![Home](readme-docs/testing/user-story-5.png)

</details>

- As a Site User I can view my pinned meals so that I can see what I've saved
<details>
<summary>Testing Results</summary>
This passes the testing because the My Meals page automatically generates the list of meals you have pinned. Alternatively, pinned meals can be seen by the icon change. 

![MyMeals](readme-docs/testing/user-story-6.png)

</details>

- As a Site User I can Click on the 'pin' to pin a meal-card so that it is added to "My Meals"
<details>
<summary>Testing Results</summary>
This passes the testing because clicking pin adds the meal to your meal list. A message gives confirmation when this is clicked. 

![Pin](readme-docs/testing/user-story-7.png)

</details>

- As a Site User I can Click on the highlighted 'pin' to unpin a meal-card so that it is removed from "My Meals"
<details>
<summary>Testing Results</summary>
This passes the testing because clicking the highlighted pin removes it from your meal list. A message gives confirmation when this is clicked. 

![Unpin](readme-docs/testing/user-story-7.png)

</details>

- As a Site User I can Click on the Info button so that I can expand the Meal Card and view the recipe in more detail
<details>
<summary>Testing Results</summary>
This passes the testing because the info button, once clicked, opens a dialog displaying the detailed information. Clicking anywhere off of the dialog, or the X on the dialog, closes this. 

![Info Button](readme-docs/testing/user-story-8.png)
![Info Dialog](readme-docs/testing/user-story-9.png)

</details>
- As a Site User I can unpin meals on the My Meals page so that they are removed from the page, and the page automatically updates
<details>
<summary>Testing Results</summary>
This passes the testing because clicking the unpin from My Meals removes it from the meal list, and from the page. 

![Unpin from My Meals](readme-docs/testing/user-story-10.png)

</details>
- As a Site Administrator I can view administrator features so that I can add, edit and remove meal cards to the site
<details>
<summary>Testing Results</summary>
This passes the testing because clicking on the Admin Panel brings up a list of the meals to review, with all CRUD functionality provided.

![Admin Panel](readme-docs/testing/user-story-11.png)

</details>
- As a Site Administrator I can view the meal CRUD Forms so that I can add, edit and remove meals from the site
<details>
<summary>Testing Results</summary>
This passes the testing because the add meal button takes you to a create form that is easy to use and understand. The edit button takes you to an edit form that is easy to use and understand. The delete button removes the meal, and gives confirmation of this action. 

![Admin Create](readme-docs/site-images/admin-create.png)
![Admin Edit](readme-docs/site-images/admin-edit.png)
![Admin Delete](readme-docs/site-images/admin-delete.png)

</details>
- As a Developer I can create a model for the Meal database so that it is available for administrators to add meals
<details>
<summary>Testing Results</summary>
This passes the testing because we can see in the admin panel that this model is complete and working as intended.

![Meal Model](readme-docs/testing/meal-model.png)

</details>


- As a Developer I can create a model for the Pinned Meal database for each user so that we can generate a list of pinned meals for each user
<details>
<summary>Testing Results</summary>
This passes the testing because we can see in the admin panel that this model is complete and working as intended.

![My Meals Model](readme-docs/testing/mymealsmodel.png)

</details>
- As a Developer I can automatically generate a list of a User's pinned meals so that when they go to the "My Meals" page it only displays the meals they have pinned
<details>
<summary>Testing Results</summary>
This passes the testing because the My Meals are automatically generated on the My Meals page. 

![My Meals List Generation](readme-docs/site-images/mymeals.png)

</details>


## Browser Compatibility
The website was tested on:
- Chrome Version 106.0.5249.119
- Firefox Version 106.0.1
- Edge Version 106.0.1370.52
- Safari iOS Version 15.6.1


## Bugs

### Fixed Bugs

- Bug:
  - **Issue:** Favicon not appearing on site
  - **Description:** Favicon was not appearing on the deployed site
  - **Fix:** Make a link in the head to reference the favicon

- Bug:
  - **Issue:** Static files not loading on deployed site
  - **Description:** Static files were not loading because they were not linked properly through cloudinary
  - **Fix:** Removed debug from settings.py and used direct link to cloudinary file for image in css file

- Bug:
  - **Issue:** Summernote recipe box malfunctioning
  - **Description:** In the info dialog, the recipe was appearing with html tags as opposed to rendering as html
  - **Fix:** added Safe filter to recipe box

- Bug:
  - **Issue:** forEach loop not working
  - **Description:** forEach loop in the javascript returning "cannot read properties of undefined"
  - **Fix:** used ```[...]``` functionality to parse it into an array

- Bug:
  - **Issue:** Removing meals redirecting incorrectly
  - **Description:** My Meals unpin button redirecting to index page
  - **Fix:** Added code ```return redirect(reverse(request.GET.get("redirect")``` to views for remove pin


### Known Bugs

There are currently no known bugs.