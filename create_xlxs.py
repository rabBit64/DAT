import xlsxwriter
        
def convert_tuple(value):
    if not isinstance(value, tuple):
        return value

        return str(value)

def make_xlxs(input_file_path, worksheet_name):
    with open(input_file_path, mode = 'r') as t:
        text = list(t)
        string = " ".join(text)
        landmarks = string.split(" ")
    
    workbook = xlsxwriter.Workbook(worksheet_name)
    worksheet = workbook.add_worksheet()
    
    row=0
    col=0

    for landmark in landmarks:
        landmark_frame = map(convert_tuple, landmarks[row*42:(row*42)+42])
        worksheet.write_row(row,col, landmark_frame)
        row += 1
    
    workbook.close()


def main():
    make_xlxs("/Users/anna/SLR/outputvideo/Sentence/sentence.txt", 'Sentence02.xlsx')
    
if __name__=="__main__":
    main()
