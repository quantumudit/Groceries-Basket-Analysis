# ![Project Logo][project_logo]

---

<h4 align="center"> Transforming Groceries Transactions Data and Performing Market Basket Analysis using <a href="https://www.python.org/" target="_blank">Python</a> and <a href="https://en.wikipedia.org/wiki/Microsoft_Power_BI" target="_blank">Power BI</a></h4>

<p align='center'>
<img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="built-with-love" border="0">
<img src="https://forthebadge.com/images/badges/powered-by-coffee.svg" alt="powered-by-coffee" border="0">
<img src="https://forthebadge.com/images/badges/cc-nc-sa.svg" alt="cc-nc-sa" border="0">
</p>


<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#demo">Demo</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
</p>

## Overview

This project is focused on conducting a comprehensive market basket analysis using both Power BI and Python. The primary objective is to uncover associations between various grocery products, empowering end-users to make data-driven decisions.

**Power BI:** An interactive report is developed in Power BI, enabling users to explore relationships between different products dynamically. This interactive approach provides valuable insights that can guide decision-making processes related to inventory management, marketing strategies, and product placement.

**Python:** In parallel, the project utilizes Python to perform the market basket analysis, generating a static report that highlights key insights. This report complements the interactive Power BI dashboard by offering a detailed analysis that captures the essence of customer purchasing patterns.

The process involves transforming raw transaction data into a refined dataset using Python, which is then seamlessly integrated into both the Python for analysis and Power BI report. This ensures that the analysis is built on clean, structured data, allowing for accurate and meaningful results.

The project repository exhibits the following structure:

```
Groceries-Basket-Analysis/
├── 📁.github
├── 📁conf
├── 📁data/
│   ├── 📁external
│   ├── 📁processed
├── 📁notebooks
├── 📁src/
│   ├── 📁components
│   ├── 📁pipelines
│   ├── 📁utils
│   ├── 🐍constants.py
│   ├── 🐍exception.py
│   └── 🐍logger.py
├── 📁logs
├── 📁reports
├── 📁resources
├── 🐍main.py
├── 🐍template.py
├── 🔒poetry.lock
├── 📇pyproject.toml
├── 🗒️requirements.txt
├── 📜.gitignore
├── 🔑LICENSE
└── 📝README.md
```
<details>
<summary>
   <strong>💡 Repository Structure Details</strong>
</summary>
<br>

To help you navigate through the project, here’s a concise guide to the repository’s structure, detailing what each directory contains and its purpose within the project:

- **`📁.github`** - Contains GitHub-related configuration files like workflows for CI/CD.
- **`📁conf`** - Configuration files and schema for the project.
- **`📁data/`**
  - **`📁external`** - Data extracted from external data source(s).
  - **`📁processed`** - Data that has been cleaned and transformed for analysis.
- **`📁notebooks`** - Jupyter notebooks for exploratory data analysis and model experimentation.
- **`📁src/`**
  - **`📁components`** - Modular components used across the project.
  - **`📁pipelines`** - Data processing and machine learning pipelines.
  - **`📁utils`** - Utility scripts for common tasks throughout the project.
  - **`🐍constants.py`** - Central file for constants used in the project.
  - **`🐍exception.py`** - Custom exception classes for error handling.
  - **`🐍logger.py`** - Logging configuration and setup.
- **`📁logs`** - Contains auto-generated logs for event and error tracking, not included in Git.
- **`📁reports`** - Generated analysis reports and insights.
- **`📁resources`** - Additional resources like images or documents used in the project
- **`🐍main.py`** - Script to orchestrates the project's workflow. It sequentially executes the pipeline scripts
- **`🐍template.py`** - Template script for standardizing code structure.
- **`🔒poetry.lock`** - Lock file for Poetry to ensure reproducible builds.
- **`📇pyproject.toml`** - Poetry configuration file for package management.
- **`🗒️requirements.txt`** - List of Python package requirements.
- **`📜.gitignore`** - Specifies intentionally untracked files to ignore.
- **`🔑LICENSE`** - The license file for the project.
- **`📝README.md`** - The introductory documentation for the project.

