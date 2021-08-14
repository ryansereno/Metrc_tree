import csv
import sys
import treelib
from treelib import Node, Tree

while True:
    input_UID = input("\n Input UID: ")

    csv_file = open("Metrc Active & Inactive Inventory 10_2 - Sheet1.csv", "r")
    csv_reader = csv.DictReader(csv_file, delimiter = ",")

    #       Tie sorting functions into repeating loop
    #       use transient "n" variable to re-loop and redefine on each pass,
    #       until source package = " "

    input_UID_line = ()
    for line in csv_reader:
        if line["Tag"] == input_UID:
            input_UID_line = line           #fetches input UID
    csv_file.seek(0)

    input_UID_batchID = ()
    for line in csv_reader:
        if line["Tag"] == input_UID:
            if line["Batch Number"] == '':
                input_UID_batchID = line["Item"]  # if no batch number given, fetch Item name of given package
            else:
                input_UID_batchID = line["Batch Number"]
    csv_file.seek(0)

    Primary_source_packages = []
    for line in csv_reader:
            if line["Tag"] == input_UID:
                # if line["Source Packages"] == " ":
                    Primary_source_packages = line["Source Packages"]#fetches all source packages of input UID
                # elif line["Source Packages"] == "":
                #     Primary_source_packages = line["Item"]

    csv_file.seek(0)

    try:
        Source_packages_primary = Primary_source_packages.split(",") #converts above string to list of elements
    except AttributeError:
        Source_packages_primary = "Error/ No source package information available"

    Source_packages_primary_reformat = [element.strip(" ") for element in Source_packages_primary]
    #   ^reformat list of elements to remove leading empty space to negate mismatches

    Primary_source_batchIDs = []
    for i in Source_packages_primary_reformat: #Use transient variable like "i" or "element" to represent all elements in a list
        for line in csv_reader:
            if line["Tag"] == i:
                if line["Batch Number"] is None:
                    Primary_source_batchIDs.append(line["Item"])  # if no batch number given, fetch Item name of given package
                else:
                    Primary_source_batchIDs.append(line["Batch Number"])
        csv_file.seek(0)

    try:
        Primary_batches = Primary_source_batchIDs       #remove; no need to .split[","] list object
    except AttributeError:
        Primary_batches = "Error/ No batch information available"
    csv_file.seek(0)
    #append output of above to the end of Primary_batches list

########################### Use transient "i" variable #############################
    # while True:
    #     for i in list:
    #         for line in csv_reader:                             # do xyz
    #             if line["Tag"] == i:
    #                 [].append(line["Source Packages"])
    #             list2 = [element.split(",") for element in list]
    #             list3 = []
    #             for element in list2:
    #                 for i in element:
    #                     i.split(",")
    #                     list3.append(i)
    #             list4 = [element.strip(" ") for element in list3]
    #   try:
      #   for i in list:
      #       do xyz
      # except if null:
      #     sys.exit
