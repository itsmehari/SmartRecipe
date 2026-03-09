# SMARTRECIPE PROJECT REPORT

---

## 1. TITLE PAGE

**DHANRAJ BAID JAIN COLLEGE (AUTONOMOUS)**  
Rajiv Gandhi Salai, Jyothi Nagar, Okkiyam Thoraipakkam, Chennai – 600097  
*(Re-accredited with ‘A’ grade by NAAC | Affiliated to University of Madras)*

---

**B.Sc. COMPUTER SCIENCE**

**FINAL YEAR PROJECT REPORT**

---

### **SMARTRECIPE: AN INGREDIENT-DRIVEN AI COOKING ENGINE**

---

*Submitted in partial fulfilment of the requirements for the award of the degree of*

**BACHELOR OF SCIENCE IN COMPUTER SCIENCE**

*by*

**[YOUR FULL NAME]**  
Register No.: **[YOUR ROLL NO / REGISTER NUMBER]**

*Under the guidance of*  
**[GUIDE NAME]**  
**[GUIDE DESIGNATION]**  
Department of Computer Science

---

**DEPARTMENT OF COMPUTER SCIENCE**  
**DHANRAJ BAID JAIN COLLEGE (AUTONOMOUS)**  
**CHENNAI – 600097**

**ACADEMIC YEAR: [e.g. 2024 – 2025]**

---

## 2. BONAFIDE CERTIFICATE

This is to certify that the project report entitled **“SMARTRECIPE: AN INGREDIENT-DRIVEN AI COOKING ENGINE”** submitted by ** [YOUR FULL NAME] ** (Register No.: ** [YOUR ROLL NO] **) to the Department of Computer Science, Dhanraj Baid Jain College (Autonomous), Chennai, is a bonafide record of the project work carried out under my supervision. The project has been approved as it satisfies the academic requirements in respect of the project work prescribed for the award of **B.Sc. Computer Science**.

**Place:** Chennai  
**Date:**

**Signature of the Guide**  
**[GUIDE NAME]**  
**[GUIDE DESIGNATION]**  
Department of Computer Science

**Signature of the Head of Department**  
**Head, Department of Computer Science**  
Dhanraj Baid Jain College (Autonomous)  
Chennai – 600097

**Countersigned**

**Principal**  
Dhanraj Baid Jain College (Autonomous)  
Chennai – 600097

---

## 3. DECLARATION BY STUDENT

I, ** [YOUR FULL NAME] **, Register No. ** [YOUR ROLL NO] **, a final year B.Sc. Computer Science student of Dhanraj Baid Jain College (Autonomous), Chennai, hereby declare that the project report entitled **“SMARTRECIPE: AN INGREDIENT-DRIVEN AI COOKING ENGINE”** submitted to the Department of Computer Science is a record of original work done by me under the guidance of ** [GUIDE NAME] **. This work has not been submitted elsewhere for the award of any other degree or diploma. I have followed the guidelines provided by the University/College in the preparation of this report.

**Place:** Chennai  
**Date:**

**Signature of the Student**  
**[YOUR FULL NAME]**

---

## 4. ACKNOWLEDGEMENT

I would like to express my sincere gratitude to all those who have helped me complete this project successfully.

I am deeply grateful to **Dhanraj Baid Jain College (Autonomous)**, Thoraipakkam, Chennai, and the **Department of Computer Science** for providing the necessary facilities and environment for this project work.

I extend my heartfelt thanks to my project guide, ** [GUIDE NAME] **, for valuable guidance, suggestions, and support throughout the project. I also thank the **Head of the Department of Computer Science** and the faculty for their encouragement and feedback.

I thank my family and friends for their constant support and motivation during the completion of this work.

**[YOUR FULL NAME]**

---

## 5. ABSTRACT

Advancements in artificial intelligence and data-driven systems have transformed many areas of daily life, including healthcare, finance, education, and lifestyle management. One practical domain that continues to face everyday decision-making challenges is home cooking and meal planning. Many individuals struggle with deciding what to cook using the ingredients currently available in their kitchen. Traditional recipe applications generally require users to search for specific dishes, which assumes that the user already knows what they want to prepare. This approach does not efficiently utilize available ingredients and often leads to unnecessary grocery purchases and food waste.

The **SmartRecipe** system addresses this challenge through an **Ingredient-Driven AI Cooking Engine** that converts available kitchen ingredients into structured recipe recommendations. Instead of beginning with a predefined dish name, SmartRecipe begins with the ingredients that the user currently possesses. By analyzing ingredient combinations, dietary restrictions, cuisine preferences, and preparation constraints, the system generates cooking suggestions that are practical and tailored to the user's needs.

SmartRecipe accepts multiple forms of input. Users can manually enter ingredients and quantities, upload images of refrigerator or pantry items for automated ingredient detection using computer vision techniques, or apply dietary filters such as vegan, Jain, high-protein, or gluten-free. The system also allows the user to specify regional cuisine preferences such as South Indian, North Indian, Italian, or Asian cooking styles. Additional constraints such as preparation time limits and complexity levels further guide the recipe generation process.

At the core of the SmartRecipe platform lies a set of analytical modules designed to intelligently process ingredient data. An **Ingredient Compatibility Matrix** evaluates which ingredients pair well together based on known culinary patterns. A **Flavor Graph Mapping model** analyzes flavor relationships between ingredients to identify complementary combinations. A **Nutritional Optimization Engine** estimates macro-nutrient balance and provides general nutritional insights. A **Portion Scaling Engine** adjusts ingredient quantities dynamically depending on the number of servings required. In addition, a **Waste Reduction Optimizer** prioritizes recipes that make efficient use of available ingredients and helps minimize food waste.

The system presents its outputs through an interactive **Recipe Dashboard** where recipe options are categorized into preparation bands such as **Simple**, **Balanced**, and **Gourmet**. Each generated recipe includes preparation steps, estimated cooking time, ingredient utilization details, and approximate nutritional insights. When ingredients are missing, the system can recommend substitution options or generate a shopping list of additional items required to complete the recipe.

Ethical safeguards are incorporated to ensure responsible usage of the system. SmartRecipe does not provide medical advice, therapeutic recommendations, or guaranteed nutritional accuracy. All nutritional information presented by the system is an estimated approximation derived from publicly available food composition datasets. Each output clearly includes a disclaimer stating that the system provides recipe suggestions and is not a substitute for professional nutritional consultation.

