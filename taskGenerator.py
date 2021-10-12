from os import path
from pydriller import RepositoryMining
from datetime import date, timedelta
import csv
import copy
from dateutil.relativedelta import relativedelta
import argparse
import os


idsCommitRelease = {}

#  cassandra
idsCommitRelease["cassandra"] = [
    "1f91e99223b0d1b7ed8390400d4a06ac08e4aa85",

    "533193a7b82c98814567c735f13a0e33c58424b1",
    "03045ca22b11b0e5fc85c4fabd83ce6121b5709b",
    "96f407bce56b98cd824d18e32ee012dbb99a0286",

    "e848d47ed171f20ccd8cf5e20d9e188ede85c17c"
]

#  egit
idsCommitRelease["egit"] = [
    "dfbdc456d8645fc0c310b5e15cf8d25d8ff7f84b",

    "3104c7a3af566617c32172f956eb57d0b135d3bf",
    "1f07f085d6bcae0caf372fffec19583ac5615d3b",
    "f85dc228e3e67b229c978f751a8723a5c810738b",
    "48712bdfa849e1afd0071b937f0b2bef04767610",
    "ba0bcbfe69b2803c843c19b6e800b2525b227cb2",

    "08c530ec099610334a4794f7fe7ed33cc619ef4f"
]


#   jgit
idsCommitRelease["jgit"] = [
    "1a6964c8274c50f0253db75f010d78ef0e739343",

    "b26ff6ebd623f7f3bf9b099ce10330d2964cc33b",
    "aacd4f721bba97eda3756e2fcbd71b5e57b3673a",
    "f384644774ae01823e850c862aeda5bddb4a4326",
    "4f221854556991e3394b3a71e77ee0b771b1500b",
    "e729a83bd24bbc25f7ac209baee01f561fe218c8",

    "91b2e167a2341d41212ea801943fb82a148e3b7f"
]


#   linuxtools
idsCommitRelease["linuxtools"] = [
    "e3ea1e9cc32a55b79c2735f36a07c90975bec67d",

    "b1172eebee348db6cd979533f0d38a67725c7da8",
    "2aa4892cece1fc393f8bec3083a6303912d17f16",
    "38b6b6787381da5d46cb9006c451a2086c64a4d2",
    "e3de351ca7ffd1bf722c9f0e2e86998cf1160bae",
    "4d86c7a081b74595b925ffa64c9578e36b0f7374",
    "fc1655d0c62b3ea7f2695f49c0f159d762bb4f27",
    "1c9cc481d11079740a3d309d7bcb9209757feaab",
    "65dafd6be0291db5a63f1269184bfde54518c7c4",

    "7ff527db3a1f93059236c270e7566e6a97ffe380"
]


#   poi
idsCommitRelease["poi"]= [
    "6c234ab6c8d9b392bc93f28edf13136b3c053894",

    None,
    "0dd67eac90ac556235d5bfa1ec9e4e1265f30931",
    "2e335762bd306da833514d3a584c5f28ef8eb184",
    "333b47391399898dca8e91366d316c5a8aeb1809",

    "382714eccd92667fc83f70115b736c64ebff9700"
]


# realm-java
idsCommitRelease["realm-java"] = [
    "b03c621431fdc7e6e43566eeef505a32f5f6ce83"

    "eef492341a17351dc671b296bf7f1cd2c2ed32a4",
    "1f19a05f820c1e43a9a0e38d8e32b0d96920df7f",
    "66fb375b32b7db660c1d06fc7e27bf708d8cebab",
    "e26255b9c5248620861565eb3caf7c908c4f8277",
    "8740eb6ce5bfc8536be2b480988a6212f2ce8466",
    "8a022573a5b095c2ec887720bd73098475829766",
    "5e1cb707bf37a4c5fa03b45cd5a4fde39fed146d",

    "fd3446d65856fc46bebf1e0632dca3b8260e2d12"
]


# sonar-java
idsCommitRelease["sonar-java"]= [
    "9140081865d82e930a0dd58db68c590880733be1",

    "5ac4cf695248bc7385cb3377216cd86340bda0b0",
    "fb4e10dcf17447ecea699934cdef0cf2009b1a52",
    "65396a609ddface8b311a6a665aca92a7da694f1",
    "b653c6c8640ab3d6015d036a060f58e027a653af",
    "fe9584c9f7812edc46f32d29440fc81b85a597a4",
    "931433c0510b161974d4844679f7bf3c73bb3e37",

    "bec6fc71cf44a9e84e711f9df693b466335185f4"
]


