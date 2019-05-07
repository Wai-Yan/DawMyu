import base64
import requests
import os
import sys
import platform


def prepareImage(pathToImage):
    print(pathToImage)

    with open(pathToImage, 'rb') as imgFile:
        image = base64.b64encode(imgFile.read())

    decodedImage = image.decode("utf-8")

    return decodedImage


def placeGoogleOrder(imageAsString, apiKey):

    # Request JSON
    googleOrder = {
      "requests": [
        {
          "image": {
            "content": imageAsString
          },
          "features": [
            {
              "type": "TEXT_DETECTION",
              "maxResults": 1
            }
          ]
        }
      ]
    }

    googleUrl = 'https://vision.googleapis.com/v1/images:annotate?key=' + apiKey
    result = requests.post(googleUrl, data=None, json=googleOrder)

    try:
        payload = result.json()['responses'][0]['textAnnotations'][0]['description']
        return payload
    except:
        print('This page does not have any text, results are empty')
        return ''


def writeIntoResultFile(extractedText, index, resultFileName):

    resultFileName += '.txt'
    textFile = open(resultFileName, 'a', encoding='utf-8')

    textFile.write(index + '\n')

    underscoreBorder = generateUnderscoreBorder(len(index))
    textFile.write(underscoreBorder + '\n')

    textFile.write(extractedText + '\n' + '\n')

    textFile.close()


def writeTitle(title):
    textFile = open(title + '.txt', 'a', encoding='utf-8')

    underscoreBorder = generateUnderscoreBorder(len(title))

    textFile.write(title + '\n' + underscoreBorder + '\n\n')


def generateUnderscoreBorder(contentLength):
    underscoreBorder = ''

    for i in range(contentLength):
        underscoreBorder += '-'

    return underscoreBorder


def changePathName(image):

    if (platform.system() == 'Darwin'):
        imagePath = folderPath + '/' + image

    elif (platform.system() == 'Windows'):
        imagePath = folderPath + '\\' + image

    return imagePath


def main(folderPath, resultFileName, apiKey):

    writeTitle(resultFileName)

    for image in os.listdir(folderPath):

        imagePath = changePathName(image)      
        imageAsString = prepareImage(imagePath)

        print('Sending ' + image + ' to Google...')
        extractedText = placeGoogleOrder(imageAsString, apiKey)

        print('Writing results of ' + image + ' into guide...' + '\n')
        writeIntoResultFile(extractedText, image, resultFileName)

    print('Done! ' + resultFileName +
          ' should be in this project\'s directory.')


# ~~~~
# Main
# ~~~~

try:
    folderPath = sys.argv[1]
    resultFileName = sys.argv[2]
    apiKey = sys.argv[3]

except:
    print('Remember to add these arguments: \n'
          '1| Folder path to the images \n'
          '2| Desired name of resultant text file \n'
          '3| Your Google API Key \n\n'
          'Try putting quotes around each individual argument')
    sys.exit()

main(folderPath, resultFileName, apiKey)
