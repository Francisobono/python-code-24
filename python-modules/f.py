import jenkins
import xml.etree.ElementTree as ET
import sys
import csv

try:
    # Connect to Jenkins server
    server = jenkins.Jenkins('http://54.237.237.41:8080/', username='devops', password='devops')
    
    # Get all jobs
    jobs = server.get_all_jobs()
    job_list = []
    for j in jobs:
        job_list.append(j.get('fullname'))
    
    print("Jobs on Jenkins server:")
    #print(job_list)
    # Fetch the job config XML for the 'geoapp' job
    jobs_url =[]
    for job in job_list:
        job_config_xml = server.get_job_config(job)
        root = ET.fromstring(job_config_xml)
        # Find the Git URL
        scm = root.find(".//scm")
        
        if scm is not None:
            url_element = scm.find(".//url")
            if url_element is not None:
                url = url_element.text
                #print(f"\nGit URL for job '{job}': {url}")
                jobs_url.append([job,url])
    print(jobs_url)
    with open("jenkins_inv.csv", 'w', newline='') as f:
        pen = csv.writer(f)  
        pen.writerow(["JOB_NAME", "JOBS_CVS_URL"])
        for line in jobs_url:
            pen.writerow(line)
                       
except Exception as e:
        print(f"An error occurred: {e}")
