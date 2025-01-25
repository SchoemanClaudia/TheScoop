# Testing

Testing file for The Scoop [README.md](README.md).

## Testing User Stories

### Developer Stories

- [x] Frontend and Backend of the project created.
- [x] Database is connected to the project.
- [x] App deployed on Heroku.

### User Stories

- [x] Open a review
- [x] View paginated list of reviews
- [x] Create draft reviews
- [x] Manage reviews
- [x] Read about the reviewers
- [x] Add and update the about reviewer text
- [x] Account registration
- [x] View comments
- [x] Comment on a review
- [x] Approve comments
- [x] Contact form
- [x] Store contact form requests
- [x] Modify or delete comment on a review
- [x] Add image to review
- [x] Add directions map to review


## Validation

### HTML Validation

[x] HTML validation all passed.

**Home page**  
![Home Page HTML Validation]()

**Login Page**  
![Login Page HTML Validation]()

**Logout Page**  
![Logout Page HTML Validation]()

**Register Page**  
![Register Page HTML Validation]()

**Review Post Page**  
![Review Post Page HTML Validation]()

**About Page**  
![About Page HTML Validation]()

### CSS Validation

[x] CSS validation all passed.

![CSS Validation]()

### JSHint

[x] JavaScript tests all passed.

![JSHint]()

### CI Python Linter

[x] Python tests all passed.

| Feature | admin.py | forms.py | models.py | urls.py | views.py |
|---------|----------|----------|-----------|---------|----------|
| TheScoop main app | na | na | na | [no errors](documentation/testing/thescoop-urls.png) | na |
| Reviews | [no errors](documentation/testing/reviews-admin.png) | [no errors](documentation/testing/review-forms.png) | [no errors](documentation/testing/review-models.png) | [no errors](documentation/testing/review-urls.png) | [no errors](documentation/testing/review-views.png) |
| About  | [no errors](documentation/testing/about-admin.png) | [no errors](documentation/testing/about-forms.png) | [no errors](documentation/testing/about-models.png) | [no errors](documentation/testing/about-urls.png) | [no errors](documentation/testing/about-views.png) |

All Python files containing the project's code have been tested. All the errors were fixed, and after running the CI Python Linter, it shows there are no errors.
NOTE: `settings.py` Stock Django code gives E501 error, left unchanged to keep app from breaking.

![Python Test Settings]()

## Lighthouse Test

- [x] Desktop view:

    **Home**  
    ![Lighthouse Report Home]()

    **Review post page**  
    ![Lighthouse Report Review Post Page]()

    **About Page**  
    ![Lighthouse Report About]()

    **Register Page**  
    ![Lighthouse Report Register]()

    **Login Page**  
    ![Lighthouse Report Login]()

    **Logout Page**  
    ![Lighthouse Report Logout]()

- [x] Mobile view:
    - Lighthouse testing was carried out in Incognito mode to acheive the best result. Performance was lower than preferred on mobile view due to the site being image heavy. Images used in the sites design were compressed to offer the best chance for a decent performance score. The CDNs used for Bootstrap were also noted in the Lighthouse report as causing issue with performance. This report will be reviewed for future development of The Scoop to raise this score.

    **Home**  
    ![Lighthouse Report Home Mobile]()

### Accessibility

Accessibility was included in every planning stage for The Scoop, through the use of the WAVE report tool I could ensure that any necessary changes were made to make the website as accessible as it could be. A minor contrast issue with logo brand on header, pagination buttons and ratings rendered too light for the feature theme and were adjusted accordingly while still keeping to original colour scheme.

- 

  ![Errors encountered](static/images/errors.webp)

- 

![No errors](static/images/clear.webp)

## Manual Testing

### User Input/Form Validation

Testing was carried out on desktop using a Chrome browser to ensure all forms take the intended input and process the input appropriately.
Manual testeing by checking the following:

| TEST INPUT | CORRECT OUTCOME | MEET REQUIREMENTS |
|:---:|:---:|:---:|
| xxx | PASS |
| 


## Bugs Encountered 
  
The below are bugs that I spent more time investigating or required the assistance of Tutor Support.
Most of these encountered were learning curves. 

| No. | Bug | Solved | Fix | Solution Credit | Commit no. |
| --- | --- | ------ | --- | --------------- | -----------|
| No. | Bug | Solved | Fix | Solution Credit | Commit no. |

### Unfixed Bugs

- No unfixed bugs, app running with no errors.

![Final Result Success]()
