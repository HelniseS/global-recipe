#  Global Recipe

GlobalRecipe is a full-stack Django web application that allows users to browse, search, and manage recipes from different cuisines around the world. The project demonstrates full CRUD functionality, user authentication, media handling, and deployment to a live production environment.

The application is designed with usability, accessibility, and performance in mind and has been successfully deployed to Heroku.


---
## Contents
- [Project Goals](#project-goals)
- [User Goals](#user-goals)
- [User Stories](#user-stories)
- [Website Goals and Objectives](#website-goals-and-objectives)
- [Wireframes](#wireframes)
- [Design Choices](#design-choices)
  - [Typography](#typography)
  - [Colour Scheme](#colour-scheme)
  - [Media](#media)
  - [Responsiveness](#responsiveness)
  - [Accessibility Considerations](#accessibility-considerations)
- [Features](#features)
- [Finished Product](#finished-product)
- [CRUD Functionality Summary](#crud-functionality-summary)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Security & Environment Variables](#security--environment-variables)
- [Performance & Accessibility](#performance--accessibility)
- [Credits](#credits)


---
## Project Goals

The goal of the Global Recipe project is to design and develop a full-stack, data-driven web application using Django that demonstrates secure user authentication, relational database design, and full CRUD functionality.

The key objectives of the project are:

- To allow users to **browse and search recipes** from different global cuisines in a clear and intuitive interface.
- To enable authenticated users to **create, read, update, and delete their own recipes**, demonstrating full CRUD functionality.
- To design a **relational database schema** using Django models, with clear relationships between recipes, ingredients, steps, nutrition data, and tags.
- To ensure **data ownership and security**, so users can only edit or delete content they have created.
- To implement **search and filtering** features that allow users to quickly find relevant recipes.
- To support **image uploads and media handling** in a production environment.
- To provide a **responsive, mobile-first user interface** that works across common screen sizes.
- To follow **accessibility best practices**, including semantic HTML, readable typography, and clear navigation.
- To deploy the application to a **live production environment** with `DEBUG` disabled and sensitive data protected using environment variables.
- To produce **clear, professional documentation** that explains design decisions, testing, deployment, and security considerations.


## User Goals

1. Browse and discover recipes  
   - As a Site User, I want to browse a wide range of recipes so that I can find inspiration for meals to cook.

2. Search and filter recipes easily  
   - As a Site User, I want to search for recipes by name, category, or tags so that I can quickly find relevant recipes.

3. View detailed recipe information  
   - As a Site User, I want to view clear ingredients, cooking steps, and preparation details so that I can follow recipes easily.

4. Create and share my own recipes  
   - As a Registered User, I want to add my own recipes with images so that I can share my cooking ideas with others.

5. Edit and delete my own recipes  
   - As a Registered User, I want to update or remove my recipes so that I can keep my content accurate and up to date.

6. Manage my account securely  
   - As a Registered User, I want to log in and out securely so that my recipes and account data are protected.

7. Access the site on any device  
   - As a Site User, I want the website to be responsive so that I can use it comfortably on mobile, tablet, and desktop devices.

## User Stories
**As a visitor**
- I can browse all recipes so that I can find something to cook.
- I can search/filter so that I can narrow results quickly.
- I can view a recipe’s details so that I can follow steps easily.

**As a registered user**
- I can add a recipe so that I can share it with others.
- I can edit or delete my own recipes so that I can keep them up-to-date.
- I can see my submitted recipes in one place.

**As an admin**
- I can manage users and recipes via Django Admin so that I can moderate content.

---

## Website Goals and Objectives
- Provide full CRUD (Create, Read, Update, Delete) functionality for recipes backed by a relational database.
- Meet accessibility guidelines (semantic HTML, ARIA where appropriate, colour contrast).
- Use clean project structure, version control, and professional documentation.
- Deploy to a cloud platform with DEBUG off and secrets protected.

---

## Wireframes

### Mobile Screens
![Home (Mobile)](docs/wireframes/home-mobile.png)
![Recipe List (Mobile)](docs/wireframes/recipe-list-mobile.png)
![Recipe Detail (Mobile)](docs/wireframes/recipe-detail-mobile.png)
![Login/Register (Mobile)](docs/wireframes/login-register.png)

### Desktop Screens
![Home (Desktop)](docs/wireframes/home-desktop.png)
![Recipe List (Desktop)](docs/wireframes/recipe-list-desktop.png)
![Recipe Detail (Desktop)](docs/wireframes/recipe-detail-desktop.png)
![Add Recipe (Desktop)](docs/wireframes/add-recipe.png)
![Login/Register (Desktop)](docs/wireframes/login-register.png)
---

## Design Choices

The design of Global Recipe focuses on clarity, accessibility, and ease of use. The interface is intentionally minimal so users can quickly browse, search, and manage recipes without distraction. All design decisions were made to support usability across devices and meet accessibility standards.

---

### Typography

- The application uses **Bootstrap’s default system UI font stack**.
- This ensures:
  - Fast loading times
  - Consistent rendering across devices and operating systems
  - Good readability for long recipe instructions
- Headings are visually distinct from body text to create a clear content hierarchy.

---

### Colour Scheme

The colour palette was kept simple and consistent to maintain readability and accessibility.

- **Primary colour:** Blue (`#0d6efd`)  
  Used for buttons, links, and primary actions such as *Search*, *Login*, and *Add Recipe*.
- **Secondary colours:** Neutral greys  
  Used for backgrounds, borders, and supporting text.
- **Background:** White (`#ffffff`)  
  Ensures high contrast and a clean layout.
- **Text:** Dark grey/black (`#212529`)  
  Chosen for optimal readability.

All colour combinations were checked to ensure sufficient contrast for accessibility.

---

### Media

- Recipe images are uploaded by users to visually represent each dish.
- Images improve user engagement and help users quickly identify recipes.
- In production, images are stored using a cloud-based media solution (**Cloudinary**) to ensure:
  - Reliable storage
  - Faster loading times
  - Scalability
- Image uploads are optional, allowing flexibility for users.

---

### Responsiveness

- The site is built using **Bootstrap’s grid system** to ensure a mobile-first approach.
- Layouts adapt smoothly across:
  - Mobile devices
  - Tablets
  - Desktop screens
- Key pages such as the home page, recipe list, recipe detail, and forms were tested at common breakpoints to confirm usability and layout consistency.

---

### Accessibility Considerations

- Semantic HTML elements are used throughout the site.
- Form inputs include clear labels to support screen readers.
- Buttons and links are large and clearly styled for ease of interaction.
- The navigation structure is consistent across all pages.

These design choices help ensure that Global Recipe is accessible, intuitive, and easy to use for a wide range of users.



## Features

Global Recipe is designed to provide a clear, intuitive, and secure experience for users who want to browse, create, and manage recipes. The application implements full CRUD functionality, user authentication, search and filtering, and responsive design.

---

### Home Page

The home page acts as the main entry point to the application and introduces users to the platform.

**Key functionality:**
- Displays a selection of recently added or popular recipes.
- Each recipe is presented as a card showing:
  - Recipe image
  - Title
  - Cooking time
  - Category
- A clear navigation bar allows users to:
  - Browse recipes
  - Search by keyword
  - Log in or register (unauthenticated users)
  - Add recipes or log out (authenticated users)

**Purpose:**
- Encourage exploration of recipes.
- Provide quick access to core features.
- Offer a clean, welcoming user interface.

---

### Recipe List & Search

The recipe list page allows users to browse and discover all available recipes.

**Key functionality:**
- Displays all recipes in a responsive card layout.
- Recipes are ordered by most recent first.
- Global search functionality allows users to search by recipe title.
- Filtering options allow users to:
  - Filter by category
  - Filter by tags
- Search and filter results update dynamically based on user input.

**Purpose:**
- Improve content discoverability.
- Allow users to quickly narrow down recipes.
- Demonstrate read and query filtering functionality.

---

### Recipe Detail Page

The recipe detail page provides complete information about a single recipe.

**Displayed information includes:**
- Recipe title and category
- Description
- Cooking time and number of servings
- Recipe image
- Ingredients list
- Step-by-step cooking instructions (ordered)
- Nutrition information (calories, protein, carbohydrates, fat)

**Conditional functionality:**
- If the logged-in user is the recipe author:
  - Edit and Delete buttons are visible.
- If the user is not the author:
  - Recipe content is read-only.

**Purpose:**
- Present recipe information clearly and logically.
- Ensure users can easily follow cooking instructions.
- Protect recipe ownership through conditional actions.

---

### User Authentication

Global Recipe uses Django’s built-in authentication system to manage users securely.

**Authentication features:**
- User registration with username and password.
- Password validation enforced by Django (minimum length, common password checks).
- Secure login and logout functionality.
- Authentication-aware navigation links.

**Purpose:**
- Ensure recipe ownership is tied to individual users.
- Protect user-generated content.
- Provide a secure, account-based experience.

---

### Add Recipe (Create)

Authenticated users can create new recipes using a structured form.

**Form sections include:**
- Basic recipe information:
  - Title
  - Category
  - Description
  - Cooking time
  - Servings
  - Rating
  - Optional image upload
- Ingredients:
  - Multiple ingredient fields using inline formsets.
- Steps:
  - Ordered step-by-step instructions.
- Nutrition:
  - Calories
  - Protein
  - Carbohydrates
  - Fat

**Validation:**
- Required fields must be completed.
- Invalid input triggers clear error messages.

**Purpose:**
- Demonstrate create functionality.
- Allow users to contribute content easily.
- Maintain structured, consistent data.

---

### Edit Recipe (Update)

Users can edit recipes they own.

**Key functionality:**
- All existing recipe data is pre-populated in the form.
- Users can update:
  - Recipe details
  - Ingredients
  - Steps
  - Nutrition information
  - Image
- Only the recipe author can access this functionality.

**Purpose:**
- Allow users to keep recipes accurate and up to date.
- Demonstrate update functionality.
- Enforce data ownership and permissions.

---

### Delete Recipe (Delete)

Users can delete recipes they own.

**Key functionality:**
- A dedicated confirmation page is shown before deletion.
- Clear warning text explains the action is permanent.
- Users can cancel deletion to return safely.

**Purpose:**
- Demonstrate delete functionality.
- Prevent accidental data loss.
- Improve user experience through confirmation steps.

---

### User Permissions & Security

Access control is enforced throughout the application.

**Permissions include:**
- Only authenticated users can create recipes.
- Only recipe authors can edit or delete their recipes.
- Unauthorized users are redirected or denied access.
- Admin users can manage content via Django Admin.

**Purpose:**
- Protect user data.
- Ensure secure CRUD operations.
- Demonstrate backend permission handling.

---

### Admin Panel

The Django Admin interface is configured to support efficient content management.

**Admin features:**
- Manage users and recipes.
- Inline management of ingredients and steps.
- Ability to edit or remove content when necessary.

**Purpose:**
- Simplify moderation and maintenance.
- Demonstrate use of Django’s built-in admin tools.

---

### Error Handling

**Implemented error handling includes:**
- User-friendly validation messages on forms.
- Custom error pages for invalid URLs (404).
- Graceful handling of missing or invalid input.

**Purpose:**
- Improve usability.
- Provide clear feedback during errors.
- Enhance overall user experience.

---

## Finished Product

### Home Page
![Home Page](docs/screenshots/home-page.png)

### Recipe Detail Page
![Recipe Detail Page](docs/screenshots/recipe-detail-page.png)

### Login Page
![Login Page](docs/screenshots/login-page.png)

### Register Page
![Register Page](docs/screenshots/user-registration.png)

### Add Recipe
![Add Recipe](docs/screenshots/add-recipe.png)

### Edit Recipe
![Edit Recipe](docs/screenshots/edit-recipe.png)

### Delete Recipe
![Delete Recipe](docs/screenshots/delete-recipe.png)


## CRUD Functionality Summary

The table below outlines how Create, Read, Update, and Delete (CRUD) operations are implemented across the main features of the Global Recipe application.

| Feature        | Create | Read | Update | Delete |
|----------------|--------|------|--------|--------|
| Users          | Yes    | No   | No     | No     |
| Recipes        | Yes    | Yes  | Yes    | Yes    |
| Ingredients    | Yes    | Yes  | Yes    | Yes    |
| Steps          | Yes    | Yes  | Yes    | Yes    |
| Nutrition      | Yes    | Yes  | Yes    | No (removed with recipe) |
| Tags           | No     | Yes  | No     | No     |

### Notes
- Users can register (Create) and authenticate, but profile editing and deletion are not included in the current scope.
- Recipes support full CRUD functionality and are securely tied to the authenticated user who created them.
- Ingredients and Steps are managed as related objects using Django formsets and inherit CRUD operations through the parent recipe.
- Nutrition data is optional and linked one-to-one with a recipe; it is deleted automatically when the recipe is deleted.
- Tags are shared entities that are assigned to recipes rather than being managed directly by users.

This summary demonstrates that Global Recipe meets the Project 3 requirement for implementing CRUD functionality within a data-driven Django application.

---

### Future Enhancements

- User favourites and saved recipes.
- Ratings and reviews system.
- Advanced filtering (dietary requirements, allergens).
- Image optimisation and thumbnails.
- Commenting system.
- Public API for third-party or mobile integrations.

---


## Technologies Used

### Languages Used

- **HTML5**  
  Used for semantic page structure across all templates, ensuring accessibility and clean markup.

- **CSS3**  
  Used for custom styling, layout, spacing, colour scheme, and responsive design.

- **JavaScript**  
  Used to enhance user experience on dynamic components such as interactive elements and client-side behaviour.

- **Python**  
  Core backend language used to power the Django framework, handle form processing, and manage application logic.

- **SQL**  
  Underlying language used by PostgreSQL for relational data storage and database queries.

---

### Libraries and Frameworks

- **Django**  
  Provides the backend architecture, ORM, templating engine, form handling, authentication, and URL routing.

- **Bootstrap 5**  
  Front-end framework used for responsive layout, grid system, utility classes, and accessible UI components.

- **Django Crispy Forms**  
  Used to improve form layout and styling while maintaining consistency across the application.

- **Cloudinary**  
  Used in production for secure and scalable media storage of uploaded recipe images.

- **Gunicorn**  
  WSGI HTTP server used to run the Django application in a production environment.

---

### Database

- **SQLite**  
  Used during local development for simplicity and rapid testing.

- **PostgreSQL**  
  Used in production as a robust relational database management system.

---

### Deployment and Hosting

- **Heroku**  
  Cloud platform used to deploy and host the live application.

- **Heroku Postgres**  
  Managed PostgreSQL database add-on used in production.

---

### Tools and Services

- **Git**  
  Used for version control throughout development.

- **GitHub**  
  Used to host the project repository and manage version control.

- **VS Code**  
  Primary development environment used for writing and managing code.

- **Google Lighthouse**  
  Used to test performance, accessibility, best practices, and SEO on the deployed site.

---
## Testing

Testing was carried out throughout the development of the Global Recipe application to ensure functionality, usability, accessibility, and security. A combination of **manual testing** and **code validation tools** was used to verify that all features work as expected and meet project requirements.

### Manual Testing

All core user journeys were tested manually to ensure correct behaviour under normal use and edge cases.

#### User Authentication

| Test Case | Action | Expected Result | Outcome |
|----------|--------|----------------|---------|
| Register account | Submit valid registration form | Account created and user redirected | Pass |
| Register account | Submit invalid data | Error message displayed | Pass |
| Login | Enter valid credentials | User logged in successfully | Pass |
| Login | Enter invalid credentials | Error message displayed | Pass |
| Logout | Click logout | User logged out and redirected | Pass |

---

#### Recipe Management (CRUD)

| Test Case | Action | Expected Result | Outcome |
|----------|--------|----------------|---------|
| View recipes | Visit recipe list | Recipes displayed correctly | Pass |
| Search recipes | Search by keyword | Relevant results returned | Pass |
| Add recipe | Submit valid form | Recipe saved and displayed | Pass |
| Add recipe | Submit incomplete form | Validation errors shown | Pass |
| Edit recipe | Update owned recipe | Changes saved | Pass |
| Edit recipe | Attempt to edit another user’s recipe | Access denied | Pass |
| Delete recipe | Confirm deletion | Recipe removed | Pass |
| Delete recipe | Cancel deletion | Recipe retained | Pass |

---

#### Navigation and Layout

| Test Case | Action | Expected Result | Outcome |
|----------|--------|----------------|---------|
| Navigation links | Click menu items | Correct page loaded | Pass |
| Responsive layout | Resize browser window | Layout adapts correctly | Pass |
| Mobile view | Load site on small screen | Content remains usable | Pass |

---

### Code Validation

The following validation tools were used to ensure code quality:

- **HTML Validation**  
  All templates were checked using the W3C Markup Validation Service. Django template warnings were noted but are expected.

- **CSS Validation**  
  Custom CSS was validated using the W3C CSS Validator with no major errors.

- **Python Validation**  
  Code was checked using `flake8`. Minor warnings were addressed where applicable.

---

### Accessibility Testing

Accessibility testing was performed manually and using automated tools:

- Semantic HTML used throughout the application.
- All forms include descriptive labels.
- Buttons and links are clearly distinguishable.
- Colour contrast checked for readability.
- Keyboard navigation tested on forms and links.


### Browser and Device Testing

The application was tested on the following platforms:

- **Browsers:** Chrome   
- **Devices:** Mobile, Tablet, Desktop  

The site remained responsive and functional across all tested environments.

---

### Bugs Fixed

| Issue | Cause | Resolution |
|-----|------|-----------|
| Images not displaying in production | Media storage misconfiguration | Implemented Cloudinary |
| Duplicate recipe slugs | Similar recipe titles | Added unique slug generation |
| Unauthorized edit access | Missing permission checks | Restricted access to recipe owners |
| Mobile layout issues | Bootstrap grid spacing | Adjusted layout classes |

---

### Known Issues

- No critical bugs identified at the time of submission.
- Automated unit tests are limited and could be expanded in future iterations.

---



## Version Control

Git was used for version control throughout development.
The project repository is hosted on GitHub and includes regular commits documenting feature development, bug fixes, and refactoring.

---



## Deployment

The Global Recipe application was deployed using **Heroku**. The deployment process ensured that the application runs in a secure, production-ready environment with sensitive data protected using environment variables.

---

### Heroku Deployment

The following steps were taken to deploy the project to Heroku:

1. Create a new Heroku application.
2. Navigate to **Settings** and open **Config Vars**.
3. Add the following environment variables:
   - `SECRET_KEY`
   - `DATABASE_URL` (automatically added when Heroku Postgres is attached)
   - `CLOUDINARY_URL` (for media storage in production)
4. Attach **Heroku Postgres** as the production database.
5. Ensure the project includes the following required files:
   - `requirements.txt`
   - `Procfile`
6. Update Django settings:
   - Set `DEBUG = False`
   - Add the Heroku app URL to `ALLOWED_HOSTS`
7. Commit changes and push the project to GitHub.
8. Connect the GitHub repository to Heroku via the **Deploy** tab or deploy using the Heroku CLI.
9. Run database migrations:
   ```bash
   heroku run python manage.py migrate


 ### Forking the Repository

To fork this repository and create your own copy:

1. Navigate to the Global Recipe repository on GitHub.
2. Click the **Fork** button located in the top-right corner of the page.
3. Select your GitHub account when prompted.
4. A copy of the repository will be created in your GitHub account.

Forking allows you to make changes to the project without affecting the original repository.
 
### Creating a Clone

To create a local clone of the Global Recipe repository:

1. Navigate to the Global Recipe repository on GitHub.
2. Click the **Code** button and copy the HTTPS repository URL.
3. Open your local terminal or command prompt.
4. Navigate to the directory where you want the project to be stored.
5. Run the following command:
   ```bash
   git clone <repository-url>


##  Performance & Accessibility

The live application was tested using **Google Lighthouse** on the deployed site.

### Lighthouse Results:
- **Performance:** 100
- **Accessibility:** 89
- **Best Practices:** 74
- **SEO:** 91

These results demonstrate strong performance optimisation, good accessibility practices, and effective SEO implementation.

## Security & Environment Variables

All sensitive data is stored securely using environment variables and is not committed to GitHub.

Environment variables used:
- `SECRET_KEY`
- `DATABASE_URL` (production)
- `CLOUDINARY_URL`

A local `.env` file is used during development and is included in `.gitignore`.
On deployment, these are set using the hosting platform Config Vars  Heroku.

## Credits

### Code and Libraries
- **Django Documentation**  
  https://docs.djangoproject.com/  
  Used as the primary reference for models, views, authentication, and ORM usage.

- **Bootstrap Documentation**  
  https://getbootstrap.com/  
  Used for responsive layout, grid system, and UI components.

- **Cloudinary Documentation**  
  https://cloudinary.com/documentation  
  Referenced for media storage and image handling in production.

---

### Media
- Recipe images were uploaded by users or sourced from royalty-free image providers for demonstration purposes.
- No copyrighted images are used without permission.

---

### Tools and Resources
- **GitHub** for repository hosting and version control.
- **Heroku** for application deployment.
- **Google Lighthouse** for performance and accessibility testing.
- **Visual Studio Code** as the primary development environment.

---

All code, models, views, templates, and styling were written by the project author unless otherwise stated.
