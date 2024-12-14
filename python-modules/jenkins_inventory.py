import jenkins
import xml.etree.ElementTree as ET
import csv

# Jenkins server details
JENKINS_URL = 'http://54.237.237.41:8080/'
USERNAME = 'devops'
PASSWORD = 'devops'

# Connect to the Jenkins server
server = jenkins.Jenkins(JENKINS_URL, username=USERNAME, password=PASSWORD)

def fetch_jenkins_inventory():
    try:
        # Get all jobs from Jenkins
        jobs = server.get_jobs()

        # Inventory list to store job details
        inventory = []

        for job in jobs:
            job_name = job['name']
            print(f"Processing job: {job_name}")

            # Fetch job configuration (XML)
            job_config = server.get_job_config(job_name)
            root = ET.fromstring(job_config)

            # Extract VCS URL
            vcs_url = None
            for scm in root.findall('.//scm'):
                if 'url' in scm.attrib:
                    vcs_url = scm.attrib['url']
                else:
                    # Check nested tags for URL
                    url_elem = scm.find('.//url')
                    if url_elem is not None:
                        vcs_url = url_elem.text

            # Append job info to inventory
            inventory.append({'Job Name': job_name, 'VCS URL': vcs_url})

        # Save inventory to a CSV file
        with open('jenkins_inventory.csv', 'w', newline='') as csvfile:
            fieldnames = ['Job Name', 'VCS URL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(inventory)

        print("Inventory saved to 'jenkins_inventory.csv' successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_jenkins_inventory()