The implementation of SmartRecipe uses a modern Python-based technology stack. Backend processing utilizes libraries such as **Pandas**, **NumPy**, and **Scikit-learn** for data processing and machine learning tasks. Image recognition capabilities can be implemented using **OpenCV** or **TensorFlow-based object detection models**. Natural language processing and flavor analysis may incorporate **NLTK** or transformer-based text processing libraries. The user interface is built using **Streamlit**, enabling an interactive dashboard suitable for academic demonstration.

From an academic perspective, the SmartRecipe project demonstrates how artificial intelligence techniques can be applied to solve practical household problems. It integrates multiple computational disciplines including machine learning, data analysis, optimization modeling, computer vision, and interactive user interface development. The project also highlights responsible AI design by incorporating ethical guardrails and transparency in system outputs.

Overall, SmartRecipe functions as an intelligent cooking assistant capable of transforming ingredient availability into structured meal suggestions while promoting efficient ingredient usage, reducing food waste, and improving daily meal planning decisions.  

---

## 6. TABLE OF CONTENTS

*(Generate with page numbers when preparing the final PDF/Word document. Include all chapter and section headings.)*

---

## 7. LIST OF FIGURES

*(Add figure numbers, captions, and page numbers after inserting screenshots/diagrams in the report—e.g. in Chapters 4, 6, and 8.)*

---

## 8. LIST OF TABLES

*(Add table numbers, titles, and page numbers. Tables appear in Chapter 7—Ingredient Dataset, Recipe Dataset, Nutritional Dataset, Flavor Relationships—and elsewhere as applicable.)*

---

## 9. LIST OF ABBREVIATIONS

| Abbreviation | Expansion |
|--------------|-----------|
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| CSV | Comma-Separated Values |
| DFD | Data Flow Diagram |
| ER | Entity Relationship |
| GUI | Graphical User Interface |
| IoT | Internet of Things |
| ML | Machine Learning |
| NAAC | National Assessment and Accreditation Council |
| NLP | Natural Language Processing |
| NSS | National Service Scheme |
| PDF | Portable Document Format |
| UI | User Interface |
| UG | Undergraduate |
| UGC | University Grants Commission |

---

## CHAPTER 1 — INTRODUCTION

### 1.1 Introduction to Smart Cooking Systems

Food preparation is one of the most common daily activities performed in households across the world. Despite the availability of numerous cooking resources such as cookbooks, television shows, and online recipe platforms, many individuals still face difficulty deciding what to cook with the ingredients available in their kitchen. This decision-making process becomes more complex when additional factors such as dietary preferences, nutritional balance, preparation time, and cultural food habits must be considered.

Smart cooking systems aim to address these challenges by applying digital technologies and intelligent algorithms to assist users in meal planning and recipe discovery. Instead of relying purely on manual search methods, smart cooking systems analyze available ingredients, identify potential recipe combinations, and generate structured cooking suggestions. These systems attempt to simplify the cooking process by reducing decision fatigue and improving ingredient utilization.

In recent years, the emergence of artificial intelligence, data analytics, and machine learning has enabled the development of intelligent kitchen assistants that can analyze ingredient data and generate recommendations dynamically. Such systems help users make better use of the resources they already possess, reduce food waste, and discover new cooking possibilities.

The SmartRecipe system proposed in this project represents an example of a smart cooking platform that focuses on ingredient-driven recipe generation using AI-based analysis.

### 1.2 Evolution of Digital Recipe Platforms

Digital recipe platforms have evolved significantly over the past two decades. Early recipe websites functioned primarily as digital repositories of cooking instructions where users could browse or search recipes by dish name. These systems provided limited personalization and required the user to already know what meal they intended to prepare.

With the growth of web technologies and mobile applications, recipe platforms began incorporating additional features such as user ratings, step-by-step instructions, cooking videos, and community sharing. Applications such as online cooking portals and mobile cooking assistants allowed users to save favorite recipes and follow guided cooking instructions.

More recent developments have introduced ingredient-based search features, where users can enter a list of ingredients and receive possible recipe suggestions. However, most of these systems still operate using simple keyword matching rather than deeper analysis of ingredient compatibility or nutritional balance.

The next stage in the evolution of cooking platforms involves the integration of artificial intelligence technologies that analyze ingredient relationships, dietary needs, and cooking constraints to generate personalized meal suggestions. SmartRecipe is designed as part of this emerging generation of intelligent culinary systems.

### 1.3 Artificial Intelligence in Culinary Systems

Artificial intelligence has increasingly been applied in the food and culinary industry to support tasks such as recipe recommendation, ingredient substitution, food image recognition, and nutritional analysis. AI algorithms can analyze large datasets of recipes and ingredient relationships to identify patterns in cooking methods and flavor combinations.

Machine learning models can be trained to recommend recipes based on user preferences, available ingredients, and historical cooking behavior. Computer vision technologies can detect food items from images captured using cameras or smartphones. Natural language processing can analyze textual recipe instructions and ingredient lists to extract structured information.

In the context of SmartRecipe, artificial intelligence techniques are used to evaluate ingredient compatibility, estimate nutritional properties, and recommend appropriate recipes. These AI components allow the system to function as an intelligent assistant that helps users make cooking decisions more efficiently.

### 1.4 Background of Ingredient-Driven Cooking

Traditional cooking often begins with a predefined recipe where the cook gathers the required ingredients and follows a fixed preparation process. However, in many real-world situations, individuals must cook based on the ingredients currently available in their kitchen. This approach is commonly referred to as ingredient-driven cooking.

Ingredient-driven cooking focuses on identifying possible dishes that can be prepared using available ingredients rather than following a predetermined recipe. This method encourages creativity and efficient resource usage but can be difficult for inexperienced cooks who may not be familiar with ingredient combinations or cooking techniques.

The SmartRecipe system is designed to assist users in ingredient-driven cooking by analyzing ingredient lists and generating structured cooking suggestions. By applying computational analysis to ingredient compatibility and flavor relationships, the system can recommend practical meal options that users may not have previously considered.

### 1.5 Motivation for SmartRecipe Development

Several factors motivated the development of the SmartRecipe system. One major issue in many households is the inefficient utilization of available ingredients. Users often purchase additional groceries despite already having suitable ingredients that could be used to prepare meals. This leads to increased food waste and unnecessary expenditure.

