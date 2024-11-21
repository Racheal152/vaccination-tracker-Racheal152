# **Vaccination Management System**

## **Project Overview**

The Vaccination Management System is designed to manage vaccination records for individuals, doctors, and admins. The application features a backend built with Python (using MySQL as the database) that allows for user registration, login, and the management of vaccination records. The system has been developed to support different types of users (admins, doctors, and individuals), each with specific roles and privileges.

The backend functionality is fully implemented, but the project has not yet included a frontend or deployment.

---

## **Features Implemented**

### 1. **User Registration & Authentication**

- **User Types**: The system supports three types of users:
  - **Admin**: Admin users have access to manage all aspects of the system, including adding and managing doctors, individuals, and vaccination records.
  - **Doctor**: Doctors can manage vaccination records for individuals, including creating, updating, and viewing them.
  - **Individual**: Individuals can view their vaccination status but do not have permission to modify records.

- **Registration**: Each user type can register with their details, including email, password, and other personal information.
- **Login**: Users can log in by entering their email and password. The system verifies their credentials, and based on their role, grants access to the appropriate functionalities.

### 2. **Database**

The database for this system uses MySQL and consists of six tables:

- **Users**: Contains basic information about all users (admin, doctor, individual).
- **Doctors**: Stores details specific to doctors (specialization, license number).
- **Individuals**: Stores details specific to individuals (age, gender, medical conditions).
- **Admins**: Stores details specific to admins.
- **Vaccinations**: Contains vaccination information (e.g., vaccine name, vaccination date).
- **Vaccination_Records**: Links individuals to their vaccination data and tracks vaccine status.

#### **Database Tables**

1. **Users**:  
   - **Columns**: `id`, `email`, `password_hash`, `role`  
   - **Description**: Stores general user information such as email, hashed password, and user role (admin, doctor, individual).
   - **Relations**: This table serves as the main entry point for authentication, and the system queries it to determine which table (doctors, individuals, admins) the user belongs to.

2. **Doctors**:  
   - **Columns**: `id`, `user_id` (foreign key to Users), `specialization`, `license_number`  
   - **Description**: Stores doctor-specific details, including their specialization and medical license number. The `user_id` foreign key relates to the Users table.

3. **Individuals**:  
   - **Columns**: `id`, `user_id` (foreign key to Users), `age`, `gender`, `address`, `medical_conditions`, `allergies`  
   - **Description**: Contains personal information about individuals, including age, gender, medical conditions, and allergies. The `user_id` foreign key connects to the Users table.

4. **Admins**:  
   - **Columns**: `id`, `user_id` (foreign key to Users), `phone_number`, `first_name`, `last_name`  
   - **Description**: Stores information about admins such as their name and phone number. It references the `user_id` from the Users table.

5. **Vaccinations**:  
   - **Columns**: `id`, `vaccine_name`, `manufacturer`, `date_approved`  
   - **Description**: This table contains details about the vaccines, including the name, manufacturer, and date of approval.

6. **Vaccination_Records**:  
   - **Columns**: `id`, `individual_id` (foreign key to Individuals), `vaccination_id` (foreign key to Vaccinations), `vaccination_date`, `status`  
   - **Description**: This table tracks which vaccines have been administered to which individuals and their vaccination status (e.g., pending, completed). It connects individuals and vaccinations through the `individual_id` and `vaccination_id` foreign keys.

---

## **Features Yet to be Implemented (Optional Features)**

### 1. **Frontend Interface**  
The project currently only has a backend that works through the command line. The frontend interface is not implemented yet, but the system can be connected to a web-based frontend or a desktop interface in the future.

- **What’s Missing**: No HTML, CSS, or JavaScript frontend has been developed for this project. A user interface for interacting with the system is still required.

### 2. **Deployment**
Currently, the system is running locally and has not been deployed on a live server.

- **What’s Missing**: The application has not been deployed on any cloud platform or hosting service. A deployment process using platforms like **Heroku** or **AWS** has not been set up yet.

### 3. **Data Visualization**  
There is no feature for visualizing vaccination data, trends, or reports. Although the database supports vaccination records, there are no tools for generating charts or data visualizations.

- **What’s Missing**: A dashboard or reports system that visualizes vaccination statistics, such as vaccine types, completion rates, and trends over time.

### 4. **Cloud Database Hosting**
The database is hosted locally and has not been set up on a cloud service.

- **What’s Missing**: A cloud-hosted database (e.g., **AWS RDS**, **Google Cloud SQL**) to allow for remote access and scalability.

---

## **Installation & Setup Instructions**

To run this project locally, follow the steps below:

### **Requirements**:
- Python 3.12.6 installed.
- MySQL Database installed.
- Required Python libraries (e.g., `mysql-connector`, `hashlib`).

### **Setup Steps**:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/vaccination-management-system.git
   ```

2. **Set up the MySQL database**:
   - Create a database named `vaccination_tracker`.
   - Run the SQL queries to create the tables (`users`, `doctors`, `individuals`, `admins`, `vaccinations`, and `vaccination_records`) as per the schema provided in the code.
   - Insert sample data if necessary.

3. **Install dependencies**:
   Install required Python libraries:
   ```bash
   pip install mysql-connector
   ```

4. **Run the backend code**:
   - Navigate to the project folder and run the Python script:
   ```bash
   python main.py
   ```

5. **Test the system**:
   - The command-line interface will allow users to register and log in as admins, doctors, or individuals, and manage vaccination records.

---

## **Testing & Validation**

### **Core Functionality Tested**:
- **User Registration**: Successfully registers admins, doctors, and individuals.
- **Login**: Verifies user credentials and grants access based on user roles.
- **Vaccination Records**: Admins and doctors can add and update vaccination records for individuals.
- **Error Handling**: Proper validation of input data during registration and login.

---

## **Future Improvements**

Although the core features are implemented, the following features are planned for future work:

- **Frontend Interface**: Develop a user-friendly web interface using **HTML**, **CSS**, and **JavaScript** (or a framework like React).
- **Data Visualization**: Implement data visualization for tracking vaccination trends.
- **Deployment**: Host the application on a cloud platform such as **Heroku** or **AWS**.
- **Cloud Database**: Migrate the database to a cloud-hosted service for remote access and scalability.
