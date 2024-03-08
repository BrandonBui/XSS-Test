# Goal
The goal of this project is to aid and automate the discovery of cross-site scripting (XSS) vulnerabilities on a website.

# Project Plan
### Phase 1: Creation of Initial Web Crawler - Current Phase
The plan is to create the web crawling functionality from scratch to ensure that the web crawler meets the exact needs and functionalites required. While I am aware that web scrapy frameworks like Scrapy exist, it both provides unecesssary functionality and is too limited. Even though it is a framework and allows the developer to extend/modify the existing code, in the time and effort it will take to understand how scrapy is implemented/works, I can implement my own web crawler that meets my exact needs and specifications.  
  
Tech Stack:
- Playwright: Headless browser functionality to ensure loading of JS heavy websites, as well as providing functionality to perform user actions/workflows (ie logging in)
- Python

### Phase 2: Collection of URL Parameters
The easiest place to begin looking for XSS vulnerabilities is URL request parameters. Often times, these parameters are reflected somewehre in the response HTML, allowing them to be exploited through XSS. For example, search queries that display what you searched for.  
  
### Phase 3: Intelligent Payload Generation
This is anticipated to be one of the most difficult aspects of the project. There is no standard way for parameters to be reflected back onto the HTML. The reflection could appear in various different HTML elements, different attributes within elements, or even as text on the page itself. Somehow automating the process of analyzing the surrounding HTML to then craft a payload that both follows the rules of the input and the rules of HTML to create a valid injection will be a vital step in this project.  
  
### Phase 4: Automated Vulnerability Testing
Involves making requests using the parameters collected in Phase 2 of the project and the payloads in Phase 3 of the project, to test if the parameter is vulnerable.

*DISCLAIMER: This project/tool is not intended to be used for malicious, illegal, or non-ethical purposes. I am not responsible for the impacts from the use of this tool, both to the user and what the tool is used on.*
