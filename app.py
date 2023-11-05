from flask import Flask, render_template, request
import re

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')


# Put your existingUsers, potentialStudyBuddies, and functions here

@app.route('/')
def index():
    return render_template('index.html')

# Check for valid class name format
def is_valid_class_name(class_name):
    return re.match(r'CSE\d{3}', class_name) is not None


@app.route('/result.html', methods=['POST'])
def result():
    className = request.form['className']
    timeToStudy = float(request.form['timeToStudy'])
    stressed = int(request.form['stressed'])
    timeToDeadline = float(request.form['timeToDeadline'])

    # Input validation
    if not is_valid_class_name(className):
        return render_template('error.html', error='Invalid Class Name Format'), 400

    existingUsers = [['Sindhu', ['CSE355', 'CSE330', 'CSE360'], 2.5, 3, 4],
                     ['Tejal', ['CSE475', 'CSE445', 'CSE492'], 3, 4, 1],
                     ['Rhea', ['CSE330', 'CSE492'], 4.5, 3, 4], ['John', ['CSE110', 'CSE120'], 6, 2, 2],
                     ['Anushka', ['CSE355', 'CSE360'], 7, 4, 2],
                     ['Stacy', ['CSE205', 'CSE230'], 3, 3, 2], ['James', ['CSE110', 'CSE495'], 5, 2, 3],
                     ['Amaya', ['CSE230', 'CSE472'], 5.5, 3, 4],
                     ['Saharya', ['CSE365', 'CSE472'], 6, 3, 3], ['Bob', ['CSE230', 'CSE492'], 5, 2, 3],
                     ['Dylan', ['CSE340', 'CSE492'], 7, 3, 2],
                     ['Thomas', ['CSE330', 'CSE493'], 8, 3, 2], ['Mike', ['CSE340', 'CSE492'], 4, 2, 3],
                     ['Gamaya', ['CSE355', 'CSE493'], 6, 3, 2],
                     ['Lizzie', ['CSE350', 'CSE492'], 6, 3, 3], ['Tara', ['CSE355', 'CSE464'], 3.5, 3, 3],
                     ['Kelsie', ['CSE330', 'CSE464'], 4, 3, 4]]

    potentialStudyBuddies = []
    # Your existing code for finding potential study buddies goes here
    for i in range(0, len(existingUsers)):
        if className in existingUsers[i][1]:
            potentialStudyBuddies.append(existingUsers[i])


    result = True if len(potentialStudyBuddies) > 0 else False

    finalProspects = []
    scoreList = []

    def sortByScore():
        # Your function to sort potential study buddies goes here
        for k in range(0, len(potentialStudyBuddies)):
            timeDiff = abs(timeToStudy - potentialStudyBuddies[k][2])
            stressDiff = abs(stressed - potentialStudyBuddies[k][3])
            deadlineDiff = abs(timeToDeadline - potentialStudyBuddies[k][4])
            score = (1 - timeDiff) * 0.4 + (1 - stressDiff) * 0.3 + (1 - deadlineDiff) * 0.3
            scoreList.append([potentialStudyBuddies[k][0], score])

        scoreList.sort(key=lambda x: x[1], reverse=True)

        for i in range(0, len(scoreList)):
            for j in range(0, len(potentialStudyBuddies)):
                if scoreList[i][0] == potentialStudyBuddies[j][0]:
                    finalProspects.append(potentialStudyBuddies[j])

    def findBuddies():
        sortByScore()
        # Your function to find buddies goes here
        print('The matching buddies for you are ranked:')

        print("\nFinal Prospects: ")

        for i in range(0, len(finalProspects)):
            print(finalProspects[i])



    if result:
        findBuddies()
        return render_template('result.html', finalProspects=finalProspects)
    else:
        return "No study buddies are taking this class"


# Error handler for 404 Not Found errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template('/error.html', error='404 - Not Found'), 404

# Error handler for 500 Internal Server errors
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('/error.html', error='500 - Internal Server Error'), 500


if __name__ == '__main__':
    app.run(debug=True)
