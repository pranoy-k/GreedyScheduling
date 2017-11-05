

# -*- coding: utf-8 -*-
"""
Created on Mon May 01 16:17:34 2017

@author: kpranoy
"""

path = "jobs.txt"
jobList = []
sortedjobList = []

def populateJobList():
    global jobList
    with open(path) as jobs:
        l= 0
        for job in jobs:
            if(l!=0):
                 job = job.split()
                 W,L = int(job[0]),int(job[1])
                 jobList.append((W/L,W,L))
            l+=1
        jobList = sorted(jobList, key=lambda job: job[0],reverse=1)



def main():
    global jobList
    populateJobList()
        
    i=0
    temp = []
    global sortedjobList
    while(i<len(jobList)):
#        j = i
        temp.append(jobList[i])
        while(((i+1)<len(jobList)) and (jobList[i][0] == jobList[i+1][0])):
            temp.append(jobList[i+1])
            i+=1
#        while(j<=i);
#            heapq.heappush(temp,(jobList[j][1][0],[jobList[j][1][0],jobList[j][1][1],jobList[j][0]))
#            j+=1
        temp = sorted(temp, key=lambda k:k[1],reverse=1)
        sortedjobList = sortedjobList + temp
        temp = []
        i+=1
#    i=0
#    for job in sortedjobList:
##        print job
#        i+=1
#        if(i<50):
#            print (job)

    sum = 0
    length=0
    i = 0
    for job in sortedjobList:
        length+=job[2]
        sum+=(length*job[1])
    
    print("The SUM is ",sum)        
main()