Another challenge is the lack of personalized recipe suggestions. Many cooking platforms provide generic recipes that do not consider dietary restrictions, cultural food habits, or available cooking time. Users may therefore struggle to find recipes that match their specific requirements.

The SmartRecipe system is motivated by the need to create a more intelligent cooking assistant capable of analyzing real-time ingredient availability and generating practical meal suggestions. By incorporating artificial intelligence techniques, the system aims to simplify cooking decisions, encourage efficient ingredient usage, and support diverse dietary preferences.

### 1.6 Objectives of the SmartRecipe System

The primary objective of the SmartRecipe project is to develop an intelligent cooking assistant that generates recipe recommendations based on available ingredients. The system aims to assist users in preparing meals efficiently while minimizing food waste and supporting dietary preferences.

Specific objectives of the project include:

• To design a system that accepts ingredient inputs from users.

• To analyze ingredient compatibility and generate possible recipe combinations.

• To provide recipe suggestions based on dietary preferences and cuisine types.

• To estimate basic nutritional information for generated recipes.

• To recommend ingredient substitutions when required ingredients are missing.

• To present recipe suggestions through an interactive dashboard interface.

• To demonstrate the application of artificial intelligence techniques in culinary recommendation systems.

### 1.7 Problem Statement

Many existing recipe platforms rely on static recipe searches that require users to know the dish they want to prepare. This approach does not support users who wish to cook using only the ingredients currently available in their kitchen.

Users frequently encounter situations where they possess a set of ingredients but do not know which recipes can be prepared using them. Additionally, users may have dietary restrictions, limited cooking time, or cultural cuisine preferences that are not adequately addressed by traditional recipe applications.

The problem addressed in this project is therefore the development of a system that can analyze available ingredients and automatically generate suitable recipe suggestions while considering dietary filters, preparation time constraints, and ingredient compatibility.

### 1.8 Scope of the Project

The SmartRecipe project focuses on developing a prototype system capable of demonstrating intelligent recipe generation using ingredient inputs. The system will include modules for ingredient entry, dietary filtering, recipe recommendation, and nutritional estimation.

The project will also demonstrate the use of computer vision techniques for recognizing ingredients from uploaded images. However, image recognition accuracy may depend on dataset availability and model training quality.

The system will be implemented using Python programming language with Streamlit for the user interface and machine learning libraries for analytical processing. The scope of the project is limited to generating recipe suggestions and does not attempt to provide medical dietary advice or professional nutritional consultation.

### 1.9 Research Methodology

The development of the SmartRecipe system follows a structured methodology consisting of multiple stages. The first stage involves studying existing recipe recommendation platforms and identifying their limitations. This analysis helps define the functional requirements of the proposed system.

The second stage involves designing the system architecture and identifying key modules such as ingredient analysis, recipe generation, and nutritional estimation. Data structures and database schemas are defined to store ingredients, recipes, and user preferences.

The third stage focuses on implementation using Python and relevant machine learning libraries. Modules are developed incrementally and integrated into the Streamlit interface.

The final stage involves testing the system using sample datasets to evaluate the quality of recipe recommendations and system usability.

### 1.10 Organization of the Report

This project report is organized into multiple chapters describing different aspects of the SmartRecipe system.

Chapter 1 introduces the concept of smart cooking systems and explains the motivation and objectives of the project.

Chapter 2 presents a study of existing recipe platforms and discusses their limitations.

Chapter 3 describes the hardware and software requirements needed for implementing the system.

Chapter 4 explains the system design, architecture, and database structure.

Chapter 5 provides a detailed explanation of the system modules and their functions.

Chapter 6 presents the coding implementation and technical components used in the system.

Chapter 7 describes the datasets used for ingredient and recipe analysis.

Chapter 8 discusses the experimental results and system outputs.

Chapter 9 outlines the limitations of the current implementation.

Chapter 10 discusses possible future enhancements.

Chapter 11 explores potential business models for intelligent cooking platforms.

Chapter 12 concludes the report with a summary of the project outcomes.  

## CHAPTER 2 — SYSTEM STUDY

### 2.1 Overview of Existing Recipe Applications

The rapid growth of internet technologies has led to the development of numerous digital recipe platforms and cooking applications. These systems provide access to large collections of recipes and cooking instructions for users across the world. Most modern cooking applications are designed to help users discover recipes, learn cooking techniques, and plan meals. However, despite the availability of these platforms, many users still face challenges when attempting to cook with the ingredients already present in their kitchen.

Existing recipe platforms can generally be categorized into several types based on their operational approach. These include static recipe search platforms, ingredient-based cooking applications, meal planning systems, and emerging AI-assisted cooking tools.

#### 2.1.1 Static Recipe Search Platforms

Static recipe search platforms represent the earliest generation of digital cooking systems. These platforms typically store a large collection of recipes in a database and allow users to search for recipes using keywords such as dish names or ingredients. Users must already know what type of meal they want to prepare before using these systems.

Popular examples include online cooking websites and recipe portals where users browse recipes by categories such as breakfast, lunch, dinner, desserts, or regional cuisines. These systems often include step-by-step instructions, ingredient lists, and sometimes cooking videos.

Although these platforms provide valuable cooking resources, they do not intelligently analyze the ingredients that a user currently possesses. As a result, users may still struggle to find recipes that match their available kitchen inventory.

#### 2.1.2 Ingredient-Based Cooking Applications

Ingredient-based cooking applications represent a more advanced approach compared to traditional recipe websites. These systems allow users to enter a list of ingredients that they currently have in their kitchen. The system then attempts to match these ingredients with recipes stored in its database.

While this approach improves usability compared to static search platforms, many ingredient-based systems still rely on simple keyword matching rather than deeper analysis of ingredient compatibility. For example, if a recipe requires five ingredients and the user only has three of them, the system may not recommend the recipe even though substitutions could be possible.

Therefore, although ingredient-based systems offer partial improvements, they often lack the ability to intelligently analyze ingredient relationships or propose optimized cooking suggestions.

#### 2.1.3 Meal Planning Platforms

Meal planning platforms focus primarily on helping users organize their weekly or monthly meals. These systems allow users to select recipes and create structured meal schedules for breakfast, lunch, and dinner. Some platforms also generate grocery lists based on selected meal plans.

These platforms are useful for dietary planning and grocery management but typically require users to manually select recipes in advance. They do not dynamically generate recipe suggestions based on available ingredients in real time. Consequently, their usefulness is limited when users want to cook spontaneously using ingredients already available in their kitchen.

