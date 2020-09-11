import PySimpleGUI as sg
import sys, os, PyPDF2, subprocess

#browse a folder
if len(sys.argv) ==1:
    event, values = sg.Window('PDF Merge',
    [[sg.Text('Folder to open')], [sg.In(), sg.FolderBrowse()],
    [sg.Text('Save Name as')], [sg.InputText(key='savefile')],
    [sg.Save(), sg.Cancel()]]).read(close=True)
    fname = values[0]
    savefile = values['savefile']
    print(fname)

    # find pdf files in the directory 
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No folder supplied")
    raise SystemExit("Cancelling: no foldername supplied")
else:
    os.chdir(fname)
    print (f'the current dir is {os.getcwd()}')
    #Get all the PDF filenames
    pdf2merge = []
    for filename in os.listdir("."):
        if filename.endswith(".pdf"):
            pdf2merge.append(filename)

    pdfWriter = PyPDF2.PdfFileWriter()

    #loop through all PDFs
    for filename in pdf2merge:
    #rb for read binary
        pdfFileObj = open(filename,"rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        #Opening each page of the PDF
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    #save PDF to file, wb for write binary
    pdfOutput = open(savefile + ".pdf", "wb")
    #Outputting the PDF
    pdfWriter.write(pdfOutput)
    #Closing the PDF writer
    pdfOutput.close()

    sg.popup(f"{savefile} was saved in {fname}")
    #MAC to opens the file
    subprocess.check_call(['open', savefile + '.pdf'])