</details>

## Prerequisites

### Tech Stack Prerequisites
![Python] ![Numpy] ![Pandas] ![Matplotlib] ![PowerBI]

To effectively engage with this project, possessing a robust understanding of the skills listed below is advisable:

- Core comprehension of Python, and Modular programming
- Acquaintance with data modelling, DAX and Power BI
- Acquaintance with the Python libraries specified in the 🗒️[requirements.txt][requirements] document

These competencies will facilitate a seamless and productive journey throughout the project.

### Development Environment Prerequisites
![Anaconda] ![Poetry] ![VS_code] ![Jupyter_Notebook] ![PowerBI] ![Notepad_plus_plus] ![Obsidian] ![Figma] ![Clickup]

Application selection and setup may vary based on individual preferences and system setups.

The development tools I've employed for this project are:
- **Anaconda** / **Poetry**: Utilized for distribution and managing packages
- **VS Code**: Employed for writing and editing code
- **Jupyter Notebook**: Used for data analysis and experimentation
- **Power BI Desktop**: Used for data modeling and visualization
- **Notepad++**: Served as an auxiliary code editor
- **Obsidian**: Utilized for documenting project notes
- **Figma**: Used for crafting application UI/UX designs
- **Click Up**: Employed for overseeing project tasks

### Automation Integration Necessities
![GitHubActions]

Integrating process automation is entirely elective, as is the choice of the automation tool.

In this project, **GitHub Actions** has been selected to automate the data transformation process as needed.

Should there be a need to adjust data-related settings, simply update the YAML configurations, and the entire development workflow can be executed directly from the repository.


## Architecture

The architectural design of this project is transparent and can be readily comprehended with the assistance of the accompanying diagram illustrated below:

![Process Architecture][process_workflow]

The project's architectural framework encompasses the following key steps:

### Data Transformation
The raw data is transformed through a series of cleaning and preparation steps to make it suitable for analysis. This involves conducting experiments in notebooks, which help in developing the script that performs all necessary steps to process and restructure the dataset. These transformations are designed to align the data with the analytical goals, ensuring that it is ready for accurate analysis and visualization.

### Process Automation
The data transformation steps are automated using GitHub Actions. This automation allows the process to be executed seamlessly and consistently without manual intervention. The setup ensures that data extraction and preparation can be performed on-demand, enhancing efficiency and scalability.

### Data Analysis & Visualization
In this phase, the transformed dataset is analyzed to extract meaningful insights and answer specific user queries. 

Various analytical techniques are employed to interpret the data, and findings are presented through interactive visualizations using Power BI. 

The dashboard provides users with a clear and engaging way to explore data insights and make informed decisions based on the analysis.


## Demo

The following illustration demonstrates the interactive Power BI report to explore insights from the data:

<p align='center'>
  <a href="https://app.powerbi.com/view?r=eyJrIjoiMWFlNGE1ZDAtNjg2YS00NTNkLTkwMjgtNzg5OGFkNWIxYWQ1IiwidCI6IjI5MmY4YmYxLTg2NzQtNGM0Ny05Yzk1LWMwNDYzZGQxMGRlNCJ9&embedImagePlaceholder=true&pageName=b67e3f421da06b0c0027">
    <img src="./resources/readme_images/powerbi_report.png" alt="Power BI Report" style="0">
  </a>
</p>

> Access the Power BI report by clicking here: **[Power BI Report][powerbi_link]**


## Support

Should you wish to inquire, offer feedback, or propose ideas, don’t hesitate to contact me via the channels listed below:

[![Linkedin Badge][linkedinbadge]][linkedin] [![Twitter Badge][twitterbadge]][twitter] [![Gmail Badge][gmailbadge]][gmail]

Discover and engage with my content on these platforms:

[![Linktree Badge][linktreebadge]][linktree] [![Youtube Badge][youtubebadge]][youtube] [![GitHub Badge][githubbadge]][github] [![Medium Badge][mediumbadge]][medium]  [![Substack Badge][substackbadge]][substack] 

To express your support for my work, consider [buying me a coffee][buymeacoffee] or, [donate through Paypal][paypal]