#####################################################################################
    Secondary_source_packages = []
    for i in Source_packages_primary_reformat:
        for line in csv_reader:
            if line["Tag"] == i:
                Secondary_source_packages.append(line["Source Packages"])
        csv_file.seek(0)

    Secondary_source_packages_reformat1 = [element.split(",") for element in Secondary_source_packages]
    Secondary_source_packages_reformat2 = []            #^Use this one in the tree to help specify which source
                                                        #packages are associated with which package
    for element in Secondary_source_packages_reformat1:
        for i in element:
            i.split(",")
            Secondary_source_packages_reformat2.append(i)
    Secondary_source_packages_reformat3= [element.strip(" ") for element in Secondary_source_packages_reformat2]
    #   ^Use this for actual sorting of source packages

    # print(Secondary_source_packages, "\n", Secondary_source_packages_reformat, "\n", Secondary_source_packages_reformat3)

    Secondary_batchIDs = []
    for i in Secondary_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Secondary_batchIDs.append(line["Batch Number"])
        csv_file.seek(0)

    Tertiary_source_packages = []
    for i in Secondary_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Tertiary_source_packages.append(line["Source Packages"])
        csv_file.seek(0)

    Tertiary_source_packages_reformat1 = [element.split(",") for element in Tertiary_source_packages]
    Tertiary_source_packages_reformat2 = []            #^Use this one in the tree to help specify which source
                                                        #packages are associated with which package
    for element in Tertiary_source_packages_reformat1:
        for i in element:
            i.split(",")
            Tertiary_source_packages_reformat2.append(i)
    Tertiary_source_packages_reformat3= [element.strip(" ") for element in Tertiary_source_packages_reformat2]

    Tertiary_batchIDs = []
    for i in Tertiary_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Tertiary_batchIDs.append(line["Batch Number"])
        csv_file.seek(0)



    Quaternary_source_packages = []
    for i in Tertiary_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Quaternary_source_packages.append(line["Source Packages"])
        csv_file.seek(0)

    Quaternary_source_packages_reformat1 = [element.split(",") for element in Quaternary_source_packages]
    Quaternary_source_packages_reformat2 = []            #^Use this one in the tree to help specify which source
                                                        #packages are associated with which package
    for element in Quaternary_source_packages_reformat1:
        for i in element:
            i.split(",")
            Quaternary_source_packages_reformat2.append(i)
    Quaternary_source_packages_reformat3= [element.strip(" ") for element in Quaternary_source_packages_reformat2]

    Quaternary_batchIDs = []
    for i in Quaternary_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Quaternary_batchIDs.append(line["Batch Number"])
        csv_file.seek(0)

    Fifth_Order_source_packages = []
    for i in Quaternary_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Fifth_Order_source_packages.append(line["Source Packages"])
        csv_file.seek(0)

    Fifth_Order_source_packages_reformat1 = [element.split(",") for element in Fifth_Order_source_packages]
    Fifth_Order_source_packages_reformat2 = []            #^Use this one in the tree to help specify which source
                                                        #packages are associated with which package
    for element in Fifth_Order_source_packages_reformat1:
        for i in element:
            i.split(",")
            Fifth_Order_source_packages_reformat2.append(i)
    Fifth_Order_source_packages_reformat3 = [element.strip(" ") for element in Fifth_Order_source_packages_reformat2]

    Fifth_Order_batchIDs = []
    for i in Fifth_Order_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Fifth_Order_batchIDs.append(line["Batch Number"])
        csv_file.seek(0)

    Sixth_Order_source_packages = []
    for i in Fifth_Order_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Sixth_Order_source_packages.append(line["Source Packages"])
        csv_file.seek(0)

    Sixth_Order_source_packages_reformat1 = [element.split(",") for element in Sixth_Order_source_packages]
    Sixth_Order_source_packages_reformat2 = []            #^Use this one in the tree to help specify which source
                                                        #packages are associated with which package
    for element in Sixth_Order_source_packages_reformat1:
        for i in element:
            i.split(",")
            Sixth_Order_source_packages_reformat2.append(i)
    Sixth_Order_source_packages_reformat3 = [element.strip(" ") for element in Sixth_Order_source_packages_reformat2]

    Sixth_Order_batchIDs = []
    for i in Sixth_Order_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Sixth_Order_batchIDs.append(line["Batch Number"])
        csv_file.seek(0)

    Seventh_Order_source_packages = []
    for i in Sixth_Order_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Seventh_Order_source_packages.append(line["Source Packages"])
        csv_file.seek(0)

    Seventh_Order_source_packages_reformat1 = [element.split(",") for element in Seventh_Order_source_packages]
    Seventh_Order_source_packages_reformat2 = []            #^Use this one in the tree to help specify which source
                                                        #packages are associated with which package
    for element in Seventh_Order_source_packages_reformat1:
        for i in element:
            i.split(",")
            Seventh_Order_source_packages_reformat2.append(i)
    Seventh_Order_source_packages_reformat3 = [element.strip(" ") for element in Seventh_Order_source_packages_reformat2]

    Seventh_Order_batchIDs = []
    for i in Seventh_Order_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Seventh_Order_batchIDs.append(line["Batch Number"])
        csv_file.seek(0)

    Eighth_Order_source_packages = []
    for i in Seventh_Order_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Eighth_Order_source_packages.append(line["Source Packages"])
        csv_file.seek(0)

    Eighth_Order_source_packages_reformat1 = [element.split(",") for element in Eighth_Order_source_packages]
    Eighth_Order_source_packages_reformat2 = []            #^Use this one in the tree to help specify which source
                                                        #packages are associated with which package
    for element in Eighth_Order_source_packages_reformat1:
        for i in element:
            i.split(",")
            Eighth_Order_source_packages_reformat2.append(i)
    Eighth_Order_source_packages_reformat3 = [element.strip(" ") for element in Eighth_Order_source_packages_reformat2]

    Eighth_Order_batchIDs = []
    for i in Eighth_Order_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Eighth_Order_batchIDs.append(line["Batch Number"])
        csv_file.seek(0)

    Ninth_Order_source_packages = []
    for i in Eighth_Order_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Ninth_Order_source_packages.append(line["Source Packages"])
        csv_file.seek(0)

    Ninth_Order_source_packages_reformat1 = [element.split(",") for element in Ninth_Order_source_packages]
    Ninth_Order_source_packages_reformat2 = []            #^Use this one in the tree to help specify which source
                                                        #packages are associated with which package
    for element in Ninth_Order_source_packages_reformat1:
        for i in element:
            i.split(",")
            Ninth_Order_source_packages_reformat2.append(i)
    Ninth_Order_source_packages_reformat3 = [element.strip(" ") for element in Ninth_Order_source_packages_reformat2]

    Ninth_Order_batchIDs = []
    for i in Ninth_Order_source_packages_reformat3:
        for line in csv_reader:
            if line["Tag"] == i:
                Ninth_Order_batchIDs.append(line["Batch Number"])
        csv_file.seek(0)


    # def strip_and_split(x):
    #     return x.strip(" ")
    #
    #
    # tree3 = Tree()
    # tree3.create_node(input_UID, "Input")
    # for element in Source_packages_primary_reformat:
    #     primary_variable = str(Source_packages_primary_reformat.index(element)).join("Primary")
    #     tree3.create_node(element, primary_variable, parent = "Input")
    #     for element2 in Secondary_source_packages_reformat1[Source_packages_primary_reformat.index(element)]:
    #         secondary_variable = str(Secondary_source_packages_reformat1[Source_packages_primary_reformat.index(element)]).join("secondary")
    #         tree3.create_node(element2, element2, parent = primary_variable)
    #                                     # ^ need to fix this to make unique and prevent duplicates
    #         for element3 in Tertiary_source_packages_reformat1[Secondary_source_packages_reformat3.index(strip_and_split(element2))]:
    #             tertiary_variable = str(Tertiary_source_packages_reformat1[Secondary_source_packages_reformat3.index(strip_and_split(element2))]).join("tertiary")
    #         #     # ^ add second unique parameter to variable
    #             try:
    #                 tree3.create_node(element3, element3, parent = element2)
    #         #                                     # ^ need to fix this to make unique and prevent duplicates
    #             except:
    #                 tree3.create_node(element3, tertiary_variable.join("2"), parent = element2)
    #                                                             # ^include unique suffix in variable, do not use .join
    #             for element4 in Quaternary_source_packages_reformat1[Tertiary_source_packages_reformat3.index(strip_and_split(element3))]:
    #                 quaternary_variable = str(Quaternary_source_packages_reformat1[Tertiary_source_packages_reformat3.index(strip_and_split(element3))]).join("quaternary")
    #             #     # try:
    #             #     #     tree3.create_node(element4, quaternary_variable, parent = tertiary_variable)
    #             #     #     # ^ need to fix this to make unique and prevent duplicates
    #             #     # except:
    #             #     #     tree3.create_node(element4, quaternary_variable.join("2"), parent = tertiary_variable)
    # tree3.show()


    tree2 = Tree()
    tree2.create_node(input_UID_batchID, "input")
    tree2.create_node(Primary_batches, "Primary", parent = "input")
    tree2.create_node(Secondary_batchIDs, "Secondary", parent = "Primary")
    tree2.create_node(Tertiary_batchIDs, "Tertiary", parent = "Secondary")
    tree2.create_node(Quaternary_batchIDs, "Quaternary", parent = "Tertiary")
    tree2.create_node(Fifth_Order_batchIDs, "5th order", parent = "Quaternary")
    tree2.create_node(Sixth_Order_batchIDs, "6th order", parent = "5th order")
    tree2.create_node(Seventh_Order_batchIDs, "7th order", parent = "6th order")
    tree2.create_node(Eighth_Order_batchIDs, "8th order", parent = "7th order")
    tree2.create_node(Ninth_Order_batchIDs, "9th order", parent = "8th order")
    tree2.show()
    ### batch number tree.create_node etc...

    tree1 = Tree()
    tree1.create_node((input_UID, input_UID_batchID), "input")
    tree1.create_node(Source_packages_primary_reformat, "primary source", parent = "input")
    tree1.create_node(Secondary_source_packages_reformat1, "secondary source", parent = "primary source")
    tree1.create_node(Tertiary_source_packages_reformat1, "tertiary source", parent = "secondary source")
    tree1.create_node(Quaternary_source_packages_reformat1, "quaternary source", parent = "tertiary source")
    tree1.create_node(Fifth_Order_source_packages_reformat1, "5th order source", parent = "quaternary source")
    tree1.create_node(Sixth_Order_source_packages_reformat1, "6th order source", parent = "5th order source")
    tree1.create_node(Seventh_Order_source_packages_reformat1, "7th order source", parent = "6th order source")
    tree1.create_node(Eighth_Order_source_packages_reformat1, "8th order source", parent = "7th order source")
    tree1.create_node(Ninth_Order_source_packages_reformat1, "9th order source", parent = "8th order source")
    tree1.show()


    print("Primary/ Parent Batch:", "\n", "UID: ", input_UID, "\n", "Batch: ", input_UID_batchID,
          "\n", "Source Package(s): ", Source_packages_primary_reformat,
          "\n", "Source Batch ID's: ", Primary_batches, ",",
          "\n", "Secondary Source Packages: ", Secondary_source_packages_reformat1,
          "\n", "Tertiary Source Packages: ", Tertiary_source_packages_reformat1,
          "\n", "Quaternary Source Packages: ", Quaternary_source_packages_reformat1,
          "\n", "5th Order Source Packages: ", Fifth_Order_source_packages_reformat1,
          "\n", "6th Order Source Packages: ", Sixth_Order_source_packages_reformat1,
          "\n", "7th Order Source Packages: ", Seventh_Order_source_packages_reformat1,
          "\n", "8th Order Source Packages: ", Eighth_Order_source_packages_reformat1,
          "\n", "9th Order Source Packages: ", Ninth_Order_source_packages_reformat1)





