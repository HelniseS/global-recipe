#  Global Recipe

A full-stack Django web app where users can browse, create, edit, and delete recipes. Designed for accessibility, responsive UX, and clean data management.

---

## Contents
- [User Goals](#user-goals)
- [User Stories](#user-stories)
- [Website Goals and Objectives](#website-goals-and-objectives)
- [Wireframes](#wireframes)
- [Design Choices](#design-choices)
  - [Typography](#typography)
  - [Colour Scheme](#colour-scheme)
  - [Media](#media)
  - [Responsiveness](#responsiveness)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Enhancements](#future-enhancements)
- [Data Model](#data-model)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Libraries & Framework](#libraries--framework)
  - [Tools](#tools)
- [Testing](#testing)
  - [Code Validation](#code-validation)
  - [Feature Testing](#feature-testing)
  - [Accessibility Testing](#accessibility-testing)
  - [Bugs Fixed](#bugs-fixed)
- [Deployment](#deployment)
  - [To deploy the project](#to-deploy-the-project)
  - [To fork the project](#to-fork-the-project)
  - [To clone the project](#to-clone-the-project)
- [Security & Environment Variables](#security--environment-variables)
- [Credits](#credits)

---

## User Goals
- Quickly discover recipes by name, tags, or ingredients.
- View clear ingredient lists and step-by-step instructions.
- Submit personal recipes with images.
- Edit or delete recipes they own.
- Save time with a clean, mobile-first interface.

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
- Provide a reliable CRUD interface backed by a relational database.
- Meet accessibility guidelines (semantic HTML, ARIA where appropriate, colour contrast).
- Use clean project structure, version control, and professional documentation.
- Deploy to a cloud platform with DEBUG off and secrets protected.

---

## Wireframes

---

## Design Choices

### Typography
- Headings: **Inter** (or Bootstrap default system UI stack).  
- Body: **System UI** for performance and readability.

### Colour Scheme
- Primary: `#198754` (Bootstrap “success” tone)  
- Secondary: `#0d6efd`  
- Background: `#ffffff`  
- Text: `#212529` 

### Media
- Recipe images uploaded by users. Images are validated for type/size and stored in `/media/recipes/`.

### Responsiveness
- Built with Bootstrap’s grid/utilities.  
- All pages tested at common breakpoints: 320px, 768px, 1024px, 1440px.

---

## Features

### Existing Features
- Home page with recent recipes and call-to-actions.
- Recipes list with pagination and basic search (title/tags).
- Recipe detail page with ingredients, steps, cooking time, and image.
- Authenticated users can **create**, **update**, and **delete** their own recipes.
- Django Admin configured with inlines for quick ingredient/step entry.
- Flash messages for user feedback (create/update/delete success).
- 404/500 user-friendly error pages (optional).

### Future Enhancements
- User favourites / ratings.
- Advanced filters (cuisine, dietary requirements).
- Image optimization (thumbnails).
- Comments and moderation workflow.
- API endpoints for mobile consumption.

---

## Data Model
The core entities are **Recipe**, **Ingredient**, and **Step** with `User` as author.

- **Recipe**
  - `title`, `description`, `image`, `author(FK User)`, `tags`, `cooking_time`, `created_at`
- **Ingredient**
  - `recipe(FK)`, `name`, `quantity`
- **Step**
  - `recipe(FK)`, `order`, `instruction` (ordered by `order`)


