## Disclaimer

..


# News On The Go.

News On The Go is a news website that offers a fast reading ability for all the latest articles that have been published. News On The Go offers clear visibility towards the variety of articles on your screen for you to be able to choose at your will.

News On The Go has a target of reaching all audiences interested in quick time news whether that be mobile, desktop, or tablet. Having the easy-to-read layout it offers entertainment for those who wish to scroll through quickly or others who want to take their time and indulge in articles.

## Features.

- ### First Instance.
  - When first looking at the website, it gives you immediate confirmation on the purpose it has. With the abrupt articles on your screen, clear organisability and colouring to match, **News On The Go** invites every reader for easy home screen navigation.
  - At the top of the page, the header is shown which displays the **News On The Go** title with a **Home** navigation button beside. (This button to be shown on all pages would of course revert the user back to the initial home screen). To The far right of the header is equipped with a slogan that reads **INFUSE with some quick NEWS** to provide a catchy read that is also the premise of the website (not to mention the viewer would glance at this slogan when visiting the site).
    - <img width="1428" alt="NOTG header" src="https://github.com/user-attachments/assets/74df56b6-ff3b-48c6-9221-bd60bb137559">
  - Colouring chose for the website ensures a clear reading as it pairs with the structured layout to provide comfortable viewing for the viewer when accessing the page.
 
- ### Django Administration.
  - First of all, to access this setting you have to append `/admin` at the end of the URL address, which will then provide you with a log in screen (log in credentials are at the bottom of this topic)
    - <img width="479" alt="Ammend admin" src="https://github.com/user-attachments/assets/bc9bfef6-c62c-40a6-ad4b-b6f2e0725378">
  - Django administration panel was used in this project for superusers to be able to edit articles, create various users, make comments and manage posts.
  - Welcoming into the administration panel, there is a navigation bar that firstly greets the admin, confirming the identity allows the admin to view the website as a normal user, change password or log out.
    - <img width="418" alt="Django welcome" src="https://github.com/user-attachments/assets/f4c1ec08-0702-4f0b-a6fb-d7e678c24e6f">
  - Throughout the administration panel, it provides countless ways to manage the website which ensures a superuser to have full control over content on the site or provided.
  - A security password reset is available when logged in as a user or admin with multiple requirements in place for extra protection, so you will have to think carefully when choosing.
    - <img width="884" alt="Password change" src="https://github.com/user-attachments/assets/21c12da5-6947-4bcc-8707-80cb492705f6">
  - There is a system in place to add a user when in the administration panel. This would offer multiple benefits as admin to be able to further control content being placed on the site and managing account access. With this feature you have the required restrictions to follow of 150 characters and symbols etc. It also comes in place with password restrictions which will refuse a password that is common, close to your username or details.
    - <img width="666" alt="Add user" src="https://github.com/user-attachments/assets/ceedb034-5946-4697-b1ea-0dce353e41a2">
  - User management is urgent when controlling a site as an admin therefore, News On The Go has a detailed process in place that makes easy power to control users. First of all there is a filtration system where you can specify to your needs the users you want to manage. There is options to delete users on command by selecting (can also be multiple at once) where it takes you to a confirmation screen showing your their interactions on the website whether that be posting on articles or writing them.
    - <img width="181" alt="User filtration" src="https://github.com/user-attachments/assets/139dbbda-36e5-4748-a866-de8689ad7cbc"> <img width="677" alt="User management" src="https://github.com/user-attachments/assets/d5cf4108-eb8f-49d3-911f-9e301bee7e66"> <img width="1158" alt="Deleting user" src="https://github.com/user-attachments/assets/1bb85f24-df18-4f9f-a6dd-87b1443a1821">
  - An ability to see comments as admin is crucial and for News On The Go, it's no different. There is a viewing of all comments placed on the website no matter the article posted on with full access to delve deeper into that if needed.
    - <img width="555" alt="Commenting" src="https://github.com/user-attachments/assets/43e9d3f0-7ee9-46dc-b7f6-f90a29c86716">
  - Adding comments is also in place from the panel as a superuser as they're also involved with the articles. Commenting from the admin panel gives you the simplest layout where choosing what post and what account you want to be able to converse with.
    - <img width="848" alt="Add comments" src="https://github.com/user-attachments/assets/f98f3293-7a6c-4773-ac16-c8e02518a358">
  - As an admin, you can also view the actions that you haven been involved in as you can revisit your queries.
    - <img width="512" alt="Admin actions" src="https://github.com/user-attachments/assets/7d7b2e2d-90c1-42f9-9012-058085d1aab7">
  - Django superuser credentials are here as provided: `Username: NewsOnTheGoAdmin` `Password: qwertyuiop` (if email is needed, it is `NewsOnTheGoAdmin@PP4.com`).
 
- ### Entity Relationship Diagrams.
  - For the models created in this project, I planned them in advance by creating two diagrams to showcase how the models will work in comparison to the code.
  - For the `Uploads` model, this is the created diagram:
    - <img width="730" alt="Uploads ERD" src="https://github.com/user-attachments/assets/d8c5aec1-4a12-4863-860f-d411b8c41c7e">
  - For the `Commenting` model, this is the created diagram:
    - <img width="710" alt="Commenting ERD" src="https://github.com/user-attachments/assets/c9c62f96-8460-44fb-9bc5-601a19ceb5b8">

- ### Projects.
  - Creating a project board full of user stories so the outlook of this project has critical criteria needed to achieve the final steps to make the website professional.
    - <img width="1279" alt="User story" src="https://github.com/user-attachments/assets/273b1d00-414e-4a7a-b9c6-c8dec2c3c81a">
  - Throughout the project, revisiting this page helped ensure the website was on the right track as it became routine to check and re-read the criteria needed for each segment listed in the to-do list.
  - Each user story followed the same structure as a template was created for this project which followed the regime of:
     As a **role** I can **capability** so that **received benefit**
      - Acceptance criteria 1
      - Acceptance criteria 2
      - Acceptance criteria 3
    

## Testing.

## Credits.

- ### Content.
  - The idea to make a news style project was from the assessment guide and the django learning module that was provided.
  - Research into news websites was all first hand research by searching and interacting with big news sites such as;
    - [Reddit](https://www.reddit.com/) , [Sky News](https://news.sky.com/uk) and [BBC News](https://www.bbc.co.uk/news).
  - Minor filler articles where provided from the [walkthrough project](https://github.com/Code-Institute-Solutions/blog/blob/main/07_Rich_text_reload/03_adding_more_posts/blog/fixtures/posts.json) to extend the depth of articles on the website for a more professional feel.
  - For deployment within this project, [Heroku](https://heroku.com) was the method used.

- ### Code.
  - The code in this project was inspired by the walkthrough project of the **I Think Therefore I Blog** project with all the Django being taught was learned from there.
  - Snippets of code throughout the project are also inspired from this project as it was needed to either install, import, or create paths throughout the various apps in the project.
  - Finally, the models in my project are inspired by the walkthrough project however, I have altered them to become unique and fit my own project.
