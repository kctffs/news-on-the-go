## Disclaimer

..


# News On The Go.

News On The Go is a news website that offers a fast reading ability for all the latest articles that have been published. News On The Go offers clear visibility towards the variety of articles on your screen for you to be able to choose at your will.

News On The Go has a target of reaching all audiences interested in quick time news whether that be mobile, desktop, or tablet. Having the easy-to-read layout it offers entertainment for those who wish to scroll through quickly or others who want to take their time and indulge in articles.

## Features.

- ## First Instance.
  - When first looking at the website, it gives you immediate confirmation on the purpose it has. With the abrupt articles on your screen, clear organisability and colouring to match, **News On The Go** invites every reader for easy home screen navigation.
  - At the top of the page, the header is shown which displays the **News On The Go** title with a **Home** navigation button beside. (This button to be shown on all pages would of course revert the user back to the initial home screen). To The far right of the header is equipped with a slogan that reads **INFUSE with some quick NEWS** to provide a catchy read that is also the premise of the website (not to mention the viewer would glance at this slogan when visiting the site).
  - Colouring chose for the website ensures a clear reading as it pairs with the structured layout to provide comfortable viewing for the viewer when accessing the page.
 
- ## Django Administration.
  - First of all, to access this setting you have to append `/admin` at the end of the URL address, which will then provide you with a log in screen (log in credentials are at the bottom of this topic)
    - <img width="479" alt="Ammend admin" src="https://github.com/user-attachments/assets/bc9bfef6-c62c-40a6-ad4b-b6f2e0725378">
  - Django administration panel was used in this project for superusers to be able to edit articles, create various users, make comments and manage posts.
  - Throughout the administration panel, it provides countless ways to manage the website which ensures a superuser to have full control over content on the site or provided.
  - A secruity password reset is available when logged in as a user or admin with multiple requirements in place for extra protection, so you will have to think carefully when choosing.
    - <img width="884" alt="Password change" src="https://github.com/user-attachments/assets/21c12da5-6947-4bcc-8707-80cb492705f6">

  - Django superuser credentials are here as provided: `Username: NewsOnTheGoAdmin` `Password: qwertyuiop` (if email is needed, it is `NewsOnTheGoAdmin@PP4.com`).
 
- ## Entity Relationship Diagrams.
  - For the models created in this project, I planned them in advance by creating two diagrams to showcase how the models will work in comparison to the code.
  - For the `Uploads` model, this is the created diagram:
    - <img width="730" alt="Uploads ERD" src="https://github.com/user-attachments/assets/d8c5aec1-4a12-4863-860f-d411b8c41c7e">
  - For the `Commenting` model, this is the created diagram:
    - <img width="710" alt="Commenting ERD" src="https://github.com/user-attachments/assets/c9c62f96-8460-44fb-9bc5-601a19ceb5b8">



## Testing.

## Credits.

- ## Content.
  - The idea to make a news style project was from the assessment guide and the django learning module that was provided.
  - Research into news websites was all first hand research by searching and interacting with big news sites such as;
    - [Reddit](https://www.reddit.com/) , [Sky News](https://news.sky.com/uk) and [BBC News](https://www.bbc.co.uk/news).
  - Minor filler articles where provided from the [walkthrough project](https://github.com/Code-Institute-Solutions/blog/blob/main/07_Rich_text_reload/03_adding_more_posts/blog/fixtures/posts.json) to extend the depth of articles on the website for a more professional feel.
  - For deployment within this project, [Heroku](https://heroku.com) was the method used.

- ### Code.
  - The code in this project was inspired by the walkthrough project of the **I Think Therefore I Blog** project with all the Django being taught was learned from there.
  - Snippets of code throughout the project are also inspired from this project as it was needed to either install, import, or create paths throughout the various apps in the project.
  - Finally, the models in my project are inspired by the walkthrough project however, I have altered them to become unique and fit my own project.