[![Buy Me a Coffee][buymeacoffeebadge]][buymeacoffee] [![Paypal][paypalbadge]][paypal]

## License

<a href = 'https://creativecommons.org/licenses/by-nc-sa/4.0/' target="_blank">
    <img src="https://i.ibb.co/mvmWGkm/by-nc-sa.png" alt="by-nc-sa" border="0" width="88" height="31">
</a>

This license allows reusers to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution is given to the creator. If you remix, adapt, or build upon the material, you must license the modified material under identical terms.

---
<p align='center'>
  <a href="https://topmate.io/quantumudit">
    <img src="https://github.com/quantumudit/Spend-Estimator/assets/54057814/8e5485b9-4777-487b-9677-9d531cef0169" alt="topmate-udit" style="0">
  </a>
</p>

---

<!-- Image Links -->

[project_logo]: ./resources/readme_images/project_cover_image.png
[process_workflow]: ./resources/readme_images/process_workflow.png

<!-- External Links -->

[powerbi_link]: https://app.powerbi.com/view?r=eyJrIjoiMWFlNGE1ZDAtNjg2YS00NTNkLTkwMjgtNzg5OGFkNWIxYWQ1IiwidCI6IjI5MmY4YmYxLTg2NzQtNGM0Ny05Yzk1LWMwNDYzZGQxMGRlNCJ9&embedImagePlaceholder=true&pageName=b67e3f421da06b0c0027
[requirements]: ./requirements.txt

<!-- Project Specific Links -->

[main]: ./main.py 

<!-- Profile Links -->

[linkedin]: https://www.linkedin.com/in/quantumudit/
[twitter]: https://twitter.com/quantumudit
[medium]: https://medium.com/@quantumudit
[linktree]: https://linktr.ee/quantumudit
[youtube]: https://www.youtube.com/@quantumudit
[github]: https://github.com/quantumudit/
[substack]: https://substack.com/
[gmail]: quantumudit@gmail.com

<!-- Payment Profile Links -->
[buymeacoffee]: https://www.buymeacoffee.com/quantumudit
[paypal]: https://paypal.me/quantumudit


<!-- Shields Profile Links -->

[linkedinbadge]: https://img.shields.io/badge/-quantumudit-0e76a8?style=flat&labelColor=0e76a8&logo=linkedin&logoColor=white
[twitterbadge]: https://img.shields.io/badge/-quantumudit-000000?style=flat&labelColor=000000&logo=x&logoColor=white
[gmailbadge]: https://img.shields.io/badge/quantumudit@gmail.com-D14836?style=flat&logo=gmail&logoColor=white
[mediumbadge]: https://img.shields.io/badge/Medium-02b875?style=for-the-badge&logo=medium&logoColor=white
[linktreebadge]:https://img.shields.io/badge/Linktree-1de9b6?style=for-the-badge&logo=linktree&logoColor=white
[youtubebadge]: https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white
[substackbadge]: https://img.shields.io/badge/Substack-%23006f5c.svg?style=for-the-badge&logo=substack&logoColor=FF6719
[githubbadge]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white

<!-- Shields Payment Links -->

[buymeacoffeebadge]: https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black
[paypalbadge]: https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white

<!-- Shields Tech stack Links -->

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Jupyter_Notebook]: https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white
[VS_code]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[Figma]: https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white
[PowerBI]: https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black
[Obsidian]: https://img.shields.io/badge/Obsidian-%23483699.svg?style=for-the-badge&logo=obsidian&logoColor=white
[NumPy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Poetry]: https://img.shields.io/badge/-Poetry-60A5FA?style=for-the-badge&labelColor=60A5FA&logo=poetry&logoColor=white
[Clickup]: https://img.shields.io/badge/-Click%20Up-7B68EE?style=for-the-badge&labelColor=7B68EE&logo=clickup&logoColor=white
[Anaconda]: https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white
[Notepad_plus_plus]: https://img.shields.io/badge/Notepad++-90E59A.svg?style=for-the-badge&logo=notepad%2b%2b&logoColor=black
[GitHubActions]: https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white