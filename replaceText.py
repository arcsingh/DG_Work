
# Script to read a file and replace the _ with spaces
#Step1: Open the file to be modified and store the content in memory
#Step2: Replace the text with ' ' using the replace function
#Step3: Write the replaced text back to a new file. Note: Can be written to the same file as well
#Step4: We can also provide the filepath from any location in the script

#Function to replace text
def replaceText(input_filename, output_filename):

    #Read the input file
    s = open(input_filename).read()

    #Replace _ with ' '
    s = s.replace('_', ' ')

    #Open the Output file and write the replaced text
    f = open(output_filename, 'w')
    f.write(s)

    #Close the output file
    f.close()
    print "Convertion Successfully completed - " +output_filename
#Function Ends

#Convert File
replaceText("neg.wn", "neg_update.wn")
replaceText("pos.wn", "pos_update.wn")