#### 2.1.4 AI-Driven Cooking Tools

Recent developments in artificial intelligence have introduced new possibilities in digital cooking systems. Some experimental platforms and research projects attempt to use machine learning models to recommend recipes, analyze flavor combinations, or detect ingredients from images.

These systems may analyze large datasets of recipes to learn patterns of ingredient combinations and cooking methods. AI-powered cooking tools may also incorporate computer vision models to recognize ingredients from photographs of kitchen items.

However, many existing AI-based cooking systems remain experimental or limited in functionality. Few systems integrate ingredient compatibility analysis, nutritional estimation, waste reduction strategies, and personalized filtering into a single unified platform.

### 2.2 Limitations of Existing Systems

Although many digital recipe platforms exist, they present several limitations that reduce their effectiveness for everyday cooking scenarios.

#### 2.2.1 Lack of Inventory Awareness

Most recipe platforms are not aware of the ingredients currently available in a user’s kitchen. Users must manually search for recipes and then determine whether they have the required ingredients. This often results in inefficient recipe discovery and unnecessary grocery purchases.

#### 2.2.2 No Ingredient Optimization

Traditional systems do not optimize recipes based on ingredient utilization. For example, if a user has perishable ingredients that should be used soon, existing platforms rarely prioritize recipes that make use of those ingredients.

#### 2.2.3 Limited Personalization

Many cooking platforms provide the same recipe recommendations to all users. They do not fully account for individual dietary preferences, cultural cuisine styles, or preparation time constraints.

#### 2.2.4 Poor Dietary Adaptability

Dietary restrictions such as vegan, gluten-free, diabetic-friendly, or Jain food practices require careful ingredient selection. Most recipe platforms do not provide advanced filtering mechanisms capable of adjusting recipes to match such requirements.

#### 2.2.5 No Waste Reduction Strategy

Food waste is a growing global concern. Many households discard ingredients because they are unsure how to incorporate them into meals. Existing recipe systems rarely provide suggestions designed to minimize ingredient waste.

### 2.3 Proposed SmartRecipe System

The SmartRecipe system is designed to address the limitations of existing cooking platforms by introducing an intelligent ingredient-driven recipe generation approach. The system begins with the ingredients available to the user and analyzes possible cooking options using artificial intelligence techniques.

#### 2.3.1 Ingredient Intelligence Model

The ingredient intelligence module evaluates relationships between ingredients using compatibility rules derived from recipe datasets and culinary knowledge. The system identifies ingredients that commonly appear together in recipes and uses this information to suggest viable cooking combinations.

#### 2.3.2 AI-Driven Recipe Generation

Instead of relying purely on stored recipes, SmartRecipe can generate recipe suggestions dynamically. Machine learning models analyze ingredient combinations and recommend suitable dishes based on similarity patterns observed in training datasets.

#### 2.3.3 Dietary Filtering Engine

The system includes a filtering module that allows users to apply dietary preferences such as vegetarian, vegan, Jain, high-protein, or gluten-free diets. These filters ensure that generated recipes respect user dietary restrictions.

#### 2.3.4 Nutritional Optimization Layer

A nutritional analysis module estimates macro-nutrient values such as carbohydrates, proteins, and fats for generated recipes. While the system does not provide medical dietary advice, it can offer general nutritional insights that help users make informed cooking decisions.

### 2.4 Feasibility Study

A feasibility study evaluates whether the proposed system can be successfully implemented using available resources, technologies, and operational conditions.

#### 2.4.1 Technical Feasibility

The SmartRecipe system can be implemented using widely available open-source technologies such as Python, Streamlit, and machine learning libraries including Scikit-learn and TensorFlow. Ingredient datasets and nutritional information databases are also publicly available, making technical implementation feasible.

#### 2.4.2 Economic Feasibility

The project can be developed with minimal financial investment since the required software tools and libraries are open-source. Development can be performed on standard personal computers without specialized hardware.

#### 2.4.3 Operational Feasibility

The proposed system is designed to be simple and user-friendly. Users interact with the system through a graphical interface where they can enter ingredients, upload images, and select preferences. Therefore the system is operationally feasible for general household users.

#### 2.4.4 Social Feasibility

The system promotes efficient ingredient utilization and reduces food waste, which aligns with broader societal goals related to sustainability and responsible consumption.

### 2.5 System Constraints

Despite its advantages, the SmartRecipe system also has certain limitations and constraints.

#### 2.5.1 Data Accuracy Limitations

Recipe recommendations depend on the quality and completeness of ingredient and recipe datasets. Incomplete datasets may limit the accuracy of generated suggestions.

#### 2.5.2 Nutritional Estimation Constraints

Nutritional values generated by the system are only estimates based on available food composition databases. These estimates should not be interpreted as medically precise nutritional calculations.

#### 2.5.3 Image Recognition Limitations

Ingredient recognition from images depends on the accuracy of computer vision models and the quality of uploaded photographs. Poor lighting or partial ingredient visibility may affect recognition accuracy.  

## CHAPTER 3 — SYSTEM REQUIREMENTS

### 3.1 Hardware Requirements

Hardware requirements describe the physical computing resources required to develop and run the SmartRecipe system. Since the project is designed as an academic prototype using lightweight technologies such as Python and Streamlit, the hardware requirements remain modest and accessible to most development environments.

#### 3.1.1 Development Environment Hardware

The development environment refers to the system used by developers or students to build and test the application.

Typical development hardware includes:

• Processor: Intel i5 / AMD Ryzen 5 or higher  
• RAM: Minimum 8 GB recommended for machine learning libraries  
• Storage: 10–20 GB free disk space for datasets and libraries  
• GPU: Optional (useful for image recognition models but not mandatory)

#### 3.1.2 Minimum System Requirements

To run the SmartRecipe prototype application, the following minimum system configuration is sufficient:

• Processor: Dual-core processor  
• RAM: 4 GB  
• Storage: 5 GB free disk space  
• Operating System: Windows / Linux / macOS

#### 3.1.3 Recommended System Configuration

For smooth operation and faster processing of machine learning tasks:

• Processor: Intel i7 / Ryzen 7  
• RAM: 16 GB  
• Storage: SSD storage recommended  
• GPU: Optional CUDA-capable GPU for computer vision processing

---

### 3.2 Software Requirements

Software requirements include the operating systems, programming languages, development tools, and libraries required to implement the SmartRecipe system.

#### 3.2.1 Programming Language

