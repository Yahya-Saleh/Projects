import urllib.parse
import webbrowser
from time import sleep
import pyautogui as gui
import pandas as pd

def main():
    #the x, y coordanite of the open whatsapp message that'll appear on chrome
    position = 747,227
    #the x, y coordanite of the whatsapp's close bar
    Xposition = 1345,62

    #getting the table
    table = tables_processing()

    #for every row i.e. person in the list
    for i in range(len(table["no"])):
        #if the number isn't exactly 11 digits we skip it, since it's an invalid number
        if len(str(table["no"][i])) != 9:
            continue
        
        #creating a message specific to the person
        #and then encoding it for proper transmition through the URL
        message = urllib.parse.quote(f'''   
        السلام عليكم ورحمة الله وبركاته 
        للتعريف بنفسي: ‏منسق هذا البحث للأطباء المذكورين لغرض البحث العلمي في اكاديمية طب الاسرة 
        شكرا لتجاوبك 

        الفئة المستهدفة
        أطباء المراكز الصحية من غير الأسنان  (استشاري-اخصائي -عام)

        إلى الدكتور {table["name"][i]}

        نرجو منكم التعاون معنا في تعبئة استبيان بحثنا حول

        Attitudes and Barriers of Point of Care Ultrasound (POCUS) implementation among primary health care physicians in Eastern Province, Saudi Arabia 2019-2020

        https://docs.google.com/forms/d/e/1FAIpQLSfiOyNcKvqRiORGi730gsjMIf0Psh86WkR4Oovop83dwNXvVw/viewform?vc=0&c=0&w=1

        مع جزيل الشكر لكم على تعاونكم🌷

        أطباء مقيمين بأكاديمية طب الأسرة
        د. علي الزاهر 
        د. بثينة اليوسف
        د. سعيد انصيران 
        الرجاء الرد ب (تم) في حال الانتهاء من تعبئة الاستبيان

        إذا تم تعبئته من قبل الرجاء الإعلام بذلك

        إذا لم يكن لك رغبة في تعبئة الاستبيان الرجاء الإعلام بذلك
        ''')

        #the URL to be called
        url = f'https://wa.me/966{table["no"][i]}?text={message}'
        webbrowser.open(url)
        #waiting for website to load
        sleep(5)
        #clicking open whatsapp
        gui.click(position)
        #waiting for whatsapp to open
        sleep(15)
        #sending the messages
        gui.press('enter')
        #waiting on the message to be sent
        sleep(10)
        #closing the whatsapp
        #gui.click(Xposition)
        #making sure everything is in pace
        sleep(2)


def tables_processing():
    #now read data
    cn1 = pd.read_excel("DataBases\contacts-1.xlsx")
    cn2 = pd.read_excel("DataBases\contacts-2.xlsx")

    #Rename columns
    cn1.columns = ["no", "occupation", "name"]
    cn2.columns = ["no", "occupation", "name"]
    #Merge both Dataframes
    Areas = cn1.merge(cn2, how="outer")

    #Convert Numbers to float so that its possible to drop all Null values.
    Areas["no"] = pd.to_numeric(Areas["no"], errors="coerce")
    #Drop all null values
    Areas = Areas.dropna()
    #Convert it back to integer
    Areas["no"] = pd.to_numeric(Areas["no"], downcast='integer', errors="coerce")

    #Drop occupation column
    Areas = Areas.drop(["occupation"], axis = 1)
    #Reset Index
    Areas = Areas.reset_index()
    #Make it back to object again
    Areas["no"] = Areas["no"].astype("object")

    return Areas

if __name__ == "__main__":
    main()