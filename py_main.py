#!/usr/bin/python -tt

import boto3
import pprint

#for compare_faces call
SIMILARITY_THRESHOLD = 85


def main():
    if __name__ == '__main__':
        #credentials are handled by ~/.aws/credentials file
        client = boto3.client('rekognition' )
        
        #test print 
        #print(SIMILARITY_THRESHOLD)
        
        # Open source image in the project folder
        with open('source.jpg', 'rb') as source_image:
            source_bytes = source_image.read()
    
        # Open target image in the project folder
        with open('target.jpg', 'rb') as target_image:
            target_bytes = target_image.read()
        
        response = client.compare_faces(
                       SourceImage={ 'Bytes': source_bytes },
                       TargetImage={ 'Bytes': target_bytes },
                       SimilarityThreshold=SIMILARITY_THRESHOLD,
        )

        logFile = open('compareFace.txt', 'w')
        pp = pprint.PrettyPrinter(indent=4, stream=logFile)
        pp.pprint(response) 
        
        response = client.detect_faces(
                       Image={ 'Bytes': target_bytes },
                       Attributes=["ALL"],
        )
        
        logFile = open('detectFace.txt', 'w')
        pp = pprint.PrettyPrinter(indent=4, stream=logFile)
        pp.pprint(response) 
        
    print("FIN!")

main()
    