from selenium import webdriver
import time

from tkinter import StringVar, messagebox
import webbrowser  

import smtplib, ssl

import tkinter as tk


def sendEmail( sender_email, receiver_email, message):
    port = 465    # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("email", "pass")
        server.sendmail(sender_email, receiver_email, message)

def main():

    months = [ "IANUARIE", "FEBRUARIE", "MARTIE", "APRILIE", "MAI", "IUNIE", "IULIE", "AUGUST", "SEPTEMBRIE", "OCTOMBRIE", "NOIEMBRIE", "DECEMBRIE" ]


    urlCancel = 'https://www.drpciv.ro/drpciv-booking/cancel-reservation/AU1WYoaVMjSQQ_PzL1WR29IkmxCWDukZopridj7s3jV_7vKknRYbiEpGbAZ5LlyvjnHF-jVeFvwiJDV4z9yhNcvCjfOdsxL3EY2k7Ai-AN_gyqyw9b97K6Doi03ihO_RNZkxxVBSZlrq-Y_dwazAhohRC-f0stD67HO_J480UEO8YLFvrrwiTdybaBvU1wLTrskIueNPPl8_Sckwg6UR4aVOlut8M1aNSGVGU1OlTXHmQ8S1UCNocd30nAnm4mK82dZOyEDN47OhvKsSfCW9mm5FCKovjj6qBiJ7_9p81xkmrbZLY28V8Qh1jg'
    # specify the url
    urlpage = 'https://www.drpciv.ro/drpciv-booking/formular/22/theoryExamination' 
    # run firefox webdriver from executable path of your choice
    driver = webdriver.Firefox()
    # get web page
    driver.get(urlpage)

    time.sleep(5)

    #cookie
    try:
        driver.find_element_by_id("btnCloseCookieMessage").click()
    except:
        print("Cookie already closed")

    nxtButton = driver.find_element_by_class_name('next')
    prvButton = driver.find_element_by_class_name('prev')
    monthTxt = driver.find_element_by_class_name('calendar-navigation')

    startDate = { "month": monthTxt.text.split()[0] , "year": monthTxt.text.split()[1] }
    
    best = {"day": 27, "month": 5}

    while True:
        for x in range(0,7):
            #results = driver.find_elements_by_xpath("//*[@class='col-sm-1 busy-day']")
            results = driver.find_elements_by_xpath("//*[@class='col-sm-1 available-day']")

            current_time = time.strftime("%H:%M:%S", time.localtime())
            print('Number of results', len(results), "for" , monthTxt.text, "at", current_time)

            for result in results:
                #print(result.text, '', month.text)

                monthInd = months.index( monthTxt.text.split()[0] ) +1
                day = int(result.text)

                if monthInd < best['month'] or ( monthInd == best['month'] and day < best['day'] ) :

                    best['day']   = int(result.text)
                    best['month'] = months.index( monthTxt.text.split()[0] ) + 1
                    print(best)
                    
                    webbrowser.open(urlCancel, new=2, autoraise=True)
                    webbrowser.open(urlpage, new=2, autoraise=True)

                    newDateStr =  str(best['day']) + " " + months[best['month'] -1]
                    mailContent = """Subject: drpciv alert - {newDateStr}

                    new date found on: {newDateStr} at {time}
                    
                    1. Cancel the old reservation:
                    {urlCancel}

                    2. Make a new one at ( {registerCode} ):
                    {urlpage}"""

                    sendEmail(sender_email="bobudragos2@gmail.com", receiver_email="bobudragos1@gmail.com", message=mailContent.format(newDateStr=newDateStr, urlCancel=urlCancel, registerCode=2718127, urlpage=urlpage, time=current_time))
                    messagebox.showwarning(title=None, message=newDateStr)
                    driver.quit()
                    quit()
                    

            nxtButton.click()

        for x in range(0,7):
            prvButton.click()

        time.sleep(5)
        time.sleep(3600/4)



# best = {"day": 29, "month": 3}

# dayVar= ''

# window = tk.Tk()
# greeting = tk.Label(text="Hello, Tkinter")
# dayInput = tk.Entry(textvariable=dayVar)
# monthInput = tk.Entry(textvariable=best['month'])
# button = tk.Button(text='Start', command=main)


# greeting.pack()
# dayInput.pack()
# monthInput.pack()

# button.pack()

# print(dayVar)

# window.mainloop()


main()
