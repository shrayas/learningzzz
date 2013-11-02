from flask import Flask, render_template
import gspread
import ConfigParser
import os.path

app = Flask(__name__)

@app.route("/")
def listLearningzzz():

    if not os.path.isfile("config.ini"):
        return "No config file set. FATAL"

    config = ConfigParser.RawConfigParser()
    config.read("config.ini")

    username = config.get("user_details","username")
    password = config.get("user_details","password")
    spreadsheetKey = config.get("spreadsheet_details","key")
    worksheetNum = config.getint("spreadsheet_details","worksheet")

    gc = gspread.login(username,password)
    sheet = gc.open_by_key(spreadsheetKey).get_worksheet(worksheetNum)

    topicsList = sheet.col_values(2)[1:]
    linksList = sheet.col_values(3)[1:]

    topicsLinksList = []
    for topic, link in zip(topicsList,linksList):
        if link is None:
            link = "#"

        obj = {}
        obj["topic"] = topic
        obj["link"] = link

        topicsLinksList.append(obj)

    return render_template('learningzzz.html',topicsLinksList=topicsLinksList)

if __name__ == "__main__":

    if not os.path.isfile("config.ini"):
        print "No config file set. FATAL"
        exit(1)

    config = ConfigParser.RawConfigParser()
    config.read("config.ini")

    debug = config.getboolean("server_details","debug")
    port = config.getint("server_details","port")

    app.run(debug=debug, port=port, host="0.0.0.0")
