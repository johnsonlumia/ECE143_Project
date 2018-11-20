# ECE 143 Project Proposal
## Group 6 Team Members
- Renjie Zhu
- Fernando Lopez Garcia
- Daoyu Li
- Ambareesh Sreekumaran Nair Jayakumari

## Problem
Analysing course offerings in engineering departments of top universities in the United States related to industry demands.

## Summary
The Electronics and Computer Software industry has been evolving vastly for the past twenty years or so. As a result, both students and the concerned departments need to keep up with the ever evolving and demanding industry changes. Therefore, we want to study the relationship between industry needs and university course offerings, to understand what choices a student should make to best fit himself (or herself) in the dynamic industry.

Our project aims to identify the relevant skills focused on by different universities that can be identified from the course offerings. Then we will compare the course offerings with the industries' demands from different dimensions including job descriptions and role requirements.

## Dataset
*Primary:*
- Course catalogs over the last 20 years from top 12 Universities. We will be scrapping for ECE, CSE and MAE Departments. Universities include: UCSD, UC Berkeley, UCLA, MIT, and so on.
- Current industry job requirements from 12 leading companies in various domains, such as Qualcomm, Amazon, Google, Apple and so on.

*Secondary:*
- Industry data from the yearly financial reports of the same companies.

## Applications
1. Identifying the most common skills that have been promoted by departments from different universities, which will serve as the basis of our project.
2. Analyzing how the course offerings of a department at UCSD have changed over time and observing the degree of change.
3. Ascertaining if changes in course curriculum of departments reflect the state of the industries that they are concerned with. We can discuss the relation between departments and the corresponding industries.
4. Analyzing how the offerings have changed for the same department across different universities.
5. Observing the extent of overlap between two departments of a university in terms of skills for domains (for e.g. Machine Learning)
6. Identifying how the present job requirements from different companies map to the course offerings.

## Milestones
| Steps                    | Time Frame       | Division                     |
| ------------------------ |:----------------:| :---------------------------:|
| Data Collection          | ~1 week (11/05)  | Four universities per member |
| Data Analysis            | ~2 weeks (11/19) | Applications 1,6 will be worked upon together; the rest will be split across four members  |
| Data Visualization       | ~1 week (11/26)  |  Similar to Analysis         |
| Results and Presentation | ~1 week (12/03)  |                              | 

## File Structure

```
Root
|
+---- raw_data
|
+---- industry_data
|
+---- scripts
|        |   __init__.py
|        |   process_data.py
|        |   word_freq.py
|        |   SQLite.py
|        |   common_words.txt
|
|   main.py
|   database.db 
```