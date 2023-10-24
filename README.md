# Docket Management System

Welcome to the Docket Management System! This web application allows you to upload and manage docket data efficiently. Below are the instructions to set up and run the project along with screenshots of different views.

## Prerequisites
- Python 3.x
- Django (install dependencies using `pip install -r requirements.txt`)

## Instructions to Run the Project
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd dockerproject
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
4. **Access the Application:**
   - Go to `http://127.0.0.1:8000/` in your web browser.
   - Use the superuser credentials to access the admin panel (`http://127.0.0.1:8000/admin/`).

## Sample Excel File for Testing
You can use the sample Excel file [`export29913.xlsx`](https://github.com/lalithpraveen/dockerproject/files/13115129/export29913.xlsx) located in the `sample_data_excel` directory to test the application. To obtain the Excel file, simply follow this [link](https://github.com/lalithpraveen/dockerproject/files/13115129/export29913.xlsx). This file contains example docket data for upload, enabling you to evaluate the application's functionality.



## Screenshots

1. **Home Page - Upload Excel:**
   ![docket1](https://github.com/lalithpraveen/dockerproject/assets/82693110/4c4be02e-a48a-4dbf-8568-0ffb4d0eb565)

2. **Uploaded Docket Data (Partial View):**
  ![docket2](https://github.com/lalithpraveen/dockerproject/assets/82693110/3ae140e8-d21e-4540-b05a-7d876e2a7b34)

3. **Pagination of Docket Data Table:**
   ![docket3](https://github.com/lalithpraveen/dockerproject/assets/82693110/8a7d9299-101f-48e6-9ca5-54e6dae4f2fd)

4. **Created Dockets View (Empty State):**
   ![docket4](https://github.com/lalithpraveen/dockerproject/assets/82693110/4e3214a7-d55f-425f-9178-56f96bf43d6e)

5. **Create Docket Entry Form (Select Supplier):**  
  ![docket5](https://github.com/lalithpraveen/dockerproject/assets/82693110/c932ea23-1bc4-4993-8009-11be9d5e828e)

6. **Select Purchase Order (Show Description):**  
  ![docket6](https://github.com/lalithpraveen/dockerproject/assets/82693110/44e218df-6d6d-4288-9907-dbd8a15052b1)

7. **Created Dockets View (After Entries):**
   ![docket7](https://github.com/lalithpraveen/dockerproject/assets/82693110/888e2d01-e0f4-45ab-bf83-4a3479a00277)

## Project Overview
The Docket Management System is a web application developed using Django, allowing users to upload docket data from Excel files. The application provides the following features:

- **File Upload:** Users can upload Excel files containing docket data.
- **Docket List:** View and paginate the uploaded docket data.
- **Create Docket Entry:** Users can create new docket entries, selecting suppliers and associated purchase orders.
- **Display Descriptions:** Descriptions of selected purchase orders are dynamically displayed on the form.
- **View Created Dockets:** Users can view the created dockets with details like start time, end time, hours worked, rate per hour, supplier, purchase order, and description.

This application offers a user-friendly interface for managing docket data efficiently.

For any issues or queries, please contact the project maintainers. Happy docket managing!