#   wicket
idsCommitRelease["wicket"] = [
    None,

    None,
    None,
    None,
    None,
    None,
    "0d75ee57abb31b4db48c0396870aba39c4d9ddee",
    "98a3a6295f426aa25a121f914a41bf792df8fdb0",
    "5e789f1c98f6d57dba17f896c6220b0202af08a9",
    "c2802f3ef8df9833da63d144fb4ad03d59e31acc",

    "048e5681df960018722237ee6254273e839b5fd2"
]



def getCorrespondingCommit(idCommitFile):#file->method
    for commit in RepositoryMining(pathRepositoryFile, include_refs=True).traverse_commits():
        if(commit.hash==idCommitFile):
            dateCommitUntil = commit.committer_date
    idCommit = ""
    dateCommit = None
    for commit in RepositoryMining(pathRepositoryMethod, include_refs=True).traverse_commits():
        if(
            (dateCommit == None and commit.committer_date <= dateCommitUntil) or
            (dateCommit != None and dateCommit <= commit.committer_date and commit.committer_date <= dateCommitUntil)
        ):
            idCommit = commit.hash
            dateCommit = commit.committer_date
            #print("dateCommitUntil"+str(dateCommitUntil))
            #print("dateCommit"+str(dateCommit))
    return idCommit

records = []
def identifyCommit_rbr(releaseIndex):
    if(releaseIDs[releaseIndex-1]==None):
        return None
    if(releaseIDs[releaseIndex-2]==None):
        return None
    testCommitID          = releaseIDs[releaseIndex]
    trainCommitID         = releaseIDs[releaseIndex-1]
    previousTrainCommitID = releaseIDs[releaseIndex-2]
    if(releaseIndex-2<0 or previousTrainCommitID==None or trainCommitID ==None):
        return None
    test  = [
        "R"+str(releaseIndex)+"_r_test",
        "method",
        "metrics_isBuggy_hasBeenBuggy",
        trainCommitID,
        testCommitID,
        releaseIDs[len(releaseIDs)-1],
        getCorrespondingCommit(trainCommitID),
        getCorrespondingCommit(testCommitID),
        getCorrespondingCommit(releaseIDs[len(releaseIDs)-1])
    ]
    records.append(test)
    train = [
        "R"+str(releaseIndex)+"_r_train",
        "method",
        "metrics_isBuggy_hasBeenBuggy",
        previousTrainCommitID,
        trainCommitID,
        testCommitID,
        getCorrespondingCommit(previousTrainCommitID),
        getCorrespondingCommit(trainCommitID),
        getCorrespondingCommit(testCommitID)
    ]
    records.append(train)
def identifyCommit_cbc(commitHashes, releaseIndex, NumOfCommits):
    commitIDsTest = [None, None, None]
    commitIDsTest[1] = releaseIDs[releaseIndex]
    if(commitHashes.index(commitIDsTest[1])-NumOfCommits*2<0):
        return None
    commitIDsTest[0] = commitHashes[commitHashes.index(commitIDsTest[1])-NumOfCommits]
    commitIDsTest[2] = releaseIDs[len(releaseIDs)-1]
    test  = [
        "R"+str(releaseIndex)+"_c"+str(NumOfCommits) + "_test",
        "method",
        "metrics_isBuggy_hasBeenBuggy",
        commitIDsTest[0],
        commitIDsTest[1],
        commitIDsTest[2],
        getCorrespondingCommit(commitIDsTest[0]),
        getCorrespondingCommit(commitIDsTest[1]),
        getCorrespondingCommit(commitIDsTest[2]),
    ]
    records.append(test)
    count = 0
    while(0 < commitHashes.index(commitIDsTest[1])-NumOfCommits-NumOfCommits*count):
        commitIDsTrain = [None, None, None]
        commitIDsTrain[0] = commitHashes[commitHashes.index(commitIDsTest[1]) - NumOfCommits*2 -NumOfCommits*count]
        commitIDsTrain[1] = commitHashes[commitHashes.index(commitIDsTest[1]) - NumOfCommits   -NumOfCommits*count]
        commitIDsTrain[2] = commitIDsTest[1]
        train = [
            "R"+str(releaseIndex)+"_c"+str(NumOfCommits) + "_train_" + str(count),
            "method",
            "metrics_isBuggy_hasBeenBuggy",
            commitIDsTrain[0],
            commitIDsTrain[1],
            commitIDsTrain[2],
            getCorrespondingCommit(commitIDsTrain[0]),
            getCorrespondingCommit(commitIDsTrain[1]),
            getCorrespondingCommit(commitIDsTrain[2])
        ]
        records.append(train)
        count+=1