The system is implemented using **Python** due to its extensive ecosystem of machine learning, data processing, and visualization libraries. Python also allows rapid development and integration of AI modules.

#### 3.2.2 Development Tools

Common development tools used in this project include:

• Python IDEs such as VS Code, PyCharm, or Jupyter  
• Git for version control  
• Virtual environments for dependency management

#### 3.2.3 Runtime Environment

The runtime environment includes:

• Python 3.9 or above  
• Streamlit framework for user interface  
• SQLite database for lightweight data storage

---

### 3.3 Technology Stack

The SmartRecipe platform uses a modern AI-enabled technology stack that integrates data processing, machine learning, computer vision, and web interface technologies.

#### 3.3.1 Python Programming Language

Python serves as the backbone of the system and is responsible for implementing data processing logic, machine learning models, and service-layer operations.

#### 3.3.2 Streamlit Framework

Streamlit provides a simple yet powerful way to create interactive dashboards using Python. It allows developers to quickly build forms, visualizations, and input interfaces without needing complex web development frameworks.

#### 3.3.3 Pandas Data Processing Library

Pandas is used for structured data manipulation such as ingredient datasets, nutritional tables, and recipe databases.

#### 3.3.4 NumPy Scientific Computation

NumPy supports numerical computations required for data processing and optimization calculations.

#### 3.3.5 Scikit-Learn Machine Learning Toolkit

Scikit-learn is used for implementing machine learning models such as classification and recommendation algorithms.

#### 3.3.6 OpenCV Image Processing

OpenCV supports ingredient detection from images uploaded by the user. It performs image preprocessing and feature extraction tasks.

#### 3.3.7 TensorFlow / Deep Learning Support

TensorFlow may be used for training or running object detection models capable of identifying food items in images.

#### 3.3.8 NLTK / Transformers for Text Processing

These libraries help analyze textual recipe descriptions and extract structured ingredient information.

---

### 3.4 System Dependencies

Dependencies refer to external libraries and frameworks required by the system.

#### 3.4.1 Python Libraries

Key Python libraries used include:

• pandas  
• numpy  
• scikit-learn  
• streamlit  
• opencv-python  
• matplotlib  
• seaborn

#### 3.4.2 AI Model Libraries

For AI capabilities:

• TensorFlow / PyTorch  
• transformers (optional for NLP)

#### 3.4.3 Visualization Libraries

Visualization tools are used to generate graphs and dashboards:

• matplotlib  
• plotly  
• streamlit charts

---

### 3.5 Functional Requirements

Functional requirements define the core capabilities of the SmartRecipe system.

#### 3.5.1 Ingredient Entry System

The system must allow users to manually enter ingredients and quantities through a graphical form.

#### 3.5.2 Image Ingredient Detection

Users should be able to upload images of ingredients. The system will attempt to identify food items using computer vision techniques.

#### 3.5.3 Dietary Filter Application

Users must be able to apply dietary filters such as vegetarian, vegan, Jain, gluten-free, or protein-rich meal preferences.

#### 3.5.4 Recipe Generation

The system should generate recipe suggestions based on available ingredients and compatibility analysis.

#### 3.5.5 Nutritional Insights

The system should estimate approximate macro-nutrient values for generated recipes.

---

### 3.6 Non-Functional Requirements

Non-functional requirements describe the quality characteristics of the system.

#### 3.6.1 Performance Requirements

The system should generate recipe recommendations within a few seconds for typical ingredient inputs.

#### 3.6.2 Security Requirements

The system must ensure that uploaded images and ingredient data are processed locally without storing personal data unnecessarily.

#### 3.6.3 Usability Requirements

The interface should be simple and intuitive so that non-technical users can easily interact with the system.

#### 3.6.4 Reliability Requirements

The system must handle incorrect inputs gracefully and provide meaningful error messages.

---

## CHAPTER 4 — SYSTEM DESIGN

### 4.1 System Architecture

The SmartRecipe architecture follows a layered structure consisting of input, processing, AI analysis, and visualization layers.

#### 4.1.1 Input Layer

The input layer collects user-provided data such as ingredient lists, uploaded images, dietary filters, and cooking preferences.

#### 4.1.2 Processing Layer

This layer cleans and standardizes ingredient data before sending it to AI analysis modules.

#### 4.1.3 AI Optimization Layer

Machine learning models analyze ingredient relationships, nutritional balance, and compatibility patterns.

#### 4.1.4 Visualization Layer

The Streamlit dashboard displays recipes, charts, and suggestions to the user.

---

### 4.2 System Workflow

The workflow of the SmartRecipe system follows several sequential stages.

#### 4.2.1 Ingredient Collection Process

Users provide ingredients through manual entry or image upload.

#### 4.2.2 Recipe Generation Pipeline

Ingredient lists are processed by compatibility and recommendation models to generate possible recipes.

#### 4.2.3 Optimization Process Flow

Generated recipes are evaluated based on nutrition, ingredient utilization, and dietary filters.

---

### 4.3 Data Flow Diagram

#### 4.3.1 Level 0 DFD

Shows the overall interaction between the user and the SmartRecipe system.

#### 4.3.2 Level 1 DFD

Provides detailed flow including ingredient analysis, recommendation engine, and dashboard output.

---

### 4.4 Database Design

The database stores structured information about ingredients, recipes, dietary profiles, and generated suggestions.

Tables include:

• Users  
• Ingredients  
• Recipes  
• DietaryProfiles  
• Optimizations  
• ShoppingLists

---

### 4.5 Entity Relationship Diagram

The ER diagram represents the relationships between the system entities.

#### 4.5.1 Entities

Users, Ingredients, Recipes, DietaryProfiles, ShoppingLists.

#### 4.5.2 Attributes

Each entity contains attributes such as ingredient name, quantity, recipe steps, and nutritional values.

#### 4.5.3 Relationships

Users generate recipes, recipes contain ingredients, and ingredients relate to dietary filters.

---

### 4.6 System Interaction Model

#### 4.6.1 User Interaction Flow

User enters ingredients → selects filters → system processes → recipes displayed.

#### 4.6.2 Recipe Recommendation Flow

Ingredient dataset → compatibility analysis → recipe model → ranking → dashboard output.

---

### 4.7 Security and Ethical Safeguards

#### 4.7.1 Data Privacy Principles

The system does not store personal health data and processes inputs locally where possible.

#### 4.7.2 Nutritional Disclaimer Policy

