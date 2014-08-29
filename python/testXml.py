import os
import xml.dom.minidom as xxxml


if __name__ == "__main__":

    folder = "./"
    searchPath = "firmware/fw/resource/UI5/"
    root = xxxml.parse(folder+"dynamic/contentsUI5.xml")
    
  
    node = root.getElementsByTagName("file")


    index = 0
    for elem in root.getElementsByTagName("file"):
        fileElem = elem.getElementsByTagName("file_name")

        if fileElem is None:
            raise "error"

        fileName = fileElem[0].childNodes[0].data


        pathElem = elem.getElementsByTagName("location")
        if len(pathElem) > 0:
            path =  pathElem[0].childNodes[0].data
            filePath = "%s/%s/%s/%s"%(folder, searchPath, path, fileName)

            if not os.path.exists(filePath):
                print "file not found", filePath
            else:
                index += 1


    print index





