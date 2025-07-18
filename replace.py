import os
import re

def replace_menu_in_files(directory):
    # Define the complete menu HTML
    complete_menu = """
<ul class="list-menu list-menu--inline" role="list">
                        <li><a href="../index.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Home</span>
                            </a></li>
                        <li><a href="../about.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>About</span>
                            </a></li>
                        <li><a href="../books.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Books</span>
                            </a></li>
                        <li><a href="../collections.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Other Works</span>
                            </a></li>
                        <li><a href="../contact.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Contact</span>
                            </a></li>
                        <li><a href="../passport.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Passport</span>
                            </a></li>
                        <li><a href="../driving-license.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Driving license</span>
                            </a></li>
                        <li><a href="../id-card.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>ID card</span>
                            </a></li>
                        <li><a href="../car-title.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Car title</span>
                            </a></li>
                        <li><a href="../residence-permit.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Residence permit</span>
                            </a></li>
                        <li><a href="../utility-bill.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Utility bill</span>
                            </a></li>
                        <li><a href="../business-utility-bill.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Business utility bill</span>
                            </a></li>
                        <li><a href="../travel-visa.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Travel visa</span>
                            </a></li>
                        <li><a href="../mix.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Mix</span>
                            </a></li>
                        <li><a href="../diploma.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>diploma</span>
                            </a></li>
                        <li><a href="../invoice.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Invoice</span>
                            </a></li>
                        <li><a href="../ssn.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>SSN</span>
                            </a></li>
                        <li><a href="../arrival-card.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Arrival card</span>
                            </a></li>
                        <li><a href="../certificate.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Certificate</span>
                            </a></li>
                        <li><a href="../business-registration-certificate.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Business registration certificate</span>
                            </a></li>
                        <li><a href="../student-ID.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Student ID</span>
                            </a></li>
                        <li><a href="../car-insurance.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Car Insurance</span>
                            </a></li>
                        <li><a href="../tax-bill.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Tax bill</span>
                            </a></li>
                        <li><a href="../receipt.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Receipt</span>
                            </a></li>
                        <li><a href="../paystub.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Paystub</span>
                            </a></li>
                        <li><a href="../bank-statement.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Bank statement</span>
                            </a></li>
                        <li><a href="../business-bank-statement.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Business bank statement</span>
                            </a></li>
                        <li><a href="../credit-card.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Credit card</span>
                            </a></li>
                        <li><a href="../business-credit-card.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Business credit card</span>
                            </a></li>
                            <li><a href="../universal.html"
                                class="header__menu-item header__menu-item list-menu__item link link--text focus-inset">
                                <span>Universal</span>
                            </a></li>
                    </ul>"""

    # Pattern to match the opening ul tag and everything until the closing ul tag
    pattern = re.compile(
        r'<ul class="list-menu list-menu--inline" role="list">.*?</ul>',
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
    project_directory = r"C:\Users\eknya\Desktop\git\jakechapmanstudio.com\student-ID"
    
    if os.path.isdir(project_directory):
        replace_menu_in_files(project_directory)
    else:
        print("Error: The specified directory does not exist.")
        print("Please check:")
        print(f"1. Does the path exist: {project_directory}")
        print("2. Are the files synced locally (not online-only in OneDrive)")