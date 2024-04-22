# Secure Password Manager

Protect your valuable online credentials with the Secure Password Manager. This Python-based application offers a robust solution for safely storing and retrieving passwords for various websites and applications. Built with cryptography techniques, it ensures that your sensitive information remains encrypted and secure.

## Key Features

1. **Encryption**: Utilizes the Fernet encryption algorithm to securely encrypt passwords before storing them in the database, ensuring confidentiality and data integrity.
   
2. **Master Password Protection**: Safeguard your stored passwords with an additional layer of security by requiring a master password for access. This feature prevents unauthorized users from accessing your sensitive information.
   
3. **Flexible Password Retrieval**: Easily retrieve passwords for specific websites or applications by providing the relevant site or app name, along with the master password for authentication.
   
4. **Dynamic Password Management**: Seamlessly create, update, and manage passwords for different accounts and platforms within a centralized and user-friendly interface.
   
5. **Secret Code Authentication**: Enhance security by associating a secret code with the master password, adding an extra level of protection against potential threats.
   
6. **Database Persistence**: Utilizes MySQL database to store encrypted passwords and master password details persistently, ensuring data availability across sessions.

## Why Choose Secure Password Manager?

- **Security First**: Prioritizes the security and confidentiality of user data through robust encryption techniques and stringent access controls.
  
- **User-Friendly Interface**: Offers an intuitive and straightforward user interface, making it easy for users to manage their passwords without any technical expertise.
  
- **Customizable**: Allows users to customize their master password and secret code, empowering them to create unique and memorable security credentials.
  
- **Open-Source**: Available as an open-source project on GitHub, encouraging community contributions, feedback, and enhancements to further improve its functionality and security.

## Get Started

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure your MySQL database credentials in the `config.py` file.
4. Run the application using `python password manager.py` and follow the on-screen instructions.

Take control of your online security today with the Secure Password Manager. Protect your passwords, safeguard your accounts, and stay one step ahead of cyber threats.
