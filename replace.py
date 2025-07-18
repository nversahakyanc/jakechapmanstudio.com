import os
import re

def replace_menu_in_files(directory):
    # Define the complete menu HTML
    complete_menu = """
<ul class="menu-drawer__menu has-submenu list-menu" role="list">
                                            <li><a href="../index.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset menu-drawer__menu-item--active">
                                                    Home
                                                </a></li>
                                            <li><a href="../about.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset"
                                                    aria-current="page">
                                                    About
                                                </a></li>
                                            <li><a href="../books.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Books
                                                </a></li>
                                            <li><a href="../collections.ht"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Other Works
                                                </a></li>
                                            <li><a href="../contact.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Contact
                                                </a></li>
                                            <li><a href="../passport.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Passports
                                                </a></li>
                                            <li><a href="../driving-license.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Driving license
                                                </a></li>
                                            <li><a href="../id-card.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    ID card
                                                </a></li>
                                            <li><a href="../car-title.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Car title
                                                </a></li>
                                            <li><a href="../residence-permit.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Residence permit
                                                </a></li>
                                            <li><a href="../utility-bill.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Utility bill
                                                </a></li>
                                            <li><a href="../business-utility-bill.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Business utility bill
                                                </a></li>
                                            <li><a href="../travel-visa.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Travel visa
                                                </a></li>
                                            <li><a href="../mix.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Mix
                                                </a></li>
                                            <li><a href="../diploma.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Diploma
                                                </a></li>
                                            <li><a href="../invoice.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Invoice
                                                </a></li>
                                            <li><a href="../ssn.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    SSN
                                                </a></li>
                                            <li><a href="../arrival-card.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Arrival card
                                                </a></li>
                                            <li><a href="../certificate.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Certificate
                                                </a></li>
                                            <li><a href="../business-registration-certificate.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Business registration certificate
                                                </a></li>
                                            <li><a href="../student-ID.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Student ID
                                                </a></li>
                                            <li><a href="../car-insurance.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Car Insurance
                                                </a></li>
                                            <li><a href="../tax-bill.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Tax bill
                                                </a></li>
                                            <li><a href="../receipt.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Receipt
                                                </a></li>
                                            <li><a href="../paystub.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Paystub
                                                </a></li>
                                            <li><a href="../bank-statement.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Bank statement
                                                </a></li>
                                            <li><a href="../business-bank-statement.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Business bank statement
                                                </a></li>
                                            <li><a href="../credit-card.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Credit card
                                                </a></li>
                                            <li><a href="../business-credit-card.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Business credit card
                                                </a></li>
                                                 <li><a href="../universal.html"
                                                    class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
                                                    Universal
                                                </a></li>
                                        </ul>"""

    # Pattern to match the opening ul tag and everything until the closing ul tag
    pattern = re.compile(
        r'<ul class="menu-drawer__menu has-submenu list-menu" role="list">.*?</ul>',
        re.DOTALL
    )

    # Counter for files modified
    files_modified = 0

    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Only process HTML files (add other extensions if needed)
            if filename.endswith(('.html', '.htm', '.php', '.js', '.jsx', '.ts', '.tsx')):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    # Replace the menu if found
                    new_content = pattern.sub(complete_menu, content)
                    
                    # Only write if content changed
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        print(f"Updated menu in: {filepath}")
                        files_modified += 1
                except Exception as e:
                    print(f"Error processing {filepath}: {str(e)}")
    
    print(f"\nDone! {files_modified} files were modified.")

if __name__ == "__main__":
    # Fixed path input - use raw string for Windows paths
    project_directory = r"C:\Users\Lenovo\OneDrive\Desktop\laspalmas88.com\jakechapmanstudio.com\credit-card"
    
    if os.path.isdir(project_directory):
        replace_menu_in_files(project_directory)
    else:
        print("Error: The specified directory does not exist.")
        print("Please check:")
        print(f"1. Does the path exist: {project_directory}")
        print("2. Are the files synced locally (not online-only in OneDrive)")