def identifyCommit_tbt(commits, releaseIndex, numOfMonths):
    commitIDsTest = [None, None, None]
    commitIDsTest[1] = releaseIDs[releaseIndex]
    commitIDsTest[2] = releaseIDs[len(releaseIDs)-1]
    testSince = commits[commitHashes.index(commitIDsTest[1])].committer_date - relativedelta(months = numOfMonths)
    testUntil = commits[commitHashes.index(commitIDsTest[1])].committer_date
    for commit in reversed(commits):
        if(testSince<=commit.committer_date and commit.committer_date<=testUntil):
            commitIDsTest[0] = commit.hash
    test  = [
        "R"+str(releaseIndex)+"_t"+str(numOfMonths) + "_test",
        "method",
        "metrics_isBuggy_hasBeenBuggy",
        commitIDsTest[0],
        commitIDsTest[1],
        commitIDsTest[2],
        getCorrespondingCommit(commitIDsTest[0]),
        getCorrespondingCommit(commitIDsTest[1]),
        getCorrespondingCommit(commitIDsTest[2])
    ]
    records.append(test)

    count = 0
    while(True):
        commitIDsTrain = [None, None, None]
        intervals = [
            [commits[commitHashes.index(commitIDsTest[1])].committer_date - relativedelta(months = numOfMonths*3 + numOfMonths*count), commits[commitHashes.index(commitIDsTest[1])].committer_date - relativedelta(months = numOfMonths*2 + numOfMonths*count)],
            [commits[commitHashes.index(commitIDsTest[1])].committer_date - relativedelta(months = numOfMonths*2 + numOfMonths*count), commits[commitHashes.index(commitIDsTest[1])].committer_date - relativedelta(months = numOfMonths*1 + numOfMonths*count)],
        ]
        for i in range(len(intervals)):
            for commit in reversed(commits):
                if(intervals[i][0] < commit.committer_date and commit.committer_date <= intervals[i][1]):
                    commitIDsTrain[i] = commit.hash
                    break
        commitIDsTrain[2] = commitIDsTest[1]
        if(commitIDsTrain[0]==None or commitIDsTrain[1]==None or commitIDsTrain[2]==None):
            break
        train = [
            "R"+str(releaseIndex)+"_t"+str(numOfMonths) + "_train_" + str(count),
            "method",
            "metrics_isBuggy_hasBeenBuggy",
            commitIDsTrain[0],
            commitIDsTrain[1],
            commitIDsTrain[2],
            getCorrespondingCommit(commitIDsTrain[0]),
            getCorrespondingCommit(commitIDsTrain[1]),
            getCorrespondingCommit(commitIDsTrain[2])
        ]
        records.append(train)
        count+=1

pathRepositoryMethod = None
pathRepositoryFile = None
releaseIDs = None
commitHashes = []

def main(nameProject, dirProject):
    global pathRepositoryMethod
    global pathRepositoryFile
    global releaseIDs
    pathRepositoryMethod = os.path.join(dirProject, "repositoryMethod")
    pathRepositoryFile = os.path.join(dirProject, "repositoryFile")
    releaseIDs = idsCommitRelease[nameProject]

    commits = []
    for commit in RepositoryMining(pathRepositoryFile, include_refs=True).traverse_commits():
        commitHashes.append(str(commit.hash))
        commits.append(commit)
    for releaseIndex in range(len(releaseIDs)):
        print("releaseID: "+str(releaseIndex))
        if(
            releaseIndex==0 or
            releaseIndex ==1 or
            releaseIndex == len(releaseIDs)-1 or
            releaseIDs[releaseIndex]==None
        ):
            continue
        print("numRelease: "+ str(releaseIndex))
        identifyCommit_rbr(releaseIndex)
        numOfCommitss = [500, 1000, 1500, 2000, 2500]
        for i, numOfCommits in enumerate(numOfCommitss):
            print("numOfCommits: "+ str(numOfCommits))
            identifyCommit_cbc(commitHashes, releaseIndex, numOfCommits)
        numOfMonthss = [1, 2, 3, 6, 12]
        for i, numOfMonths in enumerate(numOfMonthss):
            print("numOfMonths: "+ str(numOfMonths))
            identifyCommit_tbt(commits, releaseIndex, numOfMonths)
    with open(nameProject+'.csv', 'w') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(records)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Convert a git log output to json.
                                                 """)
    parser.add_argument('--nameProject', type=str)
    parser.add_argument('--dirProject', type=str)

    args = parser.parse_args()

    main(args.nameProject, args.dirProject)