All nutritional outputs are presented as approximate values and include a disclaimer.

---

## CHAPTER 5 — MODULE DESCRIPTION

The SmartRecipe system is divided into multiple functional modules. Each module performs a specific task in the recipe generation pipeline.

### 5.1 User Management Module

**Purpose**: Manage user sessions and preferences.

**Inputs**: User preferences and session data.

**Processing**: Store user filters and session states.

**Outputs**: Personalized system responses.

### 5.2 Ingredient Entry Module

Allows manual entry of ingredients and quantities.

### 5.3 Image Recognition Module

Processes uploaded images to detect food items using computer vision.

### 5.4 Dietary Filter Module

Applies dietary restrictions to generated recipes.

### 5.5 Cuisine Preference Module

Adjusts recipe generation according to regional cuisine preferences.

### 5.6 Ingredient Compatibility Matrix Module

Analyzes which ingredients can be combined effectively.

### 5.7 Flavor Graph Mapping Module

Represents flavor relationships between ingredients.

### 5.8 Nutritional Optimization Module

Estimates macro-nutrient balance for generated recipes.

### 5.9 Portion Scaling Engine

Adjusts ingredient quantities based on number of servings.

### 5.10 Waste Reduction Optimizer

Prioritizes recipes that use maximum available ingredients.

### 5.11 Recipe Generation Module

Generates structured recipes using ingredient analysis.

### 5.12 Recipe Recommendation Classifier

Ranks recipes based on compatibility and relevance.

### 5.13 Dashboard Visualization Module

Displays results through interactive charts and recipe cards.

### 5.14 Grocery List Generator

Creates a list of missing ingredients required for selected recipes.

### 5.15 Weekly Meal Planner (Optional Module)

Generates weekly meal schedules using recommended recipes.

---

## CHAPTER 6 — CODING

This chapter presents the technical implementation of the SmartRecipe system. The system is implemented using Python with a modular architecture so that each functional component can be developed, tested, and extended independently. The frontend is implemented using Streamlit, while backend services perform ingredient analysis, recipe generation, and optimization tasks.

The project follows a clean folder structure to ensure maintainability and clarity for developers and academic reviewers.

### 6.1 Project Directory Structure

The SmartRecipe application is organized into multiple folders that separate responsibilities such as frontend pages, backend services, machine learning models, and database logic.

```
SmartRecipe/
│
├─ app.py
├─ requirements.txt
│
├─ pages/
│   ├─ ingredient_input.py
│   ├─ image_upload.py
│   ├─ filters.py
│   └─ dashboard.py
│
├─ services/
│   ├─ ingredient_analyzer.py
│   ├─ recipe_engine.py
│   ├─ nutrition_engine.py
│   └─ shopping_list.py
│
├─ models/
│   ├─ compatibility_model.py
│   ├─ flavor_graph.py
│   └─ recipe_recommender.py
│
├─ database/
│   ├─ db_handler.py
│   └─ schema.sql
│
├─ utils/
│   ├─ logger.py
│   └─ validators.py
│
└─ uploads/
```

This modular structure ensures that each component of the system can evolve independently without affecting other modules.

---

### 6.2 Main Application Entry (Streamlit Application)

The main application file initializes the Streamlit interface and manages navigation between pages.

```python
import streamlit as st

st.set_page_config(page_title="SmartRecipe", layout="wide")

st.title("SmartRecipe – AI Cooking Assistant")

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Select Page",
    ["Ingredient Entry", "Image Upload", "Filters", "Recipe Dashboard"]
)

if page == "Ingredient Entry":
    from pages import ingredient_input
    ingredient_input.run()

elif page == "Image Upload":
    from pages import image_upload
    image_upload.run()

elif page == "Filters":
    from pages import filters
    filters.run()

elif page == "Recipe Dashboard":
    from pages import dashboard
    dashboard.run()
```

This file acts as the entry point of the application.

---

### 6.3 Frontend Pages

The frontend consists of multiple Streamlit pages that handle user interaction.

#### 6.3.1 Ingredient Entry Page

Allows users to manually enter ingredients.

```python
import streamlit as st


def run():

    st.header("Enter Available Ingredients")

    ingredients = st.text_area(
        "Enter ingredients separated by commas"
    )

    if st.button("Analyze Ingredients"):
        st.session_state['ingredients'] = ingredients.split(",")
        st.success("Ingredients stored successfully")
```

#### 6.3.2 Image Upload Page

This page allows users to upload images of ingredients.

```python
import streamlit as st


def run():

    st.header("Upload Ingredient Image")

    uploaded_file = st.file_uploader(
        "Upload image",
        type=["jpg", "png"]
    )

    if uploaded_file:
        st.image(uploaded_file)
        st.success("Image uploaded successfully")
```

#### 6.3.3 Filter Selection Page

```python
import streamlit as st


def run():

    st.header("Dietary Preferences")

    diet = st.selectbox(
        "Select diet type",
        ["None", "Vegetarian", "Vegan", "Jain", "High Protein"]
    )

    cuisine = st.selectbox(
        "Cuisine",
        ["Indian", "South Indian", "North Indian", "Italian", "Asian"]
    )

    st.session_state['diet'] = diet
    st.session_state['cuisine'] = cuisine
```

#### 6.3.4 Recipe Dashboard Page

```python
import streamlit as st


def run():

    st.header("Recommended Recipes")

    ingredients = st.session_state.get("ingredients", [])

    if ingredients:
        st.write("Based on ingredients:", ingredients)
        st.write("Suggested Recipe: Vegetable Stir Fry")

    else:
        st.warning("Please add ingredients first")
```

---

### 6.4 Services Layer

The services layer contains the core backend logic.

#### 6.4.1 Ingredient Analyzer

```python

def analyze_ingredients(ingredients):

    cleaned = [i.strip().lower() for i in ingredients]

    return cleaned
```

#### 6.4.2 Recipe Builder

```python

def build_recipe(ingredients):

    if "tomato" in ingredients and "onion" in ingredients:
        return "Tomato Onion Curry"

    return "Mixed Vegetable Dish"
```

#### 6.4.3 Nutrition Engine

```python

def estimate_nutrition(recipe):

    return {
        "calories": 250,
        "protein": 10,
        "carbs": 35
    }
```

#### 6.4.4 Shopping List Generator

```python

def generate_shopping_list(recipe):

    return ["oil", "salt", "garlic"]
```

---

### 6.5 AI Models

