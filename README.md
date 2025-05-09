# Email Filter — Smarter Job-Related Inbox Triage

Job hunting often floods your inbox with a mix of useful and irrelevant emails — from interview invitations to automated application confirmations and outright spam. This project is a custom email classifier designed to help organize and filter those messages efficiently.

## Project Overview

This tool uses machine learning to classify incoming emails into the following categories:

- **Interview Bookings**  
- **Job Offers**  
- **Automated Noreplies** (e.g., “Thank you for applying”)  
- **Spam or Irrelevant Emails**

The goal is to bring focus to the emails that truly matter, especially when actively applying for roles, by building a personalized email filtering system.

## Why I Built This

While applying for jobs, I noticed my inbox was overwhelmed with unnecessary clutter — making it harder to spot real opportunities. I built this project to streamline the process and regain control over my inbox during the job search.

## To-do

- [x] Read csv and json datasets;
- [ ] Web dashboard to view and triage filtered emails;
- [ ] Sklearn/lazypredict models to predict labels;
- [ ] Pytorch neural networks to predict labels;
- [ ] (Opt.) Improved accuracy with NLP and transformer models;
- [ ] (Opt.) Integration with Gmail API;