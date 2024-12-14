import jenkins
import xml.etree.ElementTree as ET

try:
    server = jenkins.Jenkins('http://54.237.237.41:8080/', username='devops', password='devops')
    jobs = server.get_all_jobs()
    job_list = []
    for j in jobs:
        job_list.append(j.get('fullname'))
        #print('*'*100)
    #print(job_list)
    #print(server.get_job_config('geoapp'))
    #print(dir(server))
    tree = ET.parse(server.get_job_config('geoapp'))
    root = tree.getroot()
    
    #find the specific element
    element = root.find('<url>')
    
    #get the text of the element
    url = element.text
    
    print(text)
    
except:
    print("please double check your credentials or url")
    


    
