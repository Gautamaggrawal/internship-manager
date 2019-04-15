# internship-manager
Rules:
1. You have to use the Django framework for the given project.
2. You can not ask anyone else to complete the project on your behalf.
3. You must be able to explain your code in the post-competition interview.
4. You can use third-party open source plugins for Django only if it is needed.
5. You have to host the code on Heroku. We will review the live website before code.
6. It is preferred to use GitHub platform to keep track of your code and link Heroku to GitHub.
7. It is preferred to use Django Rest API to have JSON API endpoints along with the regular website.
8. It is preferred to follow standard coding practices and commenting on each function/class/procedure.
9. It is not necessary to implement all features you are asked for. Try to accomplish few features properly within time.
10. Simplicity, both in the website as well as in code will be considered. It is okay to not implement a feature if it makes things complex.

Task (Project: Infroid Internship Portal)

Start Time: As soon as you join the Slack channel.
End Time: 13th April, 2019 11:59 PM

Ways to make final submission:

1. Send an email to internship@infroid.in
    Subject        : <FULL NAME> Django Internship Competition April 2019
    Body        : <Link 1 to Heroku Hosted Website>
            : <superuser ID> - <superuser password>
            : <Internship Admin ID> - <Internship Admin Password>
            : <Intern ID> - <Intern Password>
            : <Link 2 to GitHub Hosted Code>

OR

2. Send an email to internship@infroid.in
    Subject        : <FULL NAME> Django Internship Competition April 2019
    Body        : <Link 1 to Heroku Hosted Website>
            : <superuser ID> - <superuser password>
            : <Internship Admin ID> - <Internship Admin Password>
            : <Intern ID> - <Intern Password>
    Attachment    : Zipped Code file with filename <FULL NAME> Django April 2019

Overview:
You need to build a web application for Infroid to manage all its interns.
The Infroid Admins should be able to use the web app from their mobile devices as well as from thier laptops.

Features/Specifications of Project:
1. There must be exactly one superuser (Infroid Internship Manager) which could be created explicitly by the developer only.
2. There must be multiple Internship Admins which could be created/updated/deleted by the superuser (Infroid Internship Manager).
3. There must be multiple Interns which could be created/updated/deleted by any of the Internship Admins (but not by superuser).
4. Every Login/Logout/Create/Update/Delete activity done on website must be logged and logs should be accessible/downloadable by superuser.
5. Each Intern will only have one profile page with several details and options to add/change some of his/her details:
    - Full Name (view only)
    - Email ID (view only)
    - Phone Number (view and edit)
    - Profile Picture (view and edit)
    - Document/File: Signed Offer Letter (view and edit)
    - Stipend (view only)
    - Date of Joining (view only)
    - Date of Leaving (view only)
    - Internship Admin's Remark (view only)
    - Status (view only)
6. Every Internship Admin will be able to see list of all Interns (10 Interns loaded as we click on load more)
    sorted by their reverse joining date along with a dynamic search to find Intern by Name and email.
7. Every Internship Admin will be able to change the following details for the Interns:
    - Full Name
    - Email ID
    - Stipend
    - Date of Joining
    - Date of Leaving
    - Internship Admin's Remark
    - Status
8. Status field in Intern's profile is a choice field (with values either "Active" or "Inactive") set to "Active" manually by Internship Admin. However, it should not change to Active until following fields are filled:
    - Full Name
    - Email ID
    - Stipend
    - Date of Joining
    - Date of Leaving
9. As soon as the Date of Leaving is past, the Intern's profile must be automatically set to "Inactive".
10. Every Internship Admin will be able to see a Stipend Release Page, which will give a summary of all "Active" users for which payment is due for the month.