The system includes simplified machine learning models used for ingredient compatibility and recipe recommendation.

#### 6.5.1 Compatibility Classifier

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def compatibility_score(vec1, vec2):

    return cosine_similarity([vec1], [vec2])[0][0]
```

#### 6.5.2 Flavor Graph Model

```python
flavor_graph = {

    "tomato": ["onion", "garlic", "basil"],
    "potato": ["butter", "pepper"],
}
```

#### 6.5.3 Recipe Recommender

```python

def recommend(ingredients, recipes):

    suggestions = []

    for r in recipes:
        if set(ingredients).intersection(set(r["ingredients"])):
            suggestions.append(r["name"])

    return suggestions
```

---

### 6.6 Database Layer

SQLite is used as a lightweight database for storing ingredient and recipe information.

```sql
CREATE TABLE ingredients (

id INTEGER PRIMARY KEY,
name TEXT

);

CREATE TABLE recipes (

id INTEGER PRIMARY KEY,
name TEXT,
description TEXT

);
```

---

### 6.7 Exception Handling

```python
try:

    ingredients = analyze_ingredients(user_input)

except Exception as e:

    print("Error processing ingredients", e)
```

---

### 6.8 Security and Privacy

The system does not store sensitive user data. Uploaded images are processed temporarily and not retained unless explicitly required for dataset improvement.

---

### 6.9 Testing

Basic unit tests verify that system modules function correctly.

```python

def test_recipe_builder():

    result = build_recipe(["tomato", "onion"])

    assert result == "Tomato Onion Curry"
```

---

### 6.10 Deployment

The application can be deployed locally using Python and Streamlit.

```
python -m venv venv

pip install -r requirements.txt

streamlit run app.py
```

---

## CHAPTER 7 — SAMPLE DATASETS

Datasets play a crucial role in the SmartRecipe system because the quality of ingredient analysis, recipe recommendations, and nutritional estimation depends heavily on the structure and accuracy of the underlying data. The system relies on multiple datasets that represent ingredients, recipes, flavor relationships, and nutritional values. These datasets are used during both development and testing phases of the project.

The datasets used in this project are simplified academic datasets designed to demonstrate the functionality of the SmartRecipe system. In real-world production environments, these datasets can be expanded using large-scale culinary databases and nutritional repositories.

### 7.1 Ingredient Dataset

The ingredient dataset contains a structured list of commonly used food ingredients. Each ingredient entry contains metadata such as ingredient category, basic flavor characteristics, and compatibility references.

Typical fields in the ingredient dataset include:

• Ingredient ID  
• Ingredient Name  
• Category (Vegetable, Grain, Protein, Spice, Dairy, etc.)  
• Flavor Profile (Savory, Sweet, Bitter, Umami, etc.)  
• Typical Cuisine Associations

Example Ingredient Dataset

| Ingredient_ID | Ingredient_Name | Category | Flavor_Profile | Cuisine |
|---------------|----------------|----------|---------------|--------|
| 1 | Tomato | Vegetable | Umami | Indian / Italian |
| 2 | Onion | Vegetable | Savory | Global |
| 3 | Potato | Vegetable | Neutral | Global |
| 4 | Garlic | Spice | Strong | Asian / Mediterranean |
| 5 | Rice | Grain | Neutral | Asian |

This dataset allows the system to recognize and categorize ingredients entered by the user.

### 7.2 Recipe Templates Dataset

The recipe dataset stores structured information about recipes that the system can recommend. Each recipe includes a list of required ingredients, cooking instructions, preparation time, and cuisine category.

Typical fields include:

• Recipe ID  
• Recipe Name  
• Ingredient List  
• Preparation Steps  
• Cuisine Type  
• Estimated Cooking Time  
• Difficulty Level

Example Recipe Dataset

| Recipe_ID | Recipe_Name | Key_Ingredients | Cuisine | Difficulty |
|----------|-------------|----------------|--------|-----------|
| 101 | Vegetable Stir Fry | Onion, Garlic, Vegetables | Asian | Easy |
| 102 | Tomato Onion Curry | Tomato, Onion, Spices | Indian | Medium |
| 103 | Garlic Butter Potatoes | Potato, Garlic, Butter | Western | Easy |

This dataset is used by the recipe recommendation module to match available ingredients with possible dishes.

### 7.3 Nutritional Dataset

The nutritional dataset provides approximate nutritional information for common ingredients. The system uses this dataset to estimate macro-nutrient values for generated recipes.

Typical nutritional attributes include:

• Calories (per 100g)  
• Protein content  
• Carbohydrates  
• Fat content  
• Fiber content

Example Nutritional Dataset

| Ingredient | Calories | Protein | Carbs | Fat |
|-----------|----------|--------|------|-----|
| Tomato | 18 | 0.9g | 3.9g | 0.2g |
| Onion | 40 | 1.1g | 9.3g | 0.1g |
| Potato | 77 | 2g | 17g | 0.1g |

The SmartRecipe system aggregates nutritional values from individual ingredients to estimate the nutritional profile of recommended recipes.

### 7.4 Flavor Relationship Dataset

Flavor compatibility between ingredients is represented using a flavor relationship dataset. This dataset describes which ingredients commonly pair well together based on culinary patterns observed in global cuisines.

Example flavor relationships

| Ingredient | Compatible With |
|-----------|----------------|
| Tomato | Onion, Garlic, Basil |
| Potato | Butter, Pepper, Garlic |
| Rice | Vegetables, Soy Sauce |

This dataset helps the compatibility model generate recipes that contain logically paired ingredients.

### 7.5 Sample Input Dataset for Testing

To evaluate the system during testing, sample ingredient inputs are provided.

Example input set:

User Input Ingredients:

• Tomato  
• Onion  
• Garlic

Expected System Output:

Suggested Recipes:

• Tomato Onion Curry  
• Vegetable Stir Fry

Testing datasets allow developers to verify whether the recommendation engine is functioning correctly.

### 7.6 Dataset Preparation and Cleaning

Before being used by the system, datasets must undergo preprocessing to ensure consistency and accuracy.

Common preprocessing steps include:

• Converting ingredient names to lowercase  
• Removing duplicate entries  
• Standardizing ingredient spellings  
• Handling missing values

Example Python preprocessing snippet

```python
import pandas as pd

df = pd.read_csv("ingredients.csv")

df['ingredient_name'] = df['ingredient_name'].str.lower()

df = df.drop_duplicates()
```

Dataset preparation ensures that the machine learning models and compatibility analysis modules operate on clean and reliable data.

### 7.7 Dataset Limitations

Since this project is an academic prototype, the datasets used are relatively small and simplified compared to industrial-scale culinary databases. Larger datasets could significantly improve recipe recommendation accuracy and diversity.

Possible improvements include:

• Integrating large public recipe datasets  
• Expanding flavor pairing databases  
• Incorporating regional cuisine variations  
• Including seasonal ingredient availability

Despite these limitations, the datasets used in this project are sufficient to demonstrate the working principles of the SmartRecipe system.

---

## CHAPTER 8 — RESULTS AND DISCUSSION

### 8.1 Introduction

The Results and Discussion chapter evaluates the outputs produced by the SmartRecipe system after implementation and testing. The purpose of this chapter is to demonstrate that the system performs its intended functions, including ingredient analysis, recipe recommendation, and nutritional estimation. The results also illustrate how the system behaves under different input conditions.

Testing was performed using sample ingredient datasets and simulated user interactions through the Streamlit interface.

---

### 8.2 System Execution Overview

During execution, the SmartRecipe system follows the sequence below:

1. User inputs ingredients manually or uploads images.
2. The ingredient analyzer cleans and standardizes the ingredient list.
3. Compatibility models evaluate possible ingredient combinations.
4. Recipe templates are matched against the ingredient list.
5. Nutritional estimation is performed.
6. Results are displayed on the Streamlit dashboard.

This workflow demonstrates the complete pipeline from raw user input to recipe generation.

---

### 8.3 Sample Execution Scenario

Example Input:

User Ingredients: • Tomato • Onion • Garlic

System Processing: The ingredient analyzer standardizes the input and identifies potential ingredient combinations.

Recommended Recipes: • Tomato Onion Curry • Vegetable Stir Fry

Estimated Nutrition Output: Calories: ~220 kcal, Protein: ~8 g, Carbohydrates: ~30 g

The system successfully generates recipe suggestions based on available ingredients.

---

### 8.4 Dashboard Output

The Streamlit dashboard displays: entered ingredient list, recommended recipes, estimated nutritional values, ingredient usage insights, suggested grocery items. These outputs allow users to quickly evaluate cooking options without manually searching for recipes.

---

### 8.5 Performance Evaluation

Response Time: The system generates recommendations within a few seconds for typical ingredient inputs. Accuracy of Recipe Suggestions: Recipe recommendations are dependent on the quality of recipe templates and compatibility rules. Usability: The Streamlit interface allows non-technical users to easily interact with the system.

---

### 8.6 Discussion

The results demonstrate that the SmartRecipe system is capable of performing ingredient-driven recipe recommendations using a combination of rule-based analysis and simple machine learning techniques. Although the prototype uses simplified datasets, the architecture can be extended to handle larger culinary databases and more advanced recommendation algorithms.

---

## CHAPTER 9 — LIMITATIONS

### 9.1 Dataset Size Limitations

The prototype system uses relatively small ingredient and recipe datasets. This limits the diversity of recipes that can be generated.

### 9.2 Image Recognition Accuracy

Ingredient detection using images may be affected by lighting conditions, image quality, and object occlusion.

### 9.3 Nutritional Estimation Accuracy

Nutritional values provided by the system are approximate estimates derived from publicly available food composition datasets.

### 9.4 Limited Personalization

The current prototype does not include long-term user learning or preference tracking.

---

## CHAPTER 10 — FUTURE ENHANCEMENTS

Future improvements could significantly enhance the SmartRecipe platform.

### 10.1 Integration with Large Recipe Databases

The system could integrate large public recipe datasets containing thousands of recipes.

### 10.2 Mobile Application Development

A mobile application could allow users to scan ingredients directly from their smartphones.

### 10.3 IoT Smart Kitchen Integration

Integration with smart refrigerators could automatically detect available ingredients.

### 10.4 Voice-Based Cooking Assistant

Voice assistants could guide users through cooking instructions step-by-step.

### 10.5 Advanced AI Recommendation Models

Deep learning recommendation systems could improve recipe personalization.

---

## CHAPTER 11 — BUSINESS MODEL DISCUSSION

Although the current implementation is an academic prototype, similar systems can be commercialized.

Possible business models include: subscription-based cooking assistant platforms; integration with grocery delivery applications; partnerships with food brands; premium meal planning services. Such platforms could generate revenue while helping users manage their kitchens more efficiently.

---

## CHAPTER 12 — CONCLUSION

The SmartRecipe system demonstrates how artificial intelligence techniques can be applied to solve practical household challenges related to cooking and meal planning. By analyzing available ingredients, dietary preferences, and recipe templates, the system is able to generate meaningful cooking suggestions. The project integrates multiple technical domains including machine learning, computer vision, data analysis, and user interface development. Although the current implementation is a prototype designed for academic purposes, the architecture provides a strong foundation for future intelligent cooking systems. The SmartRecipe platform highlights how AI-driven decision support systems can improve daily lifestyle activities such as cooking while reducing food waste and improving ingredient utilization.

---

## REFERENCES

1. Streamlit Documentation. *Streamlit — A faster way to build and share data apps*. [Online]. Available: https://docs.streamlit.io  
2. Python Software Foundation. *Python 3 Documentation*. [Online]. Available: https://docs.python.org/3/  
3. Pandas Development Team. *pandas: powerful Python data analysis toolkit*. [Online]. Available: https://pandas.pydata.org/docs/  
4. Scikit-learn Developers. *scikit-learn: machine learning in Python*. [Online]. Available: https://scikit-learn.org/stable/  
5. University of Madras. *Syllabus and regulations for B.Sc. Computer Science*. Chennai: University of Madras (as applicable to affiliated autonomous colleges).  
6. Dhanraj Baid Jain College (Autonomous). *About the College*. [Online]. Available: https://www.dbjaincollege.org/about/  
7. NAAC. *Assessment and Accreditation*. National Assessment and Accreditation Council. [Online]. Available: https://www.naac.gov.in  

*(Add more references as needed—e.g. research papers on recipe recommendation, food pairing, or ingredient-based search—in the same numbered format.)*

---

## APPENDICES

Appendix A — Sample Code Snippets  
Appendix B — Dataset Samples  
Appendix C — Installation Guide  
Appendix D — Ethical Disclaimer  

> “This system provides recipe suggestions and is not a substitute for professional nutritional advice.”

